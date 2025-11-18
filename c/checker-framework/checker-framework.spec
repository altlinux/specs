%define _unpackaged_files_terminate_build 1

Name: checker-framework
Version: 3.52.0
Release: alt1

Summary: A powerful framework for extending the Java type system
License: GPL-2.0 WITH Classpath-exception-2.0
Group: Development/Java
Url: http://checkerframework.org
Vcs: https://github.com/typetools/checker-framework.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: jpackage-17-compat
BuildRequires: xgradle
BuildRequires: biz-aQute-bnd-gradle-plugins
BuildRequires: shadow-gradle-plugin

%description
Checker Frameworkenhances Java's type system to make it more powerful and
useful. This lets software developers detect and prevent errors in their
Java programs. The Checker Framework includes compiler plug-ins ("checkers")
that find bugs or verify their absence. It also permits you to write your
own compiler plug-ins.

%package -n checker-qual
Summary: Type qualifier annotations for Checker Framework
Group: Development/Java
BuildArch: noarch

%description -n checker-qual
A set of type qualifier annotations such as @NonNull and @Interned
that programmers add to Java source code for checking with the
Checker Framework. These annotations define additional constraints
on types that are then enforced at compile time by one of the
Framework's checkers.

This package should be installed if you are developing code that
will be checked using the Checker Framework.

%prep
%setup
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register

%gradle_install

%files -n checker-qual
%_mavenmetadatadir/checker-framework.xml
%_javadir/checker-framework/checker-qual.jar
%_mavenpomdir/checker-framework/checker-qual.pom

%changelog
* Tue Nov 18 2025 Ivan Khanas <xeno@altlinux.org> 3.52.0-alt1
- First build for ALT.
