Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          glassfish-jax-rs-api
Version:       2.1.5
Release:       alt1_3jpp8
Summary:       JAX-RS API Specification (JSR 339)
License:       EPL-2.0 or GPLv2 with exceptions
URL:           https://github.com/eclipse-ee4j/jaxrs-api
Source0:       https://github.com/eclipse-ee4j/jaxrs-api/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)

BuildArch:     noarch
Source44: import.info

%description
JAX-RS Java API for RESTful Web Services (JSR 339).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n jaxrs-api-%{version}
find . -name '*.jar' -delete
find . -name '*.class' -delete

# Plugins not needed for RPM builds
%pom_remove_plugin org.apache.maven.plugins:maven-jxr-plugin jaxrs-api
%pom_remove_plugin org.apache.maven.plugins:maven-checkstyle-plugin jaxrs-api
%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin jaxrs-api
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin jaxrs-api
%pom_remove_plugin org.apache.maven.plugins:maven-deploy-plugin jaxrs-api

%pom_xpath_remove "pom:build/pom:finalName" jaxrs-api

# Avoid duplicate invokation of javadoc plugin
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-javadoc-plugin' ]/pom:executions" jaxrs-api

%build
(
cd jaxrs-api
# Compatibility symlink
%mvn_file :{*} @1 %{name}

# Compatibility alias
%mvn_alias : javax.ws.rs:javax.ws.rs-api

%mvn_build
)

%install
(
cd jaxrs-api
%mvn_install
)

%files -f jaxrs-api/.mfiles
%doc --no-dereference LICENSE.md NOTICE.md
%doc README.md CONTRIBUTING.md

%files javadoc -f jaxrs-api/.mfiles-javadoc
%doc --no-dereference LICENSE.md NOTICE.md

%changelog
* Mon Jul 08 2019 Igor Vlasenko <viy@altlinux.ru> 2.1.5-alt1_3jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_7jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_2jpp8
- new version

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_4jpp7
- new release

