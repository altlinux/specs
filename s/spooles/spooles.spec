#
# Upstream provide static library.
# See https://www.altlinux.org/LTO
#
%define optflags_lto %nil

%global spooles_cc gcc -std=c90 -D_DEFAULT_SOURCE %optflags

%global descr SPOOLES is a library for solving sparse real and complex linear systems\
of equations, written in the C language using object oriented design.

Name: spooles
Version: 2.2
Release: alt13

Summary: A sparse matrix library
License: ALT-Public-Domain
Group: System/Libraries
Url: http://www.netlib.org/linalg/spooles/

# http://www.netlib.org/linalg/spooles/spooles.2.2.tgz
Source: %name-%version.tar

%description
%descr

%package -n lib%name-devel-static
Summary: %summary
Group: Development/C

%description -n lib%name-devel-static
%descr

%prep
%setup

%build
%make_build CC="%spooles_cc" lib
%make_build CC="%spooles_cc" -C MT/src

%install
mkdir -p %buildroot%_libdir
mkdir -p %buildroot%_includedir/%name
for f in $(find -name '*.h');
do
	install -Dt "%buildroot%_includedir/%name/$(dirname "$f")" "$f";
done
install -pm 0644 spooles.a %buildroot%_libdir/spooles.a
install -pm 0644 MT/src/spoolesMT.a %buildroot%_libdir/spoolesMT.a

%files -n lib%name-devel-static
%_includedir/%name
%_libdir/spooles.a
%_libdir/spoolesMT.a

%changelog
* Fri Sep 04 2026 Ulysses Apokin <ulysses@altlinux.org> 2.2-alt13
- Fix file conflicts with the package dyninst-devel (ALT #60374).

* Thu Jun 04 2026 Ulysses Apokin <ulysses@altlinux.org> 2.2-alt12
- Return the package to Sisyphus for FreeCAD FEM Workbench.
