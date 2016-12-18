Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name byteman
%define version 3.0.6
%global javacup_or_asm java_cup:java_cup|org.ow2.asm:asm-all


%global apphomedir %{_datadir}/%{name}
%global bindir %{apphomedir}/bin

Name:             byteman
Version:          3.0.6
Release:          alt1_1jpp8
Summary:          Java agent-based bytecode injection tool
License:          LGPLv2+
URL:              http://www.jboss.org/byteman
# wget -O 3.0.6.tar.gz https://github.com/bytemanproject/byteman/archive/3.0.6.tar.gz
Source0:          https://github.com/bytemanproject/byteman/archive/%{version}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    maven-shade-plugin
BuildRequires:    maven-failsafe-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-provider-testng
BuildRequires:    maven-surefire-provider-junit
BuildRequires:    maven-verifier-plugin
BuildRequires:    maven-dependency-plugin
BuildRequires:    java_cup
BuildRequires:    jarjar
BuildRequires:    objectweb-asm
BuildRequires:    junit
BuildRequires:    testng
# JBoss modules byteman plugin requires it
BuildRequires:    mvn(org.jboss.modules:jboss-modules)

Provides:         bundled(objectweb-asm) = 0:5.0.4-2
Provides:         bundled(java_cup) = 1:0.11b-3
Source44: import.info
%filter_from_requires /^.*mvn\\(%{javacup_or_asm}\\)$/d

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

%prep
%setup -q -n byteman-%{version}
# Fix doclint problem
%pom_xpath_inject  "pom:plugin[pom:artifactId = 'maven-javadoc-plugin']/pom:configuration" "<additionalparam>-Xdoclint:none</additionalparam>"

# Fix the gid:aid for java_cup
sed -i "s|net.sf.squirrel-sql.thirdparty-non-maven|java_cup|" agent/pom.xml
sed -i "s|java-cup|java_cup|" agent/pom.xml

# Remove scope=system and systemPath for com.sun:tools
%pom_xpath_remove "pom:profiles/pom:profile/pom:dependencies/pom:dependency[pom:artifactId='tools']/pom:scope" install
%pom_xpath_remove "pom:profiles/pom:profile/pom:dependencies/pom:dependency[pom:artifactId='tools']/pom:systemPath" install
%pom_xpath_remove "pom:profiles/pom:profile/pom:dependencies/pom:dependency[pom:artifactId='tools']/pom:scope" contrib/bmunit
%pom_xpath_remove "pom:profiles/pom:profile/pom:dependencies/pom:dependency[pom:artifactId='tools']/pom:systemPath" contrib/bmunit

# Some tests fail intermittently during builds. Disable them.
%pom_disable_module tests contrib/jboss-modules-system
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:executions" contrib/bmunit
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:configuration" '<skip>true</skip>' contrib/bmunit

# Don't build download, docs modules
%pom_disable_module download
%pom_disable_module docs

# Put maven plugin into a separate package
%mvn_package ":byteman-rulecheck-maven-plugin" rulecheck-maven-plugin

%build
%mvn_build

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

ln -s %{_javadir}/byteman/byteman.jar $RPM_BUILD_ROOT%{apphomedir}/lib/byteman.jar

%files -f .mfiles
%{apphomedir}/*
%{_bindir}/*
%doc README docs/ProgrammersGuide.pdf
%doc docs/copyright.txt

%files javadoc -f .mfiles-javadoc
%doc docs/copyright.txt

%files rulecheck-maven-plugin -f .mfiles-rulecheck-maven-plugin
%doc docs/copyright.txt

%changelog
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

