%define _unpackaged_files_terminate_build 1

Name: palantir-javapoet
Version: 0.22.0
Release: alt1

Summary: Palantir Java API for generating Java source files
License: Apache-2.0
Group: Development/Java
Url: https://github.com/palantir/javapoet
VCS: https://github.com/palantir/javapoet.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-offline.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-21-openjdk-devel
BuildRequires: rpm-build-java-osgi
BuildRequires: xgradle

%description
JavaPoet generates Java source files for code generation and annotation
processing. This package provides the com.palantir.javapoet API and Maven
artifact, with the upstream automatic Java module name.

%package javadoc
Summary: API documentation for Palantir JavaPoet
Group: Development/Documentation

%description javadoc
API documentation for the Palantir Java source generation library.

%prep
%setup
%autopatch -p1

%build
# Keep previous package publications out of reused build roots.
rm -rf %_mavenrepolocal
%gradle_publish

%install
%gradle_register --artifacts=javapoet-
%gradle_register_javadoc --artifacts=javapoet-
%gradle_install

# Upstream tests retained; test-only bootstrap dependencies omitted by request.

%files -f .mfiles
%doc README.md LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon Oct 26 2026 Ivan Khanas <xeno@altlinux.org> 0.22.0-alt1
- Initial build for ALT.
