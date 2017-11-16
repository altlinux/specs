Name:		luckybackup
Version:	0.4.9
Release:	alt1
Summary:	A powerful, fast and reliable backup and sync tool

Group:		File tools
License:	GPLv3+
URL:		http://luckybackup.sourceforge.net/index.html
Source0:	http://downloads.sourceforge.net/project/%{name}/%{version}/source/%{name}-%{version}.tar.gz

BuildRequires(pre): gcc-c++ qt5-base-devel
BuildRequires:	desktop-file-utils
Requires:	beesu

%define _pkgdocdir %{_docdir}/%{name}-%{version}

%description
luckyBackup is an application that backs-up and/or synchronizes any 
directories with the power of rsync.

It is simple to use, fast (transfers over only changes made and not all data), 
safe (keeps your data safe by checking all declared directories before 
proceeding in any data manipulation ), reliable and fully customizable.

%prep
%setup -q
sed -i 's,/usr/share/doc/luckybackup,%{_pkgdocdir},' luckybackup.pro
sed -i 's,/usr/share/doc/luckybackup/license/gpl.html,%{_pkgdocdir}/license/gpl.html,' src/global.h
sed -i 's,/usr/share/doc/luckybackup/manual/index.html,%{_pkgdocdir}/manual/index.html,' src/global.h
sed -i 's,su-to-root -X -c,/usr/bin/beesu,' menu/%{name}-gnome-su.desktop
chmod a-x manual/index.html

%build
%qmake_qt5
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%files
%doc readme/README readme/changelog
%_bindir/%name
%_desktopdir/%{name}*
%_datadir/%name
%_man8dir/*.8.*
%_datadir/menu
%_pixmapsdir/%{name}*

%changelog
* Thu Nov 16 2017 Andrey Cherepanov <cas@altlinux.org> 0.4.9-alt1
- New version.
- Build with Qt5.

* Tue Mar 17 2015 Andrey Cherepanov <cas@altlinux.org> 0.4.8-alt2
- Initial build in Sisyphus from Fedora Autoimport

