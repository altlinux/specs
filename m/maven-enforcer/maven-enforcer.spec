Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           maven-enforcer
Version:        1.4.1
Release:        alt1_4jpp8
Summary:        Maven Enforcer
License:        ASL 2.0
URL:            http://maven.apache.org/enforcer
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/enforcer/enforcer/%{version}/enforcer-%{version}-source-release.zip

Patch0:         0001-Port-to-Maven-3-API.patch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:maven-artifact-transfer)
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.apache.maven.shared:maven-dependency-tree)
BuildRequires:  mvn(org.beanshell:bsh)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-i18n)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
Source44: import.info

%description
Enforcer is a build rule execution framework.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%package api
Group: Development/Java
Summary:        Enforcer API
Provides: maven-shared-enforcer-rule-api = %{version}-%{release}

%description api
This component provides the generic interfaces needed to
implement custom rules for the maven-enforcer-plugin.

%package rules
Group: Development/Java
Summary:        Enforcer Rules

%description rules
This component contains the standard Enforcer Rules.

%package plugin
Group: Development/Java
Summary:        Enforcer Rules

%description plugin
This component contains the standard Enforcer Rules.


%prep
%setup -q -n enforcer-%{version}
%patch0 -p1

# Replace plexus-maven-plugin with plexus-component-metadata
sed -e "s|<artifactId>plexus-maven-plugin</artifactId>|<artifactId>plexus-component-metadata</artifactId>|" \
    -e "s|<goal>descriptor</goal>|<goal>generate-metadata</goal>|" \
    -i enforcer-{api,rules}/pom.xml

%build
%mvn_build -s -f

%install
%mvn_install

%files -f .mfiles-enforcer
%doc LICENSE NOTICE

%files api -f .mfiles-enforcer-api
%doc LICENSE NOTICE

%files rules -f .mfiles-enforcer-rules

%files plugin -f .mfiles-maven-enforcer-plugin

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
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

