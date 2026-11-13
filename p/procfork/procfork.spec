%define _unpackaged_files_terminate_build 1

Name: procfork
Version: 1.0.6
Release: alt1

Summary: Cross-platform Java subprocess launching library
License: BSD-2-Clause
Group: Development/Java
URL: https://github.com/carrotsearch/procfork
VCS: https://github.com/carrotsearch/procfork.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: system-build.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(com.carrotsearch.randomizedtesting:randomizedtesting-runner)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: iputils

%description
Procfork launches subprocesses with cross-platform argument escaping, separate
working directories, environment configuration and captured or streamed output.

%package javadoc
Summary: API documentation for %name
Group: Development/Java

%description javadoc
API documentation for Procfork.

%prep
%setup
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register
%gradle_register_javadoc
%gradle_install

%check
%gradle_check

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Nov 11 2026 Ivan Khanas <xeno@altlinux.org> 1.0.6-alt1
- Initial build for ALT.
