Name: maven-enforcer
Version: 3.5.0
Release: alt1

Summary: Maven Enforcer
License: Apache-2.0
Group: Development/Java
URL: http://maven.apache.org/enforcer

BuildArch: noarch

Source0: enforcer-%version-source-release.zip

BuildRequires: unzip
BuildRequires: jpackage-17-compat
BuildRequires: maven-local
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(commons-codec:commons-codec)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(javax.annotation:javax.annotation-api)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.resolver:maven-resolver-api)
BuildRequires: mvn(org.apache.maven.resolver:maven-resolver-util)
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-model-builder)
BuildRequires: mvn(org.apache.maven:maven-parent:pom:)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-settings)
BuildRequires: mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.codehaus.plexus:plexus-xml)
BuildRequires: mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires: mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires: mvn(org.slf4j:slf4j-api)

%description
Enforcer is a build rule execution framework.

%{?javadoc}

%package api
Group: Development/Java
Summary: Enforcer API
Provides: maven-shared-enforcer-rule-api = %{version}-%{release}

%description api
This component provides the generic interfaces needed to
implement custom rules for the maven-enforcer-plugin.

%package rules
Group: Development/Java
Summary: Enforcer Rules

%description rules
This component contains the standard Enforcer Rules.

%package plugin
Group: Development/Java
Summary: Enforcer Rules

%description plugin
This component contains the standard Enforcer Rules.

%prep
%setup -n enforcer-%version
find -name '*.java' -exec sed -i 's/\r//' {} +
find -name EvaluateBeanshell.java -delete
%pom_remove_dep :bsh enforcer-rules
 
%build
# Use system version of maven-enforcer-plugin instead of reactor version
%mvn_build -j -s -f -- -Dversion.maven-enforcer-plugin=SYSTEM

%install
%mvn_install

%files -f .mfiles-enforcer
%doc LICENSE NOTICE

%files api -f .mfiles-enforcer-api
%doc LICENSE NOTICE

%files rules -f .mfiles-enforcer-rules

%files plugin -f .mfiles-maven-enforcer-plugin

%changelog
* Mon Apr 28 2025 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt1
- new version

* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 0:3.0.0_M2-alt1_3jpp11
- java11 build

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 0:3.0.0_M2-alt1_3jpp8
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt1_10jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt1_5jpp8
- new jpp release

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt1_4jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_2jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_1jpp7
- new release

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_4jpp7
- added BR: for xmvn

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_4jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt4_6jpp7
- fixed build

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt3_6jpp7
- new version

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt3_5jpp7
- new fc release

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt3_4jpp7
- added maven-shared-enforcer-rule-api provides

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt2_4jpp7
- fixed depmap fragment

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_4jpp7
- fc version

* Mon Feb 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_3jpp6
- new jpp relase

* Wed Feb 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.2.b1.1.2jpp6
- new version

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.2.b1.1.2jpp6
- new version

