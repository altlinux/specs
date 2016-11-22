Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name undertow
%define version 1.1.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             undertow
Version:          1.1.0
Release:          alt1_3jpp8
Summary:          Java web server using non-blocking IO
License:          ASL 2.0 and LGPLv2
URL:              http://undertow.io/
Source0:          https://github.com/undertow-io/undertow/archive/%{namedversion}.tar.gz

# Jetty alpn is not available in fedora, we need to remove spdy protocol
Patch0:           0001-Remove-spdy-protocol-handler-alpn-is-not-available-i.patch

BuildArch:        noarch
Epoch:            1

BuildRequires:    aether
BuildRequires:    maven-local
BuildRequires:    maven-checkstyle-plugin
BuildRequires:    apache-mime4j
BuildRequires:    jboss-parent
BuildRequires:    jboss-logging
BuildRequires:    jboss-logging-tools
BuildRequires:    jboss-logmanager
BuildRequires:    xnio >= 3.3.0
BuildRequires:    easymock3
BuildRequires:    junit
BuildRequires:    netty
BuildRequires:    jboss-classfilewriter
BuildRequires:    jboss-annotations-1.2-api
BuildRequires:    jboss-jsp-2.3-api
BuildRequires:    jboss-servlet-3.1-api
BuildRequires:    jastow >= 1.0.0
BuildRequires:    mvn(org.jboss.spec.javax.websocket:jboss-websocket-api_1.1_spec)
Source44: import.info

%description
Java web server using non-blocking IO

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n undertow-%{namedversion}

%patch0 -p1

rm -rf mac-jdk-fix

# Not needed
%pom_disable_module examples
# Missing mime4j dep
%pom_add_dep org.apache.james:apache-mime4j-core:any:test servlet

%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin org.bitstrings.maven.plugins:dependencypath-maven-plugin core/pom.xml
%pom_remove_plugin org.bitstrings.maven.plugins:dependencypath-maven-plugin servlet/pom.xml
%pom_remove_dep io.undertow.build:undertow-checkstyle-config

# Not avialable in Fedora
%pom_remove_dep org.eclipse.jetty.alpn:alpn-api core/pom.xml
%pom_remove_dep org.eclipse.jetty.alpn:alpn-api servlet/pom.xml

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.1.0-alt1_3jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.1.0-alt1_2jpp8
- java 8 mass update

