Name: pxview
Version: 0.2.5
Release: alt2.1

Summary: View Paradox DB files

License: GPL v2
Url: http://pxlib.sourceforge.net/
Group: Office

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/pxlib/%{name}_%version.orig.tar.bz2
Patch0: pxview-0.2.5-alt-DSO.patch

# Automatically added by buildreq on Tue Feb 06 2007
BuildRequires: docbook-utils gcc-c++ libgsf-devel libpx-devel perl-XML-Parser sqlite-devel w3c-markup-validator-libs

%description
pxview is quite simple command line program which has been originally
created to test pxlib. pxlib is a library to read Paradox files.
During the development pxview has evolved more and more into a useful
program to examine the contents of Paradox files and to convert them
into SQL or CSV format.

%prep
%setup
%patch0 -p2
%__subst "s|/usr/lib|%_libdir|g" configure*
# man pages are build by docbook2man
%__subst 's#docbook-to-man#docbook2man#g' configure*
%__subst 's#docbook-to-man $<.*#docbook2man $<#g' doc/Makefile*
for man in doc/*.sgml; do
        name=$(basename "$man" .sgml)
        sed -i -e "s#$name#$name#gi" $man
done

%build
CPPFLAGS="$(pkg-config glib-2.0 --cflags)"
%configure \
	--with-sqlite \
	--with-gsf
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog
%_bindir/%name
%_man1dir/*

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt2.1
- Fixed build

* Sat Jul 18 2009 Vitaly Lipatov <lav@altlinux.ru> 0.2.5-alt2
- fix build on x86_64

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 0.2.5-alt1
- cleanup spec

* Tue Feb 06 2007 Vitaly Lipatov <lav@altlinux.ru> 0.2.5-alt0.1
- initial build for ALT Linux Sisyphus (spec from PLD)

