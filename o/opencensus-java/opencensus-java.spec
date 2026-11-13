%define _unpackaged_files_terminate_build 1

Name: opencensus-java
Version: 0.31.1
Release: alt1

Summary: OpenCensus Java tracing and metrics libraries
License: Apache-2.0
Group: Development/Java
URL: https://opencensus.io/
VCS: https://github.com/census-instrumentation/opencensus-java.git

BuildArch: noarch

Source0: %name-%version.tar
Source1: settings-alt.gradle
Source2: build-alt.gradle
Source3: org.mockito.plugins.MockMaker
Patch0: %name-alt.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(io.grpc:grpc-context)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(com.google.errorprone:error_prone_annotations)
BuildRequires: mvn(com.google.auto.value:auto-value)
BuildRequires: mvn(com.google.auto.value:auto-value-annotations)
BuildRequires: mvn(com.lmax:disruptor)
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(com.github.spotbugs:spotbugs-annotations)
BuildRequires: mvn(org.apache.logging.log4j:log4j-core)
BuildRequires: mvn(io.dropwizard.metrics:metrics-core)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(com.google.truth:truth)
BuildRequires: mvn(com.google.guava:guava-testlib)

%description
OpenCensus Java API, full and lite implementations, testing support, tracing
and metrics utilities, HTTP and gRPC instrumentation, and desktop exporters.

%prep
%setup -q
%autopatch -p1
cp %SOURCE1 settings.gradle
cp %SOURCE2 build.gradle
mkdir -p .alt-test-resources/mockito-extensions
cp %SOURCE3 .alt-test-resources/mockito-extensions/

%build
%gradle_publish -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk

%install
%gradle_register --artifacts=opencensus-
%gradle_install

%check
%gradle_check -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk

%files -f .mfiles
%doc LICENSE

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 0.31.1-alt1
- Initial build for ALT.
