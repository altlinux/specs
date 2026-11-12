%define _unpackaged_files_terminate_build 1
%def_without check

Name: hash4j
Version: 0.31.0
Release: alt1

Summary: Hashing algorithms and probabilistic data structures for Java
License: Apache-2.0 AND MIT AND BSD-2-Clause AND Zlib AND CC0-1.0 AND BSL-1.0 AND Unlicense
Group: Development/Java
URL: https://github.com/dynatrace-oss/hash4j
VCS: https://github.com/dynatrace-oss/hash4j.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-offline.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: rpm-build-java
BuildRequires: java-21-openjdk-devel
%if_with check
BuildRequires: java-11-openjdk-devel
BuildRequires: junit5
BuildRequires: assertj-core
BuildRequires: guava
BuildRequires: apache-commons-codec
BuildRequires: mvn(org.hipparchus:hipparchus-stat)
BuildRequires: mvn(org.hipparchus:hipparchus-optim)
BuildRequires: mvn(net.openhft:zero-allocation-hashing)
BuildRequires: mvn(com.appmattus.crypto:cryptohash-jvm)
BuildRequires: mvn(org.greenrobot:essentials)
BuildRequires: mvn(com.sangupta:murmur)
BuildRequires: mvn(at.yawk.lz4:lz4-java)
BuildRequires: mvn(org.apiguardian:apiguardian-api)
BuildRequires: mvn(org.opentest4j:opentest4j)
BuildRequires: mvn(org.jacoco:org.jacoco.agent)
BuildRequires: mvn(org.jacoco:org.jacoco.ant)
%endif

%description
Hash4j provides non-cryptographic hash functions, consistent hashing,
probabilistic data structures and random number generation for Java.
The multi-release JAR includes implementations for Java 11 and 21.

%package javadoc
Summary: API documentation for hash4j
Group: Development/Documentation

%description javadoc
API documentation for the hash4j Java library.

%prep
%setup
%autopatch -p1

%build
%gradle_publish -PreleaseVersion=%version \
    -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk

%install
%gradle_register
%gradle_register_javadoc
%gradle_install

%if_with check
%check
%gradle_check -PreleaseVersion=%version -Palt.skipLargeChecksumTests=true \
    -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk
%endif

%files -f .mfiles
%doc LICENSE licenses/*.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 0.31.0-alt1
- Initial build for ALT.
