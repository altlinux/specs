Name:           apache-commons-net
Version:        3.13.0
Release:        alt1

Summary:        Apache Commons Net
License:        Apache-2.0
Group:          Development/Java
URL:            https://commons.apache.org/net/
VCS:            https://github.com/apache/commons-net

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)

BuildArch:      noarch

%description
Apache Commons Net library contains a collection of network utilities and
protocol implementations. Supported protocols include Echo, Finger, FTP, NNTP,
NTP, POP3(S), SMTP(S), Telnet, and Whois.

%javadoc_package

%prep
%setup

%pom_remove_plugin :exec-maven-plugin

%mvn_file : commons-net %name
%mvn_alias :commons-net org.apache.commons:commons-net

%build
# Test disabled due missing deps
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%doc *.md

%changelog
* Wed May 20 2026 Evgeniy Serov <scala@altlinux.org> 3.13.0-alt1
- Updated to 3.13.0.

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:3.6-alt1_16jpp11
- update

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:3.6-alt1_13jpp11
- update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 0:3.6-alt1_8jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.6-alt1_6jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.6-alt1_4jpp8
- fc29 update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.6-alt1_3jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.6-alt1_2jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.5-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.5-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.4-alt1_3jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt1_6jpp8
- new version

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt2_4jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt2_1jpp7
- rebuild with maven-local

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt1_1jpp7
- fc update

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt1_2jpp7
- new version

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt9_6jpp6
- build without clirr plugin

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt8_6jpp6
- fixed build with maven3

* Thu Feb 24 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt7_6jpp6
- added compat osgi provides

* Thu Feb 24 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt6_6jpp6
- rebuild with new osgi.prov

* Thu Feb 24 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt5_6jpp6
- added osgi manifest

* Thu Feb 24 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt4_6jpp6
- added osgi provides

* Thu Feb 24 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt3_6jpp6
- renamed to apache-commons-net

* Fri Dec 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt3_2jpp6
- really added OSGi provides

* Fri Dec 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt2_2jpp6
- added OSGi provides

* Fri Dec 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_2jpp6
- new version

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt3_4jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt2_4jpp5
- converted from JPackage by jppimport script

* Sun Jul 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt2_3jpp1.7
- rebuilt with maven1

* Thu May 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt1_3jpp1.7
- converted from JPackage by jppimport script

* Tue Jun 07 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.4.0-alt1
- New upstream release

* Thu Dec 16 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.0-alt1
- New upstream release
- Use rpm-build-java macros
- Updated Patch0

* Sat Jun 26 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.2-alt1
- New upstream release

* Mon Jun 07 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.1-alt1
- New upstream release

* Tue May 04 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.0-alt1
- New upstream release

* Sun Feb 29 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.0-alt1
- Adapted for Sisyphus from the JPackage project
