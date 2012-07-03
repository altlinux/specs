Name: hyphen-pt
Summary: Portuguese hyphenation rules
Version: 20021021
Release: alt1
Group: Text tools
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: GPL+

Requires: libhyphen

Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/hyph_pt_PT.zip

BuildArch: noarch
BuildRequires: unzip

%description
Portuguese hyphenation rules.

%prep
%setup -q -c

%build
chmod -x *

%install
mkdir -p %buildroot%_datadir/hyphen
iconv -fISO8859-1 -tUTF-8 hyph_pt_PT.dic > %buildroot%_datadir/hyphen/hyph_pt_PT.dic
subst 's|^ISO8859-1|UTF-8|' %buildroot%_datadir/hyphen/hyph_pt_PT.dic

cd %buildroot%_datadir/hyphen/
pt_PT_aliases="pt pt_BR"
for lang in $pt_PT_aliases; do
	ln -s hyph_pt_PT.dic hyph_$lang.dic
done

%files
%doc README*
%_datadir/hyphen/*

%changelog
* Sun Mar 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 20021021-alt1
- initial release

