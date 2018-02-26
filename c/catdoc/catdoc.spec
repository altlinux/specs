Name: catdoc
Version: 0.94.2
Release: alt4

Summary: Converts MS-Word and MS-Excel files to text

License: GPL
Group: Office
Url: http://www.wagner.pp.ru/~vitus/software/catdoc/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://ftp.wagner.pp.ru/pub/catdoc/%name-%version.tar.bz2
Source1: xlsview

Patch1: catdoc-0.93.4-page-option.patch
Patch2: catdoc-fix-broken-formatting.patch
Requires: tk, mktemp >= 1:1.3.1, url_handler

BuildRequires: groff-base groff-ps tcl tk

%description
CATDOC is program which reads MS-Word file and prints readable
ASCII text to stdout, just like Unix cat command.
It also able to produce correct escape sequences if some UNICODE
charachers have to be represented specially in your typesetting system
such as (La)TeX.

It features runtime configuration, proper charset handling,
user-definable output formats and support
for Word97 files, which contain UNICODE internally.

xls2csv reads MS-Excel spreadsheet and dumps its content as
comma-separated values to stdout.

%prep
%setup -q
%patch1 -p1
#%patch2 -p1
export man1dir=%_man1dir
%configure --with-install-root="%buildroot"

%build
%make_build

%install
%make_install install
install -pD -m755 %SOURCE1 %buildroot%_bindir/xlsview

%files
%_bindir/catdoc
%_bindir/catppt
%_bindir/wordview
%_bindir/xlsview
%_bindir/xls2csv
%_datadir/%name/
%_man1dir/*
%doc README NEWS CREDITS

%changelog
* Thu Mar 31 2011 Slava Semushin <php-coder@altlinux.ru> 0.94.2-alt4
- NMU
- Updated BuildRequires to get rid of xorg-x11-libs (fixed build)

* Mon Oct 12 2009 Slava Semushin <php-coder@altlinux.ru> 0.94.2-alt3
- NMU
- Fixed xls2csv crashing (Closes: #21802)

* Fri Aug 03 2007 Vitaly Lipatov <lav@altlinux.ru> 0.94.2-alt2
- fix URL, fix Source URL

* Sun May 21 2006 Vitaly Lipatov <lav@altlinux.ru> 0.94.2-alt1
- new version (0.94.2)
- fix URL

* Sat Nov 05 2005 Vitaly Lipatov <lav@altlinux.ru> 0.94-alt1
- new version

* Thu Jun 02 2005 Vitaly Lipatov <lav@altlinux.ru> 0.93.4-alt3
- add patches (bug #6993): added -p option, fixed bad formatting as date

* Wed Jan 05 2005 Vitaly Lipatov <lav@altlinux.ru> 0.93.4-alt2
- fixed bugs #5793, #5794

* Thu Dec 09 2004 Vitaly Lipatov <lav@altlinux.ru> 0.93.4-alt1
- new version
- fix path to url_handler in xlsview 
- cleanup spec

* Tue Nov 18 2003 Ott Alex <ott@altlinux.ru> 0.93.3-alt1
- New version, many improvments

* Tue Sep 30 2003 Ott Alex <ott@altlinux.ru> 0.93.1-alt1
- New version

* Thu Sep 25 2003 Ott Alex <ott@altlinux.ru> 0.93-alt2
- Fixing url's in spec

* Mon Sep 22 2003 Ott Alex <ott@altlinux.ru> 0.93-alt1
- New release

* Tue Nov 12 2002 AEN <aen@altlinux.ru> 0.91.5-alt4
- rebuilt with gcc-3.2

* Tue Apr 16 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.91.5-alt3
- Fixed xlsview (#0000020, #0000021).
- Specfile cleanup.

* Mon Apr 15 2002 AEN <aen@logic.ru> 0.91.5-alt2
- typo in xlsview fixed

* Mon Apr 15 2002 AEN <aen@logic.ru> 0.91.5-alt1
- new version
- xlsview rewritten

* Tue Jan 30 2001 AEN <aen@logic.ru>
- 0.91.4
* Sat Jan 20 2001 AEN <aen@logic.ru>
- RE adaptation

* Fri Jan 05 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.90.3-4mdk
- rebuild

* Wed Aug 23 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.90.3-3mdk
- BM
- macros

* Tue Apr 25 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.90.3-2mdk
- fix group
- fix files section

* Mon Sep  6 1999 Giuseppe Ghibò <ghibo@linux-mandrake.com>
- First spec file for Mandrake distribution.
