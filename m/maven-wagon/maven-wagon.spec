Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global bname     wagon

Name:           maven-%{bname}
Version:        2.5
Release:        alt1_2jpp7
Epoch:          0
Summary:        Tools to manage artifacts and deployment
License:        ASL 2.0
URL:            http://maven.apache.org/wagon
Source0:        http://repo1.maven.org/maven2/org/apache/maven/wagon/wagon/%{version}/wagon-%{version}-source-release.zip

Patch0:         0001-Port-to-jetty-9.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.jcraft:jsch)
BuildRequires:  mvn(commons-httpclient:commons-httpclient)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(commons-net:commons-net)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(log4j:log4j)
BuildRequires:  mvn(nekohtml:nekohtml)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-api)
BuildRequires:  mvn(org.apache.maven:maven-parent)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interactivity-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.jetty:jetty-client)
BuildRequires:  mvn(org.eclipse.jetty:jetty-security)
BuildRequires:  mvn(org.eclipse.jetty:jetty-server)
BuildRequires:  mvn(org.eclipse.jetty:jetty-servlet)
BuildRequires:  mvn(org.eclipse.jetty:jetty-util)
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

%package scm
Group: Development/Java
Summary:        scm module for %{name}

%description scm
scm module for %{name}.

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
%pom_remove_dep :wagon-tck-http wagon-providers/wagon-http

# correct groupId for jetty
%pom_xpath_set "pom:groupId[text()='org.mortbay.jetty']" "org.eclipse.jetty"

# disable tests, missing dependencies
%pom_disable_module wagon-tcks
%pom_disable_module wagon-ssh-common-test wagon-providers/pom.xml
%pom_disable_module wagon-provider-test

# missing dependencies
%pom_disable_module wagon-webdav-jackrabbit wagon-providers

%build
%mvn_file ":wagon-{*}" %{name}/@1

# scm module has a lot of dependencies
%mvn_package ":wagon-scm" scm

# tests are disabled because of missing dependencies
%mvn_build -f

# Maven requires Wagon HTTP with classifier "shaded"
%mvn_alias :wagon-http :::shaded:

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE DEPENDENCIES
%files scm -f .mfiles-scm
%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE DEPENDENCIES

%changelog
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

