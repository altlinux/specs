%define _unpackaged_files_terminate_build 1
%def_with check
%define srcname JCTools

Name: jctools
Version: 4.0.7
Release: alt1

Summary: Java concurrency queues and collection tools
License: Apache-2.0
Group: Development/Java
URL: https://github.com/JCTools/JCTools
VCS: https://github.com/JCTools/JCTools.git
BuildArch: noarch

Source: %srcname-%version.tar
Patch: system-jvm.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-plugin-bundle
BuildRequires: exec-maven-plugin
BuildRequires: mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires: javaparser
BuildRequires: osgi-annotation
BuildRequires: guava-testlib
BuildRequires: junit
BuildRequires: hamcrest
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-util)

%description
JCTools supplies concurrent queues, maps, sets and channels for Java.
This package includes core, JDK 11 VarHandle, channels and experimental APIs.

%package javadoc
Summary: API documentation for JCTools
Group: Development/Java

%description javadoc
Generated API documentation for JCTools.

%package testlib
Summary: Shared JCTools test fixtures used by its experimental API
Group: Development/Java

%description testlib
Genuine classified test-support artifacts from the JCTools reactor.

%prep
%setup -q -n %srcname-%version
%autopatch -p1

# The stable upstream tag retains snapshot Maven versions.
%pom_xpath_set pom:project/pom:version %version
%pom_xpath_set pom:parent/pom:version %version jctools-*
%pom_xpath_set pom:properties/pom:junit.version 4.13.1
%pom_xpath_set pom:properties/pom:hamcrest.version 3.0
%pom_xpath_set pom:properties/pom:guava-testlib.version 33.7.2-jre
%pom_change_dep -r org.hamcrest:hamcrest-all org.hamcrest:hamcrest

# JUnit's legacy aggregate is replaced by the explicit genuine Hamcrest API.
%pom_xpath_inject "//pom:dependency[pom:artifactId='junit']" '
<exclusions>
  <exclusion>
    <groupId>org.hamcrest</groupId><artifactId>hamcrest-core</artifactId>
  </exclusion>
</exclusions>' jctools-core jctools-core-jdk11 jctools-channels \
    jctools-experimental

# Use genuine ASM modules instead of the retired aggregate.
%pom_change_dep -r org.ow2.asm:asm-all org.ow2.asm:asm
%pom_add_dep org.ow2.asm:asm-util jctools-channels

# JDK 11 uses this classifier only in tests; experimental exports its types.
%pom_xpath_set "//pom:dependency[pom:type='test-jar']/pom:scope" test \
    jctools-core-jdk11

%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :coveralls-maven-plugin
%pom_remove_plugin -r :jacoco-maven-plugin

# Lincheck is absent; keep both original test files and assertions.
# Upstream excludes their execution on JDK 17 and newer.
%pom_remove_dep -r org.jetbrains.kotlinx:lincheck-jvm
%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin . '
<configuration>
  <testExcludes>
    <testExclude>**/maps/linearizability_test/**</testExclude>
  </testExcludes>
</configuration>'

# Benchmark/JCStress runners are not production libraries.
%pom_disable_module jctools-benchmarks
%pom_disable_module jctools-concurrency-test

# Execute the genuine source generators in this reactor.
%mvn_package :jctools-build __noinstall
%mvn_package :jctools-core:jar:tests: testlib
%mvn_package :jctools-core-jdk11:jar:tests: testlib

%build
# Install these freshly built reactor artifacts to Maven Local for Javadoc.
%mvn_build -j \
    -G org.apache.maven.plugins:maven-install-plugin:install -- -DskipTests

# Per-module Javadoc retains real classified core fixtures in the classpath.
mkdir -p target/api
for module in jctools-core jctools-core-jdk11 jctools-channels \
              jctools-experimental; do
    xmvn --batch-mode --offline \
        -f "$module/pom.xml" org.fedoraproject.xmvn:xmvn-mojo:javadoc
    cp -pr "$module/target/xmvn-apidocs" "target/api/$module"
done
cat >target/api/index.html <<'EOF'
<!doctype html>
<meta charset="utf-8">
<title>JCTools API</title>
<h1>JCTools API</h1>
<ul>
<li><a href="jctools-core/index.html">Core</a></li>
<li><a href="jctools-core-jdk11/index.html">JDK 11 VarHandle</a></li>
<li><a href="jctools-channels/index.html">Channels</a></li>
<li><a href="jctools-experimental/index.html">Experimental</a></li>
</ul>
EOF

%install
%mvn_install -J target/api

%check
%if_with check
xmvn --batch-mode --offline test
%endif

%files -f .mfiles
%doc LICENSE

%files testlib -f .mfiles-testlib

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 4.0.7-alt1
- New version.

* Tue Dec 23 2025 Anton Meleshnikov <alton@altlinux.org> 4.0.5-alt1
- new version

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 3.3.0-alt2_5jpp11
- update

* Tue Jul 12 2022 Igor Vlasenko <viy@altlinux.org> 3.3.0-alt2_1jpp11
- build with compat javaparser3

* Mon Jun 13 2022 Igor Vlasenko <viy@altlinux.org> 3.3.0-alt1_1jpp11
- java11 build

* Mon Aug 16 2021 Igor Vlasenko <viy@altlinux.org> 3.3.0-alt1_1jpp8
- new version

* Sat Jun 12 2021 Igor Vlasenko <viy@altlinux.org> 3.2.0-alt1_1jpp8
- fc update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 3.1.0-alt1_1jpp8
- new version

* Sun Oct 11 2020 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt1_6jpp8
- new version

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt1_1jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt1_3jpp8
- java update

* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt1_2jpp8
- new version

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_0.3.alphajpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_0.2.alphajpp8
- new version

