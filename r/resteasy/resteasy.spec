Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 3.0.19
%global namedreltag .Final
%global namedversion %{version}%{namedreltag}

Name:           resteasy
Version:        3.0.19
Release:        alt1_7jpp8
Summary:        Framework for RESTful Web services and Java applications
License:        ASL 2.0 and CDDL
URL:            http://resteasy.jboss.org/
Source0:        https://github.com/resteasy/Resteasy/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz

# Support for mime4j 0.7.2
Patch0:         resteasy-3.0.19-Mime4j-0.7.2-support.patch

Patch1:         resteasy-3.0.19-port-resteasy-netty-to-netty-3.10.6.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.beust:jcommander)
BuildRequires:  mvn(com.fasterxml:classmate)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-json-provider)
BuildRequires:  mvn(com.google.inject:guice)
BuildRequires:  mvn(com.sun.mail:javax.mail)
BuildRequires:  mvn(com.sun.xml.bind:jaxb-impl)
BuildRequires:  mvn(com.sun.xml.fastinfoset:FastInfoset)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(io.netty:netty:3)
BuildRequires:  mvn(io.netty:netty-all)
BuildRequires:  mvn(io.undertow:undertow-core)
BuildRequires:  mvn(io.undertow:undertow-servlet)
BuildRequires:  mvn(javax.enterprise:cdi-api)
BuildRequires:  mvn(javax.json:javax.json-api)
BuildRequires:  mvn(javax.validation:validation-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(log4j:log4j:12)
BuildRequires:  mvn(net.jcip:jcip-annotations)
BuildRequires:  mvn(net.oauth.core:oauth-provider)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.james:apache-mime4j-core)
BuildRequires:  mvn(org.apache.james:apache-mime4j-dom)
BuildRequires:  mvn(org.apache.james:apache-mime4j-storage)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.bouncycastle:bcmail-jdk15on)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires:  mvn(org.codehaus.jackson:jackson-core-asl)
BuildRequires:  mvn(org.codehaus.jackson:jackson-jaxrs)
BuildRequires:  mvn(org.codehaus.jackson:jackson-mapper-asl)
BuildRequires:  mvn(org.codehaus.jackson:jackson-xc)
BuildRequires:  mvn(org.codehaus.jettison:jettison)
BuildRequires:  mvn(org.eclipse.jetty:jetty-server)
BuildRequires:  mvn(org.glassfish:javax.el)
BuildRequires:  mvn(org.glassfish:javax.json)
BuildRequires:  mvn(org.hibernate:hibernate-validator)
BuildRequires:  mvn(org.hibernate.javax.persistence:hibernate-jpa-2.0-api)
BuildRequires:  mvn(org.infinispan:infinispan-core)
BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
BuildRequires:  mvn(org.jboss.jandex:jandex-maven-plugin)
BuildRequires:  mvn(org.jboss.logging:jboss-logging)
BuildRequires:  mvn(org.jboss.logging:jboss-logging-annotations)
BuildRequires:  mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:  mvn(org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec)
BuildRequires:  mvn(org.jboss.spec.javax.ejb:jboss-ejb-api_3.1_spec)
BuildRequires:  mvn(org.jboss.spec.javax.el:jboss-el-api_3.0_spec)
BuildRequires:  mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_2.5_spec)
BuildRequires:  mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.1_spec)
BuildRequires:  mvn(org.jboss.spec.javax.ws.rs:jboss-jaxrs-api_2.0_spec)
BuildRequires:  mvn(org.jboss.weld:weld-api)
BuildRequires:  mvn(org.picketbox:picketbox)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.springframework:spring-core)
BuildRequires:  mvn(org.springframework:spring-test)
BuildRequires:  mvn(org.springframework:spring-webmvc)
BuildRequires:  mvn(org.yaml:snakeyaml)

