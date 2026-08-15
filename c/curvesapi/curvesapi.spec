Name:    curvesapi
Version: 1.08
Release: alt1
Summary: Java implementation of various mathematical curves that define themselves over a set of control points

License: BSD-3-Clause
Group:   Development/Java
URL:     https://github.com/virtuald/curvesapi
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-java
BuildRequires: java-devel
BuildRequires: /proc
BuildRequires: maven-local

BuildArch: noarch
Requires: java

%description
Implementation of various mathematical curves that define themselves over a set
of control points. The API is written in Java. The curves supported are:
Bezier, B-Spline, Cardinal Spline, Catmull-Rom Spline, Lagrange, Natural Cubic
Spline, and NURBS.

#javadoc_package

%prep
%setup

%build
%mvn_build -f -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc *.md

%changelog
* Thu Jun 18 2026 Andrey Cherepanov <cas@altlinux.org> 1.08-alt1
- Initial build for Sisyphus.
