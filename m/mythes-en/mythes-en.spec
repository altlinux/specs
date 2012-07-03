Name: mythes-en
Summary: English thesarus
Version: 2.1
Release: alt1
Group: Text tools
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
License: BSD

Source0: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/thes_en_US_v2.zip

BuildArch: noarch
BuildRequires: unzip

%description
English thesarus.

%prep
%setup -q -c -n %name

%build
chmod -x *

%install
mkdir -p %buildroot/%_datadir/mythes
install -m644 th_en_US_v2.* %buildroot/%_datadir/mythes

cd %buildroot/%_datadir/mythes/
en_US_aliases="en_AU en_BS en_BZ en_CA en_GH en_GB en_IE en_IN en_JM en_NA en_NZ en_PH en_TT en_ZA en_ZW"
for lang in $en_US_aliases; do
        ln -s th_en_US_v2.idx "th_"$lang"_v2.idx"
        ln -s th_en_US_v2.dat "th_"$lang"_v2.dat"
done

%files
%doc README*
%dir %_datadir/mythes
%_datadir/mythes/*

%changelog
* Sat Dec 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 2.1-alt1
- initial release

