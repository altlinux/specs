%define _unpackaged_files_terminate_build 1
%def_with legacy
%define alt_name acc

Name: alterator-explorer
Version: 0.1.7
Release: alt2

Summary: Explorer of Alterator applications operating via D-Bus
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-explorer

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-alterator
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-base-common
BuildRequires: boost-devel-headers
BuildRequires: libtomlplusplus-devel

# TODO(chernigin): validate interface on build
BuildRequires: alterator-interface-application

%if_without legacy
BuildRequires: ImageMagick-tools
%endif

Requires: alterator-interface-application >= 0.1.1
Requires: alterator-backend-categories >= 0.1.2
Requires: alterator-backend-legacy >= 0.1.2

%if_with legacy
Requires: alterator-standalone >= 7.4.3
Requires: /usr/bin/acc-legacy
Requires: alterator-backend-legacy
%else
# Oldest versions of alterator-standalone don't provides acc-legacy.
# TODO: Add force disable SwitchBack() logic in this case. So,
#       alterator-explorer conflicts with alterator-standalone until this task
#       is not completed.
Conflicts: alterator-standalone >= 7.4.3
%endif

Requires: alterator-manager >= 0.1.25
Requires: alterator-module-executor >= 0.1.14

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%if_without legacy

install -D -m644 setup/%name.desktop \
    %buildroot%_desktopdir/%name.desktop

for size in 48 64 128 256 512; do
    mkdir -p %buildroot%_datadir/icons/hicolor/''${size}x''${size}/apps/
    convert setup/logo.png -resize ''${size}x''${size} \
        %buildroot%_datadir/icons/hicolor/''${size}x''${size}/apps/%name.png
done

%else

install -d %buildroot/%_altdir
cat > %buildroot/%_altdir/%name <<EOF
%_bindir/%alt_name	%_bindir/%name 50
EOF

touch %buildroot/%_bindir/%alt_name

%endif

%files
%_datadir/alterator/categories/*
%doc *.md
%_bindir/%name

%if_with legacy
%ghost %_bindir/%alt_name
%config %_altdir/%name

%_bindir/%alt_name
%else
%_desktopdir/%name.desktop

%_datadir/icons/hicolor/48x48/apps/%name.png
%_datadir/icons/hicolor/64x64/apps/%name.png
%_datadir/icons/hicolor/128x128/apps/%name.png
%_datadir/icons/hicolor/256x256/apps/%name.png
%_datadir/icons/hicolor/512x512/apps/%name.png
%endif

%changelog
* Fri Dec 13 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.7-alt2
- fix adt category

* Mon Dec 09 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.7-alt1
- move to toml

* Mon Oct 29 2024 Michael Chernigin <chernigin@altlinux.org> 0.1.6-alt2
- rename to alterator-explorer

* Mon Oct 21 2024 Aleksey Saprunov <sav@altlinux.org> 0.1.6-alt1
- change prefix from ru.basealt to org.altlinux
- fix components and applications category icon and comment translation

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
