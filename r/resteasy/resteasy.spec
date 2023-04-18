Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 3.0.26
%global namedreltag .Final
%global namedversion %{version}%{namedreltag}

Name:           resteasy
Version:        3.0.26
Release:        alt1_17jpp11
Summary:        Framework for RESTful Web services and Java applications
License:        ASL 2.0
URL:            http://resteasy.jboss.org/
Source0:        https://github.com/resteasy/Resteasy/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz
Patch1:         0001-RESTEASY-2559-Improper-validation-of-response-header.patch
Patch2:         0001-Remove-Log4jLogger.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
#BuildRequires:  mvn(org.apache.tomcat:tomcat-servlet-api)
BuildRequires:  tomcat-servlet-4.0-api

# Jackson 2
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.fasterxml.jackson.jaxrs:jackson-jaxrs-json-provider)

BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
BuildRequires:  mvn(org.jboss.logging:jboss-logging)
BuildRequires:  mvn(org.jboss.logging:jboss-logging-annotations)
BuildRequires:  mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:  mvn(javax.annotation:javax.annotation-api)
BuildRequires:  mvn(org.jboss.spec.javax.ws.rs:jboss-jaxrs-api_2.0_spec)
BuildRequires:  mvn(org.slf4j:slf4j-api)
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

%package -n     pki-%{name}
Group: Development/Java
Summary:        Framework for RESTful Web services and Java applications
Obsoletes:      %{name} < %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
Provides:       %{name} = %{version}-%{release}

Requires:       resteasy-client = %{version}-%{release}
Requires:       resteasy-core = %{version}-%{release}
Requires:       resteasy-jackson2-provider = %{version}-%{release}

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

%description -n pki-%{name}
%{desc}

%package -n     pki-%{name}-core
Group: Development/Java
Summary:        Core modules for %{name}
Obsoletes:      resteasy-jaxrs-api < 3.0.7
Obsoletes:      %{name}-core < %{version}-%{release}
Conflicts:      %{name}-core < %{version}-%{release}
Provides:       %{name}-core = %{version}-%{release}

%description -n pki-%{name}-core
%{extdesc} %{summary}.

%package -n     pki-%{name}-jackson2-provider
Group: Development/Java
Summary:        Module jackson2-provider for %{name}
Obsoletes:      %{name}-jackson2-provider < %{version}-%{release}
Conflicts:      %{name}-jackson2-provider < %{version}-%{release}
Provides:       %{name}-jackson2-provider = %{version}-%{release}

%description -n pki-%{name}-jackson2-provider
%{extdesc} %{summary}.

%package -n     pki-%{name}-client
Group: Development/Java
Summary:        Client for %{name}
Obsoletes:      %{name}-client < %{version}-%{release}
Conflicts:      %{name}-client < %{version}-%{release}
Provides:       %{name}-client = %{version}-%{release}

%description -n pki-%{name}-client
%{extdesc} %{summary}.

%prep
%setup -q -n Resteasy-%{namedversion}
%patch1 -p1
%patch2 -p1


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
%pom_disable_module resteasy-atom
%pom_disable_module resteasy-html
%pom_disable_module resteasy-validator-provider-11
%pom_disable_module yaml
%pom_disable_module jaxb
popd

find -name '*.jar' -print -delete

%pom_remove_plugin :maven-clover2-plugin
%pom_remove_plugin :maven-javadoc-plugin

# depend on jakarta-activation
%pom_change_dep javax.activation:activation jakarta.activation:jakarta.activation-api resteasy-jaxrs
%pom_change_dep javax.activation:activation jakarta.activation:jakarta.activation-api resteasy-spring

# depend on jakarta-annotations
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api jboss-modules
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api providers/jaxb
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api resteasy-dependencies-bom
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api resteasy-guice
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api resteasy-jaxrs
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api resteasy-links
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api resteasy-spring
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api security/keystone/keystone-core
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api security/resteasy-crypto
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api security/skeleton-key-idm/skeleton-key-core
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api security/skeleton-key-idm/skeleton-key-idp
%pom_change_dep org.jboss.spec.javax.annotation:jboss-annotations-api_1.2_spec javax.annotation:javax.annotation-api server-adapters/resteasy-jdk-http

# remove resteasy-dependencies pom
%pom_remove_dep "org.jboss.resteasy:resteasy-dependencies"

# remove redundant jcip-dependencies dep from resteasy-jaxrs
%pom_remove_dep net.jcip:jcip-annotations resteasy-jaxrs

# remove junit dependency from all modules
%pom_remove_dep junit:junit resteasy-client
%pom_remove_dep junit:junit providers/resteasy-atom
%pom_remove_dep junit:junit providers/jaxb
%pom_remove_dep junit:junit resteasy-jaxrs

# remove log4j dependency
%pom_remove_dep log4j:log4j resteasy-jaxrs

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
%mvn_package ":resteasy-jackson2-provider" jackson2-provider
%mvn_package ":resteasy-client" client

# Disable useless artifacts generation, package __noinstall do not work
%pom_add_plugin org.apache.maven.plugins:maven-source-plugin . '
<configuration>
 <skipSource>true</skipSource>
</configuration>'

%build
%mvn_build -f -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -n pki-%{name}
%doc README.md
%doc --no-dereference License.html

%files -n pki-%{name}-core -f .mfiles-core
%doc --no-dereference License.html

%files -n pki-%{name}-jackson2-provider -f .mfiles-jackson2-provider
%doc --no-dereference License.html

%files -n pki-%{name}-client -f .mfiles-client
%doc --no-dereference License.html

%changelog
* Tue Apr 18 2023 Igor Vlasenko <viy@altlinux.org> 3.0.26-alt1_17jpp11
- update

* Thu May 26 2022 Igor Vlasenko <viy@altlinux.org> 3.0.26-alt1_15jpp11
- fc update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 3.0.26-alt1_7jpp11
- fc34 update

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

