Name: youtube-dl
Version: 2011.08.04
Release: alt1.1

Summary: Download videos from YouTube
License: Public domain
Group: Networking/File transfer
Url: http://bitbucket.org/rg3/youtube-dl/wiki/Home

Source0: youtube-dl

Packager: Igor Zubkov <icesik@altlinux.org>

BuildArch: noarch

%description
Youtube-dl is a small command-line program to download videos
from YouTube.com.

%install
mkdir -p %buildroot%_bindir/
install -pm 755 %SOURCE0 %buildroot%_bindir/youtube-dl

%files
%_bindir/youtube-dl

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2011.08.04-alt1.1
- Rebuild with Python-2.7

* Fri Aug 05 2011 Mykola Grechukh <gns@altlinux.ru> 2011.08.04-alt1
- 2010.12.09 -> 2011.08.04

* Fri Dec 24 2010 Mykola Grechukh <gns@altlinux.ru> 2010.12.09-alt1
- 2010.08.04 -> 2010.12.09

* Fri Aug 27 2010 Mykola Grechukh <gns@altlinux.ru> 2010.08.04-alt1
- 2010.03.13 -> 2010.08.04

* Sun Mar 14 2010 Igor Zubkov <icesik@altlinux.org> 2010.03.13-alt1
- 2010.01.19 -> 2010.03.13

* Sat Jan 23 2010 Igor Zubkov <icesik@altlinux.org> 2010.01.19-alt1
- 2010.01.06 -> 2010.01.19

* Tue Jan 12 2010 Igor Zubkov <icesik@altlinux.org> 2010.01.06-alt1
- 2009.12.26 -> 2010.01.06

* Tue Dec 29 2009 Igor Zubkov <icesik@altlinux.org> 2009.12.26-alt1
- 2009.09.13 -> 2009.12.26

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2009.09.13-alt1.1
- Rebuilt with python 2.6

* Sat Sep 19 2009 Igor Zubkov <icesik@altlinux.org> 2009.09.13-alt1
- 2009.09.08 -> 2009.09.13

* Sun Sep 13 2009 Igor Zubkov <icesik@altlinux.org> 2009.09.08-alt1
- 2009.08.08 -> 2009.09.08

* Wed Aug 26 2009 Igor Zubkov <icesik@altlinux.org> 2009.08.08-alt1
- 2009.06.29 -> 2009.08.08

* Fri Jul 31 2009 Igor Zubkov <icesik@altlinux.org> 2009.06.29-alt1
- 2009.03.03 -> 2009.06.29

* Wed Mar 25 2009 Igor Zubkov <icesik@altlinux.org> 2009.03.03-alt1
- 2008.11.01 -> 2009.03.03

* Sun Nov 16 2008 Igor Zubkov <icesik@altlinux.org> 2008.11.01-alt1
- 2008.07.26 -> 2008.11.01

* Sun Jul 27 2008 Igor Zubkov <icesik@altlinux.org> 2008.07.26-alt1
- youtube-dl from  2008.07.26
- move metacafe-dl and pornotube-dl to separate packages
- update License -> Public domain

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