Requires:       resteasy-core = %{version}-%{release}
Requires:       resteasy-atom-provider = %{version}-%{release}
Requires:       resteasy-fastinfoset-provider = %{version}-%{release}
Requires:       resteasy-jackson-provider = %{version}-%{release}
Requires:       resteasy-jackson2-provider = %{version}-%{release}
Requires:       resteasy-jaxb-provider = %{version}-%{release}
Requires:       resteasy-jettison-provider = %{version}-%{release}
Requires:       resteasy-json-p-provider = %{version}-%{release}
Requires:       resteasy-multipart-provider = %{version}-%{release}
Requires:       resteasy-validator-provider-11 = %{version}-%{release}
Requires:       resteasy-yaml-provider = %{version}-%{release}
Requires:       resteasy-client = %{version}-%{release}
Requires:       resteasy-optional = %{version}-%{release}
Requires:       resteasy-test = %{version}-%{release}
Requires:       resteasy-netty3 = %{version}-%{release}
Source44: import.info

%description
%global desc \
RESTEasy contains a JBoss project that provides frameworks to help\
build RESTful Web Services and RESTful Java applications. It is a fully\
certified and portable implementation of the JAX-RS specification.
%{desc}
%global extdesc %{desc}\
\
This package contains

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
This package contains the API documentation for %{name}.

%package        core
Group: Development/Java
Summary:        Core modules for %{name}
Obsoletes:      resteasy-jaxrs-api < 3.0.7

%description    core
%{extdesc} %{summary}.

%package        atom-provider
Group: Development/Java
Summary:        Module atom-provider for %{name}

%description    atom-provider
%{extdesc} %{summary}.

%package        fastinfoset-provider
Group: Development/Java
Summary:        Module fastinfoset-provider for %{name}

%description    fastinfoset-provider
%{extdesc} %{summary}.

%package        jackson-provider
Group: Development/Java
Summary:        Module jackson-provider for %{name}

%description    jackson-provider
%{extdesc} %{summary}.

%package        jackson2-provider
Group: Development/Java
Summary:        Module jackson2-provider for %{name}

%description    jackson2-provider
%{extdesc} %{summary}.

%package        jaxb-provider
Group: Development/Java
Summary:        Module jaxb-provider for %{name}

%description    jaxb-provider
%{extdesc} %{summary}.

%package        jettison-provider
Group: Development/Java
Summary:        Module jettison-provider for %{name}

%description    jettison-provider
%{extdesc} %{summary}.

%package        json-p-provider
Group: Development/Java
Summary:        Module json-p-provider for %{name}

%description    json-p-provider
%{extdesc} %{summary}.

%package        multipart-provider
Group: Development/Java
Summary:        Module multipart-provider for %{name}

%description    multipart-provider
%{extdesc} %{summary}.

%package        netty3
Group: Development/Java
Summary:        Netty 3 Integration for %{name}

%description    netty3
%{extdesc} %{summary}.

%package        validator-provider-11
Group: Development/Java
Summary:        Module validate-provider-11 for %{name}

%description    validator-provider-11
%{extdesc} %{summary}.

%package        yaml-provider
Group: Development/Java
Summary:        Module yaml-provider for %{name}

%description    yaml-provider
%{extdesc} %{summary}.

%package        client
Group: Development/Java
Summary:        Client for %{name}

%description    client
%{extdesc} %{summary}.

%package        optional
Group: Development/Java
# BSD: ./jaxrs/tjws/src/main/java/Acme/*
# LGPLv2: ./jaxrs/resteasy-cdi/src/main/java/org/jboss/resteasy/cdi/CdiPropertyInjector.java
License:        ASL 2.0 and BSD and LGPLv2+
Summary:        Optional modules for %{name}

%description    optional
%{extdesc} %{summary}.

%package        test
Group: Development/Java
Summary:        Test modules for %{name}

%description    test
%{extdesc} %{summary}.

