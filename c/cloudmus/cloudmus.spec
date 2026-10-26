Name: cloudmus
Version: 0.6.4
Release: alt1

Summary: Multi-service cloud music player
License: MIT
Group: Sound
URL: https://cloudmus.app/
VCS: https://github.com/cloudmus/cloudmus

Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libmpv-devel
BuildRequires: libxcb-devel
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-yaml
BuildRequires: rpm-build-python3
BuildRequires: qt6-base-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-tools-devel
BuildRequires: taglib-devel

%description
CloudMus brings Yandex Music, YouTube Music and your local music
folder into one native desktop player: one queue, one history and one
set of controls for every service, with a frosted-glass window,
light and dark themes, tray icon, media keys and MPRIS support.

Fronts and music service backends are separate processes talking
JSON-RPC over stdin/stdout; backends are discovered at startup.

# Shared NDJSON/JSON-RPC transport the backends run on. Ships the
# rpc_common package plus the protocol stubs generated from protocol/
# (a hard runtime dependency of rpc_common).
%package backend-common
Summary: Shared transport library for %name backends
Group: Sound
BuildArch: noarch

%description backend-common
Shared NDJSON/JSON-RPC transport, envelope helpers and generated
protocol stubs for CloudMus backend processes. This is a runtime
dependency of every cloudmus-backend-* package.

%package backend-local
Summary: Local music folder backend for %name
Group: Sound
BuildArch: noarch
Requires: %name-backend-common
Requires: python3

%description backend-local
CloudMus backend that plays music from a local directory tree, each
subfolder shown as a playlist.

%package backend-yandex
Summary: Yandex Music backend for %name
Group: Sound
BuildArch: noarch
Requires: %name-backend-common
Requires: python3

%description backend-yandex
CloudMus backend for Yandex Music.

%package backend-youtube
Summary: YouTube Music backend for %name
Group: Sound
BuildArch: noarch
Requires: %name-backend-common
Requires: python3

%description backend-youtube
CloudMus backend for YouTube Music.

%prep
%setup

%build
python3 protocol/codegen/generate.py --lang python cpp

cd fronts/qt
%cmake -DCLOUDMUS_VERSION_OVERRIDE="%version"
%cmake_build

%install
# --- Qt front ---
mkdir -p %buildroot%_bindir
install -p -m 755 fronts/qt/%_cmake__builddir/bin/cloudmus-qt %buildroot%_bindir/cloudmus-qt

mkdir -p %buildroot%_desktopdir
cp -p packaging/appimage/cloudmus-qt.desktop %buildroot%_desktopdir/

mkdir -p %buildroot%_iconsdir/hicolor/512x512/apps
cp -p art/logo.png %buildroot%_iconsdir/hicolor/512x512/apps/cloudmus-qt.png

# --- Backend: shared transport (protocol stubs are generated in %build) ---
mkdir -p %buildroot%python3_sitelibdir_noarch
cp -a backends/py-rpc-common/rpc_common %buildroot%python3_sitelibdir_noarch/

# --- Backends ---
# Manifests are generated (not copied) so the icon path is absolute and
# unique per backend, matching what upstream's AppRun writes into the
# per-user backends.d dir. argv[0] is the system python3. Icons are copied
# to a per-backend filename to avoid the source trees' identical icon.svg
# names colliding. protocolVersion is read from each source manifest.
mkdir -p %buildroot%python3_sitelibdir_noarch
mkdir -p %buildroot%_datadir/cloudmus/backends
mkdir -p %buildroot%_datadir/cloudmus/backend-icons

# local folder
cp -a backends/local-folder/cloudmus_backend_local %buildroot%python3_sitelibdir_noarch/
cp -p backends/local-folder/icon.svg %buildroot%_datadir/cloudmus/backend-icons/local-folder.svg
python3 - backends/local-folder/manifest.json <<'EOF'
import json, sys
m = json.load(open(sys.argv[1]))
out = {
    "id": m["id"],
    "name": m["name"],
    "argv": ["/usr/bin/python3", "-m", "cloudmus_backend_local"],
    "protocolVersion": m["protocolVersion"],
    "icon": "%_datadir/cloudmus/backend-icons/local-folder.svg",
}
json.dump(out, open("%buildroot%_datadir/cloudmus/backends/local-folder.json", "w"), indent=2)
EOF

# Yandex Music
cp -a backends/yandex-music/cloudmus_backend_yandex %buildroot%python3_sitelibdir_noarch/
cp -p backends/yandex-music/icon.svg %buildroot%_datadir/cloudmus/backend-icons/yandex-music.svg
python3 - backends/yandex-music/manifest.json <<'EOF'
import json, sys
m = json.load(open(sys.argv[1]))
out = {
    "id": m["id"],
    "name": m["name"],
    "argv": ["/usr/bin/python3", "-m", "cloudmus_backend_yandex"],
    "protocolVersion": m["protocolVersion"],
    "icon": "%_datadir/cloudmus/backend-icons/yandex-music.svg",
}
json.dump(out, open("%buildroot%_datadir/cloudmus/backends/yandex-music.json", "w"), indent=2)
EOF

# YouTube Music
cp -a backends/youtube-music/cloudmus_backend_ytmusic %buildroot%python3_sitelibdir_noarch/
cp -p backends/youtube-music/icon.svg %buildroot%_datadir/cloudmus/backend-icons/youtube-music.svg
# Drop bytecode the source trees ship; ALT compiles its own.
find %buildroot%python3_sitelibdir_noarch -name __pycache__ -exec rm -rf {} +
python3 - backends/youtube-music/manifest.json <<'EOF'
import json, sys
m = json.load(open(sys.argv[1]))
out = {
    "id": m["id"],
    "name": m["name"],
    "argv": ["/usr/bin/python3", "-m", "cloudmus_backend_ytmusic"],
    "protocolVersion": m["protocolVersion"],
    "icon": "%_datadir/cloudmus/backend-icons/youtube-music.svg",
}
json.dump(out, open("%buildroot%_datadir/cloudmus/backends/youtube-music.json", "w"), indent=2)
EOF

%files
%doc LICENSE
%doc README.md
%_bindir/cloudmus-qt
%_desktopdir/cloudmus-qt.desktop
%_iconsdir/hicolor/512x512/apps/cloudmus-qt.png

%files backend-common
%python3_sitelibdir_noarch/rpc_common/

%files backend-local
%python3_sitelibdir_noarch/cloudmus_backend_local/
%_datadir/cloudmus/backends/local-folder.json
%_datadir/cloudmus/backend-icons/local-folder.svg

%files backend-yandex
%python3_sitelibdir_noarch/cloudmus_backend_yandex/
%_datadir/cloudmus/backends/yandex-music.json
%_datadir/cloudmus/backend-icons/yandex-music.svg

%files backend-youtube
%python3_sitelibdir_noarch/cloudmus_backend_ytmusic/
%_datadir/cloudmus/backends/youtube-music.json
%_datadir/cloudmus/backend-icons/youtube-music.svg

%changelog
* Mon Oct 26 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.6.4-alt1
- 0.6.4

* Wed Oct 14 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.6.2-alt1
- initial
