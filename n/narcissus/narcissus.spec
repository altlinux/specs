%define _unpackaged_files_terminate_build 1
#def_without test

Name: narcissus
Version: 1.0.11
Release: alt2

Summary: A library for bypassing all of Java security mechanisms
License: MIT
Group: Development/Java
Url: https://github.com/toolfactory
Vcs: https://github.com/toolfactory/narcissus.git
BuildArch: noarch
Packager: Ivan Khanas <xeno@altlinux.org>

Source0: %name-%version.tar

BuildRequires(pre):rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: /proc
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: junit5
BuildRequires: assertj-core
BuildRequires: native-maven-plugin
BuildRequires: maven-antrun-plugin
BuildRequires: maven-source-plugin

%description
Narcissus is a JNI native code library that provides a small subset of the Java
reflection API, while bypassing all of Java's access/visibility checks,
security manager restrictions, and module strong encapsulation enforcement, by
calling methods and accessing fields through the JNI API. This allows code that
relies on reflective access to non-public classes, fields, and methods to keep
working even now that strong encapsulation is being enforced in JDK 16+.

%{?javadoc_package}

%prep
%setup

# make sure bundled libraries anre not used
rm -rfv lib/lib*.so lib/lib*.dynlib lib/lib*.dll

%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin

sed -i '/-m\${sun.arch.data.model}/d' pom.xml

%build
%mvn_build -- \
%if_without test
 -Dmaven.test.skip=true
%endif

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE

%changelog
* Mon Jul 06 2026 Ivan A. Melnikov <iv@altlinux.org> 1.0.11-alt2
- NMU:
  + make sure bundled libraries are not used
  + enable tests on all architectures

* Fri Nov 21 2025 Ivan Khanas <xeno@altlinux.org> 1.0.11-alt1
- First build for ALT.
