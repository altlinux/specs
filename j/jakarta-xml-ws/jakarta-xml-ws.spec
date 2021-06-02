Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global srcname jax-ws-spec

Name:           jakarta-xml-ws
Version:        2.3.1
Release:        alt1_1jpp11
Summary:        Jakarta XML Web Services API
License:        CDDL-1.1 or GPLv2 with exceptions

# development moved to https://github.com/eclipse-ee4j/jax-ws-api
URL:            https://github.com/javaee/jax-ws-spec
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(javax.annotation:javax.annotation-api)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(javax.xml.soap:saaj-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)

# package renamed in fedora 33, remove in fedora 35
Provides:       glassfish-jaxws = %{version}-%{release}
Obsoletes:      glassfish-jaxws < 2.2.10-13
Source44: import.info

%description
Jakarta XML Web Services defines a means for implementing XML-Based Web
Services based on Jakarta SOAP with Attachments and Jakarta Web Services
Metadata.


%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}

# package renamed in fedora 33, remove in fedora 35
Provides:       glassfish-jaxws-javadoc = %{version}-%{release}
Obsoletes:      glassfish-jaxws-javadoc < 2.2.10-13
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{srcname}-%{version}

pushd api
# remove unnecessary dependency on parent POM
%pom_remove_parent

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

%pom_change_dep javax.xml.soap:javax.xml.soap-api javax.xml.soap:saaj-api

# replace deprecated option that was removed with maven-jar-plugin 3.x
%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-jar-plugin"]/pom:configuration/pom:useDefaultManifestFile'
%pom_xpath_inject 'pom:plugin[pom:artifactId="maven-jar-plugin"]/pom:configuration' '<archive>
  <manifestFile>${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
</archive>'
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
%doc --no-dereference LICENSE.md api/LICENSE.txt api/copyright.txt

%files javadoc -f api/.mfiles-javadoc
%doc --no-dereference LICENSE.md api/LICENSE.txt api/copyright.txt


%changelog
* Wed Jun 02 2021 Igor Vlasenko <viy@altlinux.org> 2.3.1-alt1_1jpp11
- new version

