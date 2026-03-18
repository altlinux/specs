Name:           joda-time
Version:        2.14.0
Release:        alt1

Summary:        Joda-Time is the widely used replacement for the Java date and time classes prior to Java SE 8
License:        Apache-2.0
Group:          Development/Java
URL:            http://www.joda.org/joda-time/
VCS:            https://github.com/JodaOrg/joda-time

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.joda:joda-convert)

BuildArch:      noarch

%description
Joda-Time provides a quality replacement for the Java date and time classes. The
design allows for multiple calendar systems, while still providing a simple API.
The 'default' calendar is the ISO8601 standard which is used by XML. The
Gregorian, Julian, Buddhist, Coptic, Ethiopic and Islamic systems are also
included, and we welcome further additions. Supporting classes include time
zone, duration, format and parsing.

%javadoc_package

%prep
%setup

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

%build
%mvn_build -- -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc RELEASE-NOTES.txt LICENSE.txt NOTICE.txt *.md

%changelog
* Thu Mar 05 2026 Evgeniy Seroc <scala@altlinux.org> 2.14.0-alt1
- Updated to 2.14.0.
- Returned to Sisyphus.

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:2.9.9-alt1_9.tzdata2017bjpp11
- update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.9.9-alt1_6.tzdata2017bjpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.9.9-alt1_4.tzdata2017bjpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.9.9-alt1_3.tzdata2017bjpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.9.9-alt1_2.tzdata2017bjpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.9.9-alt1_1.tzdata2017bjpp8
- new version

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.9.3-alt1_4.tzdata2016cjpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.9.3-alt1_3.tzdata2016cjpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.9.3-alt1_2.tzdata2016cjpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.9.2-alt1_1jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.8.1-alt1_1.tzdata2015ejpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_1.tzdata2013gjpp7
- new release

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_1.tzdata2013cjpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt4_8.tzdata2011fjpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt3_8.tzdata2011fjpp7
- NMU rebuild to move poms and fragments

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt2_8.tzdata2011fjpp7
- fixed build

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt1_8.tzdata2011fjpp7
- new version

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt4_2jpp6
- fixed build with moved maven1

* Sun Dec 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt3_2jpp6
- jpp 6.0 build

* Sat Jan 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt3_1jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt2_1jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt1_1jpp5
- converted from JPackage by jppimport script

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_2jpp1.7
- updated to new jpackage release

* Tue Jul 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

