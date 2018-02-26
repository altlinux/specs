Name: barcode
Version: 0.98
Release: alt5.qa1
Group: Graphics
Summary: Utility to generate printable barcodes in PostScript format
Summary(ru_RU.UTF-8): Утилита для генерации штрих-кодов для печати в формате PostScript
License: GPL
Url: http://www.gnu.org/software/barcode/barcode.html
Packager: Mikhail Yakshin <greycat@altlinux.org>
Source: %name-%version.tar.gz
Patch: %name-info.patch

# Automatically added by buildreq on Wed Jul 08 2009
BuildRequires: ghostscript-utils /usr/bin/tex gcc

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

%package -n libbarcode-static-devel
Summary: Library to generate printable barcodes in PostScript format
Summary(ru_RU.UTF-8): Библиотека для генерации штрих-кодов для печати в формате PostScript
Group: System/Libraries

%description -n libbarcode-static-devel
The package is meant to solve most needs in barcode creation with a
conventional printer. It can create printouts for the conventional
product tagging standards: UPC-A, UPC-E, EAN-13, EAN-8, ISBN, as well
as a few other formats. Output is generated as either Postscript or
Encapsulated Postscript (other back-ends may be added if needed).

The package includes a static library.

%prep
%setup -q
%patch

%build
%configure
sed -i 's,LIBDIR = $(prefix)/lib,LIBDIR=%buildroot%_libdir,' Makefile
sed -i 's,INFODIR = $(prefix)/info,INFODIR=%buildroot%_infodir,' Makefile
sed -i 's,MAN1DIR = $(prefix)/man/man1,MAN1DIR=%buildroot%_mandir/man1,' Makefile
sed -i 's,MAN3DIR = $(prefix)/man/man3,MAN3DIR=%buildroot%_mandir/man3,' Makefile
cd doc
make clean
cd ..

%make

%install
%makeinstall

# The package contains a CVS/.svn/.git/.hg/.bzr/_MTN directory of revision control system.
# It was most likely included by accident since CVS/.svn/.hg/... etc. directories 
# usually don't belong in releases. 
# When packaging a CVS/SVN snapshot, export from CVS/SVN rather than use a checkout.
find $RPM_BUILD_ROOT -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:
# the find below is useful in case those CVS/.svn/.git/.hg/.bzr/_MTN directory is added as %%doc
find . -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:

%files
%defattr(0644,root,root,0755)
%doc README INSTALL TODO ChangeLog contrib
%attr(0755,root,root) %_bindir/barcode
%_mandir/man1/barcode.1.*
%_mandir/man3/barcode.3.*
%_infodir/barcode.info*

%files -n libbarcode-static-devel
%_includedir/barcode.h
%_libdir/libbarcode.a

%changelog
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
