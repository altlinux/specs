Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global srcname jax-rpc-api

Name:           jakarta-xml-rpc
# the obsoleted geronimo-jaxrpc had a higher version
Epoch:          1
Version:        1.1.4
Release:        alt1_2jpp11
Summary:        Jakarta XML RPC API
License:        EPL-2.0 or GPLv2 with exceptions

URL:            https://github.com/eclipse-ee4j/jax-rpc-api
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.servlet:jakarta.servlet-api)
BuildRequires:  mvn(jakarta.xml.soap:jakarta.xml.soap-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)

# package renamed in fedora 33, remove in fedora 35
Provides:       geronimo-jaxrpc = %{epoch}:%{version}-%{release}
Obsoletes:      geronimo-jaxrpc < 2.1-28
Source44: import.info

%description
Jakarta XML RPC API provides standardized Java APIs for using XML-RPC.


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}

# package renamed in fedora 33, remove in fedora 35
Provides:       geronimo-jaxrpc-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      geronimo-jaxrpc-javadoc < 2.1-28
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{srcname}-%{version}


# drop useless dependency on parent POM
%pom_remove_parent

# do not build specification documentation
%pom_disable_module spec

# drop useless maven plugins
%pom_remove_plugin :maven-javadoc-plugin api
%pom_remove_plugin :maven-source-plugin api

# add dependency for javax.xml.soap package (no longer part of OpenJDK)
%pom_add_dep jakarta.xml.soap:jakarta.xml.soap-api api

# replace deprecated option that was removed with maven-jar-plugin 3.x
%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-jar-plugin"]/pom:configuration/pom:useDefaultManifestFile' api
%pom_xpath_inject 'pom:plugin[pom:artifactId="maven-jar-plugin"]/pom:configuration' '<archive>
  <manifestFile>${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
</archive>' api

# disable spec verification (fails because spec-version-maven-plugin is too old)
%pom_xpath_remove 'pom:goal[text()="check-module"]' api

# do not install useless parent POM
%mvn_package jakarta.xml.rpc:rpc-api-parent __noinstall

# add compatibility alias for old maven artifact coordinates
%mvn_alias jakarta.xml.rpc:jakarta.xml.rpc-api javax.xml:jaxrpc-api

# add compatibility symlinks for old classpath
%mvn_file : %{name}/jakarta.xml.rpc-api geronimo-jaxrpc jaxrpc


%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8


%install
%mvn_install


%files -f .mfiles
%doc --no-dereference LICENSE.md NOTICE.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.md NOTICE.md


%changelog
* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 1:1.1.4-alt1_2jpp11
- new version

