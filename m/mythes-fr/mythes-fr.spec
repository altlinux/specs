Name: mythes-fr
Summary: French thesarus
Version: 20050329
Release: alt2
Group: Text tools
URL: http://lingucomponent.openoffice.org/thesaurus.html
License: LGPL

Source0: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/thes_fr_FR_v2.zip

BuildArch: noarch
BuildRequires: unzip

%description
French thesarus.

%prep
%setup -q -c -n %name

%build
chmod -x *

%install
mkdir -p %buildroot%_datadir/mythes
install -m644 th_fr_FR_v2.* %buildroot%_datadir/mythes

cd %buildroot%_datadir/mythes/
fr_FR_aliases="fr_BE"
for lang in $fr_FR_aliases; do
	ln -s th_fr_FR_v2.idx "th_"$lang"_v2.idx"
	ln -s th_fr_FR_v2.dat "th_"$lang"_v2.dat"
done

%files
%doc README*
%dir %_datadir/mythes
%_datadir/mythes/*

%changelog
* Sat Dec 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 20050329-alt2
- new varient alias

* Sat Dec 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 20050329-alt1
- initial release

