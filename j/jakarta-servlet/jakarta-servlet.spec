Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:           jakarta-servlet
Version:        5.0.0
Release:        alt1_8jpp11
Summary:        Server-side API for handling HTTP requests and responses
# most of the project is EPL-2.0 or GPLv2 w/exceptions,
# but some files still have Apache-2.0 license headers:
# https://github.com/eclipse-ee4j/servlet-api/issues/347
License:        (EPL-2.0 or GPLv2 with exceptions) and ASL 2.0
URL:            https://github.com/eclipse-ee4j/servlet-api
BuildArch:      noarch

Source0:        https://github.com/eclipse-ee4j/servlet-api/archive/%{version}-RELEASE/servlet-api-%{version}.tar.gz

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
%endif

Provides:       glassfish-servlet-api = %{version}-%{release}
Source44: import.info

%description
Jakarta Servlet defines a server-side API for handling HTTP requests
and responses.

%{?javadoc_package}

%prep
%setup -q -n servlet-api-%{version}-RELEASE

# remove unnecessary dependency on parent POM
%pom_remove_parent . api

# do not build specification documentation
%pom_disable_module spec

# Copy to old package name
# TODO: Remove when all dependencies are migrated from javax.servlet to jakarta.servlet
cp -pr api/src/main/java/jakarta api/src/main/java/javax
sed -i -e 's/jakarta\./javax./g' $(find api/src/main/java/javax -name *.java)
%pom_xpath_replace pom:instructions/pom:Export-Package \
  '<Export-Package>jakarta.servlet.*,javax.servlet.*;version="4.0.0"</Export-Package>' api

# do not install useless parent POM
%mvn_package jakarta.servlet:servlet-parent __noinstall

# remove unnecessary maven plugins
%pom_remove_plugin -r :formatter-maven-plugin
%pom_remove_plugin -r :impsort-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-source-plugin

# add maven artifact coordinate aliases for backwards compatibility
%mvn_alias jakarta.servlet:jakarta.servlet-api \
    javax.servlet:javax.servlet-api \
    javax.servlet:servlet-api

# add compat symlink for packages constructing the classpath manually
%mvn_file :{*} %{name}/@1 glassfish-servlet-api

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.md NOTICE.md
%doc README.md

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 5.0.0-alt1_8jpp11
- update

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 5.0.0-alt1_5jpp11
- new version

