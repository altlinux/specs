%define _unpackaged_files_terminate_build 1

%define oname ipyparallel

%def_disable check
%def_without bootstrap

Name: python3-module-%oname
Version: 6.3.0
Release: alt4
Summary: Interactive Parallel Computing with IPython
License: BSD-3-Clause
Group: Development/Python3
Url: https://ipyparallel.readthedocs.io/

BuildArch: noarch

# https://github.com/ipython/ipyparallel.git
Source: %name-%version.tar

Patch1: %oname-alt-docs.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest

%if_without bootstrap
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-alabaster python3-module-html5lib python3-module-zope
BuildRequires: python3-module-notebook python3-module-objects.inv
BuildRequires: python3-module-sphinx-sphinx-build-symlink
BuildRequires: python3(IPython)
BuildRequires: python3(IPython.testing.tests)
%else
%add_python3_req_skip IPython
%add_python3_req_skip IPython.core
%add_python3_req_skip IPython.core.application
%add_python3_req_skip IPython.core.crashhandler
%add_python3_req_skip IPython.core.display
%add_python3_req_skip IPython.core.error
%add_python3_req_skip IPython.core.magic
%add_python3_req_skip IPython.core.profiledir
%add_python3_req_skip IPython.paths
%add_python3_req_skip IPython.utils.capture
%add_python3_req_skip IPython.utils.coloransi
%add_python3_req_skip IPython.utils.path
%add_python3_req_skip IPython.utils.process
%add_python3_req_skip IPython.utils.sysinfo
%add_python3_req_skip IPython.utils.text
%add_python3_req_skip ipykernel
%add_python3_req_skip ipykernel.ipkernel
%add_python3_req_skip ipykernel.jsonutil
%add_python3_req_skip ipykernel.kernelapp
%add_python3_req_skip ipykernel.zmqshell
%add_python3_req_skip notebook.base.handlers
%add_python3_req_skip notebook.nbextensions
%add_python3_req_skip notebook.services.config
%add_python3_req_skip notebook.utils
%endif

%if_enabled check
BuildRequires: /usr/bin/iptest3
%endif

%description
Use multiple instances of IPython in parallel, interactively.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Use multiple instances of IPython in parallel, interactively.

This package contains tests for %oname.

%if_without bootstrap
%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Use multiple instances of IPython in parallel, interactively.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Use multiple instances of IPython in parallel, interactively.

This package contains documentation for %oname.
%endif

%prep
%setup
%patch1 -p1

%if_without bootstrap
%prepare_sphinx3 docs
ln -s ../objects.inv docs/source/
%endif

%build
%python3_build_debug

%install
%python3_install

# fix installation directory
mv %buildroot%_prefix%_sysconfdir %buildroot%_sysconfdir

%if_without bootstrap
export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html
cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
export PYTHONPATH=$PWD
iptest3 --coverage xml ipyparallel.tests

%files
%doc *.md
%_bindir/*
%_sysconfdir/jupyter
%_datadir/jupyter
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info
%exclude %python3_sitelibdir/%oname/tests
%if_without bootstrap
%exclude %python3_sitelibdir/%oname/pickle
%endif

%files tests
%python3_sitelibdir/%oname/tests

%if_without bootstrap
%files pickles
%python3_sitelibdir/%oname/pickle

%files docs
%doc examples docs/build/html
%endif

%changelog
* Thu Apr 27 2023 Anton Vyatkin <toni@altlinux.org> 6.3.0-alt4
- Fix BuildRequires

* Thu Jun 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 6.3.0-alt3
- Updated build dependencies.

* Fri Oct 23 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.3.0-alt2
- Updated build dependencies.

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.3.0-alt1
- Updated to upstream version 6.3.0.
- Dropped python-2 support.

* Fri May 11 2018 Andrey Bychkov <mrdrew@altlinux.org> 4.1.0-alt3
- rebuild with all requires

* Fri May 11 2018 Andrey Bychkov <mrdrew@altlinux.org> 4.1.0-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.dev.git20150819.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.1.0-alt1.dev.git20150819.1
- NMU: Use buildreq for BR.

* Sat Aug 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1.dev.git20150819
- Initial build for Sisyphus

