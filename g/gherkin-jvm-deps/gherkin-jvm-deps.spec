%define _unpackaged_files_terminate_build 1

Name: gherkin-jvm-deps
Version: 1.0.6
Release: alt1

Summary: Relocated Gson classes for Gherkin JVM
License: Apache-2.0
Group: Development/Java
URL: https://github.com/cucumber-attic/gherkin-jvm-deps
VCS: https://github.com/cucumber-attic/gherkin-jvm-deps

Source0: %name-%version.tar
Patch0: %name-%version.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)

BuildArch: noarch

%description
Gherkin JVM dependencies packages Gson classes in the gherkin.deps namespace
to avoid conflicts with other Gson versions used by applications.

%prep
%setup -q
%patch0 -p1

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-gherkin-jvm-deps

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 1.0.6-alt1
- Initial build for ALT.
