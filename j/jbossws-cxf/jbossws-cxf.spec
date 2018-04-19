Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 5.1.5
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jbossws-cxf
Version:          5.1.5
Release:          alt1_4jpp8
Summary:          JBoss Web Services CXF stack
License:          LGPLv2+
URL:              http://jbossws.jboss.org/

Source0:          http://download.jboss.org/jbossws/%{name}-%{namedversion}.zip

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(asm:asm)
BuildRequires:    mvn(com.sun.xml.fastinfoset:FastInfoset)
BuildRequires:    mvn(commons-collections:commons-collections)
BuildRequires:    mvn(commons-lang:commons-lang)
BuildRequires:    mvn(javax.xml.stream:stax-api)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(log4j:log4j)
BuildRequires:    mvn(org.apache.cxf:cxf-rt-bindings-coloc)
BuildRequires:    mvn(org.apache.cxf:cxf-rt-bindings-object)
BuildRequires:    mvn(org.apache.cxf:cxf-rt-bindings-soap)
BuildRequires:    mvn(org.apache.cxf:cxf-rt-frontend-jaxws)
BuildRequires:    mvn(org.apache.cxf:cxf-rt-management)
BuildRequires:    mvn(org.apache.cxf:cxf-rt-transports-http)
BuildRequires:    mvn(org.apache.cxf:cxf-rt-transports-http-hc)
BuildRequires:    mvn(org.apache.cxf:cxf-rt-transports-jms)
BuildRequires:    mvn(org.apache.cxf:cxf-rt-transports-local)
BuildRequires:    mvn(org.apache.cxf:cxf-rt-ws-mex)
BuildRequires:    mvn(org.apache.cxf:cxf-rt-ws-policy)
BuildRequires:    mvn(org.apache.cxf:cxf-rt-ws-rm)
BuildRequires:    mvn(org.apache.cxf:cxf-rt-ws-security)
BuildRequires:    mvn(org.apache.cxf:cxf-tools-java2ws)
BuildRequires:    mvn(org.apache.cxf:cxf-tools-wsdlto-core)
BuildRequires:    mvn(org.apache.cxf:cxf-tools-wsdlto-databinding-jaxb)
BuildRequires:    mvn(org.apache.cxf:cxf-tools-wsdlto-frontend-jaxws)
BuildRequires:    mvn(org.apache.cxf.services.sts:cxf-services-sts-core)
BuildRequires:    mvn(org.apache.cxf.services.ws-discovery:cxf-services-ws-discovery-api)
BuildRequires:    mvn(org.apache.cxf.xjcplugins:cxf-xjc-boolean)
BuildRequires:    mvn(org.apache.cxf.xjcplugins:cxf-xjc-bug986)
BuildRequires:    mvn(org.apache.cxf.xjcplugins:cxf-xjc-dv)
BuildRequires:    mvn(org.apache.cxf.xjcplugins:cxf-xjc-ts)
BuildRequires:    mvn(org.apache.cxf.xjc-utils:cxf-xjc-runtime)
BuildRequires:    mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:    mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:    mvn(org.apache.santuario:xmlsec)
BuildRequires:    mvn(org.apache.velocity:velocity)
BuildRequires:    mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:    mvn(org.codehaus.woodstox:woodstox-core-asl)
BuildRequires:    mvn(org.glassfish.jaxb:jaxb-core)
BuildRequires:    mvn(org.glassfish.jaxb:jaxb-runtime)
BuildRequires:    mvn(org.glassfish.jaxb:jaxb-xjc)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-annotations)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:    mvn(org.jboss.spec.javax.ejb:jboss-ejb-api_3.1_spec)
BuildRequires:    mvn(org.jboss.spec.javax.jms:jboss-jms-api_1.1_spec)
BuildRequires:    mvn(org.jboss.spec.javax.security.auth.message:jboss-jaspi-api_1.1_spec)
BuildRequires:    mvn(org.jboss.spec.javax.security.jacc:jboss-jacc-api_1.5_spec)
BuildRequires:    mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.1_spec)
BuildRequires:    mvn(org.jboss.spec.javax.xml.bind:jboss-jaxb-api_2.2_spec)
BuildRequires:    mvn(org.jboss.spec.javax.xml.soap:jboss-saaj-api_1.3_spec)
BuildRequires:    mvn(org.jboss.spec.javax.xml.ws:jboss-jaxws-api_2.2_spec)
BuildRequires:    mvn(org.jboss.ws:jbossws-api)
BuildRequires:    mvn(org.jboss.ws:jbossws-common)
BuildRequires:    mvn(org.jboss.ws:jbossws-common-tools)
BuildRequires:    mvn(org.jboss.ws:jbossws-parent:pom:)
BuildRequires:    mvn(org.jboss.ws:jbossws-spi)
BuildRequires:    mvn(org.jboss.ws.projects:jaxws-undertow-httpspi)
BuildRequires:    mvn(org.jboss.shrinkwrap:shrinkwrap-depchain:pom:)
BuildRequires:    mvn(org.opensaml:opensaml-saml-impl)
BuildRequires:    mvn(org.opensaml:opensaml-xacml-impl)
BuildRequires:    mvn(org.opensaml:opensaml-xacml-saml-impl)
BuildRequires:    mvn(org.picketbox:picketbox)
BuildRequires:    mvn(org.slf4j:slf4j-log4j12)
BuildRequires:    mvn(xerces:xercesImpl)
Source44: import.info

%description
JBoss Web Services CXF integration stack

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{namedversion}

%pom_remove_plugin -r :maven-deploy-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-jdocbook-plugin

# Available in JDK
%pom_remove_dep -r "javax.jws:jsr181-api"

#%% pom_disable_module modules/dist
%pom_disable_module modules/testsuite

# Disable default-jar execution of maven-jar-plugin, which is causing
# problems with version 3.0.0 of the plugin.
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions" "
<execution>
  <id>default-jar</id>
  <phase>skip</phase>
</execution>" modules/resources

%mvn_package :::wildfly*: __default

%build

%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README*

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 5.1.5-alt1_4jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 5.1.5-alt1_3jpp8
- new version

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 4.2.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.2-alt4_2jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.2-alt3_2jpp7
- NMU rebuild to move poms and fragments

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.2-alt2_2jpp7
- fixed build

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.2-alt1_2jpp7
- new version

