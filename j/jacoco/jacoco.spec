Group: System/Libraries
%filter_from_requires /osgi(org.apache.ant*/d
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
%define fedora 34
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
BuildRequires: /usr/bin/git
Name:           jacoco
Version:        0.8.7
Release:        alt1_6jpp11
Summary:        Java Code Coverage for Eclipse
License:        EPL-2.0
URL:            http://www.eclemma.org/jacoco/
BuildArch:      noarch

Source0:        https://github.com/jacoco/jacoco/archive/v%{version}/%{name}-%{version}.tar.gz

%if 0%{?fedora} >= 36
Patch0:         0001-Upgrade-maven-reporting-api-to-3.1.0.patch
%endif

BuildRequires:  git
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-analysis)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.ow2.asm:asm-tree)
# required by wrapper scripts
Requires:       javapackages-tools
Source44: import.info

%description
JaCoCo is a free code coverage library for Java, 
which has been created by the EclEmma team based on the lessons learned 
from using and integration existing libraries over the last five years. 

%package    maven-plugin
Group: System/Libraries
Summary:    A Jacoco plugin for maven

%description maven-plugin
A Jacoco plugin for maven.

%{?javadoc_package}

%prep
%setup -q
git init -q
git config user.name "rpmbuild"
git config user.email "<rpmbuild>"
git config gc.auto 0
git add --force .
git commit -q --allow-empty -a --author "rpmbuild <rpmbuild>" -m "%{NAME}-%{VERSION} base"
%if 0%{?fedora} >= 36
cat %_sourcedir/0001-Upgrade-maven-reporting-api-to-3.1.0.patch | git apply --index --reject  -p1 -
git commit -q -m 0001-Upgrade-maven-reporting-api-to-3.1.0.patch --author "rpmbuild <rpmbuild>"
%endif


find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete

%pom_disable_module ../jacoco org.jacoco.build
%pom_disable_module ../org.jacoco.doc org.jacoco.build
%pom_disable_module ../org.jacoco.examples org.jacoco.build
%pom_disable_module ../org.jacoco.tests org.jacoco.build

# Remove unnecessary dependency on maven-javadoc-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

# Remove enforcer plugin that causes build failure of 'Jacoco :: Maven Plugin'
%pom_remove_plugin -r :maven-enforcer-plugin

# Don't build jars with classifier ":nodeps:"
%pom_remove_plugin :maven-shade-plugin \
    org.jacoco.ant \
    org.jacoco.cli

%pom_remove_plugin -r :spotless-maven-plugin

# Need to redefine various properties
%pom_remove_plugin :beanshell-maven-plugin \
    org.jacoco.build

# Remove "requires osgi(org.apache.ant)"
%pom_xpath_remove 'pom:configuration/pom:instructions/pom:Require-Bundle' \
    org.jacoco.ant

# Remove requires on maven-plugin-plugin:report
%pom_xpath_remove 'pom:execution[pom:id = "report"]' \
    jacoco-maven-plugin

# Define properties
%pom_xpath_inject 'pom:properties' '
    <unqualifiedVersion>${project.version}</unqualifiedVersion>
    <buildQualifier>${maven.build.timestamp}</buildQualifier>
    <qualified.bundle.version>${unqualifiedVersion}.${buildQualifier}</qualified.bundle.version>
    <jacoco.runtime.package.name>org.jacoco.agent.rt.internal_fedora</jacoco.runtime.package.name>' \
      org.jacoco.build

%mvn_package ":jacoco-maven-plugin:{jar,pom}:{}:" maven-plugin
%mvn_package ":{org.}*:{jar,pom}:runtime:"

%mvn_package :root __noinstall
%mvn_package :org.jacoco.build __noinstall

%build
%mvn_build -f -- -Dbuild.date=$(date +%Y/%m/%d) -Dproject.build.sourceEncoding=UTF-8 -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

# ant config
mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo %{name} %{name}/org.jacoco.ant objectweb-asm/asm > %{buildroot}%{_sysconfdir}/ant.d/%{name}

# wrapper script
%jpackage_script org.jacoco.cli.internal.Main "" "" jacoco/org.jacoco.cli:args4j:objectweb-asm:jacoco/org.jacoco.core:jacoco/org.jacoco.report jacococli true

%files -f .mfiles
%config(noreplace) %{_sysconfdir}/ant.d/%{name}
%{_bindir}/jacococli
%doc --no-dereference LICENSE.md
%doc README.md

%files maven-plugin -f .mfiles-maven-plugin

%changelog
* Thu May 26 2022 Igor Vlasenko <viy@altlinux.org> 0.8.7-alt1_6jpp11
- new version

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 0.8.3-alt1_4jpp11
- new version

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 0.7.8-alt1_8jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.7.8-alt1_7jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.7.8-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.8-alt1_4jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.8-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.7-alt1_2jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.6-alt1_1jpp8
- new version

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.5-alt1_2jpp8
- java 8 mass update

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

