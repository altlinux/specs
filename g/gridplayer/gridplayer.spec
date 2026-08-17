%define xdg_name com.vzhd1701.gridplayer

%def_with check

Name: gridplayer
Version: 0.5.5
Release: alt1

Summary: Play videos side-by-side

License: GPL-3.0-or-later
Group: Video

URL: https://pypi.org/project/gridplayer
VCS: https://github.com/vzhd1701/gridplayer

Source: %name-%version.tar
Patch: %name-%version-%release.patch
Patch1: alt-add-russian-to-desktop-file.patch

Requires: vlc

BuildArch: noarch

BuildRequires: rpm-build-python3
BuildRequires: python3(uv_build)

BuildRequires: /usr/bin/appstream-util
BuildRequires: /usr/bin/desktop-file-validate

%if_with check
BuildRequires: python3(PyQt5)
BuildRequires: python3(pydantic_extra_types)
BuildRequires: python3(yt_dlp)
BuildRequires: streamlink
%endif

%description
Simple VLC-based media player that can play multiple videos at the same time.
You can play as many videos as you like, the only limit is your hardware. It
supports all video formats that VLC supports (which is all of them). You can
save your playlist retaining information about the position, sound volume,
loops, aspect ratio, etc.

%package -n python3-module-%name
Summary: Python module for %name
Group: Development/Python3

%filter_from_requires /python3(Foundation)/d
%filter_from_requires /python3(objc)/d
%filter_from_requires /python3(winreg)/d

%filter_from_requires /python3(streamlink.*)/d
Requires: streamlink

%description -n python3-module-%name
Simple VLC-based media player that can play multiple videos at the same time.
You can play as many videos as you like, the only limit is your hardware. It
supports all video formats that VLC supports (which is all of them). You can
save your playlist retaining information about the position, sound volume,
loops, aspect ratio, etc.

This package contains Python module for %name.

%prep
%setup
%autopatch -p1

# fix README.md
sed -i 's|https://raw.githubusercontent.com/vzhd1701/gridplayer/master/resources/||g;
	s|https://github.com/vzhd1701/gridplayer/blob/master/||g' README.md

# fix validate appdata.xml
sed -i '/^appstream-util/s/ validate / validate-relax --nonet /' scripts/linux_meta/build.sh

%build
%pyproject_build

scripts/linux_meta/build.sh

%install
%pyproject_install

mkdir -p %buildroot%_datadir
cp -ar build/meta/icons %buildroot%_datadir
install -Dm0644 build/meta/%xdg_name.desktop %buildroot%_desktopdir/%xdg_name.desktop
install -Dm0644 build/meta/%xdg_name.appdata.xml %buildroot%_datadir/metainfo/%xdg_name.appdata.xml
install -Dm0644 build/meta/%xdg_name.xml %buildroot%_datadir/mime/packages/%xdg_name.xml

%check
%pyproject_run_pytest \
    --ignore="tests/test_custom_menu.py" \
    --ignore="tests/test_keymap.py" \
    --ignore="tests/test_language_list.py" \
    --ignore="tests/test_managers_playlist.py" \
    --ignore="tests/test_theme.py"

%files
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/*/%{xdg_name}*
%_datadir/metainfo/%xdg_name.appdata.xml
%_datadir/mime/packages/%xdg_name.xml

%files -n python3-module-%name
%doc LICENSE *.md resources/public
%python3_sitelibdir/%name
%python3_sitelibdir/%{pyproject_distinfo %name}

%changelog
* Mon Aug 17 2026 Alexander Kovalev <alexvk@altlinux.org> 0.5.5-alt1
- Initial build for ALT.
- Update to commit 8021d3d.
