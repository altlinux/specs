Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-dependency-analyzer
Version:        1.3
Release:        alt1_7jpp7
Summary:        Maven dependency analyzer
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-dependency-analyzer/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-shared
BuildRequires:  httpcomponents-project
BuildRequires:  maven-doxia-module-xhtml
BuildRequires:  maven-plugin-testing-tools

# This is a replacement package for maven-shared-dependency-analyzer
Provides:       maven-shared-dependency-analyzer = %{version}-%{release}
Obsoletes:      maven-shared-dependency-analyzer < %{version}-%{release}
Source44: import.info

%description
Analyzes the dependencies of a project for undeclared or unused artifacts.

Warning: Analysis is not done at source but bytecode level, then some cases are
not detected (constants, annotations with source-only retention, links in
javadoc) which can lead to wrong result if they are the only use of a
dependency.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}

%prep
%setup -q

# Needed for tests only. However, the right groupId:artifactId of jmock in
# Fedora is org.jmock:jmock
%pom_remove_dep jmock:jmock

%build
# org.jmock.core package is needed, we don't have it
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_7jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_0jpp7
- new release