%prep
%setup -q -n Resteasy-%{namedversion}
%mvn_package ":resteasy-jaxrs" core
%mvn_package ":providers-pom" core
%mvn_package ":resteasy-jaxrs-all" core
%mvn_package ":resteasy-pom" core
%mvn_package ":resteasy-atom-provider" atom-provider
%mvn_package ":resteasy-fastinfoset-provider" fastinfoset-provider
%mvn_package ":resteasy-jackson-provider" jackson-provider
%mvn_package ":resteasy-jackson2-provider" jackson2-provider
%mvn_package ":resteasy-jaxb-provider" jaxb-provider
%mvn_package ":resteasy-jettison-provider" jettison-provider
%mvn_package ":resteasy-json-p-provider" json-p-provider
%mvn_package ":resteasy-multipart-provider" multipart-provider
%mvn_package ":resteasy-validator-provider-11" validator-provider-11
%mvn_package ":resteasy-yaml-provider" yaml-provider
%mvn_package ":resteasy-client" client
%mvn_package ":test-resteasy-html" test
%mvn_package ":test-all-jaxb" test
%mvn_package ":test-jackson-jaxb-coexistence" test
%mvn_package ":resteasy-jaxrs-testsuite" test
%mvn_package ":async-http-servlet-3.0" optional
%mvn_package ":asynch-http-servlet-3.0-pom" optional
%mvn_package ":http-adapter-pom" optional
%mvn_package ":jose-jwt" optional
%mvn_package ":resteasy-bom" optional
%mvn_package ":resteasy-cache-core" optional
%mvn_package ":resteasy-cache-pom" optional
%mvn_package ":resteasy-cdi" optional
%mvn_package ":resteasy-crypto" optional
%mvn_package ":resteasy-guice" optional
%mvn_package ":resteasy-html" optional
%mvn_package ":resteasy-jdk-http" optional
%mvn_package ":resteasy-jsapi" optional
%mvn_package ":resteasy-keystone-core" optional
%mvn_package ":resteasy-links" optional
%mvn_package ":resteasy-netty4" optional
%mvn_package ":resteasy-netty4-cdi" optional
%mvn_package ":resteasy-oauth" optional
%mvn_package ":resteasy-servlet-initializer" optional
%mvn_package ":resteasy-spring" optional
%mvn_package ":resteasy-undertow" optional
%mvn_package ":resteasy-wadl" optional
%mvn_package ":security-pom" optional
%mvn_package ":tjws" optional
%mvn_package ":resteasy-netty" netty3

find -name '*.jar' -print -delete

%patch0 -p1
%patch1 -p1

# Disable unnecesary modules
%pom_disable_module examples jaxrs
%pom_disable_module profiling-tests jaxrs
%pom_disable_module resteasy-test-data jaxrs
%pom_disable_module war-tests jaxrs

%pom_disable_module jboss-modules jaxrs
%pom_disable_module login-module-authenticator jaxrs/security
%pom_disable_module skeleton-key-idm jaxrs/security
#skeleton-key-as7
#skeleton-key-idp-war
%pom_disable_module keystone/keystone-as7 jaxrs/security
%pom_disable_module keystone/keystone-as7-modules jaxrs/security

%pom_disable_module test-jackson-jaxb-coexistence jaxrs/providers
%pom_disable_module test-resteasy-html jaxrs/providers

%pom_disable_module arquillian jaxrs

%pom_disable_module async-http-servlet-3.0-test jaxrs/async-http-servlet-3.0
%pom_disable_module callback-test jaxrs/async-http-servlet-3.0
# HV 4.3
%pom_disable_module resteasy-hibernatevalidator-provider jaxrs/providers

%pom_change_dep "org.mortbay.jetty:jetty" "org.eclipse.jetty:jetty-server" jaxrs/resteasy-spring
sed -i "s|org.mortbay.jetty.Server|org.eclipse.jetty.server.Server|" \
 jaxrs/resteasy-spring/src/main/java/org/jboss/resteasy/springmvc/JettyLifecycleManager.java

%pom_remove_plugin com.atlassian.maven.plugins:maven-clover2-plugin jaxrs
%pom_remove_plugin com.atlassian.maven.plugins:maven-clover2-plugin jaxrs/resteasy-jaxrs

