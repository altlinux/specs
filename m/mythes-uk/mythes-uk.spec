Name: mythes-uk
Summary: Ukrainian thesaurus
Version: 1.5.7
Release: alt1
Group: Text tools
License: GPLv2+ or LGPLv2+
URL: http://sourceforge.net/projects/ispell-uk

Source0: http://downloads.sourceforge.net/ispell-uk/spell-uk-%version.tgz

BuildArch: noarch

%description
Ukrainian thesaurus.

%prep
%setup -q -n spell-uk-%version

%build
cd src/thesaurus
mv -f th_uk_UA.dat th_uk_UA_v2.dat
../../bin/th_gen_idx.pl < th_uk_UA_v2.dat > th_uk_UA_v2.idx

%install
mkdir -p %buildroot/%_datadir/mythes
install -m644 src/thesaurus/th_uk_UA_v2.* %buildroot/%_datadir/mythes

%files
%doc README*
%dir %_datadir/mythes
%_datadir/mythes/*

%changelog
* Sun Mar 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.5.7-alt1
- initial release

