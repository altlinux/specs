Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 2.3.5
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:           weld-core
Version:        2.3.5
Release:        alt1_3jpp8
Summary:        Reference Implementation for JSR-299: Contexts and Dependency Injection (CDI)

# OFL: ./probe/core/src/main/client/font-awesome.*

# MIT: ./probe/core/target/client/app.js
# ./probe/core/target/client/basic.css
# ./probe/core/target/client/bootstrap-theme.min-3.3.1.css
# ./probe/core/target/client/bootstrap.min-3.3.1.css
# ./probe/core/target/client/bootstrap.min-3.3.1.js
# ./probe/core/target/client/d3.min-3.5.2.js
# ./probe/core/target/client/ember.prod-1.9.0.js
# ./probe/core/target/client/handlebars-v2.0.0.js
# ./probe/core/target/client/jquery-2.1.1.min.js
# ./probe/core/target/client/moment.min-2.8.4.js

# https://issues.jboss.org/browse/WELD-2173
License:        ASL 2.0 and (CDDL or GPLv2 with exceptions) and LGPLv2+ and MIT and OFL
URL:            http://weld.cdi-spec.org/
Source0:        https://github.com/weld/core/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz
Patch0:         0001-Add-support-for-newer-jboss-logging-tools.patch
Patch1:         weld-core-2.3.2.Final-Remove-gwtdev-environment.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(io.undertow:undertow-servlet)
BuildRequires:  mvn(javax.el:el-api)
BuildRequires:  mvn(javax.enterprise:cdi-api)
BuildRequires:  mvn(javax.faces:jsf-api)
BuildRequires:  mvn(javax.persistence:persistence-api)
BuildRequires:  mvn(javax.portlet:portlet-api)
BuildRequires:  mvn(javax.servlet.jsp:jsp-api)
BuildRequires:  mvn(javax.transaction:jta)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.sourceforge.findbugs:annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.tomcat:tomcat-catalina)
BuildRequires:  mvn(org.codehaus.groovy:groovy-all)
BuildRequires:  mvn(org.eclipse.jetty:jetty-server:8.1)
BuildRequires:  mvn(org.eclipse.jetty:jetty-servlet:8.1)
BuildRequires:  mvn(org.eclipse.jetty:jetty-webapp:8.1)
BuildRequires:  mvn(org.eclipse.jetty:jetty-plus)
BuildRequires:  mvn(org.hibernate.javax.persistence:hibernate-jpa-2.1-api)
BuildRequires:  mvn(org.jboss.arquillian:arquillian-bom:pom:)
BuildRequires:  mvn(org.jboss.classfilewriter:jboss-classfilewriter)
BuildRequires:  mvn(org.jboss:jandex)
BuildRequires:  mvn(org.jboss.jandex:jandex-maven-plugin)
BuildRequires:  mvn(org.jboss.logging:jboss-logging)
# https://issues.jboss.org/browse/WELD-2177
# https://issues.jboss.org/browse/LOGTOOL-110
BuildRequires:  mvn(org.jboss.jdeparser:jdeparser:1)
BuildRequires:  mvn(org.jboss.logging:jboss-logging-processor:1)
BuildRequires:  mvn(org.jboss.shrinkwrap:shrinkwrap-impl-base)
BuildRequires:  mvn(org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec)
BuildRequires:  mvn(org.jboss.spec.javax.ejb:jboss-ejb-api_3.2_spec)
BuildRequires:  mvn(org.jboss.spec.javax.el:jboss-el-api_3.0_spec)
BuildRequires:  mvn(org.jboss.spec.javax.faces:jboss-jsf-api_2.2_spec)
BuildRequires:  mvn(org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec)
BuildRequires:  mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.1_spec)
BuildRequires:  mvn(org.jboss.spec.javax.transaction:jboss-transaction-api_1.2_spec)
BuildRequires:  mvn(org.jboss.weld:weld-api)
BuildRequires:  mvn(org.jboss.weld:weld-parent:pom:)
BuildRequires:  mvn(org.jboss.weld:weld-spi)
# ./probe/core/src/main/client
Provides:       bundled(fontawesome-fonts) = 4.2.0
Provides:       bundled(fontawesome-fonts-web) = 4.2.0
Source44: import.info

%description
Weld is the reference implementation (RI) for JSR-299: Java Contexts and
Dependency Injection for the Java EE platform (CDI). CDI is the Java standard
for dependency injection and contextual lifecycle management, and integrates
cleanly with the Java EE platform. Any Java EE 6-compliant application server
provides support for JSR-299 (even the web profile). 

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n core-%{namedversion}
%patch0 -p1
%patch1 -p1

find . -name '*.jar' -exec rm {} \;
find . -name '*.class' -exec rm {} \;

# Not needed for build
%pom_remove_plugin org.eclipse.m2e:lifecycle-mapping

# We don't want to build these modules
# org.jboss.cdi.tck:cdi-tck-api:1.2.8.Final
%pom_disable_module porting-package
%pom_disable_module tests
%pom_disable_module tests-arquillian
%pom_disable_module inject-tck-runner
%pom_disable_module jboss-tck-runner
%pom_disable_module tests/base environments/servlet
%pom_disable_module tests/jetty environments/servlet
%pom_disable_module tests/tomcat environments/servlet
%pom_disable_module tests environments/se

%pom_disable_module tests probe
# ro.isdc.wro4j:wro4j-maven-plugin:1.7.7
%pom_remove_plugin ro.isdc.wro4j:wro4j-maven-plugin probe/core

# Don't ship or run checkstyle configuration, see rhbz #825355
%pom_remove_plugin org.apache.maven.plugins:maven-checkstyle-plugin

# Requires jetty6
rm -rf environments/servlet/core/src/main/java/org/jboss/weld/environment/gwtdev
%pom_remove_dep -r org.mortbay.jetty environments/servlet

# Used to compile test classes, but we do not execute tests at all
%pom_remove_plugin org.apache.maven.plugins:maven-compiler-plugin environments/se/core

# Do not bundle system libraries (e. g. com.sun.tools)
%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r :maven-shade-plugin environments/se/build environments/servlet/build
%pom_xpath_remove -r pom:dependency/pom:optional environments/se/build environments/servlet/build

%pom_change_dep org.glassfish:javax.el javax.el:el-api tests-common

%pom_xpath_set pom:properties/pom:jboss.logging.processor.version 1
%pom_change_dep -r :jboss-logging-processor ::1

%build

%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.5-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt1_5jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.6-alt1_4jpp8
- unbootsrap build

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.5-alt3_4.AS71.Finaljpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.5-alt2_4.AS71.Finaljpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.5-alt1_4.AS71.Finaljpp7
- new version

