Name:           stardict-dic-hi
Version:        3.0.1
Release:        alt2_8
Summary:        Hindi dictionary for stardict

Group:          Text tools
License:        GPL+
URL:            http://stardict.sourceforge.net/
# URL http://ltrc.iiit.net/downloads/shabdanjali-stardict/shabdanjali-fedora.tgz
# usage: source generate-tarball.sh <version> <org-source-tarball> <initial-name-of-new-tarball>
# usage example: source generate-tarball.sh 3.0.1 shabdanjali-fedora.tgz shabdanjali-fedora
Source0:        shabdanjali-fedora-3.0.1-nobinary.tar.gz
Source1:        generate-tarball.sh
Requires:       stardict
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
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt2_8
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_8
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_7
- initial release by fcimport

