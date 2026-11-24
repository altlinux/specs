%define _unpackaged_files_terminate_build 1

Name: jsonschemafriend-core
Version: 0.12.5
Release: alt1

Summary: JSON Schema loading and validation library
License: Apache-2.0
Group: Development/Java
URL: https://github.com/org-metaeffekt/jsonschemafriend
VCS: https://github.com/org-metaeffekt/jsonschemafriend.git
Source0: %name-%version.tar
Source1: jsonschemafriend-schemastore-85e5b6b.tar.xz
Source2: jsonschemafriend-json-schema-test-suite-95fe6ca.tar.xz
Patch0: jsonschemafriend-offline-schemastore-tests.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(com.damnhandy:handy-uri-templates)
BuildRequires: mvn(com.ibm.icu:icu4j)
BuildRequires: mvn(commons-validator:commons-validator)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(org.jruby.joni:joni)
BuildRequires: mvn(org.jsoup:jsoup)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires: mvn(org.json:json)
BuildRequires: mvn(org.hamcrest:hamcrest-core)
BuildRequires: mvn(com.fasterxml.jackson.dataformat:jackson-dataformat-yaml)

%description
JSON Schema Friend is a Java library for loading and validating JSON schemas.

%prep
%setup -q -a 1 -a 2
%patch0 -p1
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%pom_change_dep \
    commons-validator:commons-validator:1.9.0 \
    commons-validator:commons-validator:1.11.0 \
    library/pom.xml
%pom_change_dep com.ibm.icu:icu4j:75.1 com.ibm.icu:icu4j:79.1 library/pom.xml
%pom_change_dep \
    com.fasterxml.jackson.core:jackson-databind:2.18.0 \
    com.fasterxml.jackson.core:jackson-databind:2.22.1 \
    library/pom.xml
%pom_change_dep \
    org.jruby.joni:joni:2.2.1 \
    org.jruby.joni:joni:2.1.43 \
    library/pom.xml
%pom_change_dep org.jsoup:jsoup:1.18.1 org.jsoup:jsoup:1.22.2 library/pom.xml
%pom_change_dep \
    org.junit.jupiter:junit-jupiter-engine:5.11.1 \
    org.junit.jupiter:junit-jupiter-engine:5.14.4 \
    library/pom.xml
%pom_change_dep \
    org.junit.jupiter:junit-jupiter-api:5.11.1 \
    org.junit.jupiter:junit-jupiter-api:5.14.4 \
    library/pom.xml
%pom_change_dep \
    org.junit.jupiter:junit-jupiter-params:5.11.0 \
    org.junit.jupiter:junit-jupiter-params:5.14.4 \
    library/pom.xml
%pom_change_dep org.json:json:20240303 org.json:json:20260814 library/pom.xml
%pom_change_dep \
    com.fasterxml.jackson.dataformat:jackson-dataformat-yaml:2.18.0 \
    com.fasterxml.jackson.dataformat:jackson-dataformat-yaml:2.22.4 \
    library/pom.xml

%build
# The two excluded methods fetch schemas over the network.
%mvn_build -s -j -- -Drun.smoke.test=true \
    '-Dtest=*,!ApiTest#fromWeb,!MetaSchemaTest#testMetaSchema'

%install
%mvn_install

%files -f .mfiles-ae-jsonschemafriend-core
%_mavenpomdir/%name/ae-jsonschemafriend-bundle.pom
/usr/share/maven-metadata/%name-ae-jsonschemafriend-bundle.xml
%doc LICENSE NOTICE README.md

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 0.12.5-alt1
- Initial build for ALT.
