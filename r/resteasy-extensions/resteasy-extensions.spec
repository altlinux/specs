%define _unpackaged_files_terminate_build 1

Name: resteasy-extensions
Version: 2.0.2
Release: alt1

Summary: RESTEasy extension project POM
License: Apache-2.0
Group: Development/Java
URL: https://resteasy.dev/
VCS: https://github.com/resteasy/resteasy-extensions.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.jboss:jboss-parent:pom:)

%description
Maven parent POM for the RESTEasy extensions. This build includes the
independent tracing API used by the RESTEasy core.

%package tracing-api
Summary: RESTEasy tracing API
Group: Development/Java

%description tracing-api
Tracing events, configuration and format providers for RESTEasy.

%package javadoc
Summary: API documentation for RESTEasy tracing
Group: Development/Documentation

%description javadoc
Generated API documentation for the RESTEasy tracing API.

%prep
%setup
%pom_disable_module eagledns
%pom_disable_module cache
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :formatter-maven-plugin
%pom_remove_plugin :impsort-maven-plugin
%pom_remove_dep org.jboss.resteasy:resteasy-bom
%pom_remove_dep org.junit:junit-bom
%pom_xpath_remove 'pom:dependencies/pom:dependency[pom:scope="test"]' tracing
%pom_xpath_remove 'pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration/pom:annotationProcessorPaths'
%mvn_package :resteasy-tracing-api tracing-api
%mvn_package :*::sources: __noinstall

%build
%mvn_build -f

%install
%mvn_install
rm -f -- %buildroot%_javadocdir/%name/args
rm -rf -- %buildroot%_javadocdir/%name/module-source-path

%files -f .mfiles
%doc LICENSE.md

%files tracing-api -f .mfiles-tracing-api

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 2.0.2-alt1
- Initial build for ALT.
