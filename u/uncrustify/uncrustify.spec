Name: uncrustify
Version: 0.59
Release: alt1

Summary: Uncrustify is a source code beautifier

License: GPL
Group: Text tools
Url: http://uncrustify.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-%version.tar

# Automatically added by buildreq on Tue Jul 18 2006
BuildRequires: gcc-c++

%description
Uncrustify is a source code beautifier that allows you to banish crusty
code. It works with C, C++, C#, D, and Java and indents (with spaces,
tabs and spaces, and tabs only), adds and removes newlines, has a high
degree of control over operator spacing, aligns code, is extremely
configurable, and is easy to modify.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc README ChangeLog AUTHORS
%_bindir/*
%_datadir/%name/
%_man1dir/*

%changelog
* Mon Oct 10 2011 Vitaly Lipatov <lav@altlinux.ru> 0.59-alt1
- new version 0.59

* Thu Jan 14 2010 Vitaly Lipatov <lav@altlinux.ru> 0.55-alt1
- new version 0.55 (with rpmrb script)
- remove doc subpackage

* Sun Oct 11 2009 Vitaly Lipatov <lav@altlinux.ru> 0.53-alt1
- new version 0.53 (with rpmrb script)

* Mon Jul 28 2008 Vitaly Lipatov <lav@altlinux.ru> 0.48-alt1
- new version 0.48 (with rpmrb script)

* Tue May 27 2008 Vitaly Lipatov <lav@altlinux.ru> 0.46-alt1
- new version 0.46 (with rpmrb script)
- update package (fix #15801), thanks to Slava Semushin

* Tue Jan 22 2008 Vitaly Lipatov <lav@altlinux.ru> 0.43-alt1
- new version 0.43 (with rpmrb script)

* Fri Dec 21 2007 Vitaly Lipatov <lav@altlinux.ru> 0.42-alt1
- new version 0.42 (with rpmrb script)

* Sat Sep 15 2007 Vitaly Lipatov <lav@altlinux.ru> 0.38-alt1
- new version 0.38 (with rpmrb script)

* Thu Jun 21 2007 Vitaly Lipatov <lav@altlinux.ru> 0.34-alt2
- dir datadir/name packing (thanks to php-coder)

* Wed Jun 20 2007 Vitaly Lipatov <lav@altlinux.ru> 0.34-alt1
- new version 0.34 (with rpmrb script)

* Wed Mar 07 2007 Vitaly Lipatov <lav@altlinux.ru> 0.33-alt1
- new version 0.33 (with rpmrb script)

* Sun Sep 10 2006 Vitaly Lipatov <lav@altlinux.ru> 0.26-alt0.1
- new version 0.26 (with rpmrb script)

* Tue Jul 18 2006 Vitaly Lipatov <lav@altlinux.ru> 0.0.22-alt0.1
- initial build for ALT Linux Sisyphus

