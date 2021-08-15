Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name byteman
# Note to the interested reader:
#   fedpkg mockbuild --without tests
# will make mvn_build macro skip tests.
# See: https://github.com/fedora-java/javapackages/issues/62

%global javacup_or_asm java_cup:java_cup|org\\.ow2\\.asm:asm.*
# Don't have generated mvn()-style requires for java_cup or asm
%global mvn_javacup_or_asm_matcher .*mvn\\(%{javacup_or_asm}\\)
# Don't have generated requires for java-headless >= 1:1.9
%global java_headless_matcher java-headless >= 1:(1\\.9|9)


%global apphomedir %{_datadir}/%{name}
%global bindir %{apphomedir}/bin

Name:             byteman
Version:          4.0.11
Release:          alt2_3jpp11
Summary:          Java agent-based bytecode injection tool
License:          LGPLv2+
URL:              http://www.jboss.org/byteman
# wget -O 4.0.11.tar.gz https://github.com/bytemanproject/byteman/archive/4.0.11.tar.gz
Source0:          https://github.com/bytemanproject/byteman/archive/%{version}.tar.gz

BuildArch:        noarch

# Byteman 4.x requires JDK 9+ to build. Require JDK 10 explicitly.
BuildRequires:    java-11-openjdk-devel
BuildRequires:    maven-local
BuildRequires:    maven-shade-plugin
BuildRequires:    maven-source-plugin
BuildRequires:    maven-plugin-plugin
BuildRequires:    maven-plugin-bundle
BuildRequires:    maven-assembly-plugin
BuildRequires:    maven-failsafe-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-provider-testng
BuildRequires:    maven-surefire-provider-junit
BuildRequires:    maven-surefire-provider-junit5
BuildRequires:    maven-verifier-plugin
BuildRequires:    maven-dependency-plugin
BuildRequires:    java_cup
BuildRequires:    objectweb-asm
BuildRequires:    junit
BuildRequires:    junit5
BuildRequires:    testng
BuildRequires:    mvn(org.apache.maven:maven-project)
# JBoss modules byteman plugin requires it
BuildRequires:    mvn(org.jboss.modules:jboss-modules)

Provides:         bundled(objectweb-asm) = 7.0
Provides:         bundled(java_cup) = 1:0.11b-8
# We are filtering java-headless >= 1:1.9 requirement. Add
# JDK 8 requirement here explicitly which shouldn't match the filter.

# Related pieces removed via pom_xpath_remove macros
Patch1:           remove_submit_integration_test_verification.patch
Patch2:           tests_pom_xml.patch
Source44: import.info
%filter_from_requires /^%{mvn_javacup_or_asm_matcher}|%{java_headless_matcher}$/d

%description
Byteman is a tool which simplifies tracing and testing of Java programs.
Byteman allows you to insert extra Java code into your application,
either as it is loaded during JVM startup or even after it has already
started running. The injected code is allowed to access any of your data
and call any application methods, including where they are private.
You can inject code almost anywhere you want and there is no need to
prepare the original source code in advance nor do you have to recompile,
repackage or redeploy your application. In fact you can remove injected
code and reinstall different code while the application continues to execute.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%package rulecheck-maven-plugin
Group: Development/Java
Summary:          Maven plugin for checking Byteman rules.

%description rulecheck-maven-plugin
This package contains the Byteman rule check maven plugin.

%package bmunit
Group: Development/Java
Summary:          TestNG and JUnit integration for Byteman.

%description bmunit
The Byteman bmunit jar provides integration of Byteman into
TestNG and JUnit tests.

%package dtest
Group: Development/Java
Summary:          Remote byteman instrumented testing.

%description dtest
The Byteman dtest jar supports instrumentation of test code executed on
remote server hosts and validation of assertions describing the expected
operation of the instrumented methods.

%prep
%setup -q -n byteman-%{version}

# Fix the gid:aid for java_cup
sed -i "s|net.sf.squirrel-sql.thirdparty-non-maven|java_cup|" agent/pom.xml
sed -i "s|java-cup|java_cup|" agent/pom.xml
sed -i "s|net.sf.squirrel-sql.thirdparty-non-maven|java_cup|" tests/pom.xml
sed -i "s|java-cup|java_cup|" tests/pom.xml

# Remove Submit integration test invocations (agent)
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-failsafe-plugin']/pom:executions/pom:execution[pom:id='submit.TestSubmit']" agent
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-failsafe-plugin']/pom:executions/pom:execution[pom:id='submit.TestSubmit.compiled']" agent
%patch1 -p2
%patch2 -p2

# Remove Submit integration test invocations (tests)
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-failsafe-plugin']/pom:executions/pom:execution[pom:id='submit.TestSubmit']" tests
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-failsafe-plugin']/pom:executions/pom:execution[pom:id='submit.TestSubmit.compiled']" tests

