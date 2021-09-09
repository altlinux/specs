%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%global optflags_lto %optflags_lto -ffat-lto-objects

Name: barcode
Version: 0.99
Release: alt3
Group: Graphics
Summary: Utility to generate printable barcodes in PostScript format
Summary(ru_RU.UTF-8): Утилита для генерации штрих-кодов для печати в формате PostScript
License: GPLv3
Url: http://www.gnu.org/software/barcode/barcode.html

Source: %name-%version.tar
Patch0: barcode-0.99-info.patch
Patch1: barcode-0.98-leak-fix.patch
Patch2: barcode-0.99-fix-renamed-include.patch
Patch3: barcode-0.99-gcc-10.patch

# Automatically added by buildreq on Wed Jul 08 2009
BuildRequires: ghostscript-utils /usr/bin/tex gcc
# explicitly added texinfo for info files
BuildRequires: texinfo

%description 
The package is meant to solve most needs in barcode creation with a
conventional printer. It can create printouts for the conventional
product tagging standards: UPC-A, UPC-E, EAN-13, EAN-8, ISBN, as well
as a few other formats. Output is generated as either Postscript or
Encapsulated Postscript (other back-ends may be added if needed).

This package includes a command-line barcode generation frontend.

%description -l ru_RU.UTF-8
Этот пакет призван удовлетворить большинство потребностей по созданию
штрих-кодов с помощью обычного принтера. Он может выдавать распечатки
всех основных стандартных кодов, таких, как UPC-A, UPC-E, EAN-13,
EAN-8, ISBN и еще нескольких. Вывод генерируется в Postscript или
Encapsulated Postscript (возможно также добавление иных форматов при
необходимости).

В пакет входят и библиотека, и утилита командной строки, так что вы
можете добавить поддержку генерации штрих-кодов в ваше приложение.

%package -n libbarcode-devel-static
Summary: Library to generate printable barcodes in PostScript format
Summary(ru_RU.UTF-8): Библиотека для генерации штрих-кодов для печати в формате PostScript
Group: System/Libraries
Provides: libbarcode-static-devel = %EVR
Obsoletes: libbarcode-static-devel

%description -n libbarcode-devel-static
The package is meant to solve most needs in barcode creation with a
conventional printer. It can create printouts for the conventional
product tagging standards: UPC-A, UPC-E, EAN-13, EAN-8, ISBN, as well
as a few other formats. Output is generated as either Postscript or
Encapsulated Postscript (other back-ends may be added if needed).

The package includes a static library.

%prep
%setup
%patch0 -p2
%patch1 
%patch2 -p1
%patch3 -p2

# don't build unpackaged binary
sed -i -e 's:barcode sample:barcode:' Makefile.am

%build
%autoreconf
%configure

%make

%install
%makeinstall
install -Dm0644 .libs/libbarcode.a %buildroot%_libdir/libbarcode.a
install -Dm0644 barcode.h %buildroot%_includedir/barcode.h
sed -i '/^#include.*config.h"$/d' %buildroot%_includedir/barcode.h

%files
%defattr(0644,root,root,0755)
%doc README INSTALL TODO NEWS
%attr(0755,root,root) %_bindir/barcode
%_infodir/barcode.info*

%files -n libbarcode-devel-static
%_includedir/barcode.h
%_libdir/libbarcode.a

%changelog
* Thu Sep 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.99-alt3
- Fixed build with LTO.

* Fri Mar 12 2021 Slava Aseev <ptrnine@altlinux.org> 0.99-alt2
- Fixed build with gcc-10
- Rename libbarcode-static-devel to libbarcode-devel-static (closes: #36963)

* Mon Oct 09 2017 Anton Farygin <rider@altlinux.ru> 0.99-alt1
- new version

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.98-alt5.qa2.1
- NMU: added BR: texinfo

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.98-alt5.qa2
- NMU: rebuilt for debuginfo.

* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.98-alt5.qa1
- NMU (by repocop): the following fixes applied:
  * pkg-contains-cvs-or-svn-control-dir for barcode
  * postclean-05-filetriggers for spec file

* Wed Jul 08 2009 Mikhail Yakshin <greycat@altlinux.org> 0.98-alt5
- Fixed texinfo directory entry
- Separated library in separate RPM (closes #13982)

* Thu Aug 09 2007 Mikhail Yakshin <greycat@altlinux.ru> 0.98-alt4
- Fixed encoding, closes bug #12504

* Wed Aug 08 2007 Mikhail Yakshin <greycat@altlinux.ru> 0.98-alt3
- Fixed x86_64 build

* Mon Nov 28 2005 Mikhail Yakshin <greycat@altlinux.org> 0.98-alt2
- Fixed URL and buildreq

* Fri Feb 27 2004 Mikhail Yakshin <greycat@altlinux.org> 0.98-alt1
- Initial build
