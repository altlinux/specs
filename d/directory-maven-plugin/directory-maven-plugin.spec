Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:       directory-maven-plugin
Version:    0.3.1
Release:    alt1_3jpp11
Summary:    Establish locations for files in multi-module builds

License:    ASL 2.0
URL:        https://github.com/jdcasey/directory-maven-plugin

Source0:    https://github.com/jdcasey/directory-maven-plugin/archive/directory-maven-plugin-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(junit:junit)
Source44: import.info

%description
The Directory Plugin for Maven is used to discover various project-related 
paths, such as the execution root directory, the directory for a specific 
project in the current build session, or the highest project base directory 
(closest to the filesystem root directory) available in the projects loaded 
from disk (not resolved from a remote repository). The plugin will then reflect
this value to the console, and also inject it into each project's properties 
using the value of the property plugin parameter.

%package javadoc
Group: Development/Java
Summary:  Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n directory-maven-plugin-directory-maven-plugin-0.3.1


%pom_remove_parent

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 0.3.1-alt1_3jpp11
- new version

