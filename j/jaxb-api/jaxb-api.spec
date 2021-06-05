Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jaxb-api
Version:        2.3.3
Release:        alt1_3jpp11
Summary:        Jakarta XML Binding API
License:        BSD

URL:            https://github.com/eclipse-ee4j/jaxb-api
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

# package renamed from glassfish-jaxb-api in fedora 33
Provides:       glassfish-jaxb-api = %{version}-%{release}
Obsoletes:      glassfish-jaxb-api < 2.3.3-2

# javadoc subpackage is currently not built
Obsoletes:      glassfish-jaxb-api-javadoc < 2.3.3-2
Source44: import.info

%description
The Jakarta XML Binding provides an API and tools that automate the mapping
between XML documents and Java objects.

%prep
%setup -q

# remove unnecessary dependency on parent POM
%pom_remove_parent

# disable unwanted test module
%pom_disable_module jaxb-api-test

# remove unnecessary maven plugins
%pom_remove_plugin -r :glassfish-copyright-maven-plugin
%pom_remove_plugin -r :buildnumber-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin

# mark dependency on jakarta.activation as optional
%pom_xpath_inject "pom:dependency[pom:groupId='jakarta.activation']" "<optional>true</optional>" jaxb-api

# add compatibility aliases for old artifact coordinates
%mvn_alias jakarta.xml.bind:jakarta.xml.bind-api javax.xml.bind:jaxb-api
%mvn_file :jakarta.xml.bind-api glassfish-jaxb-api/jakarta.xml.bind-api jaxb-api


%build
# skip javadoc build due to https://github.com/fedora-java/xmvn/issues/58
%mvn_build -j -- -Dmaven.compiler.source=9 -Dmaven.compiler.target=9 -Dmaven.javadoc.source=9 -Dmaven.compiler.release=9 -DbuildNumber=unknown -DscmBranch=%{version}


%install
%mvn_install


%files -f .mfiles
%doc --no-dereference LICENSE.md NOTICE.md


%changelog
* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 2.3.3-alt1_3jpp11
- new version

