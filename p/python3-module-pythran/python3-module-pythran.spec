%ifarch x86_64
%def_with check
%else
%def_without check
%endif

%define pyname pythran

%ifarch %e2k
%def_without docs
%else
%def_without docs
%endif

Name: python3-module-%pyname
Version: 0.16.1
Release: alt1
Summary: Ahead of Time Python compiler for numeric kernels
License: BSD and MIT
Provides: %pyname
Group: Development/Python3

BuildArch: noarch

Url: https://github.com/serge-sans-paille/pythran
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-scipy
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-gast
BuildRequires: python3-module-beniget
BuildRequires: python3-module-ply
BuildRequires: boost-devel
BuildRequires: libflexiblas-devel
BuildRequires: libnumpy-py3-devel
BuildRequires: xsimd-devel >= 13.0.0
BuildRequires: gcc-c++
BuildRequires: unzip
BuildRequires: ipython3
BuildRequires: python3-module-pip
BuildRequires: libopenblas-devel
%endif

%if_with docs
BuildRequires: python3-module-nbsphinx
BuildRequires: /usr/bin/sphinx-build
BuildRequires: pandoc
%endif

# This is a package that compiles code, it runtime requires devel packages
Requires: gcc-c++
Requires: python3-dev
Requires: boost-devel
Requires: xsimd-devel

%description
Pythran is an ahead of time compiler for a subset of the Python language, with
a focus on scientific computing. It takes a Python module annotated with a few
interface description and turns it into a native Python module with the same
interface, but (hopefully) faster. It is meant to efficiently compile
scientific programs, and takes advantage of multi-cores and SIMD
instruction units.

%prep
%setup
%patch0 -p1

# drop distutils
sed -i 's/distutils.errors/setuptools.errors/' pythran/run.py

# remove bundled use the ones from system
rm -r pythran/{boost,xsimd}

# Both OpenBLAS and FlexiBLAS are registered as "openblas" in numpy
sed -i 's|blas=blas|blas=openblas|' pythran/pythran-linux*.cfg
sed -i 's|libs=|libs=flexiblas|' pythran/pythran-linux*.cfg
sed -i 's|include_dirs=|include_dirs=/usr/include/flexiblas|' pythran/pythran-linux*.cfg

# The tests have some cflags in them
# We need to adapt the flags to play nicely with other Fedora's flags
# E.g. fortify source implies at least -O1
sed -i -e 's/-O0/-O1/g' -e 's/-Werror/-w/g' pythran/tests/__init__.py

%build
%pyproject_build

%if_with docs
PYTHONPATH=$PWD make -C docs html
rm -rf docs/_build/html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

%check
%pyproject_run_pytest -n auto

%files
%doc LICENSE
%doc README.rst
%_bindir/%pyname
%_bindir/%pyname-config
%python3_sitelibdir/%pyname
%python3_sitelibdir/%pyname-%version.dist-info
%python3_sitelibdir/omp
%if_with docs
%doc docs/_build/html
%endif

%changelog
* Sun Jul 14 2024 Anton Farygin <rider@altlinux.ru> 0.16.1-alt1
- 0.15.0 -> 0.16.1

* Tue Feb 06 2024 Anton Vyatkin <toni@altlinux.org> 0.15.0-alt2
- Fixed FTBFS.

* Sun Jan 21 2024 Anton Vyatkin <toni@altlinux.org> 0.15.0-alt1
- New version 0.15.0.

* Fri Oct 27 2023 Anton Vyatkin <toni@altlinux.org> 0.14.0-alt2
- (NMU) Dropped dependency on distutils.

* Thu Sep 28 2023 Anton Vyatkin <toni@altlinux.org> 0.14.0-alt1
- (NMU) New version 0.14.0.

* Sun May 14 2023 Anton Farygin <rider@altlinux.ru> 0.13.1-alt1
- 0.12.1 -> 0.13.1

* Wed Feb 15 2023 Anton Farygin <rider@altlinux.ru> 0.12.1-alt1
- 0.12.1

* Sat Dec 03 2022 Anton Farygin <rider@altlinux.ru> 0.12.0-alt1
- first build for ALT, based on Fedora specfile

