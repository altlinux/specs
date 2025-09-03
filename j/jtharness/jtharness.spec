%define _unpackaged_files_terminate_build 1

Name: jtharness
Version: 6.0
Release: alt1

Summary: The JT harness is a general purpose, fully-featured, flexible, and configurable test harness very well suited for most types of unit testing.
License: GPL-2.0
Group: Development/Java
Url: https://github.com/openjdk/jtharness
Vcs: https://github.com/openjdk/jtharness

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: ant
BuildRequires: java-21-openjdk-devel

ExcludeArch: i586

%description
%summary
Originally developed as a test harness to run TCK test suites,
it has since evolved into a general purpose test platform.

%prep
%setup

%build
cd build
ant

%install
cd ../JTHarness-build/binaries/lib/
install -D -m 0644 ./javatest.jar %buildroot%_javadir/javatest.jar

%files
%_javadir/javatest.jar
%doc LICENSE README.md

%changelog
* Mon Aug 18 2025 Timofei Fedotov <sovtouch@altlinux.org> 6.0-alt1
- Initial build for ALT Sisyphus.
