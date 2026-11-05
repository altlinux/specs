%define _unpackaged_files_terminate_build 1

Name: test-parameter-injector
Version: 1.25
Release: alt1

Summary: Parameterized test runner for JUnit
License: Apache-2.0
Group: Development/Java
URL: https://github.com/google/TestParameterInjector
VCS: https://github.com/google/TestParameterInjector.git

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: rpm-build-java
BuildRequires: java-21-openjdk-devel
BuildRequires: kotlin-maven
BuildRequires: kotlin-reflect
BuildRequires: kotlin-stdlib
BuildRequires: kotlin-compiler
BuildRequires: kotlin-gradle-plugin
BuildRequires: maven-plugin-annotations
BuildRequires: gradle
BuildRequires: auto-value
BuildRequires: auto-value-annotations
BuildRequires: guava
BuildRequires: jsr-305
BuildRequires: snakeyaml
BuildRequires: geronimo-annotation
BuildRequires: jetbrains-annotations
BuildRequires: junit
BuildRequires: junit5
BuildRequires: truth
BuildRequires: protobuf-javalite
BuildRequires: protobuf-java
BuildRequires: maven-source-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-surefire-plugin

%description
TestParameterInjector is a parameterized test runner supporting annotation
values, YAML parameters, custom providers and Kotlin default parameters.
This package contains its JUnit 4 integration.

%package parent
Summary: Parent POM for TestParameterInjector
Group: Development/Java

%description parent
Shared Maven configuration for the JUnit integrations.

%package junit5
Summary: TestParameterInjector integration for JUnit 5
Group: Development/Java

%description junit5
Parameterized JUnit Jupiter test runner with annotation values, YAML
parameters, custom providers and Kotlin default parameters.

%prep
%setup
%pom_add_dep org.apache.geronimo.specs:geronimo-annotation_1.3_spec:1.0:provided
plugin_xpath='pom:project/pom:build/pom:plugins/pom:plugin'
plugin_xpath="$plugin_xpath[pom:artifactId=\"maven-compiler-plugin\"]"
%pom_xpath_inject "$plugin_xpath" \
    '<groupId>org.apache.maven.plugins</groupId>'
# Gradle ships the genuine coroutine runtime used by the system Kotlin plugin.
# Keep its real version in build-local XMvn metadata; no binary vendoring.
mkdir -p rpm-metadata
cat > rpm-metadata/gradle-coroutines.xml <<'EOF'
<metadata xmlns="http://fedorahosted.org/xmvn/METADATA/3.2.0">
  <artifacts>
    <artifact>
      <groupId>org.jetbrains.kotlinx</groupId>
      <artifactId>kotlinx-coroutines-core-jvm</artifactId>
      <version>1.10.2</version>
      <path>%_datadir/gradle/lib/kotlinx-coroutines-core-jvm-1.10.2.jar</path>
    </artifact>
  </artifacts>
</metadata>
EOF
test -r %_datadir/gradle/lib/kotlinx-coroutines-core-jvm-1.10.2.jar
tpi_repos="<repository>%_datadir/maven-metadata</repository>"
tpi_repos="$tpi_repos<repository>$PWD/rpm-metadata</repository>"
%mvn_config resolverSettings/metadataRepositories "$tpi_repos"

%build
%mvn_build -s -j

%install
%mvn_install
# Upstream Kotlin hooks target Java 17 even though Java sources target 8.
python3 - <<'PY'
from pathlib import Path
import xml.etree.ElementTree as ET
ns = {'m': 'http://fedorahosted.org/xmvn/METADATA/3.2.0'}
ET.register_namespace('', ns['m'])
metadata_dir = Path('%buildroot%_datadir/maven-metadata')
for path in metadata_dir.glob('test-parameter-injector-*.xml'):
    tree = ET.parse(path)
    for node in tree.findall('.//m:requiresJava', ns):
        node.text = '17'
    tree.write(path, encoding='UTF-8', xml_declaration=True)
PY

%files -f .mfiles-test-parameter-injector
%doc LICENSE CHANGELOG.md

%files parent -f .mfiles-test-parameter-injector-parent

%files junit5 -f .mfiles-test-parameter-injector-junit5

%changelog
* Tue Oct 27 2026 Ivan Khanas <xeno@altlinux.org> 1.25-alt1
- Initial build for ALT.
