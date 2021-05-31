Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 3.0.26
%global namedreltag .Final
%global namedversion %{version}%{namedreltag}

Name:           resteasy
Version:        3.0.26
Release:        alt1_5jpp11
Summary:        Framework for RESTful Web services and Java applications
License:        ASL 2.0 and CDDL
URL:            http://resteasy.jboss.org/
Source0:        https://github.com/resteasy/Resteasy/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(com.sun.xml.bind:jaxb-impl)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(log4j:log4j)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.tomcat:tomcat-servlet-api)

# Jackson 2
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-json-provider)

BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
BuildRequires:  mvn(org.jboss.logging:jboss-logging)
BuildRequires:  mvn(org.jboss.logging:jboss-logging-annotations)
BuildRequires:  mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:  mvn(org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec)
BuildRequires:  mvn(org.jboss.spec.javax.ws.rs:jboss-jaxrs-api_2.0_spec)
BuildRequires:  mvn(org.slf4j:slf4j-api)

Requires:       resteasy-atom-provider = %{version}-%{release}
Requires:       resteasy-client = %{version}-%{release}
Requires:       resteasy-core = %{version}-%{release}
Requires:       resteasy-jackson2-provider = %{version}-%{release}
Requires:       resteasy-jaxb-provider = %{version}-%{release}

# subpackages removed in fedora 32
Obsoletes:      %{name}-fastinfoset-provider < 3.0.26-1
Obsoletes:      %{name}-jackson-provider < 3.0.26-1
Obsoletes:      %{name}-jettison-provider < 3.0.26-1
Obsoletes:      %{name}-json-p-provider < 3.0.26-1
Obsoletes:      %{name}-multipart-provider < 3.0.26-1
Obsoletes:      %{name}-netty3 < 3.0.26-1
Obsoletes:      %{name}-optional < 3.0.26-1
Obsoletes:      %{name}-test < 3.0.26-1
Obsoletes:      %{name}-validator-provider-11 < 3.0.26-1
Obsoletes:      %{name}-yaml-provider < 3.0.26-1
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

%package        client
Group: Development/Java
Summary:        Client for %{name}

%description    client
%{extdesc} %{summary}.

%prep
%setup -q -n Resteasy-%{namedversion}

%pom_disable_module arquillian
%pom_disable_module eagledns
%pom_disable_module jboss-modules
%pom_disable_module profiling-tests
%pom_disable_module resteasy-bom
%pom_disable_module resteasy-cache
%pom_disable_module resteasy-cdi
%pom_disable_module resteasy-dependencies-bom
%pom_disable_module resteasy-guice
%pom_disable_module resteasy-jaxrs-testsuite
%pom_disable_module resteasy-jsapi
%pom_disable_module resteasy-jsapi-testing
%pom_disable_module resteasy-links
%pom_disable_module resteasy-servlet-initializer
%pom_disable_module resteasy-spring
%pom_disable_module resteasy-wadl
%pom_disable_module resteasy-wadl-undertow-connector
%pom_disable_module security
%pom_disable_module server-adapters
%pom_disable_module testsuite
%pom_disable_module tjws

pushd providers
%pom_disable_module fastinfoset
%pom_disable_module jackson
%pom_disable_module jettison
%pom_disable_module json-p-ee7
%pom_disable_module multipart
%pom_disable_module resteasy-html
%pom_disable_module resteasy-validator-provider-11
%pom_disable_module yaml
popd

find -name '*.jar' -print -delete

%pom_remove_plugin :maven-clover2-plugin

# remove activation.jar dependencies
%pom_remove_dep -r javax.activation:activation resteasy-jaxrs resteasy-spring

# remove resteasy-dependencies pom
%pom_remove_dep "org.jboss.resteasy:resteasy-dependencies"

# remove redundant jcip-dependencies dep from resteasy-jaxrs
%pom_remove_dep net.jcip:jcip-annotations resteasy-jaxrs

# remove junit dependency from all modules
%pom_remove_dep junit:junit resteasy-client
%pom_remove_dep junit:junit providers/resteasy-atom
%pom_remove_dep junit:junit providers/jaxb
%pom_remove_dep junit:junit resteasy-jaxrs

# depend on servlet-api from pki-servlet-4.0-api
%pom_change_dep org.jboss.spec.javax.servlet: org.apache.tomcat:tomcat-servlet-api resteasy-jaxrs
%pom_change_dep org.jboss.spec.javax.servlet: org.apache.tomcat:tomcat-servlet-api providers/abdera-atom
%pom_change_dep org.jboss.spec.javax.servlet: org.apache.tomcat:tomcat-servlet-api providers/jaxb
%pom_change_dep org.jboss.spec.javax.servlet: org.apache.tomcat:tomcat-servlet-api providers/jackson2

# add dependencies for EE APIs that were removed in Java 11
%pom_add_dep javax.xml.bind:jaxb-api resteasy-jaxrs

%pom_remove_plugin :maven-clean-plugin

%mvn_package ":resteasy-jaxrs" core
%mvn_package ":providers-pom" core
%mvn_package ":resteasy-jaxrs-all" core
%mvn_package ":resteasy-pom" core
%mvn_package ":resteasy-atom-provider" atom-provider
%mvn_package ":resteasy-jackson2-provider" jackson2-provider
%mvn_package ":resteasy-jaxb-provider" jaxb-provider
%mvn_package ":resteasy-client" client

# Disable useless artifacts generation, package __noinstall do not work
%pom_add_plugin org.apache.maven.plugins:maven-source-plugin . '
<configuration>
 <skipSource>true</skipSource>
</configuration>'

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files
%doc README.md
%doc --no-dereference License.html

%files core -f .mfiles-core
%doc --no-dereference License.html

%files atom-provider -f .mfiles-atom-provider
%doc --no-dereference License.html

%files jackson2-provider -f .mfiles-jackson2-provider
%doc --no-dereference License.html

%files jaxb-provider -f .mfiles-jaxb-provider
%doc --no-dereference License.html

%files client -f .mfiles-client
%doc --no-dereference License.html

%files javadoc -f .mfiles-javadoc
%doc --no-dereference License.html

%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 3.0.26-alt1_5jpp11
- update

* Wed May 12 2021 Igor Vlasenko <viy@altlinux.org> 3.0.26-alt1_2jpp8
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.19-alt1_9jpp8
- new version

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

