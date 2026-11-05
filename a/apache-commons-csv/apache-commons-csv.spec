%define _unpackaged_files_terminate_build 1

Name: apache-commons-csv
Version: 1.14.1
Release: alt1

Summary: Utilities to assist with handling of CSV files
License: Apache-2.0
Group: Development/Java
URL: https://commons.apache.org/proper/commons-csv/
VCS: https://github.com/apache/commons-csv.git

Source: %name-%version.tar
Patch: bootstrap-jdbc-tests.patch

BuildArch: noarch
BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(commons-codec:commons-codec)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apache.commons:commons-parent:pom:)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(com.github.spotbugs:spotbugs-annotations)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)

%description
Apache Commons CSV provides a common interface for reading and writing
CSV files in a variety of formats.

%package javadoc
Summary: API documentation for %name
Group: Development/Java

%description javadoc
API documentation for Apache Commons CSV.

%prep
%setup -q
%autopatch -p1

# Retain all ordinary unit tests; upstream already excludes JMH benchmarks.
%pom_remove_dep org.openjdk.jmh:jmh-core
# Break the test-only commons-csv -> H2 -> JTS -> commons-csv cycle.
%pom_remove_dep com.h2database:h2

%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :spotbugs-maven-plugin

%mvn_file ":{*}" %name @1
%mvn_alias : commons-csv:

%build
%mvn_build -- -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc RELEASE-NOTES.txt LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Oct 30 2026 Ivan Khanas <xeno@altlinux.org> 1.14.1-alt1
- New version.

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_2jpp8
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_4jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_3jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_2jpp8
- java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_1jpp8
- new version

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_1jpp8
- new version

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.7.svn1071189jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.6.svn1071189jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.3.svn1071189jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.3.svn1071189jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.3.svn1071189jpp7
- new version