# Replace 2.5 servlet with the jboss-servlet-2.5-api provides
%pom_change_dep "javax.servlet:servlet-api" "org.jboss.spec.javax.servlet:jboss-servlet-api_2.5_spec" jaxrs/tjws

%pom_xpath_set pom:properties/pom:dep.netty.version 3 jaxrs

# remove activation.jar dependencies
%pom_remove_dep -r javax.activation:activation jaxrs jaxrs/resteasy-jaxrs jaxrs/resteasy-spring jaxrs/resteasy-test-data

# Remove duplicate entry
%pom_remove_dep :tjws::test jaxrs/resteasy-jaxrs-testsuite

# Fixing JDK7 ASCII issues
files='
jaxrs/resteasy-jaxrs/src/main/java/org/jboss/resteasy/annotations/Query.java
jaxrs/resteasy-jaxrs/src/main/java/org/jboss/resteasy/core/QueryInjector.java
jaxrs/resteasy-jsapi/src/main/java/org/jboss/resteasy/jsapi/JSAPIWriter.java
jaxrs/resteasy-jsapi/src/main/java/org/jboss/resteasy/jsapi/JSAPIServlet.java
jaxrs/resteasy-jsapi/src/main/java/org/jboss/resteasy/jsapi/ServiceRegistry.java
jaxrs/resteasy-links/src/main/java/org/jboss/resteasy/links/AddLinks.java
jaxrs/resteasy-links/src/main/java/org/jboss/resteasy/links/ELProvider.java
jaxrs/resteasy-links/src/main/java/org/jboss/resteasy/links/LinkELProvider.java
jaxrs/resteasy-links/src/main/java/org/jboss/resteasy/links/LinkResource.java
jaxrs/resteasy-links/src/main/java/org/jboss/resteasy/links/LinkResources.java
jaxrs/resteasy-links/src/main/java/org/jboss/resteasy/links/ParentResource.java
jaxrs/resteasy-links/src/main/java/org/jboss/resteasy/links/RESTServiceDiscovery.java
jaxrs/resteasy-links/src/main/java/org/jboss/resteasy/links/ResourceFacade.java
jaxrs/resteasy-links/src/main/java/org/jboss/resteasy/links/ResourceID.java
jaxrs/resteasy-links/src/main/java/org/jboss/resteasy/links/ResourceIDs.java
jaxrs/security/resteasy-oauth/src/main/java/org/jboss/resteasy/auth/oauth/OAuthConsumer.java
jaxrs/security/resteasy-oauth/src/main/java/org/jboss/resteasy/auth/oauth/OAuthException.java
jaxrs/security/resteasy-oauth/src/main/java/org/jboss/resteasy/auth/oauth/OAuthFilter.java
jaxrs/security/resteasy-oauth/src/main/java/org/jboss/resteasy/auth/oauth/OAuthMemoryProvider.java
jaxrs/security/resteasy-oauth/src/main/java/org/jboss/resteasy/auth/oauth/OAuthProvider.java
jaxrs/security/resteasy-oauth/src/main/java/org/jboss/resteasy/auth/oauth/OAuthProviderChecker.java
jaxrs/security/resteasy-oauth/src/main/java/org/jboss/resteasy/auth/oauth/OAuthRequestToken.java
jaxrs/security/resteasy-oauth/src/main/java/org/jboss/resteasy/auth/oauth/OAuthServlet.java
jaxrs/security/resteasy-oauth/src/main/java/org/jboss/resteasy/auth/oauth/OAuthToken.java
jaxrs/security/resteasy-oauth/src/main/java/org/jboss/resteasy/auth/oauth/OAuthValidator.java
'

for f in ${files}; do
native2ascii -encoding UTF8 ${f} ${f}
done

# Disable useless artifacts generation, package __noinstall do not work
%pom_add_plugin org.apache.maven.plugins:maven-source-plugin jaxrs '
<configuration>
 <skipSource>true</skipSource>
</configuration>'

%build

%mvn_build -f

# Create Jandex index file(s)
# Not all files are required by WildFly, but let's create indexes for all of them
find -name 'resteasy-*-%{namedversion}.jar' | while read f; do
  java -cp $(build-classpath jandex) org.jboss.jandex.Main -j ${f}
