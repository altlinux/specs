Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global srcname common-annotations-api

Name:           jakarta-annotations
Version:        1.3.5
Release:        alt1_6jpp11
Summary:        Jakarta Annotations
License:        EPL-2.0 or GPLv2 with exceptions

URL:            https://github.com/eclipse-ee4j/common-annotations-api
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)

# renamed in fedora 33, remove in fedora 35
Obsoletes:      glassfish-annotation-api < 1.3.5-1
Provides:       glassfish-annotation-api = %{version}-%{release}
Source44: import.info

%description
Jakarta Annotations defines a collection of annotations representing
common semantic concepts that enable a declarative style of programming
that applies across a variety of Java technologies.


%javadoc_package


%prep
%setup -q -n %{srcname}-%{version}

# remove unnecessary dependency on parent POM
# org.eclipse.ee4j:project is not packaged and isn't needed
%pom_remove_parent

# disable spec submodule: it's not needed, and
# it has missing dependencies (jruby, asciidoctor-maven-plugin, ...)
%pom_disable_module spec

# remove plugins not needed for RPM builds
%pom_remove_plugin :maven-javadoc-plugin api
%pom_remove_plugin :maven-source-plugin api
%pom_remove_plugin :findbugs-maven-plugin api

# provide aliases for the old artifact coordinates
%mvn_alias jakarta.annotation:jakarta.annotation-api \
  javax.annotation:javax.annotation-api \
  javax.annotation:jsr250-api

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8


%install
%mvn_install


%files -f .mfiles
%doc --no-dereference LICENSE.md NOTICE.md
%doc README.md


%changelog
* Wed Jun 02 2021 Igor Vlasenko <viy@altlinux.org> 1.3.5-alt1_6jpp11
- new version

