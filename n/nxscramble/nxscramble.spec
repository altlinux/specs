Name: nxscramble
Version: 0.1
Release: alt4

Summary: Utility which scrambles password string same way as Nomachine NX client
Group: Text tools
License: GPL

Source: %name-%version.tar

Url: http://www.nomachine.com/ar/view.php?ar_id=AR01C00125
Packager: Lenar Shakirov <snejok@altlinux.org>

BuildRequires: libxml2-devel libqt4-devel cmake gcc-c++ qt4-settings

%description
Small tool which scrambles an plain text string the same way as Nomachine
NX Client does it.

%prep
%setup

%build
cd build
cmake ..
%make

%install
cd build
%makeinstall DESTDIR=%buildroot

%files
%_bindir/nxscramble

%changelog
* Tue May 26 2009 Lenar Shakirov <snejok@altlinux.ru> 0.1-alt4
- Url added. Thanks to repocop!

* Fri Dec 26 2008 Lenar Shakirov <snejok@altlinux.ru> 0.1-alt3
- BuildRequires updated

* Fri Dec 26 2008 Lenar Shakirov <snejok@altlinux.ru> 0.1-alt2
- New packager

* Wed Mar 26 2008 Maxim Ivanov <redbaron@altlinux.ru> 0.1-alt1
- Initial build for Sisyphus

