%define _unpackaged_files_terminate_build 1

Name: openbeans
Version: 1.0.2
Release: alt1

Summary: JavaBeans implementation for Groovy
License: Apache-2.0
Group: Development/Java
Url: https://github.com/melix/openbeans
VCS: https://github.com/melix/openbeans.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: 0001-ALT-Use-system-Gradle-publication.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-17-openjdk-devel
BuildRequires: xgradle

%description
OpenBeans provides a JavaBeans implementation for environments where the
standard java.beans package is unavailable.

%prep
%setup -q
%patch0 -p1

%build
%gradle_publish

%check
%gradle_check

%install
%gradle_register
%gradle_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt README.md

%changelog
* Thu Oct 29 2026 Ivan Khanas <xeno@altlinux.org> 1.0.2-alt1
- Initial build for ALT.
