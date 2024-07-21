%define _unpackaged_files_terminate_build 1

%define sover 0

Name: cadical
Version: 2.0.0
Release: alt1

Summary: CaDiCaL SAT Solver
License: MIT
Group: Sciences/Mathematics
Url: https://fmv.jku.at/cadical/
Vcs: https://github.com/arminbiere/cadical.git

Source: %name-%version.tar
Patch0: %name-shared.patch

BuildRequires: gcc-c++

%description
The goal of the development of CaDiCaL was to obtain a CDCL solver,
which is easy to understand and change, while at the same time not being much
slower than other state-of-the-art CDCL solvers.

%package -n lib%name%sover
Summary: Shared library for minisat
Group: System/Libraries

%description -n lib%name%sover
%summary

%package -n lib%name-devel
Summary: Development headers for %name
Group: Development/C++
Requires: lib%name%sover = %EVR

%description -n lib%name-devel
%summary

%package -n lib%name-devel-static
Summary: Static library for %name
Group: Development/C++
Requires: lib%name-devel = %EVR

%description -n lib%name-devel-static
%summary

%prep
%setup
%patch0 -p0

%build
export CXXFLAGS="-fPIC"
./configure -a
%make_build

%install
mkdir -p %buildroot%_bindir
cp build/cadical %buildroot%_bindir
cp build/mobical %buildroot%_bindir

mkdir -p %buildroot%_libdir
cp build/lib%name.so.0.0.0 %buildroot%_libdir
ln -s lib%name.so.0.0.0 %buildroot%_libdir/lib%name.so
ln -s lib%name.so.0.0.0 %buildroot%_libdir/lib%name.so.0
cp build/lib%name.a %buildroot%_libdir

mkdir -p %buildroot%_includedir
cp src/%{name}.hpp %buildroot%_includedir
cp src/c%{name}.h %buildroot%_includedir

%check
sed -i '/make -C \$CADICALBUILD/d;/^make$/d' test/*/run.sh
export LD_LIBRARY_PATH=%buildroot%_libdir
%make_build -C test

%files
%doc README.md NEWS.md VERSION CONTRIBUTING.md
%_bindir/*

%files -n lib%name-devel
%_libdir/lib%{name}.so
%_includedir/*%{name}.h*

%files -n lib%name%sover
%_libdir/lib%{name}.so.*

%files -n lib%name-devel-static
%_libdir/lib%{name}.a

%changelog
* Tue Jun 18 2024 Daniel Zagaynov <kotopesutility@altlinux.org> 2.0.0-alt1
- Update to upstream 2.0.0

* Sun Mar 10 2024 Daniel Zagaynov <kotopesutility@altlinux.org> 1.9.5-alt1
- Update to upstream 1.9.5

* Tue Jan 16 2024 Daniel Zagaynov <kotopesutility@altlinux.org> 1.9.4-alt1
- Initial build for Sisyphus.
