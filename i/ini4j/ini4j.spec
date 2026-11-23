%define _unpackaged_files_terminate_build 1
%define jdk8 %_jvmdir/java-1.8.0-openjdk

Name: ini4j
Version: 0.5.5.2
Release: alt1

Summary: Java library for reading and writing INI files
License: Apache-2.0
Group: Development/Java
URL: https://github.com/JetBrains/intellij-deps-ini4j
VCS: https://github.com/JetBrains/intellij-deps-ini4j.git

Source: %name-%version.tar
Source1: ini4j-java6-map.java
Patch0: 0001-Isolate-configuration-test-properties.patch

BuildArch: noarch
BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.easymock:easymock)
BuildRequires: mvn(org.apache-extras.beanshell:bsh)

%description
ini4j provides a Java API for reading and writing Windows INI configuration
files, including map, preferences, and JavaBeans APIs.

%package javadoc
Summary: API documentation for ini4j
Group: Development/Documentation

%description javadoc
API documentation for the JetBrains ini4j library.

%prep
%setup -q
%autopatch -p1
mkdir -p target/javac-compat-src/java/util target/javac-compat
cp %SOURCE1 target/javac-compat-src/java/util/Map.java
%jdk8/bin/javac -source 1.6 -target 1.6 \
    -d target/javac-compat target/javac-compat-src/java/util/Map.java
%pom_xpath_remove 'pom:profiles/pom:profile[pom:id="release-candidate"]'
%pom_xpath_remove 'pom:build/pom:extensions/pom:extension[pom:artifactId="wagon-ssh-external"]'
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin
%pom_remove_plugin com.google.code.maven-license-plugin:maven-license-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-changes-plugin
%pom_xpath_remove 'pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-antrun-plugin"]'
%pom_xpath_remove 'pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-site-plugin"]'
%pom_xpath_remove 'pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-dependency-plugin"]'
%pom_xpath_inject 'pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration' \
    '<fork>true</fork>'
%pom_xpath_inject 'pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration' \
    '<executable>%jdk8/bin/javac</executable>'
%pom_xpath_inject 'pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration' \
    '<compilerArgs><arg>-Xbootclasspath/p:${project.build.directory}/javac-compat</arg></compilerArgs>'
%pom_remove_dep net.sf.retrotranslator:retrotranslator-runtime
%pom_remove_dep org.easymock:easymockclassextension

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-ini4j
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 0.5.5.2-alt1
- Initial build for ALT.