done

# async-http-servlet-3.0 jose-jwt tjws

%install
%mvn_install

find -name "resteasy-*-jandex.jar" | while read f; do
  install -pm 644 ${f} %{buildroot}%{_javadir}/%{name}/$(basename -s "-%{namedversion}-jandex.jar" $f)-jandex.jar
done

%files
%doc README.md jaxrs/README.html
%doc --no-dereference jaxrs/License.html

%files core -f .mfiles-core
%{_javadir}/%{name}/resteasy-jaxrs-jandex.jar

%files atom-provider -f .mfiles-atom-provider
%{_javadir}/%{name}/resteasy-atom-provider-jandex.jar

%files fastinfoset-provider -f .mfiles-fastinfoset-provider
%{_javadir}/%{name}/resteasy-fastinfoset-provider-jandex.jar
   
%files jackson-provider -f .mfiles-jackson-provider
%{_javadir}/%{name}/resteasy-jackson-provider-jandex.jar
   
%files jackson2-provider -f .mfiles-jackson2-provider
%{_javadir}/%{name}/resteasy-jackson2-provider-jandex.jar

%files jaxb-provider -f .mfiles-jaxb-provider
%{_javadir}/%{name}/resteasy-jaxb-provider-jandex.jar

%files jettison-provider -f .mfiles-jettison-provider
%{_javadir}/%{name}/resteasy-jettison-provider-jandex.jar

%files json-p-provider -f .mfiles-json-p-provider
%{_javadir}/%{name}/resteasy-json-p-provider-jandex.jar

%files multipart-provider -f .mfiles-multipart-provider
%{_javadir}/%{name}/resteasy-multipart-provider-jandex.jar

%files netty3 -f .mfiles-netty3
%{_javadir}/%{name}/resteasy-netty-jandex.jar

%files validator-provider-11 -f .mfiles-validator-provider-11
%{_javadir}/%{name}/resteasy-validator-provider-11-jandex.jar

%files yaml-provider -f .mfiles-yaml-provider
%{_javadir}/%{name}/resteasy-yaml-provider-jandex.jar

%files client -f .mfiles-client
%{_javadir}/%{name}/resteasy-client-jandex.jar

%files optional -f .mfiles-optional
%{_javadir}/%{name}/resteasy-cache-core-jandex.jar
%{_javadir}/%{name}/resteasy-cdi-jandex.jar
%{_javadir}/%{name}/resteasy-crypto-jandex.jar
%{_javadir}/%{name}/resteasy-guice-jandex.jar
%{_javadir}/%{name}/resteasy-html-jandex.jar
%{_javadir}/%{name}/resteasy-jdk-http-jandex.jar
%{_javadir}/%{name}/resteasy-jsapi-jandex.jar
%{_javadir}/%{name}/resteasy-keystone-core-jandex.jar
%{_javadir}/%{name}/resteasy-links-jandex.jar
%{_javadir}/%{name}/resteasy-netty4-cdi-jandex.jar
%{_javadir}/%{name}/resteasy-netty4-jandex.jar
%{_javadir}/%{name}/resteasy-oauth-jandex.jar
%{_javadir}/%{name}/resteasy-servlet-initializer-jandex.jar
%{_javadir}/%{name}/resteasy-undertow-jandex.jar
%{_javadir}/%{name}/resteasy-wadl-jandex.jar

%files test -f .mfiles-test
%{_javadir}/%{name}/resteasy-jaxrs-testsuite-jandex.jar

%files javadoc -f .mfiles-javadoc
%doc --no-dereference jaxrs/License.html

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.19-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.19-alt1_6jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.19-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.6-alt1_11jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.6-alt1_9jpp8
- new version

* Sat Aug 02 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt3_12jpp7
- new release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt3_9jpp7
- fixed build with new cdc - added BR: weld-parent

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt2_9jpp7
- fixed build

* Sun Sep 16 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt1_9jpp7
- new version

