%define _unpackaged_files_terminate_build 1

%def_with check

Name: context-propagation
Version: 1.2.1
Release: alt1

Summary: Context Propagation API
License: Apache-2.0
Group: Development/Java
Url: https://github.com/micrometer-metrics/context-propagation
VCS: https://github.com/micrometer-metrics/context-propagation
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-build.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: java-21-openjdk-devel
BuildRequires: rpm-build-java-osgi
BuildRequires: xgradle
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(org.jspecify:jspecify)
BuildRequires: mvn(org.slf4j:slf4j-api)
%if_with check
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
%endif

%description
A library that assists with context propagation across different
types of context mechanisms such as ThreadLocal,
Reactor Context, and others.

%prep
%setup
%autopatch -p1

%build
%gradle_publish

%if_with check
%check
%gradle_check
%endif

%install
%gradle_register --artifacts=context-propagation-
%gradle_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Sat Oct 31 2026 Ivan Khanas <xeno@altlinux.org> 1.2.1-alt1
- Initial build for ALT.
