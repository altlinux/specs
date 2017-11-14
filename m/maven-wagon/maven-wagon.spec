Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_without  scm
%bcond_without  ssh
%global bname     wagon
%global split_verrel 2.6-4

Name:           maven-%{bname}
Version:        2.10
Release:        alt1_4jpp8
Epoch:          0
Summary:        Tools to manage artifacts and deployment
License:        ASL 2.0
URL:            http://maven.apache.org/wagon
Source0:        http://repo1.maven.org/maven2/org/apache/maven/wagon/wagon/%{version}/wagon-%{version}-source-release.zip

Patch0:         0001-Port-to-jetty-9.patch

BuildArch:      noarch

BuildRequires:  maven-local
%if %{with ssh}
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(com.jcraft:jsch.agentproxy.connector-factory)
BuildRequires:  mvn(com.jcraft:jsch.agentproxy.jsch)
%endif
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(commons-net:commons-net)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
%if %{with scm}
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-api)
%endif
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interactivity-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.jsoup:jsoup)
BuildRequires:  mvn(org.slf4j:slf4j-api)

Obsoletes:      %{name}-manual < %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-provider-test < %{epoch}:%{version}-%{release}
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

%package provider-api
Group: Development/Java
Summary:        provider-api module for %{name}
Obsoletes:      %{name} < %{split_verrel}
Obsoletes:      %{name}-webdav-jackrabbit < 2.9-2

%description provider-api
provider-api module for %{name}.

%package providers
Group: Development/Java
Summary:        providers module for %{name}

%description providers
providers module for %{name}

%package file
Group: Development/Java
Summary:        file module for %{name}

%description file
file module for %{name}.

%package ftp
Group: Development/Java
Summary:        ftp module for %{name}

%description ftp
ftp module for %{name}.

%package http
Group: Development/Java
Summary:        http module for %{name}

%description http
http module for %{name}.

%package http-shared
Group: Development/Java
Summary:        http-shared module for %{name}

%description http-shared
http-shared module for %{name}.

%package http-lightweight
Group: Development/Java
Summary:        http-lightweight module for %{name}

%description http-lightweight
http-lightweight module for %{name}.

%if %{with scm}
%package scm
Group: Development/Java
Summary:        scm module for %{name}

%description scm
scm module for %{name}.
%endif

%if %{with ssh}
%package ssh-external
Group: Development/Java
Summary:        ssh-external module for %{name}

%description ssh-external
ssh-external module for %{name}.

%package ssh-common
Group: Development/Java
Summary:        ssh-common module for %{name}

%description ssh-common
ssh-common module for %{name}.

%package ssh
Group: Development/Java
Summary:        ssh module for %{name}

%description ssh
ssh module for %{name}.
%endif

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n wagon-%{version}

%patch0 -p1

%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_dep :wagon-tck-http wagon-providers/wagon-http

# correct groupId for jetty
%pom_xpath_set "pom:groupId[text()='org.mortbay.jetty']" "org.eclipse.jetty"

# disable tests, missing dependencies
%pom_disable_module wagon-tcks
%pom_disable_module wagon-ssh-common-test wagon-providers/pom.xml
%pom_disable_module wagon-provider-test
%pom_remove_dep :wagon-provider-test
%pom_remove_dep :wagon-provider-test wagon-providers

# missing dependencies
%pom_disable_module wagon-webdav-jackrabbit wagon-providers

%if %{without scm}
%pom_disable_module wagon-scm wagon-providers
%endif
%if %{without ssh}
%pom_disable_module wagon-ssh wagon-providers
%pom_disable_module wagon-ssh-common wagon-providers
%pom_disable_module wagon-ssh-external wagon-providers
%endif

%build
%mvn_file ":wagon-{*}" %{name}/@1

%mvn_package ":wagon"

# tests are disabled because of missing dependencies
%mvn_build -f -s

# Maven requires Wagon HTTP with classifier "shaded"
%mvn_alias :wagon-http :::shaded:


%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE DEPENDENCIES
%files provider-api -f .mfiles-wagon-provider-api
%dir %{_javadir}/%{name}
%files providers -f .mfiles-wagon-providers
%files file -f .mfiles-wagon-file
%files ftp -f .mfiles-wagon-ftp
%files http -f .mfiles-wagon-http
%files http-shared -f .mfiles-wagon-http-shared
%files http-lightweight -f .mfiles-wagon-http-lightweight
%if %{with scm}
%files scm -f .mfiles-wagon-scm
%endif
%if %{with ssh}
%files ssh-external -f .mfiles-wagon-ssh-external
%files ssh-common -f .mfiles-wagon-ssh-common
%files ssh -f .mfiles-wagon-ssh
%endif

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE DEPENDENCIES

%changelog
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

