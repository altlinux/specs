%define _unpackaged_files_terminate_build 1
%def_with check

Name: plumelib-hashmap-util
Version: 1.0.0
Release: alt1

Summary: Plume-lib utility libraries for Java HashMaps
License: GPL-2.0 WITH Classpath-exception-2.0
Group: Development/Java
Url: https://github.com/plume-lib/hashmap-util
Vcs: https://github.com/plume-lib/hashmap-util.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: jpackage-17-compat
BuildRequires: xgradle
BuildRequires: checker-qual
%if_with check
BuildRequires: junit5
%endif

%{?javadoc_package}

%description
Hashmap Java utility libraries from the plume-lib project.
These libraries include Hasher, WeakHashMap, and WeakIdentityHashMap.

This package provides specialized Map utilities that offer alternatives to the
standard Java HashMap for specific use cases, such as maps that use weak
references or provide custom hashing behavior.

This package should be installed if you are developing Java applications that
require these specialized map implementations from the Plume-lib collection of
programming utilities.

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
%gradle_check -Dfile.encoding=UTF-8

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Tue Nov 18 2025 Ivan Khanas <xeno@altlinux.org> 1.0.0-alt1
- First build for ALT.
