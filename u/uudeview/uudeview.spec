Name: uudeview
Version: 0.5.20
Release: alt5.1

Summary: smart uuenc/xxenc/base64 encoder/decoder
License: GPL
Group: Text tools

Url: http://www.fpx.de/fp/Software/UUDeview
Packager: Vladimir V Kamarzin <vvk@altlinux.ru>
Source: %name-%version.tar
Source1: %name-library.pdf

# Automatically added by buildreq on Tue Mar 16 2004
BuildRequires: sendmail-common tcl-devel tetex-core tetex-dvips tetex-latex tk-devel transfig

%description 
Smart multi-file multi-part decoder for uuencoded,
xxencoded, Base64 and BinHex encoded files. Also
includes a similarly powerful encoder.

%package doc
Requires: %name
Summary: Documentation for uudeview - smart uuenc/xxenc/base64 encoder/decoder
Summary(ru_RU.KOI8-R): Документация для uudeview - быстрого uuenc/xxenc/base64 кодера/декодера
License: GPL
Group: Text tools

%description doc
Smart multi-file multi-part decoder for uuencoded,
xxencoded, Base64 and BinHex encoded files. Also
includes a similarly powerful encoder.
This package includes documentation.

%package -n libuu
Summary: uulib shared library
License: GPL
Group: System/Libraries

%description -n libuu
%summary

%package -n libuu-devel
Summary: Header files for uulib shared library
License: GPL
Group: Development/C

%description -n libuu-devel
%summary

%prep
%setup
install -pDm0644 %SOURCE1 doc/library.pdf

%build
%add_optflags %optflags_shared
%configure
%make_build
make -C doc ps 

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir
mkdir -p %buildroot%_datadir/doc/%name-%version
%makeinstall prefix=%buildroot/usr execprefix=%buildroot/usr BINDIR=%buildroot%_bindir MANDIR=%buildroot%_mandir
%makeinstall -C uulib

%files 
%_bindir/*
%_man1dir/*
%doc HISTORY INSTALL README

%files -n libuu
%_libdir/libuu.so.*

%files -n libuu-devel
%_includedir/*.h
%_libdir/libuu.so

%files doc
%doc doc/library.ps doc/library.dvi doc/library.ltx doc/library.pdf

%changelog
* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.20-alt5.1
- Rebuilt for soname set-versions

* Fri Oct 23 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.5.20-alt5
- Add libuu and libuu-devel packages.

* Fri Apr 17 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.5.20-alt4
- Revert uudeview-0.5.20-unknown_filename_fix.patch (Closes: #5976)

* Wed Aug 13 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.5.20-alt3
- Security fix: CVE-2008-2266
- Pull in source patches from Debian:
  + Fix temporary file issue (CVE-2004-2265, CVE-2008-2266, DEB#222275)
  + Update uudeview man page, include uuwish man page
  + Don't force overwrite mode if auto-rename enabled, DEB#378076
- Drop uudeview-0.5.20-mkstemp.patch

* Thu Mar 13 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.5.20-alt2
- Rebuild with libtcl8.5

* Fri Nov 03 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 0.5.20-alt1
- Updated to 0.5.20
- uudeview.patch splitted to separate patches
  + uudeview-0.5.20-unknown_filename_fix.patch
  + uudeview-0.5.20-mkstemp.patch
  + other patches unneeded now
- Minor spec cleanup

* Tue Mar 16 2004 Egor S. Orlov <oes@altlinux.ru> 0.5.19-alt2
- Added OpenPKG patch

* Tue Oct 14 2003 Egor S. Orlov <oes@altlinux.ru> 0.5.19-alt1
- New version

* Tue Oct 14 2003 Egor S. Orlov <oes@altlinux.ru> 0.5.18-alt4
- fixed changelog entry

* Mon Oct 13 2003 Egor S. Orlov <oes@altlinux.ru> 0.5.18-alt2
- fixed doc dependency bug

* Thu Sep 25 2003 Egor S. Orlov <oes@altlinux.ru> 0.5.18-alt1
- Initial spec

