%define _unpackaged_files_terminate_build 1

%define oname rendersnake

Name:    rendersnake
Version: 1.9
Release: alt1
Summary: Java library for creating components and pages
License: Apache-2.0
Group:   Development/Java
URL:     https://github.com/emicklei/rendersnake

BuildArch: noarch

# https://github.com/emicklei/rendersnake.git
Source: %name-%version.tar

Patch1: %name-%version-alt-build.patch

BuildRequires: rpm-build-java
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
BuildRequires: java-devel >= 1.6
BuildRequires: javapackages-local
BuildRequires: maven-local
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(javax.servlet:servlet-api)
BuildRequires: mvn(org.springframework:spring-webmvc)

%description
RenderSnake is a Java library for creating components
and pages that produce HTML using only Java.
Its purpose is to support the creation of Web applications
that are better maintainable, allows for easier reuse,
have testable UI components and produces
compact HTML in an efficient way.

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{oname}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{oname}.

%prep
%setup
%patch1 -p1

%build
%mvn_build --skip-tests

%install
%mvn_install

%files -f .mfiles
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc README.md

%changelog
* Mon Nov 19 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9-alt1
- Initial build for ALT.
