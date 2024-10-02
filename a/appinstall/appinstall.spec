Name: appinstall
Version: 1.4.4
Release: alt1
Summary: GUI frontend for install third-party applications

License: GPL-3.0+
Group: System/Configuration/Packaging
URL: http://www.altlinux.org

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-qt6
BuildRequires(pre): libpam-devel
BuildRequires: gcc-c++
BuildRequires: qt6-tools
BuildRequires: python3-module-PyQt6

Requires: eepm

%description
GUI frontend for install third-party applications using epm play.

%prep
# For translators:
# 1. Install eepm
# 2. make make LUPDATE=lupdate-qt6 LRELEASE=lrelease-qt6 update_translations all clean
# 3. subst '/oldsource/d' *.ts
# 4. Translate appinstall_ru.ts in kde5-lokalize
# 5. Commit strings.cpp and *.ts
%setup -q

%build
export PATH=$PATH:%_qt6_bindir
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_sbindir/%name
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/allow.d
%dir %_datadir/%name/
%_datadir/%name/*
%_pixmapsdir/%name.svg
%_desktopdir/%name.desktop
%config(noreplace) %_sysconfdir/pam.d/%name
%config(noreplace) %_sysconfdir/security/console.apps/%name

%changelog
* Thu Aug 29 2024 2023 Kirill Izmestev <felixz@altlinux.org> 1.4.4-alt1
- Upgrading a program and this package from using PyQt5 to using PyQt6.
- Added quick filtering of applications when entering in the search \
line (thanks Sergey Shevchenko <sergey.shevchenko04@gmail.com>).

* Mon Jun 26 2023 Andrey Cherepanov <cas@altlinux.org> 1.4.3-alt1
- Update Russian translation for eepm-3.57.7 (ALT #46564).

* Tue Jun 13 2023 Andrey Cherepanov <cas@altlinux.org> 1.4.2-alt1
- Used /dev/null as stdin for prevent epm hang (thanks Mikhail Tergoev) (ALT #43747).

* Thu May 11 2023 Andrey Cherepanov <cas@altlinux.org> 1.4.1-alt1
- Apply changes for processed item, not selected (ALT #41897).
- Fix run from KDE menu (ALT #43747).
- Store installed flag in Qt::UserRole instead of Qt::ToolTipRole.
- Update translations for eepm-3.28.1.
- Move all actions from spec file to Makefile.

* Mon May 08 2023 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- Show window immediately and display loading animation (ALT #43747)
- Show only allowed applications from /etc/appinstall/allow.d (ALT #41900)
- Change installed icon to QStyle.SP_ArrowDown
- Get installed application list with new epm play parameter --short (ALT #42812, #42802)


* Sun May 15 2022 Andrey Cherepanov <cas@altlinux.org> 1.3.3-alt1
- Update localization for eepm-3.18.6.

* Mon Mar 21 2022 Andrey Cherepanov <cas@altlinux.org> 1.3.2-alt1
- Update localization for eepm-3.15.1.

* Wed Jan 05 2022 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- Add extract script for localization.
- Update localization for eepm-3.14.6.

* Thu Nov 25 2021 Andrey Cherepanov <cas@altlinux.org> 1.3-alt1
- Hack for wrong exit code of install glusterfs7 (see bug 41429).

* Thu Nov 25 2021 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- Show remove action in top of detail pane on removing.
- Use epm play --auto for all operation.
- Ignore unsupported Unicode symbols in process output.

* Wed Nov 24 2021 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- Fix crash after install or remove.
- Prevent of double run of installation.

* Wed Nov 17 2021 Andrey Cherepanov <cas@altlinux.org> 1.0-alt2
- Fix typo in Russian translation.

* Sat Nov 13 2021 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
