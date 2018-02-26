Name: mythes-pt
Summary: Portuguese thesaurus
Version: 20060817
Release: alt1
Group: Text tools
URL: http://openthesaurus.caixamagica.pt/
License: GPLv2+

Source0: http://openthesaurus.caixamagica.pt/download/thes_pt_PT_v2.zip

BuildArch: noarch
BuildRequires: unzip

%description
Portuguese thesaurus.

%prep
%setup -q -c

%build
chmod -x *

%install
mkdir -p %buildroot%_datadir/mythes
install -m644 th_pt_PT_v2.* %buildroot%_datadir/mythes

cd %buildroot%_datadir/mythes/
pt_PT_aliases="pt_BR"
for lang in $pt_PT_aliases; do
        ln -s th_pt_PT_v2.idx "th_"$lang"_v2.idx"
        ln -s th_pt_PT_v2.dat "th_"$lang"_v2.dat"
done

%files
%doc README*
%dir %_datadir/mythes
%_datadir/mythes/*

%changelog
* Sun Mar 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 20060817-alt1
- initial release

