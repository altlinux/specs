%define _unpackaged_files_terminate_build 1
%def_with legacy
%define alt_name acc

Name: alterator-explorer
Version: 0.1.16
Release: alt1

Summary: Explorer of Alterator applications operating via D-Bus
License: GPLv2+
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-explorer

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-alterator
BuildRequires(pre): rpm-macros-alternatives
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel
BuildRequires: qt6-base-common
BuildRequires: boost-devel-headers
BuildRequires: libtomlplusplus-devel
BuildRequires: libqtsingleapplication-qt6-devel

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

install -D -m644 setup/%name.desktop \
    %buildroot%_desktopdir/%name.desktop
%if_with legacy
install -d %buildroot/%_altdir
cat > %buildroot/%_altdir/%name <<EOF
%_bindir/%alt_name	%_bindir/%name 50
EOF
echo "NoDisplay=true" >> %buildroot%_desktopdir/%name.desktop
touch %buildroot/%_bindir/%alt_name
%endif

%files
%_datadir/alterator/categories/*
%doc *.md
%_bindir/%name
%_desktopdir/%name.desktop

%if_with legacy
%ghost %_bindir/%alt_name
%config %_altdir/%name
%_bindir/%alt_name
%endif

%changelog
* Tue Aug 19 2025 Andrey Limachko <liannnix@altlinux.org> 0.1.16-alt1
- correct icon handling in Wayland (thx Semen Fomchenkov)
- use standard Alterator icon (thx Semen Fomchenkov)

* Thu Jul 10 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.15-alt1
- restricted to single instance
- unknown objects not being displaying
- added branding style

* Tue May 13 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.14-alt1
- add objects interfaces from available applications

* Mon Mar 31 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.13-alt1
- support release-notes-applications
- add control interface
- refresh button
- fixed category icons size
- hide legacy switch button if acc-legacy not available
- toolbar apperance in different themes

* Tue Mar 11 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.12-alt1
- fix empty categories by <alekseevam@altlinux.org>

* Tue Mar 04 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.11-alt1
- support systeminfo application by <sheriffkorov@altlinux.org>

* Tue Feb 25 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.10-alt1
- move to qt6 by <alekseevam@altlinux.org>

* Fri Feb 21 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.9-alt1
- infinite connection to DBus while alterator interface is not present, or not responding by <alekseevam@altlinux.org>
- category order by <alekseevam@altlinux.org>
- module order by <alekseevam@altlinux.org>
- object parsing by <alekseevam@altlinux.org>
- removed empty space in the bottom of scroll area by <alekseevam@altlinux.org>
- icons and styles to display correctly on different desktop environments by <alekseevam@altlinux.org>

* Thu Jan 09 2025 Aleksey Saprunov <sav@altlinux.org> 0.1.8-alt1
- implement overriding legacy modules

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
