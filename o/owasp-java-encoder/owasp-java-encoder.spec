Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		owasp-java-encoder
Version:	1.2.2
Release:	alt1_5jpp11
Summary:	Collection of high-performance low-overhead contextual encoders

License:	BSD
URL:		https://github.com/OWASP/owasp-java-encoder/

Source0:	https://github.com/OWASP/owasp-java-encoder/archive/v%{version}.tar.gz

# package as a bundle instead of a jar
Patch0:		0_bundle-packaging.patch
# source/target option of 1.5 not compatible with maven-compiler-plugin 3.8.1 >= in f33
Patch1:		1_update-compiler-plugin-version.patch

BuildArch:	noarch

BuildRequires:	maven-local
BuildRequires:	mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:	mvn(org.apache.felix:maven-bundle-plugin)
Source44: import.info

%description
The OWASP Encoders package is a collection of high-performance low-overhead
contextual encoders, that when utilized correctly, is an effective tool in
preventing Web Application security vulnerabilities such as
Cross-Site Scripting.

%package javadoc
Group: Development/Java
Summary:  Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q

%patch0 -p1
%patch1 -p1

%pom_disable_module jsp
%pom_disable_module esapi

%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin

# analysis tool for testing coverage is not required
%pom_remove_plugin :cobertura-maven-plugin

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
* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1.2.2-alt1_5jpp11
- new version

