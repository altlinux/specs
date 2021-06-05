Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global srcname jpa-api
%global specver 2.2

Name:           jakarta-persistence
Version:        2.2.3
Release:        alt1_2jpp11
Summary:        JPA / Jakarta Persistence API
License:        EPL-2.0 or BSD

%global src_ver %{specver}-%{version}-RELEASE

URL:            https://github.com/eclipse-ee4j/jpa-api
Source0:        %{url}/archive/%{src_ver}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)

# package renamed in fedora 33, remove in fedora 35
Provides:       geronimo-jpa = %{version}-%{release}
Obsoletes:      geronimo-jpa < 1.1.1-28
Source44: import.info

%description
Jakarta Persistence defines a standard for management of persistence
and object/relational mapping in Java environments.


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}

# package renamed in fedora 33, remove in fedora 35
Provides:       geronimo-jpa-javadoc = %{version}-%{release}
Obsoletes:      geronimo-jpa-javadoc < 1.1.1-28
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{srcname}-%{src_ver}

pushd api
# remove unnecessary dependency on parent POM
%pom_remove_parent

# remove unnecessary maven plugins
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-javadoc-plugin

# add alias for old artifact coordinates used by osgi-compendium
%mvn_alias jakarta.persistence:jakarta.persistence-api javax.persistence:persistence-api
popd


%build
pushd api
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8
popd


%install
pushd api
%mvn_install
popd


%files -f api/.mfiles
%doc --no-dereference LICENSE.md NOTICE.md
%doc README.md

%files javadoc -f api/.mfiles-javadoc
%doc --no-dereference LICENSE.md NOTICE.md


%changelog
* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 2.2.3-alt1_2jpp11
- new version

