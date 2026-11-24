Name: spdx-tools-java
Version: 2.0.7
Release: alt1

Summary: Java tools for reading, validating and converting SPDX documents
License: Apache-2.0
Group: Development/Java
URL: https://github.com/spdx/tools-java
VCS: https://github.com/spdx/tools-java
Source0: %name-%version.tar
Patch1: tools-java-alt-use-jsonschemafriend.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
# Spreadsheet comparison tests initialize AWT font metrics.
BuildRequires: fonts-ttf-dejavu
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(org.apache.commons:commons-compress)
BuildRequires: mvn(org.apache.ws.xmlschema:xmlschema-core)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.spdx:java-spdx-library)
BuildRequires: mvn(org.spdx:spdx-jackson-store)
BuildRequires: mvn(org.spdx:spdx-rdf-store)
BuildRequires: mvn(org.spdx:spdx-spreadsheet-store)
BuildRequires: mvn(org.spdx:spdx-tagvalue-store)
BuildRequires: mvn(org.spdx:spdx-v3jsonld-store)
BuildRequires: mvn(org.metaeffekt.bundle.jsonschemafriend:ae-jsonschemafriend-core)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)

Requires: java-headless >= 21

%description
SPDX Java utilities provide commands for verifying, comparing and converting
SPDX documents and for generating XSD from SPDX RDF schemas.

%prep
%setup -q
%autopatch -p1
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
%pom_remove_plugin org.owasp:dependency-check-maven
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-shade-plugin
%pom_remove_plugin org.spdx:spdx-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-release-plugin
%pom_remove_plugin org.sonarsource.scanner.maven:sonar-maven-plugin
%pom_change_dep org.spdx:java-spdx-library org.spdx:java-spdx-library:2.0.5
%pom_change_dep org.spdx:spdx-jackson-store org.spdx:spdx-jackson-store:2.0.7
%pom_change_dep \
    org.spdx:spdx-tagvalue-store org.spdx:spdx-tagvalue-store:2.0.5
%pom_change_dep \
    org.spdx:spdx-v3jsonld-store org.spdx:spdx-v3jsonld-store:1.0.6
%pom_change_dep \
    com.networknt:json-schema-validator \
    org.metaeffekt.bundle.jsonschemafriend:ae-jsonschemafriend-core:0.12.5.1
%pom_remove_dep org.slf4j:slf4j-simple
%pom_change_dep \
    org.apache.ws.xmlschema:xmlschema-core \
    org.apache.ws.xmlschema:xmlschema-core:2.3.3
plugins='pom:project/pom:build/pom:plugins/pom:plugin'
%pom_xpath_set \
    "$plugins[pom:artifactId='maven-compiler-plugin']/pom:version" 3.14.0
%pom_xpath_set \
    "$plugins[pom:artifactId='maven-enforcer-plugin']/pom:version" 3.6.2

# This one test downloads the live SPDX schema; Hasher has no network.
# Keep it in testCompile and run all independent offline upstream tests.
%pom_add_plugin org.apache.maven.plugins:maven-surefire-plugin . '<configuration><excludes><exclude>**/LatestSchemaVersionTest.java</exclude></excludes></configuration>'

%build
%mvn_package :tools-java %name
%mvn_file :tools-java spdx/tools-java
%mvn_build -s -j
xmvn -q org.apache.maven.plugins:maven-dependency-plugin:build-classpath \
    -DincludeScope=runtime -Dmdep.outputFile=runtime.classpath

%install
%mvn_install
install -d %buildroot%_bindir
runtime_classpath=$(cat runtime.classpath)
test -n "$runtime_classpath"
printf '%%s\n' "$runtime_classpath" | tr : '\n' > runtime.jars
while IFS= read -r jar; do
    case "$jar" in
        %_javadir/*.jar) test -f "$jar" ;;
        *) printf 'Unexpected Maven runtime path: %%s\n' "$jar" >&2; exit 1 ;;
    esac
done < runtime.jars
cat > %buildroot%_bindir/tools-java <<EOF
#!/bin/sh
exec java -cp "%_javadir/spdx/tools-java.jar:$runtime_classpath" \
    org.spdx.tools.Main "\$@"
EOF
chmod 0755 %buildroot%_bindir/tools-java

%files -f .mfiles-%name
%_bindir/tools-java
%doc LICENSE README.md

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 2.0.7-alt1
- Initial build for ALT.
