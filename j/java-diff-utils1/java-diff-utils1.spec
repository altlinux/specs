%define _unpackaged_files_terminate_build 1

Name: java-diff-utils1
Version: 1.3.0
Release: alt1

Summary: Legacy Java library for computing and applying diffs
License: Apache-2.0
Group: Development/Java
URL: https://github.com/dnaumenko/java-diff-utils
VCS: https://github.com/dnaumenko/java-diff-utils

# Upstream 1.3.0 POM commit; this repository has no release tags.
Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(junit:junit)

BuildArch: noarch

%description
The DiffUtils library computes differences between texts, applies patches,
and generates side-by-side views. This package provides the legacy difflib
API and com.googlecode.java-diff-utils:diffutils Maven artifact.

%package javadoc
Summary: API documentation for java-diff-utils1
Group: Documentation

%description javadoc
API documentation for the legacy Java DiffUtils library.

%prep
%setup -q
# Java 5 bytecode is unsupported by the build JDK; preserve the Java sources.
%pom_xpath_set \
    'pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration/pom:source' \
    1.8
%pom_xpath_set \
    'pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration/pom:target' \
    1.8
%mvn_file :diffutils java-diff-utils1/diffutils

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-diffutils

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 1.3.0-alt1
- Initial build for ALT.
