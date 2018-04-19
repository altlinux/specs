# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commit bd245c9

Name:           pcfi
Version:        2010.08.09
Release:        alt2_13.20111103gitbd245c9jpp8
Summary:        PDF Core Font Information

Group:          Publishing
License:        BSD
URL:            https://github.com/jukka/pcfi
Source0:        https://github.com/jukka/pcfi/tarball/%{commit}/jukka-pcfi-%{commit}.tar.gz
# Originally downloaded from: http://opensource.adobe.com/wiki/display/cmap/License
# This now points to Adobe's sourceforge pages
Source1:        License
BuildArch:      noarch
BuildRequires:  maven-local
Requires:       jpackage-utils
Source44: import.info


%description
Collection of PDF core font information files downloaded from Adobe's
Developer Center and elsewhere. This collection contains font metrics for the
14 PDF core fonts, CMaps for the PDF CJK fonts and the Adobe Glyph List.   The
files are stored inside the com/adobe/pdf/pcfi directory. See the individual
files for exact licensing information.


%prep
%setup -q -n jukka-pcfi-%{commit}
sed -i 's/\r//' src/main/resources/META-INF/LICENSE.txt
cp %SOURCE1 .


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%doc README.txt src/main/resources/META-INF/LICENSE.txt License


%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2010.08.09-alt2_13.20111103gitbd245c9jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2010.08.09-alt2_12.20111103gitbd245c9jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2010.08.09-alt2_11.20111103gitbd245c9jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2010.08.09-alt2_10.20111103gitbd245c9jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2010.08.09-alt2_9.20111103gitbd245c9jpp8
- new version

* Sun Sep 14 2014 Igor Vlasenko <viy@altlinux.ru> 2010.08.09-alt2_7.20111103gitbd245c9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2010.08.09-alt2_6.20111103gitbd245c9jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2010.08.09-alt2_4.20111103gitbd245c9jpp7
- NMU rebuild to move poms and fragments

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 2010.08.09-alt1_4.20111103gitbd245c9jpp7
- new release

