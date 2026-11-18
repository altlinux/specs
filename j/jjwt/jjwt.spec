%define _unpackaged_files_terminate_build 1

Name: jjwt
Version: 0.13.0
Release: alt1

Summary: Java JSON Web Token API, implementation and JSON adapters
License: Apache-2.0
Group: Development/Java
URL: https://github.com/jwtk/jjwt
VCS: https://github.com/jwtk/jjwt.git

Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: json
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(org.apache.groovy:groovy)
BuildRequires: mvn(org.easymock:easymock)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.bouncycastle:bcprov-jdk18on)
BuildRequires: mvn(org.bouncycastle:bcpkix-jdk18on)
BuildRequires: mvn(org.codehaus.gmavenplus:gmavenplus-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-failsafe-plugin)

%description
JSON Web Token library with a complete API and implementation for signed and
encrypted tokens, keys and JSON Web Keys. Includes Jackson, Gson and org.json
adapters, genuine deprecated compatibility classifiers and the upstream BOM.

%package javadoc
Summary: API documentation for %name
Group: Development/Java

%description javadoc
API documentation for JJWT and its JSON adapters.

%package api
Summary: JSON Web Token API
Group: Development/Java

%description api
JSON Web Token API.

%package impl
Summary: JSON Web Token implementation
Group: Development/Java

%description impl
JSON Web Token implementation.

%package extensions
Summary: Parent POM for JJWT JSON adapters
Group: Development/Java

%description extensions
Parent POM for JJWT JSON adapters.

%package jackson
Summary: Jackson JSON adapter for JJWT
Group: Development/Java

%description jackson
Jackson JSON adapter for JJWT.

%package orgjson
Summary: org.json JSON adapter for JJWT
Group: Development/Java

%description orgjson
org.json JSON adapter for JJWT.

%package gson
Summary: Gson JSON adapter for JJWT
Group: Development/Java

%description gson
Gson JSON adapter for JJWT.

%package bom
Summary: Bill of materials for JJWT
Group: Development/Java

%description bom
Bill of materials for JJWT.

%package legacy
Summary: Legacy transition POM for JJWT
Group: Development/Java

%description legacy
Legacy transition POM for JJWT.

%prep
%setup
# Release publication and optional external coverage services.
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-release-plugin
%pom_remove_plugin io.jsonwebtoken.coveralls:coveralls-maven-plugin
%pom_remove_plugin org.openclover:clover-maven-plugin
# The historical0.11.2 comparison artifacts are unavailable offline.
%pom_remove_plugin com.github.siom79.japicmp:japicmp-maven-plugin api
%pom_remove_plugin com.github.siom79.japicmp:japicmp-maven-plugin extensions/jackson
%pom_remove_plugin com.github.siom79.japicmp:japicmp-maven-plugin extensions/orgjson
%pom_remove_plugin com.github.siom79.japicmp:japicmp-maven-plugin extensions/gson
# Use the real current Groovy coordinates for independent upstream tests.
%pom_change_dep org.codehaus.groovy:groovy org.apache.groovy:groovy
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId='gmavenplus-plugin']" \
    '<configuration><targetBytecode>17</targetBytecode></configuration>'
# Only these two suites require the unavailable PowerMock provider.
%pom_remove_dep org.powermock:powermock-module-junit4
%pom_remove_dep org.powermock:powermock-api-easymock
%pom_remove_dep org.powermock:powermock-core
rm impl/src/test/groovy/io/jsonwebtoken/impl/security/ProvidersWithoutBCTest.groovy
rm extensions/orgjson/src/test/groovy/io/jsonwebtoken/orgjson/io/AndroidOrgJsonSerializerTest.groovy
# Keep both genuine upstream compatibility classifiers.
%mvn_package io.jsonwebtoken:jjwt-jackson:jar:deprecated: jjwt-jackson
%mvn_package io.jsonwebtoken:jjwt-orgjson:jar:deprecated: jjwt-orgjson
# The upstream transition artifact has no product classes; retain its POM.
%mvn_package io.jsonwebtoken:jjwt:jar: __noinstall
%mvn_package io.jsonwebtoken:jjwt:pom: legacy

%build
%mvn_build -s -- -Dgroovy.version=6.0.0 -Dgmavenplus.version=5.1.0

%install
%mvn_install

%files -f .mfiles-jjwt-root
%doc LICENSE NOTICE.md

%files javadoc -f .mfiles-javadoc

%files api -f .mfiles-jjwt-api
%files impl -f .mfiles-jjwt-impl
%files extensions -f .mfiles-jjwt-extensions
%files jackson -f .mfiles-jjwt-jackson
%files orgjson -f .mfiles-jjwt-orgjson
%files gson -f .mfiles-jjwt-gson
%files bom -f .mfiles-jjwt-bom
%files legacy -f .mfiles-legacy

%changelog
* Mon Nov 16 2026 Ivan Khanas <xeno@altlinux.org> 0.13.0-alt1
- Initial build for ALT.
