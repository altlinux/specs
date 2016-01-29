Name: testng
Version: 6.8.21
Summary: Java-based testing framework
License: ASL 2.0 and CPL
Url: http://testng.org/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.testng:testng) = 6.8.21
Provides: mvn(org.testng:testng::jdk15:) = 6.8.21
Provides: mvn(org.testng:testng:pom:) = 6.8.21
Provides: mvn(org.testng:testng:pom:jdk15:) = 6.8.21
Provides: testng = 6.8.21-2.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.beust:jcommander)
Requires: mvn(org.beanshell:bsh)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: testng-6.8.21-2.fc23.cpio

%description
TestNG is a testing framework inspired from JUnit and NUnit but introducing
some new functionality, including flexible test configuration, and
distributed test running.  It is designed to cover unit tests as well as
functional, end-to-end, integration, etc.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 0:6.8.21-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:6.8.7-alt1_1jpp7
- new release

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 0:6.8-alt1_1jpp7
- new version

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:6.0.1-alt3_4jpp7
- fixed deps

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:6.0.1-alt2_4jpp7
- new release

* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:6.0.1-alt2_1jpp7
- added oss-parent pom dependency

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:6.0.1-alt1_1jpp7
- new version

* Sat Feb 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.8-alt2_2jpp6
- fixed build

* Thu Oct 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.8-alt1_2jpp6
- new version

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.6-alt4_1jpp5
- fixes for java6 support

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.6-alt3_1jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.6-alt2_1jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.6-alt1_1jpp5
- converted from JPackage by jppimport script

