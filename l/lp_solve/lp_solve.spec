%def_disable static

%define origname lpsolve
%define libname lib%origname

%define lp_branch 5.5
%define lp_subver 2.5

Name: lp_solve
Version: %lp_branch.%lp_subver
Release: alt1

Summary: Tool that solves linear programming problem
License: LGPL
Group: Sciences/Mathematics

Url: http://sourceforge.net/projects/lpsolve
Source: %{name}_%{version}_source.tar.gz
Patch0: lp_solve-5.5.0.15-alt-shared.patch
Patch1: lpsolve-5.5.0.11-fedora-cflags.patch
Patch2: lpsolve-5.5.2.5-gcc6.patch
Packager: Michael Shigorin <mike@altlinux.org>

%description
Tool that solves linear programming problem using Simplex algorithm.

%package -n %libname
Summary: Library that solves linear programming problem
Group: Sciences/Mathematics

%description -n %libname
Library that solves linear programming problem using Simplex algorithm.

%package -n %libname-devel
Summary: %libname header files
Group: Development/C
Requires: %libname = %version-%release

%description -n %libname-devel
%libname header files.

%if_enabled static
%package -n %libname-devel-static
Summary: Static %libname library
Group: Development/C
Requires: %libname-devel = %version-%release

%description -n %libname-devel-static
Static %libname library.
%endif

%prep
%setup -n %{name}_%lp_branch
%patch1 -p1
%patch2 -p1

%build
cd lpsolve55
sh -x ccc
rm bin/ux*/liblpsolve55.a
cd ../lp_solve
sh -x ccc

#check
#make test

%install
install -d %buildroot{%_bindir,%_libdir,%_includedir/%name}
install -pm755 lp_solve/bin/ux*/lp_solve %buildroot%_bindir/
install -pm755 lpsolve55/bin/ux*/liblpsolve55.so %buildroot%_libdir/
install -pm644 lp*.h %buildroot%_includedir/%name
ln -s %name %buildroot%_includedir/%origname

%files
%doc README.txt bfp/bfp_LUSOL/LUSOL/LUSOL*.txt
%_bindir/%name

%files -n %libname
%_libdir/*.so*

%files -n %libname-devel
%_includedir/%name/
%_includedir/%origname

%if_enabled static
%files -n %libname-devel-static
%_libdir/lib*.a
%_libdir/lib*.la
%_libdir/%name/lib*.a
%_libdir/%name/lib*.la
%endif

%changelog
* Tue Jan 17 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 5.5.2.5-alt1
- Updated to 5.5.2.5.

* Sat Sep 24 2011 Michael Shigorin <mike@altlinux.org> 5.5.2.0-alt1
- 5.5.2.0
- had to disable tests (no target as well as no makefile), alas

* Fri Sep 18 2009 Michael Shigorin <mike@altlinux.org> 5.5.0.15-alt1
- 5.5.0.15 built for Sisyphus
  + based on *heavily* cleaned up 5.5.0.6 Daedalus spec
    - I've seen no such violent macro exaltation before!!
  + also looked into current PLD and Rawhide specs
- dropped PLD spec from docs, cvs.pld-linux.org is better source
- dropped patch1 (seems applied upstream)
- tweaked patch0
  + then replaced patch0 with PLD one
  + then updated it for 5.5.0.15
  + then postponed shared colamd and stuck Fedora patch instead
- redone build in Fedora-like manner (so that it at least builds)
- introduced %%check section

* Mon May 22 2006 Aleksey Avdeev <solo@altlinux.ru> 5.5.0.6-alt1.0
- Porting in PLD (lp_solve-3.2-1), see lp_solve.PLD.spec (original spec
  in docs)
- Use aclocal, libtoolize and automake if automake version >= "1.9.6"
