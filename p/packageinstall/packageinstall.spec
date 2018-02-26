
Name:		packageinstall
Version:	1.1.1
Release:	alt1
Summary:	GUI frontend for install packages using apt-get

License:	GPL
Group:		System/Configuration/Packaging
URL:		http://www.altlinux.org/PackageInstall

Packager:   	Andrey Cherepanov <cas@altlinux.org>

Source0:	%name-%version.tar.gz

BuildRequires: gcc-c++ libqt4-devel
Requires: apt consolehelper
BuildPreReq: libpam-devel

%description
This application is GUI frontend for install package(s) using apt-get.

%prep
%setup -q
lrelease-qt4 %name.pro
DESTDIR=%buildroot PREFIX=/usr qmake-qt4 %name.pro

%build
%make_build

%install
%makeinstall
mkdir -p %buildroot%_sbindir/
mv %buildroot%_bindir/%name %buildroot%_sbindir
ln -s %_libexecdir/consolehelper/helper %buildroot%_bindir/%name
install -pD -m640 %name.pamd %buildroot%_sysconfdir/pam.d/%name
install -pD -m640 %name.security %buildroot%_sysconfdir/security/console.apps/%name

%files
%doc AUTHORS README
%_bindir/%name
%_sbindir/%name
%dir %_datadir/apps/%name/
%_datadir/apps/%name/
%config(noreplace) %_sysconfdir/pam.d/%name
%config(noreplace) %_sysconfdir/security/console.apps/%name

%changelog
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


