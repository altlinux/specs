Name: hyphen-uk
Summary: Ukrainian hyphenation rules
Version: 20021219
Release: alt3
Group: Text tools
URL: http://lingucomponent.openoffice.org/hyphenator.html
License: GPL

Requires: libhyphen

Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/hyph_uk_UA.zip

BuildArch: noarch
BuildRequires: unzip

%description
Ukrainian hyphenation rules.

%prep
%setup -q -c -n %name

%build
chmod -x *

%install
mkdir -p %buildroot%_datadir/hyphen
iconv -fKOI8-U -tUTF-8 hyph_uk_UA.dic > %buildroot%_datadir/hyphen/hyph_uk_UA.dic
subst 's|^KOI8-U|UTF-8|' %buildroot%_datadir/hyphen/hyph_uk_UA.dic

cd %buildroot%_datadir/hyphen/
uk_UA_aliases="uk"
for lang in $uk_UA_aliases; do
	ln -s hyph_uk_UA.dic hyph_$lang.dic
done

%files
%doc README*
%_datadir/hyphen/*

%changelog
* Sun Mar 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 20021219-alt3
- convert to UTF-8

* Sun Dec 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 20021219-alt2
- new varient alias

* Sat Dec 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 20021219-alt1
- initial release
