%define _unpackaged_files_terminate_build 1

Name: netty-jni-util
Version: 0.0.12
Release: alt1

Summary: Helper functions for Netty JNI libraries
License: Apache-2.0
Group: Development/Java
URL: https://github.com/netty/netty-jni-util
VCS: https://github.com/netty/netty-jni-util
Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildArch: noarch

%description
%summary.

%javadoc_package

%package source
Summary: C sources for dependent Netty JNI libraries
Group: Development/Java

%description source
Source files from netty-jni-util required to build dependent Netty native
packages, with the genuine Maven sources artifact.

%prep
%setup
%pom_remove_plugin :central-publishing-maven-plugin
%mvn_package :netty-jni-util:jar:sources: source

%build
%mvn_build

%install
%mvn_install

%check
# The upstream CI compiles the C implementation independently of Maven.
cmake -S . -B native-check -DCMAKE_POLICY_VERSION_MINIMUM=3.5
cmake --build native-check

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt license/*.txt

%files source -f .mfiles-source

%changelog
* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 0.0.12-alt1
- New version.

* Mon May 18 2026 Evgeniy Serov <scala@altlinux.org> 0.0.10-alt1
- Initial build for Sisyphus.
