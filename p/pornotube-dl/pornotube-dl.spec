Name: pornotube-dl
Version: 2008.06.08
Release: alt3.1.1

Summary: Download videos from PornoTube
License: MIT
Group: Networking/File transfer
Url: http://www.arrakis.es/~rggi3/pornotube-dl/

Source0: pornotube-dl

Packager: Evgenii Terechkov <evg@altlinux.ru>

BuildArch: noarch

%description
Pornotube-dl is a small command-line program to download videos
from PornoTube.com.

%install
mkdir -p %buildroot%_bindir/
install -pm 755 %SOURCE0 %buildroot%_bindir/pornotube-dl.py

ln -sf pornotube-dl.py %buildroot%_bindir/pornotube-dl

%files
%_bindir/pornotube-dl*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2008.06.08-alt3.1.1
- Rebuild with Python-2.7

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2008.06.08-alt3.1
- Rebuilt with python 2.6

* Sun Mar 29 2009 Terechkov Evgenii <evg@altlinux.ru> 2008.06.08-alt3
- Tech rebuild

* Sun Jul 27 2008 Igor Zubkov <icesik@altlinux.org> 2008.06.08-alt2
- build as separated package
- update Url

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
