Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name resteasy
%define version 3.0.6
%global namedreltag .Final
%global namedversion %{version}%{namedreltag}

Name:       resteasy
Version:    3.0.6
Release:    alt1_11jpp8
Summary:    Framework for RESTful Web services and Java applications
License:    ASL 2.0 and CDDL
URL:        http://www.jboss.org/resteasy
Source0:    https://github.com/resteasy/Resteasy/archive/%{namedversion}.tar.gz

# Support for mime4j 0.7.2
Patch0:     0001-Mime4j-0.7.2-support.patch
Patch1:     0002-bcmail-api-change.patch
Patch2:     0003-resteasy-cve-2014-3490.patch
Patch3:     0004-fix-deprecated-api-usage.patch

BuildArch: noarch

BuildRequires:  maven-local
BuildRequires:  mvn(asm:asm)
BuildRequires:  mvn(com.beust:jcommander)
BuildRequires:  mvn(com.fasterxml:classmate)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-json-provider)
BuildRequires:  mvn(com.google.inject:guice)
BuildRequires:  mvn(commons-httpclient:commons-httpclient)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(com.sun.xml.bind:jaxb-impl)
BuildRequires:  mvn(com.sun.xml.fastinfoset:FastInfoset)
BuildRequires:  mvn(httpunit:httpunit)
BuildRequires:  mvn(io.undertow:undertow-core)
BuildRequires:  mvn(io.undertow:undertow-servlet)
BuildRequires:  mvn(javax.annotation:jsr250-api)
BuildRequires:  mvn(javax.el:javax.el-api)
BuildRequires:  mvn(javax.enterprise:cdi-api)
BuildRequires:  mvn(javax.json:javax.json-api)
BuildRequires:  mvn(javax.mail:mail)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(log4j:log4j)
BuildRequires:  mvn(net.jcip:jcip-annotations)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.james:apache-mime4j-core)
BuildRequires:  mvn(org.apache.james:apache-mime4j-dom)
BuildRequires:  mvn(org.apache.james:apache-mime4j-storage)
BuildRequires:  mvn(org.apache.maven.plugins:maven-deploy-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.bouncycastle:bcmail-jdk16)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk16)
BuildRequires:  mvn(org.codehaus.jackson:jackson-core-asl)
BuildRequires:  mvn(org.codehaus.jackson:jackson-jaxrs)
BuildRequires:  mvn(org.codehaus.jackson:jackson-mapper-asl)
BuildRequires:  mvn(org.codehaus.jackson:jackson-xc)
BuildRequires:  mvn(org.codehaus.jettison:jettison)
BuildRequires:  mvn(org.eclipse.jetty:jetty-server)
BuildRequires:  mvn(org.glassfish:javax.json)
BuildRequires:  mvn(org.glassfish.web:javax.el)
BuildRequires:  mvn(org.hibernate:hibernate-validator)
BuildRequires:  mvn(org.hibernate.javax.persistence:hibernate-jpa-2.0-api)
BuildRequires:  mvn(org.infinispan:infinispan-core)
BuildRequires:  mvn(org.jboss.spec.javax.annotation:jboss-annotations-api_1.1_spec)
BuildRequires:  mvn(org.jboss.spec.javax.ejb:jboss-ejb-api_3.1_spec)
BuildRequires:  mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_2.5_spec)
BuildRequires:  mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec)
BuildRequires:  mvn(org.jboss.weld.se:weld-se)
BuildRequires:  mvn(org.jboss.weld:weld-core)
BuildRequires:  mvn(org.picketbox:picketbox)
BuildRequires:  mvn(org.scannotation:scannotation)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  mvn(org.springframework:spring-core)
BuildRequires:  mvn(org.springframework:spring-webmvc)
BuildRequires:  mvn(org.yaml:snakeyaml)

%if 0%{?fedora} > 20
BuildRequires:  mvn(io.netty:netty-all)
%else
BuildRequires:  mvn(io.netty:netty)
%endif

Requires:       resteasy-jaxrs-api = %{version}
Requires:       resteasy-core = %{version}
Requires:       resteasy-atom-provider = %{version}
Requires:       resteasy-fastinfoset-provider = %{version}
Requires:       resteasy-jackson-provider = %{version}
Requires:       resteasy-jackson2-provider = %{version}
Requires:       resteasy-jaxb-provider = %{version}
Requires:       resteasy-jettison-provider = %{version}
Requires:       resteasy-json-p-provider = %{version}
Requires:       resteasy-multipart-provider = %{version}
Requires:       resteasy-validator-provider-11 = %{version}
Requires:       resteasy-yaml-provider = %{version}
Requires:       resteasy-client = %{version}
Requires:       resteasy-optional = %{version}
Requires:       resteasy-test = %{version}
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
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%package        jaxrs-api
Group: Development/Java
Summary:        Module jaxrs-api for %{name}

%description    jaxrs-api
%{extdesc} %{summary}.

%package        core
Group: Development/Java
Summary:        Core modules for %{name}

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
%mvn_package ":jaxrs-api" jaxrs-api
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
%mvn_package ":resteasy-servlet-initializer" optional
%mvn_package ":resteasy-spring" optional
%mvn_package ":resteasy-undertow" optional
%mvn_package ":security-pom" optional
%mvn_package ":tjws" optional

