%ifarch x86_64
%def_with check
%else
%def_without check
%endif
%define pyname pythran
Name: python3-module-%pyname
Version: 0.12.1
Release: alt1
Summary: Ahead of Time Python compiler for numeric kernels
License: BSD and MIT
Provides: %pyname
Group: Development/Python3
BuildArch: noarch

Url: https://github.com/serge-sans-paille/pythran
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: make
BuildRequires: boost-devel
BuildRequires: gcc-c++
BuildRequires: pandoc
BuildRequires: rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-nbsphinx
BuildRequires: /usr/bin/sphinx-build
BuildRequires: python3-module-gast
BuildRequires: python3-module-beniget
BuildRequires: python3-module-ply

%if_with check
BuildRequires: xsimd-devel
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-scipy
BuildRequires: python3-module-ply
BuildRequires: libflexiblas-devel unzip
BuildRequires: python3-module-numpy-testing libnumpy-py3-devel
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
find -name '*.hpp' -exec chmod -x {} +
sed -i '1{/#!/d}' pythran/run.py

# Remove bundled header libs and use the ones from system
rm -r third_party/boost third_party/xsimd
cat >> setup.cfg << EOF
[build_py]
no_boost=True
no_xsimd=True
EOF

# Both OpenBLAS and FlexiBLAS are registered as "openblas" in numpy
sed -i 's|blas=blas|blas=openblas|' pythran/pythran-linux*.cfg
sed -i 's|libs=|libs=flexiblas|' pythran/pythran-linux*.cfg
sed -i 's|include_dirs=|include_dirs=/usr/include/flexiblas|' pythran/pythran-linux*.cfg

# not yet available in Fedora
sed -i '/guzzle_sphinx_theme/d' docs/conf.py docs/requirements.txt

# The tests have some cflags in them
# We need to adapt the flags to play nicely with other Fedora's flags
# E.g. fortify source implies at least -O1
sed -i -e 's/-O0/-O1/g' -e 's/-Werror/-w/g' pythran/tests/__init__.py

%build
%pyproject_build
PYTHONPATH=$PWD make -C docs html
rm -rf docs/_build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject -- -k "not test_cli and not test_toolchain"

%files 
%doc LICENSE
%doc README.rst
%doc docs/_build/html
%_bindir/%pyname
%_bindir/%pyname-config
%python3_sitelibdir_noarch/%pyname
%python3_sitelibdir_noarch/%{pyname}*.dist-info
%python3_sitelibdir_noarch/omp

%changelog
* Wed Feb 15 2023 Anton Farygin <rider@altlinux.ru> 0.12.1-alt1
- 0.12.1

* Sat Dec 03 2022 Anton Farygin <rider@altlinux.ru> 0.12.0-alt1
- first build for ALT, based on Fedora specfile

