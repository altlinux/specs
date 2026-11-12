%define _unpackaged_files_terminate_build 1

Name: spock
Version: 2.5
Release: alt1

Summary: Testing and specification framework for Java and Groovy
License: Apache-2.0
Group: Development/Java
URL: https://spockframework.org
VCS: https://github.com/spockframework/spock.git
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-offline.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-17-openjdk-devel
BuildRequires: xgradle
BuildRequires: groovy
BuildRequires: mvn(org.apache.groovy:groovy-ant)
BuildRequires: mvn(org.apache.groovy:groovy-templates)
BuildRequires: mvn(org.apache.groovy:groovy-test)
BuildRequires: mvn(org.apache.groovy:groovy-sql)
BuildRequires: mvn(org.apache.groovy:groovy-nio)
BuildRequires: mvn(org.apache.groovy:groovy-jmx)
BuildRequires: mvn(io.leangen.geantyref:geantyref)
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.junit.platform:junit-platform-testkit)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.junit.platform:junit-platform-console)
BuildRequires: mvn(org.hamcrest:hamcrest)
BuildRequires: mvn(org.ow2.asm:asm-util)
BuildRequires: mvn(net.bytebuddy:byte-buddy)
BuildRequires: mvn(net.bytebuddy:byte-buddy-agent)
BuildRequires: mvn(cglib:cglib-nodep)
BuildRequires: mvn(org.objenesis:objenesis)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(com.google.inject:guice)
BuildRequires: mvn(com.h2database:h2)
BuildRequires: mvn(junit:junit)

%description
Spock is a testing and specification framework for Java and Groovy.
This package provides the core engine, JUnit 4 and Guice integrations,
and the matching bill of materials for the system Groovy 6 variant.

%prep
%setup
%autopatch -p1
cp rpm-settings.gradle settings.gradle
cp rpm-build.gradle build.gradle

%build
%gradle_publish

%install
%gradle_register --artifacts=spock-
%gradle_register_bom --artifacts=spock-bom
%gradle_install

%check
gradle test --offline

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 2.5-alt1
- New version.

* Wed Jun 06 2018 Igor Vlasenko <viy@altlinux.ru> 0.7-alt4_0.17.groovy.2.0jpp8
- fixed build with new ant

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 0.7-alt3_0.17.groovy.2.0jpp8
- fixed build

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.7-alt3_0.14.groovy.2.0jpp8
- new fc release

* Fri Dec 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.7-alt3_0.13.groovy.2.0jpp8
- new fc release

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.7-alt3_0.9.groovy.2.0jpp8
- unbootstrap build

* Mon Apr 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt2_0.3%(echo -groovy-1.8 | tr - . )jpp7
- fixed build with new junit

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_0.3%(echo -groovy-1.8 | tr - . )jpp7
- new version
