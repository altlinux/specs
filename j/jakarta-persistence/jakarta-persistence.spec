%define _unpackaged_files_terminate_build 1

Name: jakarta-persistence
Version: 3.2.0
Release: alt1

Summary: Jakarta Persistence API
License: EPL-2.0 OR BSD-3-Clause
Group: Development/Java
Url: https://github.com/jakartaee/persistence
Vcs: https://github.com/jakartaee/persistence.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-default
BuildRequires: maven-plugin-bundle
BuildRequires: maven-plugin-build-helper
BuildRequires: spec-version-maven-plugin

# package renamed in fedora 33, remove in fedora 35
Provides: geronimo-jpa = %EVR
Obsoletes: geronimo-jpa < 1.1.1-28

%description
Jakarta Persistence defines a standard for management of persistence and
object/relational mapping in Java environments.

%prep
%setup

pushd api
# lower bytecode target for ALT build
sed -i 's|<maven.compiler.release>[0-9][0-9]*</maven.compiler.release>|<maven.compiler.release>11</maven.compiler.release>|' pom.xml

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
%mvn_build -j
popd

%install
pushd api
%mvn_install
popd

%files -f api/.mfiles
%doc --no-dereference LICENSE.md NOTICE.md README.md

%changelog
* Tue Mar 31 2026 Ivan Khanas <xeno@altlinux.org> 3.2.0-alt1
- New version.

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 2.2.3-alt1_2jpp11
- new version
