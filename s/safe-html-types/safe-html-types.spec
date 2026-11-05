%define _unpackaged_files_terminate_build 1

Name: safe-html-types
Version: 1.0.8
Release: alt1

Summary: Safe HTML and related web content types for Java
License: Apache-2.0
Group: Development/Java
URL: https://github.com/google/safe-html-types
VCS: https://github.com/google/safe-html-types.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %name-%version-protobuf31.1.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: perl
BuildRequires: mvn(com.google.protobuf:protobuf-java)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.google.guava:guava-testlib)
BuildRequires: mvn(com.google.auto.value:auto-value)
BuildRequires: mvn(com.google.auto.value:auto-value-annotations)
BuildRequires: mvn(com.google.jsinterop:jsinterop-annotations)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(com.google.errorprone:error_prone_annotations)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
Safe HTML Types supplies wrappers for HTML, JavaScript, URLs and style
content. Their contracts support safe construction of web content.

%package proto
Summary: Protocol buffer schemas for Safe HTML Types
Group: Development/Java

%description proto
Original protocol buffer schemas describing Safe HTML Types values.

%package javadoc
Summary: API documentation for Safe HTML Types
Group: Development/Documentation

%description javadoc
Generated Java API documentation for Safe HTML Types.

%prep
%setup -a1
%pom_remove_plugin external.atlassian.jgitflow:jgitflow-maven-plugin
%pom_remove_plugin com.comoyo.maven.plugins:protoc-bundled-plugin
%pom_remove_plugin com.comoyo.maven.plugins:protoc-bundled-plugin types
%pom_xpath_set pom:properties/pom:java.version 8
%pom_xpath_inject pom:properties \
    '<maven.compiler.release>8</maven.compiler.release>'
# Generated has SOURCE retention and is part of the Java 8 release API.
%pom_remove_dep javax.annotation:jsr250-api types
%pom_add_dep com.google.auto.value:auto-value-annotations::test types
%pom_xpath_set '//pom:executable' \
    '${project.parent.basedir}/src/main/scripts/make_fences_xml.sh' types
%mvn_package :proto proto

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE AUTHORS

%files proto -f .mfiles-proto

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 1.0.8-alt1
- Initial build for ALT.
