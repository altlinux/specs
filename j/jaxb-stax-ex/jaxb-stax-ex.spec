Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jaxb-stax-ex
Version:        1.8.3
Release:        alt1_8jpp11
Summary:        Extended StAX API
License:        BSD

URL:            https://github.com/eclipse-ee4j/jaxb-stax-ex
Source0:        https://github.com/eclipse-ee4j/jaxb-stax-ex/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
Source44: import.info

%description
This project contains a few extensions to complement JSR-173 StAX API in
the following areas:

- Enable parser instance reuse (which is important in the
  high-performance environment like Eclipse Implementation of JAXB and
  Eclipse Metro)
- Improve the support for reading from non-text XML infoset, such as
  FastInfoset.
- Improve the namespace support.

%{?javadoc_package}

%prep
%setup -q


# remove unnecessary dependency on parent POM
%pom_remove_parent

# remove unnecessary maven plugins
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%doc --no-dereference LICENSE.md NOTICE.md
%doc README.md


%changelog
* Sat Jul 09 2022 Igor Vlasenko <viy@altlinux.org> 1.8.3-alt1_8jpp11
- update

* Sun Aug 15 2021 Igor Vlasenko <viy@altlinux.org> 1.8.3-alt1_4jpp11
- update

* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 1.8.3-alt1_2jpp11
- new version