# Remove scope=system and systemPath for com.sun:tools
%pom_xpath_remove "pom:profiles/pom:profile/pom:dependencies/pom:dependency[pom:artifactId='tools']/pom:scope" install
%pom_xpath_remove "pom:profiles/pom:profile/pom:dependencies/pom:dependency[pom:artifactId='tools']/pom:systemPath" install
%pom_xpath_remove "pom:profiles/pom:profile/pom:dependencies/pom:dependency[pom:artifactId='tools']/pom:scope" contrib/bmunit
%pom_xpath_remove "pom:profiles/pom:profile/pom:dependencies/pom:dependency[pom:artifactId='tools']/pom:systemPath" contrib/bmunit

# Some tests fail intermittently during builds. Disable them.
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:executions" contrib/bmunit
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:configuration" '<skip>true</skip>' contrib/bmunit

# Don't build download, docs modules
%pom_disable_module download
%pom_disable_module docs

# Don't use javadoc plugin, use XMvn for javadocs
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_xpath_remove 'pom:execution[pom:id="make-javadoc-assembly"]' byteman

# Put byteman-rulecheck-maven-plugin into a separate package
%mvn_package ":byteman-rulecheck-maven-plugin" rulecheck-maven-plugin
# Put byteman-bmunit/byteman-dtest into a separate packages since they
# runtime require junit
%mvn_package ":byteman-bmunit" bmunit
%mvn_package ":byteman-dtest" dtest

%build
#export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
# Use --xmvn-javadoc so as to avoid maven-javadoc-plugin issue
# (fixed in 3.1.0, fedora has 3.0.1):
# See https://issues.apache.org/jira/browse/MJAVADOC-555
#     https://bugs.openjdk.java.net/browse/JDK-8212233
%mvn_build --xmvn-javadoc

%install
%mvn_install

install -d -m 755 $RPM_BUILD_ROOT%{_bindir}

install -d -m 755 $RPM_BUILD_ROOT%{apphomedir}
install -d -m 755 $RPM_BUILD_ROOT%{apphomedir}/lib
install -d -m 755 $RPM_BUILD_ROOT%{bindir}

install -m 755 bin/bmsubmit.sh $RPM_BUILD_ROOT%{bindir}/bmsubmit
install -m 755 bin/bminstall.sh  $RPM_BUILD_ROOT%{bindir}/bminstall
install -m 755 bin/bmjava.sh  $RPM_BUILD_ROOT%{bindir}/bmjava
install -m 755 bin/bmcheck.sh  $RPM_BUILD_ROOT%{bindir}/bmcheck

for f in bmsubmit bmjava bminstall bmcheck; do
cat > $RPM_BUILD_ROOT%{_bindir}/${f} << EOF
#!/bin/sh

export BYTEMAN_HOME=/usr/share/byteman
export JAVA_HOME=/usr/lib/jvm/java

\$BYTEMAN_HOME/bin/${f} \$*
EOF
done

chmod 755 $RPM_BUILD_ROOT%{_bindir}/*

for m in bmunit dtest install sample submit; do
  ln -s %{_javadir}/byteman/byteman-${m}.jar $RPM_BUILD_ROOT%{apphomedir}/lib/byteman-${m}.jar
done

# Create contrib/jboss-module-system structure since bminstall expects it
# for the -m option.
install -d -m 755 $RPM_BUILD_ROOT%{apphomedir}/contrib
install -d -m 755 $RPM_BUILD_ROOT%{apphomedir}/contrib/jboss-modules-system
ln -s %{_javadir}/byteman/byteman-jboss-modules-plugin.jar $RPM_BUILD_ROOT%{apphomedir}/contrib/jboss-modules-system/byteman-jboss-modules-plugin.jar

ln -s %{_javadir}/byteman/byteman.jar $RPM_BUILD_ROOT%{apphomedir}/lib/byteman.jar

%files -f .mfiles
%{apphomedir}/lib/byteman.jar
%{apphomedir}/lib/byteman-install.jar
%{apphomedir}/lib/byteman-sample.jar
%{apphomedir}/lib/byteman-submit.jar
%{apphomedir}/contrib/*
%{bindir}/*
%{_bindir}/*
%doc README
%doc --no-dereference docs/copyright.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference docs/copyright.txt

%files rulecheck-maven-plugin -f .mfiles-rulecheck-maven-plugin
%doc --no-dereference docs/copyright.txt

%files bmunit -f .mfiles-bmunit
%doc --no-dereference docs/copyright.txt
%{apphomedir}/lib/byteman-bmunit.jar

%files dtest -f .mfiles-dtest
%doc --no-dereference docs/copyright.txt
%{apphomedir}/lib/byteman-dtest.jar

%changelog
* Sun Aug 15 2021 Igor Vlasenko <viy@altlinux.org> 4.0.11-alt2_3jpp11
- fixed build

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 4.0.11-alt1_3jpp11
- new version

* Mon May 10 2021 Igor Vlasenko <viy@altlinux.org> 4.0.5-alt1_5jpp11
- update

* Sun Jul 14 2019 Igor Vlasenko <viy@altlinux.ru> 4.0.5-alt1_3jpp9
- new version

* Sat Jul 06 2019 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt1_2jpp9
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.6-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.6-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.6-alt1_3jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.6-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.4-alt1_1jpp8
- new version

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.4.1-alt1_7jpp8
- java8 mass update

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.4.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.4-alt1_3jpp7
- new version

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_5jpp7
- new fc release

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_4jpp7
- fc build

