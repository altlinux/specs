Name: appinstall
Version: 1.3.2
Release: alt1
Summary: GUI frontend for install third-party applications

License: GPL-3.0+
Group: System/Configuration/Packaging
URL: http://www.altlinux.org

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): libpam-devel
BuildRequires: gcc-c++
BuildRequires: qt5-tools
BuildRequires: python3-module-PyQt5

Requires: eepm

%description
GUI frontend for install third-party applications using epm play.

%prep
%setup -q

%build
lrelease-qt5 %{name}_ru.ts

%install
install -Dpm 0755 %name %buildroot%_sbindir/%name
mkdir -p %buildroot%_bindir/
ln -s %_libexecdir/consolehelper/helper %buildroot%_bindir/%name
install -pD -m640 %name.pamd %buildroot%_sysconfdir/pam.d/%name
install -pD -m640 %name.security %buildroot%_sysconfdir/security/console.apps/%name

mkdir -p %buildroot%_datadir/%name
cp -a %name.svg %name.ui *.qm %buildroot%_datadir/%name
install -Dpm 0644 %name.svg %buildroot%_pixmapsdir/%name.svg
install -Dpm 0644 %name.desktop %buildroot%_desktopdir/%name.desktop

%files
%_bindir/%name
%_sbindir/%name
%dir %_datadir/%name/
%_datadir/%name/*
%_pixmapsdir/%name.svg
%_desktopdir/%name.desktop
%config(noreplace) %_sysconfdir/pam.d/%name
%config(noreplace) %_sysconfdir/security/console.apps/%name

%changelog
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
