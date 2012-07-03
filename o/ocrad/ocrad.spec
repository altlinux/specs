Name: ocrad
Version: 0.20
Release: alt1

Summary: Ocrad is an OCR program based on a feature extraction method
License: GPL
Group: Office

Url: http://www.gnu.org/software/ocrad/ocrad.html

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source0: %name-%version.tar.gz

# from Debian
Patch0: ocrad_0.17-3.diff.gz
Patch1: ocrad-0.17-gcc43.patch
# Automatically added by buildreq on Sat Nov 15 2008
BuildRequires: gcc-c++

%description
GNU Ocrad is an OCR (Optical Character Recognition) program based on a
feature extraction method. It reads a bitmap image in pbm format and
produces text in byte (8-bit) or UTF-8 formats.

%prep
%setup -q
#patch0 -p1
#patch1 -p1 -b .gcc43

%build
./configure --prefix=%prefix
make CXXFLAGS="%optflags"
make check || exit 1

%install
%makeinstall
make install-man DESTDIR=%buildroot


%files
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%_bindir/*
%_infodir/*
%_man1dir/*

%changelog
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
