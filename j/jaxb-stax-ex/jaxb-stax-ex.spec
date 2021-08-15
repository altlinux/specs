Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jaxb-stax-ex
Version:        1.8.3
Release:        alt1_4jpp11
Summary:        Extended StAX API
License:        BSD

URL:            https://github.com/eclipse-ee4j/jaxb-stax-ex
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

# package renamed in fedora 33, remove in fedora 35
Provides:       stax-ex = %{version}-%{release}
Obsoletes:      stax-ex < 1.7.7-16

# javadoc subpackage is currently not built
Obsoletes:      stax-ex-javadoc < 1.7.7-16
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


%prep
%setup -q

# remove unnecessary dependency on parent POM
%pom_remove_parent

# remove unnecessary maven plugins
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin


%build
# skip javadoc build due to https://github.com/fedora-java/xmvn/issues/58
%mvn_build -f -j -- -DbuildNumber=unknown


%install
%mvn_install


%files -f .mfiles
%doc --no-dereference LICENSE.md NOTICE.md
%doc README.md


%changelog
* Sun Aug 15 2021 Igor Vlasenko <viy@altlinux.org> 1.8.3-alt1_4jpp11
- update

* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 1.8.3-alt1_2jpp11
- new version

