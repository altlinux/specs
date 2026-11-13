%define _unpackaged_files_terminate_build 1

Name: xmlresolver
Version: 6.1.1
Release: alt1

Summary: XML Resolver for Java
License: Apache-2.0 and W3C
Group: Development/Java
URL: https://xmlresolver.org/
VCS: https://codeberg.org/XmlResolver/xmlresolver.git

Source0: %name-%version.tar
Source1: xmlresolverdata-153159b.tar.gz
Source2: rpm-build.gradle
Source3: rpm-init.gradle
Source4: rpm-buildsrc.gradle

BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: rpm-build-java
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(net.sf.saxon:Saxon-HE)
BuildRequires: mvn(org.relaxng:jing)
BuildRequires: mvn(xerces:xercesImpl)
BuildRequires: junit5
BuildRequires: mvn(org.apiguardian:apiguardian-api)

%description
A Java library for resolving XML resources using XML catalogs.

%package javadoc
Summary: API documentation for XML Resolver
Group: Development/Java

%description javadoc
API documentation for XML Resolver.

%prep
%setup -q -a1
# The catalog generator uses XSLT 2.0 constructs, also supported by stock Saxon.
sed -i 's/version="3.0"/version="2.0"/' data/tools/make-catalog.xsl
cp %SOURCE2 rpm-build.gradle
cp %SOURCE3 rpm-init.gradle
cp %SOURCE4 buildSrc/rpm-build.gradle

%build
export LC_ALL=C.UTF-8
%gradle_publish -I rpm-init.gradle \
    -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk

%install
%gradle_register --artifacts=xmlresolver-
%mvn_artifact org.xmlresolver:xmlresolver:jar:data:%version \
    build/libs/%name-%version-data.jar
# Override the system XMvn default that skips nonempty classifiers.
%mvn_package org.xmlresolver:xmlresolver:jar:data:%version
%gradle_register_javadoc --artifacts=xmlresolver-
%gradle_install

%check
export LC_ALL=C.UTF-8
%gradle_check -I rpm-init.gradle -PofflineTests \
    -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk

%files -f .mfiles
%doc LICENSE.md data/src/notices

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 6.1.1-alt1
- Initial build for ALT.
