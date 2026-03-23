%define _unpackaged_files_terminate_build 1

%ifarch %ix86
%def_with fix_heapsize
%else
%def_without fix_heapsize
%endif

Name: jsqlparser
Version: 5.3
Release: alt1

Summary: JSQLParser is a SQL statement parser built from JavaCC
Group: Development/Java
License: Apache-2.0 and LGPL-2.1
Url: https://jsqlparser.github.io/JSqlParser
Vcs: https://github.com/JSQLParser/JSqlParser
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch
Patch1: %name-alt-i586-heapsize.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: java-17-openjdk-devel
BuildRequires: xgradle
BuildRequires: javacc-gradle-plugin
BuildRequires: biz-aQute-bnd-gradle-plugins
BuildRequires: apache-commons-io
BuildRequires: apache-commons-text
BuildRequires: apache-commons-lang3
BuildRequires: mockito-core
BuildRequires: mockito-junit-jupiter
BuildRequires: assertj-core
BuildRequires: hamcrest
BuildRequires: junit5

%package javadoc
Summary: JSQLParser is a SQL statement parser built from JavaCC
Group: Development/Java

%description
JSQLParser is a SQL statement parser built from JavaCC. It translates SQLs in
a traversable hierarchy of Java classes.

%description javadoc
JSQLParser is a SQL statement parser built from JavaCC. It translates SQLs in
a traversable hierarchy of Java classes.

This package contains javadoc for jsqlparser.

%prep
%setup
%patch0 -p1
%if_with fix_heapsize
# Fix JVM heap size due to 32-bit limit.
%patch1 -p1
%endif

%build
export VERSION=%version
%gradle_build
%gradle_publish

%install
%gradle_register
%gradle_register_javadoc
%gradle_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Mar 23 2026 Arseniy Kostevich <faux@altlinux.org> 5.3-alt1
- Initial build for ALT.
