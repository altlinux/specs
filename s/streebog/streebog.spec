%define gitrev 8de633e

Name: 	  streebog
Version:  0.11
Release:  alt1.git%gitrev

Summary:  GOST R 34.11-2012: Streebog Hash Function
License:  BSD
Group:    Other
Url: 	  https://www.streebog.net/
#VCS:	  https://github.com/degtyarevalexey/streebog

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

%description
This is portable implementation of the GOST R 34.11-2012 hash function.
The standard for this hash function developed by the Center for
Information Protection and Special Communications of the Federal
Security Service of the Russian Federation with participation of the
Open joint-stock company "Information Technologies and Communication
Systems" (InfoTeCS JSC).

%prep
%setup

%build
%make_build

%install
install -Dm 0755 gost3411-2012 %buildroot%_bindir/gost3411-2012

%files
%doc README LICENSE
%_bindir/gost3411-2012

%changelog
* Fri Jun 02 2017 Andrey Cherepanov <cas@altlinux.org> 0.11-alt1.git8de633e
- Initial package in Sisyphus

