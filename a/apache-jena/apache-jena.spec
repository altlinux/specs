Name: apache-jena
Version: 5.6.0
Release: alt1

Group: Development/Java
Summary: Apache Jena RDF framework modules
License: Apache-2.0
URL: https://jena.apache.org/
BuildArch: noarch

Source0: %name-%version.tar.gz
Patch0: jena-provider-compat.patch
Patch1: jena-hasher-test-environment.patch
Patch2: jena-arq-offline-jsonld-tests.patch
Patch3: jena-arq-timeout-tests.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.enforcer:enforcer-rules)
BuildRequires: mvn(org.apache.maven.enforcer:enforcer-api)
BuildRequires: mvn(com.github.andrewoma.dexx:collection)
BuildRequires: mvn(org.apache.thrift:libthrift)
BuildRequires: mvn(org.roaringbitmap:RoaringBitmap)
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.apache.logging.log4j:log4j-bom:pom:)
BuildRequires: mvn(org.apache.logging.log4j:log4j-slf4j-impl)
BuildRequires: mvn(org.junit:junit-bom:pom:)
BuildRequires: mvn(org.junit.platform:junit-platform-suite-api)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher) = 1.14.4
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:jcl-over-slf4j)
BuildRequires: mvn(org.slf4j:jul-to-slf4j)
BuildRequires: mvn(org.apache.commons:commons-csv) = 1.14.1
BuildRequires: mvn(org.apache.commons:commons-collections4) = 4.6.0
BuildRequires: mvn(com.github.ben-manes.caffeine:caffeine) = 3.2.3
BuildRequires: mvn(org.jspecify:jspecify)
BuildRequires: mvn(org.awaitility:awaitility) = 4.3.0
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin) = 3.8.1
BuildRequires: mvn(com.apicatalog:titanium-json-ld) = 1.7.0
BuildRequires: mvn(org.glassfish:jakarta.json) = 2.0.1
BuildRequires: mvn(com.google.protobuf:protobuf-java) = 4.31.1

%description
Apache Jena is a Java framework for RDF and SPARQL. This package provides
the Maven parent POM used by the separately packaged Jena modules.

%package iri
Summary: Apache Jena IRI module
Group: Development/Java

%description iri
Apache Jena's IRI module.

%package iri3986
Summary: Apache Jena IRI 3986 module
Group: Development/Java

%description iri3986
Apache Jena's IRI 3986 module.

%package langtag
Summary: Apache Jena language tag module
Group: Development/Java

%description langtag
Apache Jena's language tag module.

%package base
Summary: Apache Jena base module
Group: Development/Java

%description base
Apache Jena's base module.

%package core
Summary: Apache Jena core module
Group: Development/Java

%description core
Apache Jena's RDF core module.

%package arq
Summary: Apache Jena ARQ module
Group: Development/Java

%description arq
Apache Jena's ARQ query module.

%prep
%setup -q
%autopatch -p1
# Run tests directly when the system JUnit only provides the suite API.
surefire='pom:plugin[pom:artifactId="maven-surefire-plugin"]/pom:configuration'
%pom_xpath_inject "$surefire/pom:includes" '<include>**/Test*.java</include>' \
    jena-base jena-arq
%pom_xpath_inject "$surefire/pom:includes" \
    '<include>**/TestIRI3986.java</include>' jena-iri3986
# Only the scripting tests require the unavailable GraalJS runtime.
%pom_xpath_inject "$surefire" \
    '<excludes><exclude>**/TestScriptFunction.java</exclude></excludes>' jena-arq
%pom_add_dep org.junit.platform:junit-platform-launcher:1.14.4:test jena-arq
# The properties goal is supported by the official dependency plugin 3.8.1.
%pom_xpath_inject 'pom:plugin[pom:artifactId="maven-dependency-plugin"]' '<version>3.8.1</version>'
%pom_remove_plugin org.cyclonedx:cyclonedx-maven-plugin
%pom_xpath_set 'pom:properties/pom:ver.caffeine' 3.2.3
%pom_xpath_set 'pom:properties/pom:ver.protobuf' 4.31.1
%pom_xpath_set 'pom:properties/pom:ver.commons-collections' 4.6.0
jspecify_dep='<dependency>
  <groupId>org.jspecify</groupId>
  <artifactId>jspecify</artifactId>
  <version>1.0.0</version>
</dependency>'
%pom_xpath_inject 'pom:project/pom:dependencyManagement/pom:dependencies' \
    "$jspecify_dep"
%pom_remove_dep org.graalvm.js:js-scriptengine jena-arq
%pom_remove_dep org.graalvm.js:js-community jena-arq
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin jena-iri
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin jena-langtag
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin jena-base
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin jena-core
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin jena-arq
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin jena-iri
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin jena-iri3986
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin jena-langtag
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin jena-base
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin jena-core
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin jena-arq

%build
%mvn_package org.apache.jena:jena %name
%mvn_package org.apache.jena:jena-iri %name-iri
%mvn_package org.apache.jena:jena-iri3986 %name-iri3986
%mvn_package org.apache.jena:jena-langtag %name-langtag
%mvn_package org.apache.jena:jena-base %name-base
%mvn_package org.apache.jena:jena-core %name-core
%mvn_package org.apache.jena:jena-arq %name-arq
%mvn_build -s -j -- -pl jena-base,jena-core,jena-arq -am

%install
%mvn_install

%files -f .mfiles-%name
%doc LICENSE NOTICE

%files iri -f .mfiles-%name-iri
%files iri3986 -f .mfiles-%name-iri3986
%files langtag -f .mfiles-%name-langtag
%files base -f .mfiles-%name-base
%files core -f .mfiles-%name-core
%files arq -f .mfiles-%name-arq

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 5.6.0-alt1
- Package Apache Jena 5.6.0 for the SPDX RDF store.
- Split the Maven modules into separate packages.
- Use system dependencies and run offline tests.
