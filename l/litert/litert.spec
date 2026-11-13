%define _unpackaged_files_terminate_build 1

Name: litert
Version: 2.3.2
Release: alt1

Summary: LiteRT model support libraries
License: Apache-2.0
Group: Development/Java
URL: https://ai.google.dev/edge/litert
VCS: https://github.com/google-ai-edge/LiteRT.git

Source: %name-%version.tar
Source1: litert-metadata.pom
Patch0: litert-host-tests.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: libflatbuffers-devel
BuildRequires: flatbuffers-java
BuildRequires: mvn(org.checkerframework:checker-qual)
BuildRequires: mvn(com.google.errorprone:error_prone_annotations)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(com.google.truth:truth)
BuildRequires: mvn(commons-io:commons-io)

BuildArch: noarch

%description
LiteRT support libraries provide utilities for model metadata and data processing.

%package -n litert-metadata
Summary: LiteRT model metadata Java library
Group: Development/Java

%description -n litert-metadata
The complete LiteRT host metadata Java library extracts model metadata and
associated files. It includes generated metadata and TFLite model schemas.

%package -n litert-metadata-javadoc
Summary: API documentation for the LiteRT metadata Java library
Group: Development/Documentation

%description -n litert-metadata-javadoc
API documentation for the LiteRT host metadata Java library.

%prep
%setup
%autopatch -p1
cp %SOURCE1 pom.xml
%pom_change_dep com.google.flatbuffers:flatbuffers-java \
    com.google.flatbuffers:flatbuffers-java:25.12.19
%mvn_package :litert-metadata litert-metadata

# Upstream Bazel targets set these two custom Java packages.
mkdir -p build-java
sed 's/^namespace tflite;/namespace com.google.ai.edge.litert.support.metadata.schema;/' \
    litert/support_lib/metadata/metadata_schema.fbs > build-java/metadata_schema.fbs
sed 's/^namespace tflite;/namespace org.tensorflow.lite.schema;/' \
    tflite/converter/schema/schema.fbs > build-java/schema.fbs
flatc --java -o litert/support_lib/metadata/java \
    build-java/metadata_schema.fbs build-java/schema.fbs

%build
%mvn_build -s

%install
%mvn_install

%check
# The upstream JUnit suite runs during the Maven build.

%files -n litert-metadata -f .mfiles-litert-metadata
%doc LICENSE

%files -n litert-metadata-javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 03 2026 Ivan Khanas <xeno@altlinux.org> 2.3.2-alt1
- Initial build for ALT.
