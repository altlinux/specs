%define _unpackaged_files_terminate_build 1

Name: truth
Version: 1.4.5
Release: alt1

Summary: Assertion framework for Java unit tests
License: Apache-2.0
Group: Development/Java
Url: https://github.com/google/truth
VCS: https://github.com/google/truth.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-jvm-markers.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(com.google.auto.value:auto-value)
BuildRequires: mvn(com.google.auto.value:auto-value-annotations)
BuildRequires: mvn(com.google.errorprone:error_prone_annotations)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.google.guava:guava-testlib)
BuildRequires: mvn(com.google.protobuf:protobuf-java)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-annotation_1.3_spec)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.jspecify:jspecify)
BuildRequires: mvn(org.ow2.asm:asm)

%description
Truth provides fluent assertions for Java unit tests, including extensions
for Java 8 and full or lite Protocol Buffers.

%prep
%setup
%autopatch -p1
# RE2/J is unavailable in Sisyphus; keep the other extensions enabled.
%pom_disable_module re2j extensions
%pom_xpath_remove pom:project/pom:profiles
%pom_remove_plugin -r :gwt-maven-plugin
%pom_remove_plugin -r :animal-sniffer-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-gpg-plugin
%pom_remove_plugin -r :maven-site-plugin
%pom_remove_plugin -r :maven-project-info-reports-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :protobuf-maven-plugin
%pom_remove_dep :gwt-user core
%pom_remove_dep :gwt-dev core
%pom_remove_dep :guava-gwt core
%pom_xpath_inject 'pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration/pom:testExcludes' '<testExclude>**/gwt/*.java</testExclude>' core
%pom_xpath_remove pom:project/pom:build/pom:extensions extensions/liteproto extensions/proto
%pom_change_dep :protobuf-lite :protobuf-java extensions/liteproto
%pom_add_dep org.apache.geronimo.specs:geronimo-annotation_1.3_spec:1.0:provided
%pom_xpath_inject 'pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-compiler-plugin"]' '<groupId>org.apache.maven.plugins</groupId>' core extensions/liteproto extensions/proto

# The available native protoc conflicts with Sisyphus protobuf-java.
# Keep both libraries; skip only their generated protobuf test fixtures.
%pom_xpath_inject pom:project '<properties><maven.test.skip>true</maven.test.skip></properties>' extensions/liteproto
%pom_xpath_inject pom:project '<properties><maven.test.skip>true</maven.test.skip></properties>' extensions/proto

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE README.md

%changelog
* Sat Oct 31 2026 Ivan Khanas <xeno@altlinux.org> 1.4.5-alt1
- New version.

* Sat Jul 16 2022 Igor Vlasenko <viy@altlinux.org> 1.0.1-alt1_4jpp11
- fixed build with new auto

* Wed Jun 08 2022 Igor Vlasenko <viy@altlinux.org> 1.0.1-alt1_2jpp11
- new version

* Wed May 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2_6jpp8
- fixed build with maven-javadoc-plugin 3

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_5jpp8
- new jpp release

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_4jpp8
- new version

