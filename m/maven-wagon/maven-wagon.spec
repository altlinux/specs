Epoch: 0
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

Name:           maven-wagon
Version:        3.4.2
Release:        alt1_4jpp11
Summary:        Tools to manage artifacts and deployment
License:        ASL 2.0
URL:            https://maven.apache.org/wagon
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/wagon/wagon/%{version}/wagon-%{version}-source-release.zip

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.jsoup:jsoup)
BuildRequires:  mvn(org.slf4j:jcl-over-slf4j)
BuildRequires:  mvn(org.slf4j:slf4j-api)
%endif

Provides:       maven-wagon-file = %{version}-%{release}
Provides:       maven-wagon-http = %{version}-%{release}
Provides:       maven-wagon-http-shared = %{version}-%{release}
Provides:       maven-wagon-provider-api = %{version}-%{release}
Provides:       maven-wagon-providers = %{version}-%{release}

Obsoletes:      maven-wagon-file < 3.4.2-2
Obsoletes:      maven-wagon-http < 3.4.2-2
Obsoletes:      maven-wagon-http-shared < 3.4.2-2
Obsoletes:      maven-wagon-provider-api < 3.4.2-2
Obsoletes:      maven-wagon-providers < 3.4.2-2
Obsoletes:      maven-wagon-ftp < 3.4.2-2
Obsoletes:      maven-wagon-http-lightweight < 3.4.2-2
Source44: import.info

%description
Maven Wagon is a transport abstraction that is used in Maven's
artifact and repository handling code. Currently wagon has the
following providers:
* File
* HTTP
* FTP
* SSH/SCP
* WebDAV
* SCM (in progress)

%{?javadoc_package}

%prep
%setup -q -n wagon-%{version}

%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_dep :wagon-tck-http wagon-providers/wagon-http

# disable tests, missing dependencies
%pom_disable_module wagon-tcks
%pom_disable_module wagon-ssh-common-test wagon-providers
%pom_disable_module wagon-provider-test
%pom_remove_dep :wagon-provider-test
%pom_remove_dep :wagon-provider-test wagon-providers

# missing dependencies
%pom_disable_module wagon-ftp wagon-providers
%pom_disable_module wagon-http-lightweight wagon-providers
%pom_disable_module wagon-scm wagon-providers
%pom_disable_module wagon-ssh wagon-providers
%pom_disable_module wagon-ssh-common wagon-providers
%pom_disable_module wagon-ssh-external wagon-providers
%pom_disable_module wagon-webdav-jackrabbit wagon-providers

%pom_remove_plugin :maven-shade-plugin wagon-providers/wagon-http

%mvn_file ":wagon-{*}" %{name}/@1
%mvn_package ":wagon"

%build
# tests are disabled because of missing dependencies
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

# Maven requires Wagon HTTP with classifier "shaded"
%mvn_alias :wagon-http :::shaded:

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE
%doc DEPENDENCIES

%changelog
* Tue Aug 17 2021 Igor Vlasenko <viy@altlinux.org> 0:3.4.2-alt1_4jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:3.4.2-alt1_1jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:3.4.1-alt1_3jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:3.3.3-alt1_4jpp8
- new version

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.2.0-alt1_2jpp8
- new version

* Thu Jun 20 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt1_2jpp8
- new version

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.0.0-alt1_1jpp8
- new version

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.10-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.10-alt1_3jpp8
- new jpp release

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.10-alt1_2jpp8
- new version

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.9-alt1_4jpp8
- java 8 mass update

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.9-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_2jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt0.2jpp
- rebuild to add provides

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt10_6jpp7
- added maven-local BR:

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt9_6jpp7
- new fc release

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt9_3jpp7
- complete build

* Sun Mar 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt8jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

