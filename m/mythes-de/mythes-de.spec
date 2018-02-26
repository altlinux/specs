Name: mythes-de
Summary: German thesarus
Version: 20070206
Release: alt1
Group: Text tools
URL: http://www.openthesaurus.de
License: LGPL

Source0: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/thes_de_DE_v2.zip

BuildArch: noarch
BuildRequires: unzip

%description
German thesarus.

%prep
%setup -q -c -n %name

%build
chmod -x *

%install
mkdir -p %buildroot/%_datadir/mythes
install -m644 th_de_DE_v2.* %buildroot/%_datadir/mythes

cd %buildroot/%_datadir/mythes/
de_DE_aliases="de_CH"
for lang in $de_DE_aliases; do
        ln -s th_de_DE_v2.idx "th_"$lang"_v2.idx"
        ln -s th_de_DE_v2.dat "th_"$lang"_v2.dat"
done

%files
%doc README*
%dir %_datadir/mythes
%_datadir/mythes/*

%changelog
* Sat Dec 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 20070206-alt1
- initial release

