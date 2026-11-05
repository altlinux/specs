%define _unpackaged_files_terminate_build 1

Name: zero-allocation-hashing
Version: 2026.0
Release: alt1

Summary: Allocation-free non-cryptographic hash functions for Java
License: Apache-2.0
Group: Development/Java
URL: https://github.com/OpenHFT/Zero-Allocation-Hashing
VCS: https://github.com/OpenHFT/Zero-Allocation-Hashing.git

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)

%description
Allocation-free implementations of non-cryptographic hash functions for byte
sequences, strings, buffers, arrays and native memory.

%package sources
Summary: Java sources for zero-allocation-hashing

Group: Development/Java

%description sources
Java source archive for zero-allocation-hashing.

%package javadoc
Summary: API documentation for zero-allocation-hashing

Group: Development/Documentation

%description javadoc
API documentation for zero-allocation-hashing.

%prep
%setup -q
%autopatch -p1
# OpenHFT release parents are absent in ALT. Retain the effective compiler,
# source attachment, assertion and compact-string test settings locally.
%pom_remove_parent
%pom_xpath_inject pom:project \
    '<groupId>net.openhft</groupId>
    <licenses>
      <license>
        <name>Apache License, Version 2.0</name>
        <url>https://www.apache.org/licenses/LICENSE-2.0</url>
      </license>
    </licenses>'
%pom_change_dep com.intellij:annotations org.jetbrains:annotations
%pom_xpath_inject pom:properties \
    '<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <argLine/>
    <jvm.requiredArgs/>'
%pom_xpath_inject \
    "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-bundle-plugin']" \
    '<version>${maven.bundle.plugin.version}</version>'
%pom_xpath_inject \
    "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']
    /pom:configuration" \
    '<parameters>true</parameters>
    <encoding>UTF-8</encoding>
    <proc>none</proc>'
%pom_xpath_inject \
    "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-source-plugin']" \
    '<executions>
      <execution>
        <id>attach-sources</id>
        <goals>
          <goal>jar-no-fork</goal>
        </goals>
      </execution>
    </executions>'
%pom_xpath_inject \
    "pom:profiles/pom:profile/pom:build/pom:plugins
    /pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:executions
    /pom:execution[pom:id='test-without-compact-string']/pom:configuration" \
    '<reportsDirectory>
      ${project.build.directory}/surefire-no-compact-reports
    </reportsDirectory>'
# XMvn's native Javadoc goal produces the packaged API documentation.
%pom_remove_plugin :maven-javadoc-plugin
# Use the effective upstream parent versions for a complete standalone model.
%pom_xpath_inject \
    "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']" \
    '<version>3.14.0</version>'
%pom_xpath_inject \
    "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']" \
    '<version>3.1.2</version>'
%pom_xpath_inject \
    "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-source-plugin']" \
    '<version>3.3.0</version>'
%pom_xpath_inject \
    "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-enforcer-plugin']" \
    '<version>3.3.0</version>'
# Platform signatures are build inputs, never published source or API docs.
%pom_xpath_inject \
    "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-source-plugin']
    /pom:configuration/pom:excludes" \
    '<exclude>java/**</exclude>'
%pom_add_plugin org.apache.maven.plugins:maven-antrun-plugin:3.1.0 . \
    '<executions>
      <execution>
        <id>remove-platform-doc-inputs</id>
        <phase>prepare-package</phase>
        <goals>
          <goal>run</goal>
        </goals>
        <configuration>
          <target>
            <delete dir="${project.basedir}/src/main/java-stub"/>
          </target>
        </configuration>
      </execution>
    </executions>'
%pom_xpath_set \
    "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-bundle-plugin']
    /pom:configuration/pom:instructions/pom:Import-Package" \
    'javax.annotation;resolution:=optional,sun.misc;resolution:=optional,*'
# Compile bytecode for Java 8; document real Unsafe signatures from the build
# JDK.
%pom_add_plugin org.fedoraproject.xmvn:xmvn-mojo:4.2.0 . \
    '<configuration>
      <release>21</release>
    </configuration>'
# Runtime publication and signing plugins belong to the upstream release
# service.
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-scm-publish-plugin
%mvn_package :*:jar:sources: sources
%mvn_file :zero-allocation-hashing zero-allocation-hashing

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files sources -f .mfiles-sources

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Oct 27 2026 Ivan Khanas <xeno@altlinux.org> 2026.0-alt1
- Initial build for ALT.
