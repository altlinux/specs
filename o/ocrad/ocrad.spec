Name: ocrad
Version: 0.28
Release: alt1

Summary: Ocrad is an OCR program based on a feature extraction method
License: GPLv3+
Group: Office

Url: http://www.gnu.org/software/ocrad/ocrad.html

Packager: Ilya Mashkin <oddity@altlinux.ru>


# Source-url: https://mirror.tochlab.net/pub/gnu/ocrad/ocrad-%version.tar.lz
Source: %name-%version.tar

# Automatically added by buildreq on Sat Nov 15 2008
BuildRequires: gcc-c++ lzip libpng-devel

%description
GNU Ocrad is an OCR (Optical Character Recognition) program based on a
feature extraction method. It reads a bitmap image in pbm format and
produces text in byte (8-bit) or UTF-8 formats.

%prep
%setup

%build
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
./configure --prefix=%prefix
%make_build CXXFLAGS="%optflags"

%install
%makeinstall
make install-man DESTDIR=%buildroot

%check
make check

%files
%doc AUTHORS ChangeLog INSTALL NEWS README
%_bindir/*
%_infodir/*
%_man1dir/*

%changelog
* Wed Jan 26 2022 Ilya Mashkin <oddity@altlinux.ru> 0.28-alt1
- 0.28

* Thu Nov 11 2021 Ilya Mashkin <oddity@altlinux.ru> 0.27-alt2
- Fix FTBFS
- Update License tag to GPLv3+

* Fri Jun 28 2019 Vitaly Lipatov <lav@altlinux.ru> 0.27-alt1
- new version (0.27) with rpmgs script

* Thu Dec 10 2015 Ilya Mashkin <oddity@altlinux.ru> 0.25-alt1
- 0.25

* Wed Sep 04 2013 Ilya Mashkin <oddity@altlinux.ru> 0.22-alt1
- 0.22

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.20-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Dec 12 2010 Ilya Mashkin <oddity@altlinux.ru> 0.20-alt1
- 0.20

* Sun Jul 19 2009 Ilya Mashkin <oddity@altlinux.ru> 0.17-alt4
- fix build with gcc
- remove depracated macros

* Sat Nov 15 2008 Igor Zubkov <icesik@altlinux.org> 0.17-alt3
- fix rebuild with fresh gcc4.3
- buildreq

* Sat Jun 07 2008 Igor Zubkov <icesik@altlinux.org> 0.17-alt2
- fix install info files

* Wed Aug 08 2007 Igor Zubkov <icesik@altlinux.org> 0.17-alt1
- 0.16 -> 0.17

* Mon Jun 18 2007 Igor Zubkov <icesik@altlinux.org> 0.16-alt2
- add Url

* Tue May 22 2007 Igor Zubkov <icesik@altlinux.org> 0.16-alt1
- 0.15 -> 0.16
- use optflags during build
- build with test's

* Sat Apr 29 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.15-alt1
- 0.15

* Fri Feb 17 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.14-alt1
- 0.14

* Mon Oct 17 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.13-alt1
- new version

* Thu Jun 09 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.12-alt1
- 0.12

* Tue Dec 21 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.10-alt1
- 0.10

* Thu Oct 28 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.9-alt1
- new version

* Tue May 25 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.8-alt1
- First version of RPM package.
