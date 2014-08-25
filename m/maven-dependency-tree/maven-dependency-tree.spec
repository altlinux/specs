# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat

Name:          maven-dependency-tree
Version:       2.0
Release:       alt2_4jpp7
Summary:       Maven dependency tree artifact
Group:         Development/Java
License:       ASL 2.0
Url:           http://maven.apache.org/
Source0:       http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: plexus-containers-component-metadata
BuildRequires: plexus-containers-component-annotations

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
%pom_add_dep org.apache.maven:maven-compat:3.0.4
%pom_add_dep org.apache.maven:maven-artifact:2.2.1

%build
# we have no jmock yet
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_4jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_1jpp7
- rebuild with maven-local

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_1jpp7
- update

