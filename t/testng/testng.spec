Epoch: 0
Group: Development/Java
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:           testng
Version:        7.4.0
Release:        alt1_3jpp11
Summary:        Java-based testing framework
License:        ASL 2.0
URL:            http://testng.org/

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz

# Allows building with maven instead of gradle
Source1:        pom.xml

# Remove bundled binaries to make sure we don't ship anything forbidden
Source2:        generate-tarball.sh

Patch0:         0001-Avoid-accidental-javascript-in-javadoc.patch
Patch1:         0002-Replace-bundled-jquery-with-CDN-link.patch

BuildArch:      noarch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(com.beust:jcommander)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.inject:guice::no_aop:)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
%endif
Source44: import.info

%description
TestNG is a testing framework inspired from JUnit and NUnit but introducing
some new functionality, including flexible test configuration, and
distributed test running.  It is designed to cover unit tests as well as
functional, end-to-end, integration, etc.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%(echo %{version} | tr '~' '-')

%patch0 -p1
%patch1 -p1

sed 's/@VERSION@/%{version}/' %{SOURCE1} > pom.xml

# remove any bundled libs, but not test resources
find ! -path "*/test/*" -name *.jar -print -delete
find -name *.class -delete

# these are unnecessary
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

%pom_remove_dep org.yaml:snakeyaml
rm src/main/java/org/testng/internal/Yaml*.java
rm src/main/java/org/testng/Converter.java

%pom_remove_dep :bsh

%pom_xpath_inject "pom:dependency[pom:artifactId='guice']" "<classifier>no_aop</classifier>"

sed -i -e 's/DEV-SNAPSHOT/%{version}/' src/main/java/org/testng/internal/Version.java

cp -p ./src/main/java/*.dtd.html ./src/main/resources/.

%mvn_file : %{name}
# jdk15 classifier is used by some other packages
%mvn_alias : :::jdk15:

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.txt README.md
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:7.4.0-alt1_3jpp11
- new version

* Sun May 29 2022 Igor Vlasenko <viy@altlinux.org> 0:7.3.0-alt1_3jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:6.14.3-alt1_13jpp11
- update

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:6.14.3-alt1_9jpp8
- update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:6.14.3-alt1_7jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:6.14.3-alt1_2jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:6.12-alt2_2jpp8
- fixed build

* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:6.12-alt1_2jpp8
- new version

* Mon Oct 30 2017 Igor Vlasenko <viy@altlinux.ru> 0:6.9.12-alt1_4jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:6.9.11-alt1_1jpp8
- new version

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:6.9.10-alt1_2jpp8
- new version

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0:6.8.21-alt2_2jpp8
- added osgi provides

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:6.8.21-alt1_2jpp8
- unbootsrap build

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

