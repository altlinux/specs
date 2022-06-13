Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           xmlpull
Version:        1.2.0
Release:        alt1_3jpp11
Summary:        XML Pull Parsing API

License:        Public Domain
URL:            https://github.com/xmlpull-xpp3/%{name}-xpp3
Source0:        https://github.com/xmlpull-xpp3/%{name}-xpp3/archive/%{name}-xpp3-parent-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(junit:junit)
Source44: import.info

%description
XmlPull v1 API is a simple to use XML pull parsing API that was
designed for simplicity and very good performance both in constrained
environment such as defined by J2ME and on server side when used in
J2EE application servers.

%javadoc_package

%prep
%setup -q -n %{name}-xpp3-%{name}-xpp3-parent-%{version}


find \( -name \*.jar -o -name \*.class \) -delete

%pom_disable_module xpp3_min

# using java 8, we need to remove the java module
rm xmlpull/src/main/java/module-info.java

%mvn_package :%{name}-xpp3-parent __noinstall

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference %{name}/LICENSE.txt
%doc %{name}/README.adoc

%changelog
* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 1.2.0-alt1_3jpp11
- new version

