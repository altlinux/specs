%define _unpackaged_files_terminate_build 1

Name: jimfs
Version: 1.3.2
Release: alt1

Summary: An in-memory file system for Java 8+
License: Apache-2.0
Group: Development/Java
URL: https://github.com/google/jimfs
VCS: https://github.com/google/jimfs.git

BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: jsr-305
BuildRequires: jspecify
BuildRequires: guava-testlib
BuildRequires: truth
BuildRequires: icu4j
BuildRequires: junit
BuildRequires: google-error-prone-annotations
BuildRequires: google-error-prone-core
BuildRequires: auto-common
BuildRequires: auto-service
BuildRequires: compile-testing
BuildRequires: maven-plugin-bundle
BuildRequires: guava-beta-checker

%description
Jimfs is an in-memory file system for Java 8 and above, implementing the
java.nio.file abstract file system APIs.

%{?javadoc_package}

%prep
%setup
%autopatch -p1

%pom_remove_plugin -r :maven-javadoc-plugin
# The complete source tree is provided by the SRPM, not an attached source JAR.
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :central-publishing-maven-plugin

# Bundle packaging must retain the upstream automatic module name.
bundle_plugin="pom:build/pom:plugins/pom:plugin"
bundle_plugin="$bundle_plugin[pom:artifactId='maven-bundle-plugin']"
%pom_xpath_inject \
    "$bundle_plugin/pom:configuration/pom:instructions" \
    '<Automatic-Module-Name>com.google.common.jimfs</Automatic-Module-Name>' \
    jimfs

%pom_remove_dep -r com.google.auto.service:auto-service-annotations
%pom_add_dep com.google.errorprone:error_prone_annotations jimfs

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Tue Oct 27 2026 Ivan Khanas <xeno@altlinux.org> 1.3.2-alt1
- New version.
- Preserve Java 8 bytecode compatibility.
- Preserve the upstream automatic module name in the bundle.

* Tue Dec 2 2025 Ivan Khanas <xeno@altlinux.org> 1.3.1-alt1
- First build for ALT.
