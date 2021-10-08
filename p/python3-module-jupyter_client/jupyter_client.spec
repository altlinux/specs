%define _unpackaged_files_terminate_build 1

%define oname jupyter_client

%def_enable check

Name: python3-module-%oname
Version: 7.0.6
Release: alt1
Summary: Jupyter protocol implementation and client libraries
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/jupyter-client/

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-ipython_genutils-tests python3-module-notebook python3-module-pbr
BuildRequires: python3-module-unittest2 python3-module-zmq-tests python3-module-pytest
BuildRequires: python3-module-sphinx_rtd_theme python3-module-pathlib2
BuildRequires: python3-module-sphinx-sphinx-build-symlink
BuildRequires: python3(sphinxcontrib_github_alt)
BuildRequires: python3(IPython)
BuildRequires: python3(IPython.testing.tests)
BuildRequires: python3(async_generator)
BuildRequires: python3(nest_asyncio)
BuildRequires: python3(myst_parser)
BuildRequires: python3(entrypoints)

%py3_provides %oname
%py3_requires traitlets jupyter_core zmq

%description
jupyter_client contains the reference implementation of the [Jupyter
protocol][]. It also provides client and kernel management APIs for
working with kernels.

It also provides the jupyter kernelspec entrypoint for installing
kernelspecs for use with Jupyter frontends.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
jupyter_client contains the reference implementation of the [Jupyter
protocol][]. It also provides client and kernel management APIs for
working with kernels.

It also provides the jupyter kernelspec entrypoint for installing
kernelspecs for use with Jupyter frontends.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
jupyter_client contains the reference implementation of the [Jupyter
protocol][]. It also provides client and kernel management APIs for
working with kernels.

It also provides the jupyter kernelspec entrypoint for installing
kernelspecs for use with Jupyter frontends.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
jupyter_client contains the reference implementation of the [Jupyter
protocol][]. It also provides client and kernel management APIs for
working with kernels.

It also provides the jupyter kernelspec entrypoint for installing
kernelspecs for use with Jupyter frontends.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs pickle
%make -C docs html
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%if_enabled check
%check
rm -fR build
export PYTHONPATH=$PWD
py.test3 -vv
%endif

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/pickle

%files tests
%python3_sitelibdir/%oname/tests

%files pickles
%python3_sitelibdir/%oname/pickle

%files docs
%doc docs/_build/html/*

%changelog
* Thu Oct 07 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 7.0.6-alt1
- Updated to upstream version 7.0.6.

* Thu Aug 19 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.0-alt1
- Updated to upstream version 6.2.0.

* Thu Jun 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.7-alt3
- Updated build dependencies.

* Fri Oct 23 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.7-alt2
- Updated build dependencies.

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.7-alt1
- Updated to upstream version 6.1.7.
- Disabled build for python-2.

* Wed Jan 30 2019 Stanislav Levin <slev@altlinux.org> 5.1.0-alt2
- Applied upstream patches for Tornado5 support.

* Wed Aug 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.1.0-alt1
- Updated to upstream release 5.1.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.0-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0.0-alt2.1
- NMU: Use buildreq for BR.

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Enabled check

* Fri Aug 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus

