Name:	 packageinstall
Version: 1.4
Release: alt1
Summary: GUI frontend for install packages using apt-get

License: GPL-3.0+
Group:   System/Configuration/Packaging
URL:     http://www.altlinux.org/Install

Packager: Andrey Cherepanov <cas@altlinux.org>

Requires: apt consolehelper

Source0: %name-%version.tar

BuildRequires(pre): libpam-devel
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel qt5-tools

%description
This application is GUI frontend for install package(s) using apt-get.

%prep
%setup -q

%build
%qmake_qt5 PREFIX=%_prefix %name.pro
%make_build
lrelease-qt5 %name.pro

%install
%installqt5
mkdir -p %buildroot%_sbindir/
mv %buildroot%_bindir/%name %buildroot%_sbindir
ln -s %_libexecdir/consolehelper/helper %buildroot%_bindir/%name
install -pD -m640 %name.pamd %buildroot%_sysconfdir/pam.d/%name
install -pD -m640 %name.security %buildroot%_sysconfdir/security/console.apps/%name
for f in *.qm; do install -m 0644 $f %buildroot/%_datadir/apps/%name/ ||: ; done

%files
%doc AUTHORS README.md
%_bindir/%name
%_sbindir/%name
%dir %_datadir/apps/%name/
%_datadir/apps/%name/
%config(noreplace) %_sysconfdir/pam.d/%name
%config(noreplace) %_sysconfdir/security/console.apps/%name

%changelog
* Fri Jul 30 2021 Andrey Cherepanov <cas@altlinux.org> 1.4-alt1
- Fix progress calculation by hash count (ALT #40479).
- README: fix URL and copyright notes (ALT #40511).

* Tue Jul 13 2021 Andrey Cherepanov <cas@altlinux.org> 1.3-alt1
- Fix Russian localization for group of processed packages (ALT #30931).

* Fri Jul 09 2021 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- Run apt-get update before installation (ALT #39768).
- Check apt-get exit code and show error if installation is failed.
- Remove wait proposal on finish stage (ALT #30389).
- Adapt output parse to modern apt-rpm.
- Fix localization.

* Fri Nov 02 2018 Sergey V Turchin <zerg at altlinux dot org> 1.1.2-alt1
- port to Qt5

* Tue Oct 02 2018 Oleg Solovyov <mcpain@altlinux.org> 1.1.1-alt2
- spec cleanup

* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 1.1.1-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Thu Aug 11 2011 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- Reset show details on show information

* Tue Jul 26 2011 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Complete rewrite UI
- Append statistics to main dialog
- Copy apt output to console
- Use buffer read apt output (closes: #25882)
- Add support for debug script
- Do not show statistics if it is no additional packages to install

* Mon Sep 20 2010 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt2
- clear spec
- small fixes

* Thu Mar 19 2009 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial release


