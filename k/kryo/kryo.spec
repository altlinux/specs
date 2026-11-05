%define _unpackaged_files_terminate_build 1

Name: kryo
Version: 5.7.1
Release: alt1

Summary: Object graph serialization framework for Java
License: BSD-3-Clause and Apache-2.0
Group: Development/Java
URL: https://github.com/EsotericSoftware/kryo
VCS: https://github.com/EsotericSoftware/kryo.git

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
# Use the ordinary source-built coroutine runtime dependency.
BuildRequires: mvn(org.jetbrains.kotlinx:kotlinx-coroutines-core-jvm)
BuildRequires: mvn(com.esotericsoftware:minlog)
BuildRequires: mvn(com.esotericsoftware:reflectasm)
BuildRequires: mvn(org.objenesis:objenesis)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-maven-plugin)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
# Kotlin Maven plugin needs tooling-core but does not pull it in.
# The current repository GAV index incorrectly selects kotlin-maven.
BuildRequires: kotlin-tooling-core
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-build-tools-api)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-build-tools-impl)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-compiler-embeddable)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-scripting-compiler-embeddable)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-reflect)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)

%description
Kryo provides fast binary serialization and copying for Java object graphs.
This package contains the ordinary com.esotericsoftware:kryo artifact.

%package -n kryo5
Summary: Relocated Kryo 5 serialization library
Group: Development/Java

%description -n kryo5
The genuine versioned Kryo artifact relocates its classes and embedded
runtime dependencies under com.esotericsoftware.kryo.kryo5. It can coexist
with applications using the ordinary Kryo namespace.

%javadoc_package

%prep
%setup
# Keep API, engine and params on the same genuine system JUnit release.
junit_version=$(rpm -q --qf '%%{VERSION}' junit5)
%pom_xpath_set pom:properties/pom:junit.version "$junit_version"
kotlin_version=$(rpm -q --qf '%%{VERSION}' kotlin-maven)
%pom_xpath_set pom:properties/pom:kotlin.version "$kotlin_version"
# Shading uses the source-built system libraries; retain their actual notices.
mkdir shading-licenses
for package in minlog reflectasm objenesis objectweb-asm; do
    version=$(rpm -q --qf '%%{VERSION}' "$package")
    mkdir "shading-licenses/$package"
    find -L %_defaultdocdir/$package-$version -maxdepth 1 -type f \
        \( -iname '*license*' -o -iname '*copying*' -o -iname '*notice*' \) \
        -exec cp -p '{}' "shading-licenses/$package/" \;
    test -n "$(find "shading-licenses/$package" -type f -print -quit)"
done
# Use RPM-provided dependencies rather than upstream binary distributions.
find . -type f \( -name '*.jar' -o -name '*.class' \) -delete
# JMH benchmarks are outside the retained IDE runtime and regression suite.
%pom_disable_module benchmarks
# Central publication is a release service, not an RPM build input.
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
# XMvn generates the packaged Javadoc without the release attachment plugin.
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
# This ZIP only repackages sources and binary dependencies for distribution.
%pom_remove_plugin org.apache.maven.plugins:maven-assembly-plugin main
# Upstream already skips this historical binary compatibility check.
%pom_remove_plugin org.codehaus.mojo:clirr-maven-plugin main

# Isolate reactor outputs and preserve genuine sources for the shaded artifact.
for module in main main-versioned; do
    %pom_xpath_set pom:build/pom:directory '${project.basedir}/target' $module
done
%pom_add_plugin org.apache.maven.plugins:maven-source-plugin main \
    "<executions><execution><id>attach-sources</id><phase>package</phase>\
    <goals><goal>jar-no-fork</goal></goals></execution></executions>"
# ALT ReflectASM uses the system ASM package, whose namespace is unrelocated.
shade_config="pom:build/pom:plugins/pom:plugin"
shade_config="$shade_config[pom:artifactId='maven-shade-plugin']"
shade_config="$shade_config/pom:executions/pom:execution/pom:configuration"
%pom_xpath_inject "$shade_config/pom:relocations" \
    "<relocation><pattern>org.objectweb.asm</pattern>\
    <shadedPattern>com.esotericsoftware.kryo.kryo5.asm</shadedPattern>\
    </relocation>" \
    main-versioned
%pom_xpath_inject "$shade_config/pom:filters" \
    "<filter><artifact>org.ow2.asm:asm</artifact><excludes>\
    <exclude>META-INF/MANIFEST.MF</exclude>\
    <exclude>module-info.class</exclude>\
    <exclude>META-INF/versions/**/module-info.class</exclude></excludes>\
    </filter>" \
    main-versioned

%mvn_package com.esotericsoftware:kryo-parent kryo
%mvn_package com.esotericsoftware:kryo kryo
%mvn_package com.esotericsoftware.kryo:kryo5 kryo5

%build
# Register the final reduced POM instead of XMvn's pre-shading dependency graph.
%mvn_build -s -i -- -Dmaven.compiler.source=8 -Dmaven.javadoc.source=8
%mvn_artifact pom.xml
%mvn_artifact main/pom.xml main/target/kryo-%version.jar
%mvn_artifact 'com.esotericsoftware:kryo:jar:sources:%version' \
    main/target/kryo-%version-sources.jar
%mvn_artifact main-versioned/target/kryo5-%version.pom \
    main-versioned/target/kryo5-%version.jar
%mvn_artifact 'com.esotericsoftware.kryo:kryo5:jar:sources:%version' \
    main-versioned/target/kryo5-%version-sources.jar

%install
%mvn_install

%files -f .mfiles-kryo
%doc LICENSE.md shading-licenses

%files -n kryo5 -f .mfiles-kryo5

%changelog
* Tue Nov 03 2026 Ivan Khanas <xeno@altlinux.org> 5.7.1-alt1
- New version.

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt1_7jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt1_5jpp8
- java update

* Tue Nov 07 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt1_3jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt1_2jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_2jpp8
- new version

