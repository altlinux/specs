Name: heirloom-doctools
Version: 080407
Release: alt1

Summary: The Heirloom Documentation Tools
License: Various, see LICENSE dir
Group: Text tools

Url: http://heirloom.sf.net/

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source: %name-%version.tar

BuildPreReq: flex gcc-c++

%define basedir %_libexecdir/heirloom
%define makeoptions \\\
	PREFIX=%basedir \\\
	ROOT=%buildroot \\\
	MANDIR=%_mandir/5man \\\
	CFLAGS="%optflags"

#	YACC=%basedir/ccs/bin/yacc \\\
#	LEX=%basedir/ccs/bin/lex \\\


%description
The Heirloom Documentation Tools provide troff, nroff, and related
utilities to format manual pages and other documents for output on
terminals and printers. They are portable and enhanced versions of
the respective OpenSolaris utilities, which descend to ditroff and
the historical Unix troff. troff provides advanced typographical
features such as kerning, tracking, and hanging characters. It can
access PostScript Type 1, OpenType, and TrueType fonts directly.
Internationalized hyphenation, international paper sizes, and UTF-8
input are supported.


%prep
%setup

%build
%make_build %makeoptions

%install
%makeinstall %makeoptions


%files
%doc CHANGES README LICENSE/
%basedir/
%_mandir/5man

%changelog
* Mon Mar 30 2009 Andrey Rahmatullin <wrar@altlinux.ru> 080407-alt1
- initial build
