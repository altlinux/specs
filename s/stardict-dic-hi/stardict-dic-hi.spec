Group: Text tools
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           stardict-dic-hi
Version:        3.0.1
Release:        alt2_28
Summary:        Hindi dictionary for stardict

License:        GPL-1.0-or-later
URL:            http://stardict.sourceforge.net/
# URL http://ltrc.iiit.net/downloads/shabdanjali-stardict/shabdanjali-fedora.tgz
# usage: source generate-tarball.sh <version> <org-source-tarball> <initial-name-of-new-tarball>
# usage example: source generate-tarball.sh 3.0.1 shabdanjali-fedora.tgz shabdanjali-fedora
Source0:        shabdanjali-fedora-3.0.1-nobinary.tar.gz
Source1:        generate-tarball.sh
Requires:       stardict stardict-plugin-espeak stardict-plugin-spell
BuildArch:      noarch
Source44: import.info

%description
Hindi dictionary for stardict. The actual dictionary comes from
http://www.iiit.net/ltrc/Dictionaries/gen_eng_hin_hlp.html and Sriram
Chaudhry has converted it to a form usable by stardict.

%prep
%setup -q -n shabdanjali-fedora

%build
# Empty build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/stardict/dic
cp -p -rf shabdanjali* ${RPM_BUILD_ROOT}%{_datadir}/stardict/dic/
chmod 644 README

%files
%doc README
%{_datadir}/stardict/dic/*

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 3.0.1-alt2_28
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt2_17
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt2_15
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt2_13
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt2_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt2_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt2_9
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt2_8
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_8
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_7
- initial release by fcimport

