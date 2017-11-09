Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.4.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
Name:             undertow
Version:          1.4.0
Release:          alt1_3jpp8
Summary:          Java web server using non-blocking IO
License:          ASL 2.0
URL:              http://undertow.io/
Source0:          https://github.com/undertow-io/undertow/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz
# Remove unavailable methods in jetty-alpn-api-1.1.0
Patch0:           undertow-1.4.0-jetty-alpn-api-1.1.0.patch

BuildArch:        noarch
Epoch:            1

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.eclipse.jetty.alpn:alpn-api)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.classfilewriter:jboss-classfilewriter)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:    mvn(org.jboss.logmanager:jboss-logmanager)
BuildRequires:    mvn(org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec)
BuildRequires:    mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.1_spec)
BuildRequires:    mvn(org.jboss.spec.javax.websocket:jboss-websocket-api_1.1_spec)
BuildRequires:    mvn(org.jboss.xnio:xnio-api)
BuildRequires:    mvn(org.jboss.xnio:xnio-nio)
Source44: import.info

%description
Java web server using non-blocking IO

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%patch0 -p1

rm -rf mac-jdk-fix

# Not needed
%pom_disable_module examples

%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin org.bitstrings.maven.plugins:dependencypath-maven-plugin core
%pom_remove_plugin org.bitstrings.maven.plugins:dependencypath-maven-plugin servlet
%pom_remove_dep -r io.undertow.build:undertow-checkstyle-config

# Disable default-jar execution of maven-jar-plugin, which is causing
# problems with version 3.0.0 of the plugin.
for p in core servlet;do
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions" "
 <execution>
  <id>default-jar</id>
  <phase>skip</phase>
 </execution>" ${p}
done

%build

%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.4.0-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.4.0-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.4.0-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.1.0-alt1_3jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.1.0-alt1_2jpp8
- java 8 mass update

