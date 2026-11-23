%define _unpackaged_files_terminate_build 1

Name: roaringbitmap
Version: 1.6.28
Release: alt1

Summary: Compressed bitmap data structure for Java
License: Apache-2.0
Group: Development/Java
URL: https://github.com/RoaringBitmap/RoaringBitmap
VCS: https://github.com/RoaringBitmap/RoaringBitmap.git

Source: %name-%version.tar
Patch0: 0001-Build-Java-8-and-JPMS-artifacts-with-system-Gradle.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(com.esotericsoftware:kryo)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.openjdk.jol:jol-core)

%description
RoaringBitmap is a compressed bitmap implementation for Java. It provides
space-efficient bitmap operations for integer sets and exposes a Java API
with Java 8-compatible classes and a Java module descriptor.

%package bsi
Summary: Bit-sliced index module for RoaringBitmap
Group: Development/Java

%description bsi
The bit-sliced index module builds on RoaringBitmap and provides bitmap-based
indexing operations.

%prep
%setup -q
%autopatch -p1

%build
%gradle_publish

%install
%mvn_package org.roaringbitmap:RoaringBitmap
%mvn_package org.roaringbitmap:bsi bsi
%gradle_register
%gradle_install

%check
%gradle_check

%files -f .mfiles
%doc LICENSE LICENSE-2.0.txt

%files bsi -f .mfiles-bsi

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 1.6.28-alt1
- Initial build for ALT.
