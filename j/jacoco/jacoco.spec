Name: jacoco
Version: 0.8.14
Release: alt3

Summary: Java Code Coverage for Eclipse
Group: System/Libraries
License: EPL-2.0
URL: http://www.eclemma.org/jacoco/
VCS: https://github.com/jacoco/jacoco.git
BuildArch: noarch

Source0: %name-%version.tar

Patch0: 0001-maven-doxia-2-repair.patch

# required by wrapper script
Requires: javapackages-tools

BuildRequires: javapackages-tools
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildRequires: maven-antrun-plugin
BuildRequires: maven-dependency-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-shade-plugin
BuildRequires: maven-reporting-api
BuildRequires: maven-plugin-build-helper
BuildRequires: buildnumber-maven-plugin
BuildRequires: exec-maven-plugin
BuildRequires: objectweb-asm

%description
JaCoCo is a free code coverage library for Java, which has been created by the
EclEmma team based on the lessons learned from using and integration existing
libraries over the last five years.

%package maven-plugin
Group: System/Libraries
Summary: A Jacoco plugin for maven

%description maven-plugin
A Jacoco plugin for maven.

%javadoc_package

%package cli
Group: Development/Tools
Summary: Jacoco binary wrapper
Requires: jacoco

%description cli
Jacoco binary wrapper.

%prep
%setup
%autopatch -p1

find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete

%pom_disable_module ../jacoco org.jacoco.build
%pom_disable_module ../org.jacoco.doc org.jacoco.build
%pom_disable_module ../org.jacoco.examples org.jacoco.build
%pom_disable_module ../org.jacoco.tests org.jacoco.build

# Remove unnecessary dependency on maven-javadoc-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

# Remove enforcer plugin that causes build failure of 'Jacoco :: Maven Plugin'
%pom_remove_plugin -r :maven-enforcer-plugin

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

%pom_remove_plugin -r :maven-source-plugin

%mvn_package ":jacoco-maven-plugin:{jar,pom}:{}:" maven-plugin
%mvn_package ":{org.}*:{jar,pom}:runtime:"

%mvn_package :root __noinstall
%mvn_package :org.jacoco.build __noinstall

%build
%mvn_build -- -Dbuild.date=$(date +%Y/%m/%d) \
              -Dproject.build.sourceEncoding=UTF-8 \
              -Dmaven.compiler.source=1.8 \
              -Dmaven.compiler.target=1.8 \
              -Dmaven.compiler.release=8 \

%install
%mvn_install

# ant config
mkdir -p %buildroot%_sysconfdir/ant.d
echo %name %name/org.jacoco.ant objectweb-asm/asm > %buildroot%_sysconfdir/ant.d/%name

# wrapper script
%jpackage_script org.jacoco.cli.internal.Main "" "" jacoco/org.jacoco.cli:args4j:objectweb-asm:jacoco/org.jacoco.core:jacoco/org.jacoco.report jacococli true

%files -f .mfiles
%config(noreplace) %_sysconfdir/ant.d/%name
%doc --no-dereference LICENSE.md
%doc README.md

%files maven-plugin -f .mfiles-maven-plugin
%files cli
%_bindir/jacococli

%changelog
* Mon Apr 06 2026 Evgeniy Serov <scala@altlinux.org> 0.8.14-alt3
- Fix build with new maven-doxia.

* Mon Feb 16 2026 Ilya Muhamadeev <nicourced@altlinux.org> 0.8.14-alt2
- Return jacococli.

* Mon Feb 02 2026 Ilya Muhamadeev <nicourced@altlinux.org> 0.8.14-alt1
- New version.

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

