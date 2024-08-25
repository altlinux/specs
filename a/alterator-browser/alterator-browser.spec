%define _unpackaged_files_terminate_build 1
%def_with legacy
%define alt_name acc

Name: alterator-browser
Version: 0.1.5
Release: alt1

Summary: Browser of Alterator modules operating via D-Bus
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-browser

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-alterator
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-base-common
BuildRequires: boost-devel-headers

# TODO(chernigin): validate interface on build
BuildRequires: alterator-interface-application

%if_without legacy
BuildRequires: ImageMagick-tools
%endif

Requires: alterator-interface-application
Requires: alterator-backend-categories

%if_with legacy
Requires: alterator-standalone >= 7.4.3
Requires: /usr/bin/acc-legacy
Requires: alterator-backend-legacy
%else
# Oldest versions of alterator-standalone don't provides acc-legacy.
# TODO: Add force disable SwitchBack() logic in this case. So, alterator-browser
#       conflicts with alterator-standalone until this task is not completed.
Conflicts: alterator-standalone >= 7.4.3
%endif

%description
Browser of Alterator modules operating via D-Bus.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%if_without legacy

install -D -m644 setup/alterator-browser.desktop \
    %buildroot%_desktopdir/alterator-browser.desktop

for size in 48 64 128 256 512; do
    mkdir -p %buildroot%_datadir/icons/hicolor/''${size}x''${size}/apps/
    convert setup/logo.png -resize ''${size}x''${size} \
        %buildroot%_datadir/icons/hicolor/''${size}x''${size}/apps/alterator-browser.png
done

%else

install -d %buildroot/%_altdir
cat > %buildroot/%_altdir/%name <<EOF
%_bindir/%alt_name	%_bindir/alterator-browser 50
EOF

touch %buildroot/%_bindir/%alt_name

%endif

%files
%_datadir/alterator/categories/*
%_bindir/alterator-browser
%doc *.md
%_bindir/%name

%if_with legacy
%ghost %_bindir/%alt_name
%config %_altdir/%name

%_bindir/%alt_name
%else
%_desktopdir/alterator-browser.desktop

%_datadir/icons/hicolor/48x48/apps/alterator-browser.png
%_datadir/icons/hicolor/64x64/apps/alterator-browser.png
%_datadir/icons/hicolor/128x128/apps/alterator-browser.png
%_datadir/icons/hicolor/256x256/apps/alterator-browser.png
%_datadir/icons/hicolor/512x512/apps/alterator-browser.png
%endif

%changelog
* Sat Aug 24 2024 Evgeny Sinelnikov <sin@altlinux.org> 0.1.5-alt1
- add support for execution with acc-legacy

* Wed Jul 17 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.4-alt3
- add desktop file

* Wed Jun 26 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.4-alt2
- changed dependecies to up to date packages

* Mon Jun 03 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.4-alt1
- added alterator-module-components support
- added adt and components categories
- changed adt and component category icons and introduced xdg icons

* Tue Apr 02 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.3-alt1
- fix builder to comply with spec
- integrated with AMP
- brought up to specification
- update and combine docs into readme.md
- log outputs of application runs

* Fri Feb 16 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.2-alt1
- closes window after running acc
- add toolbar with button running acc
- fix loadnig and installing translator
- add Ctrl+q shortcut to main window

* Sun Jan 28 2024 Evgeny Sinelnikov <sin@altlinux.org> 0.1.1-alt1
- first build for Sisyphus

* Wed Oct 25 2023 Aleksey Saprunov <sav@altlinux.org> 0.1.0-alt1
- added support for acc files

* Wed Jul 5 2023 Kozyrev Yuri <kozyrevid@altlinux.org> 0.0.1-alt1
- initial build
