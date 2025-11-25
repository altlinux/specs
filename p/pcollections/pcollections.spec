%define _unpackaged_files_terminate_build 1
%def_with check

Name: pcollections
Version: 5.0.0
Release: alt1

Summary: A Persistent Java Collections Library
License: Apache-2.0
Group: Development/Java
Url: https://github.com/hrldcpr/pcollections
Vcs: https://github.com/hrldcpr/pcollections.git
BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: jpackage-default
%if_with check
BuildRequires: junit5
%endif

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

%description
PCollections serves as a persistent and immutable analogue of the Java
Collections Framework. This includes efficient, thread-safe, generic,
immutable, and persistent stacks, maps, vectors, sets, and bags, compatible
with their Java Collections counterparts.

%{?javadoc_package}

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

%changelog
* Mon Nov 24 2025 Ivan Khanas <xeno@altlinux.org> 5.0.0-alt1
- First build for ALT.
