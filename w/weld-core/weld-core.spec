Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name weld-core
%define version 2.2.6
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:       weld-core
Version:    2.2.6
Release:    alt1_5jpp8
Summary:    Reference Implementation for JSR-299: Contexts and Dependency Injection (CDI)
License:    ASL 2.0 and LGPLv2+ and (CDDL or GPLv2 with exceptions)
URL:        http://seamframework.org/Weld
Source0:    https://github.com/weld/core/archive/%{namedversion}.tar.gz

Patch0:     0001-Add-support-for-newer-jboss-logging-tools.patch
Patch1:     0001-Remove-gwtdev-environment.patch

BuildArch: noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.eclipse.jetty:jetty-server:8.1.14.v20131031)
BuildRequires:  mvn(org.eclipse.jetty:jetty-servlet:8.1.14.v20131031)
BuildRequires:  mvn(org.eclipse.jetty:jetty-webapp:8.1.14.v20131031)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(javax.el:el-api)
BuildRequires:  mvn(javax.enterprise:cdi-api)
BuildRequires:  mvn(javax.faces:jsf-api)
BuildRequires:  mvn(javax.persistence:persistence-api)
BuildRequires:  mvn(javax.portlet:portlet-api)
BuildRequires:  mvn(javax.servlet.jsp:jsp-api)
BuildRequires:  mvn(javax.transaction:jta)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.sourceforge.findbugs:annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.tomcat:tomcat-catalina)
BuildRequires:  mvn(org.codehaus.groovy:groovy-all)
BuildRequires:  mvn(org.eclipse.jetty:jetty-plus)
BuildRequires:  mvn(org.jboss.classfilewriter:jboss-classfilewriter)
BuildRequires:  mvn(org.jboss:jandex)
BuildRequires:  mvn(org.jboss.logging:jboss-logging)
BuildRequires:  mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:  mvn(org.jboss.shrinkwrap:shrinkwrap-impl-base)
BuildRequires:  mvn(org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec)
BuildRequires:  mvn(org.jboss.spec.javax.ejb:jboss-ejb-api_3.1_spec)
BuildRequires:  mvn(org.jboss.spec.javax.el:jboss-el-api_3.0_spec)
BuildRequires:  mvn(org.jboss.spec.javax.faces:jboss-jsf-api_2.2_spec)
BuildRequires:  mvn(org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec)
BuildRequires:  mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec)
BuildRequires:  mvn(org.jboss.weld:weld-api)
BuildRequires:  mvn(org.jboss.weld:weld-parent:pom:)
BuildRequires:  mvn(org.jboss.weld:weld-spi)
Source44: import.info

%description
Weld is the reference implementation (RI) for JSR-299: Java Contexts and
Dependency Injection for the Java EE platform (CDI). CDI is the Java standard
for dependency injection and contextual lifecycle management, and integrates
cleanly with the Java EE platform. Any Java EE 6-compliant application server
provides support for JSR-299 (even the web profile). 

%package javadoc
Group: Development/Java
Summary: Javadocs for %{name}
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
%pom_disable_module porting-package/1.1
%pom_disable_module tests
%pom_disable_module tests-arquillian
%pom_disable_module inject-tck-runner
%pom_disable_module jboss-tck-runner/1.1
%pom_disable_module tests/base environments/servlet
%pom_disable_module tests/jetty environments/servlet
%pom_disable_module tests/tomcat environments/servlet

# Don't ship or run checkstyle configuration, see rhbz #825355
%pom_remove_plugin org.apache.maven.plugins:maven-checkstyle-plugin

# Requires jetty6
rm -rf environments/servlet/core/src/main/java/org/jboss/weld/environment/gwtdev
%pom_remove_dep -r org.mortbay.jetty environments/servlet

# Used to compile test classes, but we do not execute tests at all
%pom_remove_plugin org.apache.maven.plugins:maven-compiler-plugin environments/se/core/pom.xml

%pom_remove_dep org.glassfish:javax.el tests-common/pom.xml
%pom_add_dep javax.el:el-api tests-common/pom.xml

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
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

