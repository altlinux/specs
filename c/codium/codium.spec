%define app_id com.vscodium.codium

Name:    codium
Version: 1.96.4.25026
Release: alt2

Summary: Visual Studio Code without MS branding/telemetry/licensing

License: MIT 
Group:   Development/Other
Url:     https://github.com/VSCodium/vscodium
Vcs:     https://github.com/VSCodium/vscodium

#Source0-url: https://github.com/VSCodium/vscodium/releases/download/%{version}/VSCodium-linux-x64-%{version}.tar.gz
Source0: %name-x64-%version.tar
#Source1-url: https://github.com/VSCodium/vscodium/releases/download/%{version}/VSCodium-linux-arm64-%{version}.tar.gz
Source1: %name-arm64-%version.tar

Source2: codium.desktop
Source3: codium.svg
Source4: %app_id.metainfo.xml

%set_verify_elf_method skip
%global __find_debuginfo_files %nil

%filter_from_requires /deepin-api/d
%filter_from_requires /enlightenment/d
%filter_from_requires /exo-utils/d
%filter_from_requires /kde-cli-tools/d
%filter_from_requires /gnustep-Backbone/d
%filter_from_requires /pcmanfm/d
%filter_from_requires /github-cli/d
%filter_from_requires /^\/usr\/lib\/ld-linux-aarch64.*/d

BuildRequires: electron29
BuildRequires: libgio
BuildRequires: libnss
BuildRequires: libnspr
BuildRequires: libatk
BuildRequires: at-spi2-atk
BuildRequires: libcups
BuildRequires: libdbus
BuildRequires: libdrm
BuildRequires: libgtk+3
BuildRequires: libpango
BuildRequires: libcairo 
BuildRequires: libgdk-pixbuf
BuildRequires: libX11
BuildRequires: libXcomposite
BuildRequires: libXdamage
BuildRequires: libXext
BuildRequires: libXfixes
BuildRequires: libXrandr
BuildRequires: libgbm
BuildRequires: libexpat
BuildRequires: libxcb
BuildRequires: libxkbcommon
BuildRequires: libalsa
BuildRequires: libat-spi2-core
BuildRequires: libsecret
BuildRequires: libxkbfile

Provides: vscodium = %EVR

ExclusiveArch: x86_64 aarch64

%description
Community-driven, freely-licensed binary distribution of Microsoft's editor VSCode
without MS branding/telemetry/licensing.
Visual Studio Code is a new choice of tool that combines the simplicity
of a code editor with what developers need for the core edit-build-debug cycle.
See FAQ at https://code.visualstudio.com/docs/setup/linux .

%prep
%ifarch x86_64
    tar -xf %SOURCE0
%endif
%ifarch aarch64
    tar -xf %SOURCE1
%endif

%build
#

%install
mkdir -p %buildroot%_libdir/%name/
cp -r %_builddir/%name-*-%version/* %buildroot%_libdir/%name/

mkdir -p %buildroot%_bindir/
# set suid for chrome-sandbox to avoid a startup error
chmod 4711 %buildroot%_libdir/%name/chrome-sandbox
ln -rs %buildroot%_libdir/%name/bin/codium %buildroot/%_bindir/codium
ln -rs %buildroot%_libdir/%name/bin/codium %buildroot/%_bindir/vscodium

install -m644 -D %SOURCE2 %buildroot%_desktopdir/%name.desktop
install -m644 -D %SOURCE3 %buildroot%_iconsdir/hicolor/scalable/apps/codium.svg
install -m644 -D %SOURCE4 %buildroot%_datadir/appdata/%app_id.metainfo.xml


%files
%_bindir/%name
%_bindir/vs%name
%_libdir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/codium.svg
%_datadir/appdata/%app_id.metainfo.xml

%changelog
* Sat Feb 01 2025 Semen Fomchenkov <armatik@altlinux.org> 1.96.4.25026-alt2
- add Wayland support (Closes: 47792)
- add appstream-data (Closes: 52900)
- remove gitlab-ci dependency (Closes: 52896)
- new .svg icon instead of the old .png
- add Vcs tag to spec-file (Closes: 52899)

* Thu Jan 30 2025 Semen Fomchenkov <armatik@altlinux.org> 1.96.4.25026-alt1
- new version (1.96.4.25026) (Closes: 50953, 52311)
- drop arm-32bit version

* Sun Sep 10 2023 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.82.0.23250-alt1
- new version (1.82.0.23250) (Closes: 46710)

* Thu Oct 13 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.72.1.22284-alt1
-  new version (1.72.1.22284) (Closes: 43921)

* Mon Aug 08 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.70.0-alt1
- new version (1.70.0)

* Fri Jun 03 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.67.2-alt1
- new version (1.67.2)
- added Provides: vscodium

* Thu Apr 28 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.66.2-alt1
- changed build from source to packing from binaries
- new version (1.66.2) ALT #42144

* Sat Mar 05 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.63.2-alt2
- set ExclusiveArch: x86_64

* Sat Mar 05 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 1.63.2-alt1
- initial version (1.63.2) with rpmgs script
  + import sources from codium-1.63.2.tar
  + import sources from code-1.63.2.tar
  + workaround "python: command not found" error
  + workaround "Error: Command failed: git config pull.rebase merges"
  + add predownloaded node_modules for vscode
  + add predownloaded node_modules for extensions
  + disable download marketplace builtin extensions during the build
  + workaround to download electron and ffmpeg
  + fixed aarch64 and armh packing
  + sandbox mode is disabled to avoid a startup error
  + add icons and desktop files
  + packing README.md

