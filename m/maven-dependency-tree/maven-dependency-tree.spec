# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat

Name:          maven-dependency-tree
Version:       3.0
Release:       alt1_2jpp8
Summary:       Maven dependency tree artifact
Group:         Development/Other
License:       ASL 2.0
Url:           http://maven.apache.org/
Source0:       http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:     noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.shared:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-util)

Provides:      maven-shared-dependency-tree = %{version}-%{release}
Obsoletes:     maven-shared-dependency-tree < %{version}-%{release}
Source44: import.info

%description
Apache Maven dependency tree artifact. Originally part of maven-shared.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

find -name Maven3DependencyGraphBuilder.java -delete
%pom_remove_dep org.sonatype.aether:

%pom_remove_plugin :apache-rat-plugin

%build
# Incompatible version of jMock (Fedora has 2.x, upstream uses 1.x)
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_2jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_2jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_4jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_1jpp7
- rebuild with maven-local

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_1jpp7
- update

