Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jakarta-json
Version:        1.1.6
Release:        alt1_7jpp11
Summary:        Jakarta JSON Processing

License:        EPL-2.0 or GPLv2 with exceptions
URL:            https://eclipse-ee4j.github.io/jsonp/
Source0:        https://github.com/eclipse-ee4j/jsonp/archive/1.1-%{version}-RELEASE.tar.gz
# Update deprecated method calls
Patch0:         %{name}-deprecated.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)

BuildArch:      noarch

# These can be removed when Fedora 36 reaches EOL
Obsoletes:      jsonp < 1.0.4-12
Provides:       jsonp = %{version}-%{release}
Obsoletes:      jsonp-javadoc < 1.0.4-12

# These can be removed when Fedora 38 reaches EOL
Obsoletes:      jakarta-json-jaxrs < 1.1.6-5
Obsoletes:      jakarta-json-jaxrs-1x < 1.1.6-5

%global _desc \
Jakarta JSON Processing provides portable APIs to parse, generate,\
transform, and query JSON documents.
Source44: import.info

%description 
%_desc

This package contains an implementation of Jakarta JSON Processing.

# Uncomment this once javadocs can be generated again
# See https://github.com/fedora-java/xmvn/issues/58
#%%{?javadoc_package}

%package        api
Group: Development/Java
Summary:        Jakarta JSON Processing API

%description    api 
%_desc

This package contains the Jakarta JSON Processing API.

%package        impl
Group: Development/Java
Summary:        Jakarta JSON Processing default provider
Requires:       %{name}-api = %{version}-%{release}

%description    impl 
%_desc

This package contains the default provider for Jakarta JSON Processing.

%prep
%setup -q -n jsonp-1.1-%{version}-RELEASE
%patch0 -p1


# org.eclipse.ee4j:project is not available in Fedora
%pom_remove_parent

# Disable unwanted modules in the default profile
# - bundles: make distribution bundles
# - demos: build demos
# - gf: create WARs
# - jaxrs: depends on jaxb, which has been retired
# - jaxrs-1x: depends on jaxb, which has been retired
%pom_xpath_remove "//pom:profile[//pom:id='all']/pom:modules/pom:module[text()='bundles' or text()='demos' or text()='gf' or text()='jaxrs' or text()='jaxrs-1x']"

# Unnecessary plugins for an RPM build
%pom_remove_plugin -r org.apache.maven.plugins:maven-release-plugin
%pom_remove_plugin -r org.glassfish.copyright:glassfish-copyright-maven-plugin
%pom_remove_plugin org.codehaus.mojo:wagon-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin api
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin impl

# Due to jaxb retirement, remove support for jsr311-api (javax.ws.rs-api)
%pom_remove_dep javax.ws.rs:jsr311-api

# Do not copy the API classes into the implementation JAR
%pom_xpath_remove "//pom:plugin[pom:artifactId ='maven-bundle-plugin']//pom:Export-Package" impl

# Do not install the tests
%mvn_package org.glassfish:jsonp-tests __noinstall

# Provide aliases for old names
%mvn_alias jakarta.json:jakarta.json-api javax.json:javax.json-api
%mvn_alias org.glassfish:jakarta.json org.glassfish:javax.json

%build
# Skip javadoc build due to https://github.com/fedora-java/xmvn/issues/58
%mvn_build -s -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles-json
%doc --no-dereference LICENSE.md NOTICE.md

%files api -f .mfiles-jakarta.json-api
%doc README.md
%doc --no-dereference LICENSE.md NOTICE.md

%files impl -f .mfiles-jakarta.json

%changelog
* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1.1.6-alt1_7jpp11
- update

* Thu May 26 2022 Igor Vlasenko <viy@altlinux.org> 1.1.6-alt1_3jpp11
- update

* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 1.1.6-alt1_2jpp11
- new version

