Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global srcname saaj-api

Name:           jakarta-saaj
Version:        1.4.2
Release:        alt1_2jpp11
Summary:        SOAP with Attachments API for Java
License:        BSD

URL:            https://github.com/eclipse-ee4j/saaj-api
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)

# package renamed in fedora 33, remove in fedora 35
Provides:       geronimo-saaj = %{version}-%{release}
Obsoletes:      geronimo-saaj < 1.1-28

# javadoc subpackage is currently not built
Obsoletes:      geronimo-saaj-javadoc < 1.1-28
Source44: import.info

%description
Jakarta SOAP with Attachments defines an API enabling developers to
produce and consume messages conforming to the SOAP 1.1, SOAP 1.2, and
SOAP Attachments Feature.


%prep
%setup -q -n %{srcname}-%{version}


pushd api
# remove unnecessary dependency on parent POM
%pom_remove_parent

# remove unnecessary maven plugins
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :spotbugs-maven-plugin

# add compatibility alias for old maven artifact coordinates
%mvn_alias jakarta.xml.soap:jakarta.xml.soap-api javax.xml.soap:saaj-api

# add compatibility symlink for old classpath
%mvn_file : %{name}/jakarta.xml.soap-api geronimo-saaj
popd


%build
pushd api
# - skip tests because metro-saaj is not packaged for fedora yet:
#   https://github.com/eclipse-ee4j/metro-saaj
# - skip javadoc build due to https://github.com/fedora-java/xmvn/issues/58
%mvn_build -f -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -DbuildNumber=unknown
popd


%install
pushd api
%mvn_install
popd


%files -f api/.mfiles
%doc --no-dereference LICENSE.md NOTICE.md
%doc README.md


%changelog
* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1.4.2-alt1_2jpp11
- new version

