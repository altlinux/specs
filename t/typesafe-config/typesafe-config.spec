%define _unpackaged_files_terminate_build 1

Name: typesafe-config
Version: 1.4.9
Release: alt1

Summary: HOCON configuration library for JVM languages
License: Apache-2.0
Group: Development/Java
URL: https://github.com/lightbend/config
VCS: https://github.com/lightbend/config.git

Source: %name-%version.tar
Patch: %name-system.patch

BuildArch: noarch
BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-17-openjdk-devel
BuildRequires: xgradle
BuildRequires: scala
BuildRequires: junit

%description
Typesafe Config provides HOCON, JSON and Java properties configuration,
substitution, merging and validation for JVM applications.

%prep
%setup
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register --artifacts=config
%gradle_install

%check
%gradle_check

%files -f .mfiles
%doc LICENSE-2.0.txt

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 1.4.9-alt1
- Initial build for ALT.