%if 0%{?fedora} > 20
%mvn_package ":resteasy-netty4" optional
%else
%mvn_package ":resteasy-netty" optional
%endif

# Disable unnecesary modules
%pom_disable_module examples jaxrs/pom.xml
%pom_disable_module profiling-tests jaxrs/pom.xml
%pom_disable_module resteasy-test-data jaxrs/pom.xml
%pom_disable_module war-tests jaxrs/pom.xml
%pom_disable_module resteasy-links jaxrs/pom.xml
%pom_disable_module jboss-modules jaxrs/pom.xml

%pom_disable_module resteasy-oauth jaxrs/security/pom.xml
%pom_disable_module login-module-authenticator jaxrs/security/pom.xml
%pom_disable_module skeleton-key-idm jaxrs/security/pom.xml
%pom_disable_module keystone/keystone-as7 jaxrs/security/pom.xml
%pom_disable_module keystone/keystone-as7-modules jaxrs/security/pom.xml

%pom_disable_module async-http-servlet-3.0-test jaxrs/async-http-servlet-3.0/pom.xml
%pom_disable_module callback-test jaxrs/async-http-servlet-3.0/pom.xml
# HV 4.3
%pom_disable_module resteasy-hibernatevalidator-provider jaxrs/providers/pom.xml

%if 0%{?fedora} > 20
# Leave Netty 4, disable Netty 3
%pom_disable_module resteasy-netty jaxrs/server-adapters/pom.xml
%else
# Leave Netty 3, disable Netty 4
%pom_disable_module resteasy-netty4 jaxrs/server-adapters/pom.xml
%endif

# Replace 2.5 servlet with the jboss-servlet-2.5-api provides
for m in jaxrs/tjws; do
%pom_remove_dep "javax.servlet:servlet-api" ${m}/pom.xml
%pom_add_dep "org.jboss.spec.javax.servlet:jboss-servlet-api_2.5_spec" ${m}/pom.xml
done

# Need to be patched to work with Jetty 9
rm jaxrs/resteasy-spring/src/main/java/org/jboss/resteasy/springmvc/JettyLifecycleManager.java

%pom_remove_dep "org.springframework:spring-test" jaxrs/resteasy-spring/pom.xml
%pom_remove_dep "org.mortbay.jetty:jetty" jaxrs/resteasy-spring/pom.xml
%pom_add_dep "org.eclipse.jetty:jetty-server" jaxrs/resteasy-spring/pom.xml

%pom_remove_plugin com.atlassian.maven.plugins:maven-clover2-plugin jaxrs/pom.xml
%pom_remove_plugin com.atlassian.maven.plugins:maven-clover2-plugin jaxrs/resteasy-jaxrs/pom.xml

# remove activation.jar dependencies
%pom_remove_dep "javax.activation:activation" jaxrs/resteasy-jaxrs/pom.xml
%pom_remove_dep "javax.activation:activation" jaxrs/pom.xml
%pom_remove_dep "javax.activation:activation" jaxrs/resteasy-spring/pom.xml

# Fixing JDK7 ASCII issues
files='
jaxrs/resteasy-jsapi/src/main/java/org/jboss/resteasy/jsapi/JSAPIWriter.java
jaxrs/resteasy-jsapi/src/main/java/org/jboss/resteasy/jsapi/JSAPIServlet.java
jaxrs/resteasy-jsapi/src/main/java/org/jboss/resteasy/jsapi/ServiceRegistry.java
'

for f in ${files}; do
native2ascii -encoding UTF8 ${f} ${f}
done

%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1

# additional gId:aId for jaxrs-api
%mvn_alias ":jaxrs-api" "org.jboss.spec.javax.ws.rs:jboss-jaxrs-api_1.1_spec"

%build
%mvn_build -f

# Create Jandex index file(s)
# Not all files are required by WildFly, but let's create indexes for all of them
find -name 'resteasy-*-%{namedversion}.jar' | while read f; do
  java -cp $(build-classpath jandex) org.jboss.jandex.Main -j ${f}
done

%install
%mvn_install

find -name "resteasy-*-jandex.jar" | while read f; do
  install -pm 644 ${f} %{buildroot}%{_javadir}/%{name}/$(basename -s "-%{namedversion}-jandex.jar" $f)-jandex.jar
done

%files
%doc jaxrs/License.html jaxrs/README.html
%files jaxrs-api -f .mfiles-jaxrs-api
%files core -f .mfiles-core
%dir %{_javadir}/%{name}
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
%{_javadir}/%{name}/resteasy-servlet-initializer-jandex.jar
%{_javadir}/%{name}/resteasy-undertow-jandex.jar
%if 0%{?fedora} > 20
%{_javadir}/%{name}/resteasy-netty4-jandex.jar
%else
%{_javadir}/%{name}/resteasy-netty-jandex.jar
%endif
%files test -f .mfiles-test
%{_javadir}/%{name}/resteasy-jaxrs-testsuite-jandex.jar
%files javadoc -f .mfiles-javadoc
%doc jaxrs/License.html



%changelog
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

