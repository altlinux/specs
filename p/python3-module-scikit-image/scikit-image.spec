%define _unpackaged_files_terminate_build 1

%define oname scikit-image

%def_disable docs
%def_enable check
%def_with pythran

Name: python3-module-%oname
Version: 0.19.3
Release: alt1
Summary: Image processing routines for SciPy
License: BSD-3-Clause and MIT
Group: Development/Python3
Url: https://pypi.org/project/scikit-image/

VCS: https://github.com/scikit-image/scikit-image.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: libgomp-devel
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-Cython python3-module-matplotlib
BuildRequires: python3-module-scipy libnumpy-py3-devel
BuildRequires: python3-module-six python3-module-networkx
BuildRequires: python3-module-Pillow
BuildRequires: python3-module-wheel

%if_with pythran
BuildRequires: python3-module-pythran
BuildRequires: libflexiblas-devel
%endif

# for tests
%if_enabled check
BuildRequires: pytest3 /usr/bin/xvfb-run
BuildRequires: python3-module-wavelets python3-module-imageio
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-tifffile
%endif

# for docs
%if_enabled docs
BuildRequires: xvfb-run
BuildRequires: python3-module-sphinx python3-module-sphinx-sphinx-build-symlink
BuildRequires: python3-module-sphinx-gallery
BuildRequires: python3-module-sphinx-copybutton
BuildRequires: python3-module-numpydoc
BuildRequires: python3-module-matplotlib-sphinxext
BuildRequires: python3-module-pandas
BuildRequires: python3-module-dask
BuildRequires: python3-module-scikit-learn
BuildRequires: python3-module-seaborn
%endif

%py3_provides skimage
%py3_requires numpy scipy networkx matplotlib

%add_python3_self_prov_path %buildroot%python3_sitelibdir/skimage/data

# optional dependence is not packaged for ALT
%add_python3_req_skip astropy.io

%description
Image processing algorithms for SciPy, including IO, morphology,
filtering, warping, color manipulation, object detection, etc.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Image processing algorithms for SciPy, including IO, morphology,
filtering, warping, color manipulation, object detection, etc.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Image processing algorithms for SciPy, including IO, morphology,
filtering, warping, color manipulation, object detection, etc.

This package contains documentation for %oname.

%prep
%setup

%if_enabled docs
%prepare_sphinx3 doc
ln -s ../objects.inv doc/source/
%endif

%build
export SCIPY_USE_PYTHRAN=0%{?with_pythran}
%add_optflags -fno-strict-aliasing
%pyproject_build

%install
export SCIPY_USE_PYTHRAN=0%{?with_pythran}
%pyproject_install
rm -rf %buildroot%python3_sitelibdir/doc

%if_enabled docs
export PYTHONPATH=%buildroot%python3_sitelibdir
xvfb-run make -C doc pickle PYTHON=python3
xvfb-run make -C doc html PYTHON=python3

install -d %buildroot%python3_sitelibdir/skimage
cp -fR doc/build/pickle %buildroot%python3_sitelibdir/skimage/
%endif

%check
mkdir -p matplotlib
touch matplotlib/matplotlibrc
export XDG_CONFIG_HOME=$(pwd)
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS='-p no:cacheprovider'
pushd %buildroot%python3_sitelibdir
xvfb-run pytest-3 \
	  --deselect="data/tests/test_data.py::test_skin"  \
  --deselect "io/tests/test_collection.py::TestImageCollection::test_custom_load_func_w_kwarg" \
  --deselect "restoration/tests/test_rolling_ball.py::test_ndim" \
  --deselect="io/tests/test_io.py::test_imread_http_url"  \
	-v skimage
popd
%files
%doc LICENSE.txt
%doc CONTRIBUTING.txt CONTRIBUTORS.txt RELEASE.txt TODO.txt
%doc *.md
%_bindir/*
%python3_sitelibdir/skimage
%python3_sitelibdir/scikit_image-%version.dist-info
%if_enabled docs
%exclude %python3_sitelibdir/skimage/pickle
%endif

%if_enabled docs
%files pickles
%python3_sitelibdir/skimage/pickle
%endif

%files docs
%doc doc/examples viewer_examples
%if_enabled docs
%doc doc/build/html
%endif

%changelog
* Fri Feb 17 2023 Anton Farygin <rider@altlinux.ru> 0.19.3-alt1
- 0.18.2 -> 0.19.3

* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 0.18.2-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Thu Aug 19 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.18.2-alt1
- Updated to upstream version 0.18.2.

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.17.2-alt3
- NMU: add if_enabled docs for sphinx using
- NMU: drop tests packing, disable tests (need review)

* Tue Aug 25 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.17.2-alt2
- Fixed build with new numpy.

* Tue Aug 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.17.2-alt1
- Updated to upstream version 0.17.2.

* Mon Mar 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.15.0-alt3
- Fixed build with numpy.

* Sat Mar 14 2020 Michael Shigorin <mike@altlinux.org> 0.15.0-alt2
- Explicit BR: python3-module-sphinx

* Mon Apr 08 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.15.0-alt1
- Updated to latest upstream release.
- Disabled build for python-2.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.12-alt1.dev.git20150413.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.12-alt1.dev.git20150413.1
- NMU: Use buildreq for BR.

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt1.dev.git20150413
- Version 0.12dev

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.dev.git20141124
- New snapshot
- Moved all tests into tests subpackage

* Sun Nov 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.dev.git20141123
- Initial build for Sisyphus

