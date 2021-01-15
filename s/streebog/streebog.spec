%define gitrev 62e2120

Name: 	  streebog
Version:  0.13
Release:  alt1.git%gitrev

Summary:  GOST R 34.11-2012: Streebog Hash Function
License:  BSD-2-Clause or GPL-2.0+
Group:    Other
Url: 	  https://www.streebog.net/
#VCS:	  https://github.com/degtyarevalexey/streebog

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Patch: %name-gcc-10.patch

BuildRequires: help2man

%description
This is portable implementation of the GOST R 34.11-2012 hash function.
The standard for this hash function developed by the Center for
Information Protection and Special Communications of the Federal
Security Service of the Russian Federation with participation of the
Open joint-stock company "Information Technologies and Communication
Systems" (InfoTeCS JSC).

%prep
%setup
%patch -p1
rm -f auto/header/{mmx,sse2,sse41} auto/mk/{mmx,sse2,sse41}
touch auto/{header,mk}/empty

%build
%make_build gost3411-2012-config.h all man

%install
install -Dpm 0755 gost3411-2012 %buildroot%_bindir/gost3411-2012
install -Dpm 0644 gost3411-2012.1 %buildroot%_man1dir/gost3411-2012.1

%files
%doc README.md
%_bindir/gost3411-2012
%_man1dir/gost3411-2012.1*

%changelog
* Fri Jan 15 2021 Andrey Cherepanov <cas@altlinux.org> 0.13-alt1.git62e2120
- New version.
- Fix build by GCC 10.

* Mon Oct 16 2017 Andrey Cherepanov <cas@altlinux.org> 0.11-alt3.git8de633e
- Completely fix for AMD CPUs (ALT #33592)
- Package man page

* Mon Jul 31 2017 Andrey Cherepanov <cas@altlinux.org> 0.11-alt2.git8de633e
- Set compatibility flags (ALT #33592) Solution is supplied by gremlin@

* Fri Jun 02 2017 Andrey Cherepanov <cas@altlinux.org> 0.11-alt1.git8de633e
- Initial package in Sisyphus

