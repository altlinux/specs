Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name apache-commons-jci
%define version 1.1
%global base_name  jci
%global short_name commons-%{base_name}
%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}

Name:          apache-commons-jci
Version:       1.1
Release:       alt1_3jpp8
Summary:       Commons Java Compiler Interface
License:       ASL 2.0
URL:           http://commons.apache.org/jci/
Source0:       http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{namedversion}-src.tar.gz
Patch0:        %{name}-1.1-janino27.patch

BuildRequires: maven-local
BuildRequires: maven-antrun-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: ecj >= 3.4.2
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(org.apache.commons:commons-parent:pom:)
BuildRequires: mvn(org.codehaus.groovy:groovy)
BuildRequires: mvn(org.codehaus.janino:janino)
BuildRequires: mvn(rhino:js)

# test deps
BuildRequires: mvn(junit:junit)
BuildRequires: objectweb-asm3
BuildRequires: mvn(org.apache.commons:commons-lang3)

Requires:      %{name}-core = %{version}
BuildArch:     noarch
Source44: import.info

#* jsr199 Commons JCI compiler implementation for JDK 1.6 and up.

%description
JCI is a java compiler interface featuring a compiling class loader.
The current implementation supports compilation via the following
compilers:

* eclipse
* groovy
* janino
* rhino

%package core
Group: Development/Java
Summary:       Commons Java Compiler Interface - core

%description core
Commons JCI core interfaces and implementations.

%package fam
Group: Development/Java
Summary:       Commons Java Compiler Interface - FAM

%description fam
Commons JCI FileAlterationMonitor (FAM) to
monitor local file systems and get notified
about changes.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

# compilers

%package eclipse
Group: Development/Java
Summary:       Commons Java Compiler Interface - eclipse

%description eclipse
Commons JCI compiler implementation for the eclipse compiler.

%package groovy
Group: Development/Java
Summary:       Commons Java Compiler Interface - groovy

%description groovy
Commons JCI compiler implementation for the groovy compiler.

%package janino
Group: Development/Java
Summary:       Commons Java Compiler Interface - janino

%description janino
Commons JCI compiler implementation for the janino compiler.

%package rhino
Group: Development/Java
Summary:       Commons Java Compiler Interface - rhino

%description rhino
Commons JCI compiler implementation for rhino JavaScript.

%prep
%setup -q -n %{short_name}-%{namedversion}-src
find . -name "*.class" -delete
find . -name "*.jar" -delete

%patch0 -p1

# require old version of jdependency
%pom_disable_module examples

%pom_xpath_remove "pom:build/pom:extensions"

%pom_xpath_set "pom:properties/pom:maven.compiler.source" 1.6
%pom_xpath_set "pom:properties/pom:maven.compiler.target" 1.6

%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-site-plugin

%pom_xpath_set "pom:dependencyManagement/pom:dependencies/pom:dependency[pom:groupId = 'org.codehaus.groovy']/pom:artifactId" groovy
%pom_xpath_set "pom:dependencyManagement/pom:dependencies/pom:dependency[pom:groupId = 'org.codehaus.groovy']/pom:version" 1.8.9
%pom_xpath_set "pom:dependencies/pom:dependency[pom:groupId = 'org.codehaus.groovy']/pom:artifactId" groovy compilers/groovy
%pom_xpath_inject "pom:dependencies/pom:dependency[pom:groupId = 'org.codehaus.groovy']" "<version>1.8.9</version>" compilers/groovy

# Fix installation directory      
%mvn_file :%{short_name}-core    %{short_name}/%{short_name}-core
%mvn_file :%{short_name}-fam     %{short_name}/%{short_name}-fam
%mvn_file :%{short_name}-eclipse %{short_name}/%{short_name}-eclipse
%mvn_file :%{short_name}-groovy  %{short_name}/%{short_name}-groovy
%mvn_file :%{short_name}-janino  %{short_name}/%{short_name}-janino
%mvn_file :%{short_name}-rhino   %{short_name}/%{short_name}-rhino

%build

# random tests failures
%mvn_build -s -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles-%{short_name}
%dir %{_javadir}/%{short_name}
%doc README.txt TODO.txt
%doc LICENSE.txt NOTICE.txt

%files core -f .mfiles-%{short_name}-core

%files fam -f .mfiles-%{short_name}-fam

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%files eclipse -f .mfiles-%{short_name}-eclipse

%files groovy -f .mfiles-%{short_name}-groovy

%files janino -f .mfiles-%{short_name}-janino

%files rhino -f .mfiles-%{short_name}-rhino

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt1_3jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt1_2jpp8
- new version

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt4_10jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt4_7jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt4_5jpp7
- rebuild with maven-local

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt3_5jpp7
- fixed build

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt2_5jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_5jpp7
- fc update

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_4jpp7
- fc release

* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_0.r831715.4jpp6
- fixed build with new asm

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_0.r831715.4jpp6
- fixed build with maven3

* Wed Feb 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_0.r831715.4jpp6
- new version

