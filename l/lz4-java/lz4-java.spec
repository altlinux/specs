Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
%define fedora 33
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# empty debuginfo
%global debug_package %nil

Name:          lz4-java
Version:       1.7.1
Release:       alt1_12jpp11
Summary:       LZ4 compression for Java
License:       ASL 2.0
# GPLv2+ and BSD for lz4 and xxhash libs that are shared in liblz4-java.so
URL:           https://github.com/lz4/lz4-java
Source0:       https://github.com/lz4/lz4-java/archive/%{version}.tar.gz

# lz4-java v1.3.0 introduced usage of sun.misc.Unsafe, which would later become
# depricated in jdk 9 and kept as an unexposed API in later jdk releases.
# lz4-java optionally uses Unsafe to achieve faster compression and decompression,
# however it's implementation is not critical to functionality, and can be removed.
Patch0:        0-remove-unsafe.patch
# After updating mvel to version 2.4.10, MVEL generated classes have formatting issues where
# code after comments are not being formatted with new lines. As a result, including comments
# in the templates results in classes with invalid code following the first comment.
# This patch simply removes comments from the templates so the classes can be generated as expected.
# Related bug: https://github.com/mvel/mvel/issues/152
Patch1:        1-remove-comments-from-templates.patch
# Adds a simple makefile to be run in-place of the cpptasks in the build.xml
Patch2:        2-remove-cpptasks.patch
# some lz4-java tests require randomizedtesting, which is not currently
# shipped or maintained in Fedora; remove those and use system ant-junit to run applicable tests
Patch3:        3-remove-randomizedtesting-tests.patch

# Build tools
BuildRequires: apache-parent
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: aqute-bnd
BuildRequires: gcc
BuildRequires: ivy-local
BuildRequires: javapackages-local
BuildRequires: lz4
BuildRequires: liblz4-devel
BuildRequires: mvel
BuildRequires: objectweb-asm
BuildRequires: xerces-j2
BuildRequires: libxxhash-devel
Source44: import.info

%description
LZ4 compression for Java, based on Yann Collet's work.
This library provides access to two compression methods
that both generate a valid LZ4 stream:

* fast scan (LZ4):
    A. low memory footprint (~ 16 KB),
    A. very fast (fast scan with skipping heuristics in case the
      input looks incompressible),
    A. reasonable compression ratio (depending on the
      redundancy of the input).
* high compression (LZ4 HC):
    A. medium memory footprint (~ 256 KB),
    A. rather slow (~ 10 times slower than LZ4),
    A. good compression ratio (depending on the size and
      the redundancy of the input).

The streams produced by those 2 compression algorithms use the
same compression format, are very fast to decompress and can be
decompressed by the same decompressor instance.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch:     noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Cleanup
find -name '*.dylib' -print -delete
find -name '*.so' -print -delete

%build
export LIB_DIR=%{_libdir}
%if 0%{?fedora} >= 33
    export JAVA_HOME=/usr/lib/jvm/java-11/
%else
    export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk
%endif

ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  -Divy.mode=local -Divy.revision=1.7.1 -Divy.pom.version=1.7.1 jar test docs makepom
bnd wrap -p lz4-java.bnd -o dist/lz4-java-%{version}.jar --version %{version} dist/lz4-java.jar

%install
%mvn_artifact dist/lz4-java-%{version}.pom dist/lz4-java-%{version}.jar
%mvn_install -J build/docs

%files -f .mfiles
%doc CHANGES.md README.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1.7.1-alt1_12jpp11
- new version

* Thu Oct 08 2020 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_13jpp8
- fixed build with new java

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_9jpp8
- java update

* Wed Apr 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt2_8jpp8
- e2k support

* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_8jpp8
- new version

