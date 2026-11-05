%define _unpackaged_files_terminate_build 1

Name: mvel
Version: 2.6.0
Release: alt1

Summary: Expression language for Java applications
License: Apache-2.0 and BSD-3-Clause
Group: Development/Java
URL: https://github.com/mvel/mvel
VCS: https://github.com/mvel/mvel.git

Source0: %name-%version.tar
Patch0: %name-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: objectweb-asm
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)

%description
MVEL evaluates expressions and scripts for Java applications. It supports
property access, method invocation and compilation to Java bytecode.
The library includes ASM relocated into the org.mvel2.asm namespace.

%package tests
Summary: Regression test classes for MVEL
Group: Development/Java

%description tests
Test classes and resources from the MVEL regression suite.

%package sources
Summary: Java sources for MVEL and its regression tests
Group: Development/Java

%description sources
Source JARs for the MVEL library and its regression tests.

%javadoc_package

%prep
%setup -n mvel-%version
%autopatch -p1

# This extension is only used to publish artifacts over WebDAV.
%pom_xpath_remove \
    'pom:build/pom:extensions/pom:extension[pom:artifactId="wagon-webdav"]'
# Preserve API documentation through XMvn instead of release attachments.
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin

# Include the notice from the system ASM package selected for shading.
asm_version=$(rpm -q --qf '%%{VERSION}' objectweb-asm)
cp -p %_defaultdocdir/objectweb-asm-$asm_version/LICENSE.txt \
    ASM-SYSTEM-LICENSE.txt

# Explicit mappings retain classified artifacts with singleton packaging.
%mvn_package org.mvel:mvel2:jar:tests: mvel-tests
%mvn_package org.mvel:mvel2:jar:sources: mvel-sources
%mvn_package org.mvel:mvel2:jar:test-sources: mvel-sources
%mvn_package org.mvel:mvel2 mvel

%build
sh .gear/build-eventing-fixture.sh
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-mvel
%doc LICENSE.txt ASM-LICENSE.txt ASM-SYSTEM-LICENSE.txt

%files tests -f .mfiles-mvel-tests

%files sources -f .mfiles-mvel-sources

%changelog
* Thu Oct 29 2026 Ivan Khanas <xeno@altlinux.org> 2.6.0-alt1
- Initial build for ALT.
