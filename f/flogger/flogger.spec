%define _unpackaged_files_terminate_build 1

Name: flogger
Version: 0.9
Release: alt1

Summary: Fluent logging API for Java
License: Apache-2.0
Group: Development/Java
URL: https://github.com/google/flogger
VCS: https://github.com/google/flogger.git

Source0: %name-%version.tar
Source1: %name-alt-build.tar
BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: rpm-build-java
BuildRequires: java-21-openjdk-devel
BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: python3
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(com.google.errorprone:error_prone_annotations)
BuildRequires: mvn(org.jspecify:jspecify)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(com.google.guava:guava-testlib)
BuildRequires: mvn(com.google.truth:truth)
BuildRequires: mvn(com.google.truth.extensions:truth-java8-extension)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(com.google.auto.service:auto-service)
BuildRequires: mvn(io.grpc:grpc-api)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.apache.logging.log4j:log4j-api)
BuildRequires: mvn(org.apache.logging.log4j:log4j-core)

%description
A fluent logging API with lazy evaluation, metadata, logging contexts and
pluggable logging backends.

%package system-backend
Summary: Java system logging backend for Flogger
Group: Development/Java

%description system-backend
Java system logging backend from the Flogger project.

%package testing
Summary: Testing support for Flogger
Group: Development/Java

%description testing
Testing support from the Flogger project.

%package google-extensions
Summary: GoogleLogger extensions for Flogger
Group: Development/Java

%description google-extensions
GoogleLogger extensions from the Flogger project.

%package grpc-context
Summary: gRPC context support for Flogger
Group: Development/Java

%description grpc-context
gRPC context support from the Flogger project.

%package slf4j-backend
Summary: SLF4J backend for Flogger
Group: Development/Java

%description slf4j-backend
SLF4J backend from the Flogger project.

%package log4j2-backend
Summary: Log4j 2 backend for Flogger
Group: Development/Java

%description log4j2-backend
Log4j 2 backend from the Flogger project.

%prep
%setup -a1
%mvn_file com.google.flogger:flogger \
    %name/flogger
%mvn_file com.google.flogger:flogger-system-backend \
    %name/flogger-system-backend
%mvn_file com.google.flogger:flogger-testing \
    %name/flogger-testing
%mvn_file com.google.flogger:google-extensions \
    %name/google-extensions
%mvn_file com.google.flogger:flogger-grpc-context \
    %name/flogger-grpc-context
%mvn_file com.google.flogger:flogger-slf4j-backend \
    %name/flogger-slf4j-backend
%mvn_file com.google.flogger:flogger-log4j2-backend \
    %name/flogger-log4j2-backend
%mvn_package com.google.flogger:flogger-system-backend system-backend
%mvn_package com.google.flogger:flogger-testing testing
%mvn_package com.google.flogger:google-extensions google-extensions
%mvn_package com.google.flogger:flogger-grpc-context grpc-context
%mvn_package com.google.flogger:flogger-slf4j-backend slf4j-backend
%mvn_package com.google.flogger:flogger-log4j2-backend log4j2-backend

%build
python3 flogger-alt-build/build.py build
%mvn_artifact flogger-alt-build/poms/flogger.pom \
    build/jars/flogger.jar
%mvn_artifact flogger-alt-build/poms/flogger-system-backend.pom \
    build/jars/flogger-system-backend.jar
%mvn_artifact flogger-alt-build/poms/flogger-testing.pom \
    build/jars/flogger-testing.jar
%mvn_artifact flogger-alt-build/poms/google-extensions.pom \
    build/jars/google-extensions.jar
%mvn_artifact flogger-alt-build/poms/flogger-grpc-context.pom \
    build/jars/flogger-grpc-context.jar
%mvn_artifact flogger-alt-build/poms/flogger-slf4j-backend.pom \
    build/jars/flogger-slf4j-backend.jar
%mvn_artifact flogger-alt-build/poms/flogger-log4j2-backend.pom \
    build/jars/flogger-log4j2-backend.jar

%install
%mvn_install

%check
python3 flogger-alt-build/build.py check

%files -f .mfiles
%dir %_javadir/%name
%dir %_mavenpomdir/%name
%doc LICENSE AUTHORS

%files system-backend -f .mfiles-system-backend

%files testing -f .mfiles-testing

%files google-extensions -f .mfiles-google-extensions

%files grpc-context -f .mfiles-grpc-context

%files slf4j-backend -f .mfiles-slf4j-backend

%files log4j2-backend -f .mfiles-log4j2-backend

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 0.9-alt1
- Initial build for ALT.
