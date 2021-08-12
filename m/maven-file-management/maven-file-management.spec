Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
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

Name:           maven-file-management
Epoch:          1
Version:        3.0.0
Release:        alt1_14jpp11
Summary:        Maven File Management API
License:        ASL 2.0
URL:            http://maven.apache.org/shared/file-management
BuildArch:      noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/file-management/%{version}/file-management-%{version}-source-release.zip

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-io)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
%endif
Source44: import.info

%description
Provides a component for plugins to easily resolve project dependencies.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch
    
%description javadoc
API documentation for %{name}.

%prep
%setup -q -n file-management-%{version}

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1:3.0.0-alt1_14jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1:3.0.0-alt1_9jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1:3.0.0-alt1_7jpp8
- new version

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.0.0-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.0.0-alt1_3jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.0.0-alt1_2jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.2.1-alt3_12jpp8
- new version

* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.2.1-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.2.1-alt1_6jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.2.1-alt1_0jpp7
- new release

