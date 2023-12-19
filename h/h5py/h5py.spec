%define _unpackaged_files_terminate_build 1
%define pypi_name h5py
%define mod_name %pypi_name

# disable tests on 32bit architectures
%ifnarch %ix86 armh
%def_with check
%else
%def_without check
%endif

%define descr \
The h5py package provides both a high- and low-level interface to the HDF5 \
library from Python. The low-level interface is intended to be a complete \
wrapping of the HDF5 API, while the high-level component supports access to HDF5 \
files, datasets and groups using established Python and NumPy concepts.

Name: %pypi_name
Version: 3.10.0
Release: alt1
Summary: Read and write HDF5 files from Python
License: BSD-3-Clause
Group: Development/Python3
Url: http://www.h5py.org/
Vcs: https://github.com/h5py/h5py
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: f406f9326e7d8ca51167809882360652e011b2bc.patch
%pyproject_runtimedeps_metadata
# custom ipython completer for ipython session
%filter_from_requires /python3(IPython\(\..*\)\?)/d
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: libhdf5-devel
BuildRequires: liblzf-devel
%if_with check
%pyproject_builddeps_metadata
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-mpi
%endif

%description
%descr

%package -n python3-module-%name
Summary: %summary
Group: Development/Python3
%add_python3_req_skip Tkinter

%description -n python3-module-%name
%descr

%package -n python3-module-%name-tests
Summary: Tests for %name
Group: Development/Python3
Requires: python3-module-%name = %EVR

%description -n python3-module-%name-tests
This package contains tests for %name.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%add_optflags -fno-strict-aliasing
# build against system lzf library
export H5PY_SYSTEM_LZF=1
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- bash -s <<-'ENDTESTS'
set -eu
mkdir empty
cd empty
python -m pytest -ra -Wignore --pyargs %pypi_name
ENDTESTS

%files -n python3-module-%name
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%name-tests
%python3_sitelibdir/*/tests

%changelog
* Tue Dec 19 2023 Grigory Ustinov <grenka@altlinux.org> 3.10.0-alt1
- Automatically updated to 3.10.0.

* Wed Jun 21 2023 Stanislav Levin <slev@altlinux.org> 3.9.0-alt1
- 3.2.1 -> 3.9.0.

* Fri Feb 03 2023 Anton Vyatkin <toni@altlinux.org> 3.2.1-alt3
- Fixed BuildRequires.

* Mon May 30 2022 Grigory Ustinov <grenka@altlinux.org> 3.2.1-alt2
- Fixed BuildRequires.

* Fri Apr 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2.1-alt1
- Updated to upstream version 3.2.1.

* Tue Nov 10 2020 Vitaly Lipatov <lav@altlinux.ru> 2.10.0-alt3
- fix build, fix tests packing

* Mon Mar 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.10.0-alt2
- Fixed build with numpy.

* Fri Feb 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.10.0-alt1
- Version updated to 2.10.0
- build for python2 disabled.

* Thu Feb 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.9.0-alt4
- Enabled tests (disabled to ppc64le only)
- cleanup build requires.

* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.9.0-alt3
- Fixed build requires.

* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 2.9.0-alt2
- Added missing dep on `numpy.testing`.

* Wed Mar 27 2019 Grigory Ustinov <grenka@altlinux.org> 2.9.0-alt1
- Build new version.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.1-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.7.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Jan 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.1-alt1
- Updated to upstream version 2.7.1.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.5.0-alt2.git20150720.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt2.git20150720
- Version 2.5.0

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.a0.git20150227
- Version 2.5.0a0

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1.b1.git20141107
- New snapshot

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1.b1.git20141031
- Version 2.4.0b1
- Enabled testing

* Sat Aug 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1.a0.git20140805
- New snapshot
- Added module for Python 3

* Fri Jul 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1.a0.git20140625
- Version 2.4.0a0

* Wed Jun 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt2.a1.hg20120919
- Rebuilt with new libhdf5

* Tue Feb 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1.a1.hg20120919
- Version 2.2.0a1

* Wed Sep 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt2.beta.hg20120911
- New snapshot

* Fri Jun 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt2.beta.hg20120219
- Rebuilt

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.0-alt1.beta.hg20120219.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Feb 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.beta.hg20120219
- Version 2.1.0-beta

* Sun Nov 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.hg20111016
- Version 2.0.1

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.1-alt1.svn20101222.1.1
- Rebuild with Python-2.7

* Wed Sep 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.svn20101222.1
- Rebuilt with libhdf5-7

* Thu May 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.svn20101222
- New snapshot

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.svn20100926.2
- Rebuild with python-module-sphinx-devel

* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.svn20100926.1
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.svn20100926
- Version 1.3.1

* Tue Jun 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.svn20100417
- New snapshot

* Mon Mar 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.svn20100319
- New snapshot
- Fixed build

* Thu Mar 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.svn20100304
- Version 1.3.0
- Rebuilt with reformed NumPy
- Added:
  + documentation in PDF
  + tests and pickles packages

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt2
- Rebuilt with python 2.6

* Sat Sep 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus

