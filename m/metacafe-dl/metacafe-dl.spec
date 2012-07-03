Name: metacafe-dl
Version: 2008.07.23
Release: alt2.1.1

Summary: Download videos from Metacafe
License: MIT
Group: Networking/File transfer
Url: http://www.arrakis.es/~rggi3/metacafe-dl/

Source0: metacafe-dl

Packager: Igor Zubkov <icesik@altlinux.org>

BuildArch: noarch

%description
Metacafe-dl is a small command-line program to download videos 
from MetaCafe.com.

%install
mkdir -p %buildroot%_bindir/
install -pm 755 %SOURCE0 %buildroot%_bindir/metacafe-dl

%files
%_bindir/metacafe-dl

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2008.07.23-alt2.1.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2008.07.23-alt2.1
- Rebuilt with python 2.6

* Sat Sep 19 2009 Igor Zubkov <icesik@altlinux.org> 2008.07.23-alt2
- remove symlink

* Sun Jul 27 2008 Igor Zubkov <icesik@altlinux.org> 2008.07.23-alt1
- build as sepatated package
- update Url
- [metacafe-dl] 2008.06.07 -> 2008.07.23

* Thu Jul 10 2008 Igor Zubkov <icesik@altlinux.org> 2008.06.08-alt1
- youtube-dl from 2008.06.08
- metacafe-dl from 2008.06.07
- pornotube-dl from 2008.06.03

* Sun Feb 03 2008 Grigory Batalov <bga@altlinux.ru> 2008.01.28-alt1.1
- Rebuilt with python-2.5.

* Tue Jan 29 2008 Pavlov Konstantin <thresh@altlinux.ru> 2008.01.28-alt1
- youtube-dl from 2008.01.24.

* Tue Nov 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 2007.10.12-alt1
- youtube-dl from 2007.10.12.
- metacafe-dl from 2007.10.09.
- pornotube-dl from 2007.10.09.

* Fri Sep 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 2007.09.13-alt1
- youtube-dl from 2007.08.24.
- metacafe-dl from 2007.09.13.

* Wed Jun 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 2007.06.22-alt1
- youtube-dl from 2007.06.22.
- pornotube-dl from 2007.05.22.

* Fri Apr 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 2007.03.27-alt1
- 2007.03.27 version.

* Thu Mar 01 2007 Pavlov Konstantin <thresh@altlinux.ru> 2007.02.18-alt2
- Fix wrong symlink.

* Tue Feb 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 2007.02.18-alt1
- Initial build for ALT Linux.

