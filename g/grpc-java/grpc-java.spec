%define _unpackaged_files_terminate_build 1

Name: grpc-java
Version: 1.85.1
Release: alt1

Summary: gRPC Java API and context libraries
License: Apache-2.0
Group: Development/Java
URL: https://github.com/grpc/grpc-java
VCS: https://github.com/grpc/grpc-java.git

Source0: grpc-java-%version.tar
Source1: grpc-java-api-alt-build.tar
BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: rpm-build-java
BuildRequires: java-21-openjdk-devel
BuildRequires: python3
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.google.guava:guava-testlib)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(com.google.errorprone:error_prone_annotations)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(com.google.truth:truth)
BuildRequires: mvn(org.mockito:mockito-core)

%description
API and context libraries from the gRPC Java project.

%package api
Summary: gRPC Java API library
Group: Development/Java

%description api
The gRPC Java API, including context propagation, deadlines, metadata,
channel and server interfaces.

%package context
Summary: Context compatibility artifact for gRPC Java
Group: Development/Java

%description context
The upstream context compatibility artifact. Its context classes are
provided by the gRPC API artifact through its normal Maven dependency.

%prep
%setup -n grpc-java-%version -a1
%mvn_file io.grpc:grpc-api %name-api/grpc-api
%mvn_file io.grpc:grpc-context %name-api/grpc-context
%mvn_package io.grpc:grpc-api api
%mvn_package io.grpc:grpc-context context

%build
python3 grpc-java-api-alt-build/build.py build
%mvn_artifact grpc-java-api-alt-build/poms/grpc-api.pom \
    build/jars/grpc-api.jar
%mvn_artifact grpc-java-api-alt-build/poms/grpc-context.pom \
    build/jars/grpc-context.jar

%install
%mvn_install

%check
python3 grpc-java-api-alt-build/build.py check

%files api -f .mfiles-api
%dir %_javadir/%name-api
%dir %_mavenpomdir/%name-api
%doc LICENSE NOTICE.txt

%files context -f .mfiles-context

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 1.85.1-alt1
- Initial build for ALT.
