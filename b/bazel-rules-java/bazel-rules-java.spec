%define _unpackaged_files_terminate_build 1

Name: bazel-rules-java
Version: 9.9.0
Release: alt1

Summary: Java rules sources for Bazel
License: Apache-2.0
Group: Development/Other
Url: https://github.com/bazelbuild/rules_java
VCS: https://github.com/bazelbuild/rules_java.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-module-version.patch
Source1: runfiles-pom.xml
Source2: runfiles-processor.service
Source3: README.runfiles.alt

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java maven-local java-21-openjdk-devel
BuildRequires: junit guava jsr-305 mvn(com.google.truth:truth)

%description
Source files for the rules_java Bazel module, including Java rules, runfiles
library sources and toolchain definitions. The module is installed in
%_datadir/bazel/rules/rules_java for use with a local_path_override.

Java tools, JDKs and transitive Bazel modules are not included. Consumers
must provide those dependencies separately for an offline build.

%package -n bazel-java-runfiles
Summary: Java runfiles lookup and repository annotation processor for Bazel
Group: Development/Java
Requires: java-headless >= 1.8

%description -n bazel-java-runfiles
Source-built Java runfiles library from rules_java. Provides directory and
manifest runfiles lookup, repository mappings, and the AutoBazelRepository
annotation processor. Compiled from the upstream module sources using XMvn.

%prep
%setup
%autopatch -p1
cp %SOURCE1 pom.xml
mkdir -p runfiles-resources/META-INF/services
cp %SOURCE2 runfiles-resources/META-INF/services/javax.annotation.processing.Processor
cp %SOURCE3 README.runfiles.alt
%mvn_file : bazel-java-runfiles

%build
export TEST_TMPDIR="$PWD/runfiles-test-tmp"
mkdir -p "$TEST_TMPDIR"
%mvn_build -j

%install
%mvn_install
install -d %buildroot%_datadir/bazel/rules/rules_java
cp -a AUTHORS BUILD LICENSE MODULE.bazel WORKSPACE java toolchains third_party \
    %buildroot%_datadir/bazel/rules/rules_java/
find %buildroot%_datadir/bazel/rules/rules_java -type d -exec chmod 755 {} +
find %buildroot%_datadir/bazel/rules/rules_java -type f -exec chmod 644 {} +

# Bazel analysis and upstream tests require the separately packaged toolchain
# and its offline repository closure. They are not run by this source package.

# Keep upstream README files in the source archive only.
find %buildroot%_datadir/bazel -type f -iname '*readme*' -delete

%files
%doc LICENSE AUTHORS
%dir %_datadir/bazel
%dir %_datadir/bazel/rules
%_datadir/bazel/rules/rules_java/

%files -n bazel-java-runfiles -f .mfiles
%doc AUTHORS

%changelog
* Mon Nov 02 2026 Ivan Khanas <xeno@altlinux.org> 9.9.0-alt1
- Initial build for ALT.
