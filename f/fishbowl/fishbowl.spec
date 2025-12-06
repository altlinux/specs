%define _unpackaged_files_terminate_build 1

Name: fishbowl
Version: 1.4.1
Release: alt1

Summary: Fishbowl provides helper methods for dealing with exceptions
License: Apache-2.0
Group: Development/Java
Url: http://stefanbirkner.github.io/fishbowl/index.html
Vcs: https://github.com/stefanbirkner/fishbowl.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: maven-plugin-build-helper

%description
%summary.

%prep
%setup
%autopatch -p1

%pom_remove_parent

%build
%mvn_build -f -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Wed Dec 03 2025 Ivan Khanas <xeno@altlinux.org> 1.4.1-alt1
- First build for ALT.
