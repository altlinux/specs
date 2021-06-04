Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jaxb-dtd-parser
Version:        1.4.3
Release:        alt1_4jpp11
Summary:        SAX-like API for parsing XML DTDs
License:        BSD

URL:            https://github.com/eclipse-ee4j/jaxb-dtd-parser
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

Obsoletes:      glassfish-dtd-parser < 1.4.3-1
Provides:       glassfish-dtd-parser = %{version}-%{release}
Source44: import.info

%description
SAX-like API for parsing XML DTDs.


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q

pushd dtd-parser
# remove unnecessary dependency on parent POM
# org.eclipse.ee4j:project is not packaged and isn't needed
%pom_remove_parent

# remove unnecessary plugins
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin

popd


%build
pushd dtd-parser
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8
popd


%install
pushd dtd-parser
%mvn_install
popd


%files -f dtd-parser/.mfiles
%doc --no-dereference LICENSE.md NOTICE.md
%doc README.md

%files javadoc -f dtd-parser/.mfiles-javadoc
%doc --no-dereference LICENSE.md NOTICE.md


%changelog
* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1.4.3-alt1_4jpp11
- new version

