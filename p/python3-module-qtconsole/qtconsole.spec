%define _unpackaged_files_terminate_build 1

%define oname qtconsole

Name: python3-module-%oname
Version: 5.2.2
Release: alt1
Summary: Jupyter Qt console
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/qtconsole/

BuildArch: noarch

# https://github.com/jupyter/qtconsole
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-PyQt5
BuildRequires: python3(qtpy)
BuildRequires: python3-module-html5lib
BuildRequires: python3-module-ipython_genutils-tests python3-module-notebook
BuildRequires: python3(IPython)
BuildRequires: python3(IPython.testing.tests)
BuildRequires: python3-module-pbr python3-module-traitlets-tests python3-module-unittest2
BuildRequires: python3(sphinx_rtd_theme)
BuildRequires: python3-module-sphinx-sphinx-build-symlink
BuildRequires: python3(flaky)
BuildRequires: /usr/bin/py.test3
BuildRequires: python3-module-pytest-qt
BuildRequires: xvfb-run
BuildRequires: python3(nest_asyncio)

%py3_provides %oname
%py3_requires traitlets jupyter_core jupyter_client pygments ipykernel

%description
Qt-based console for Jupyter with support for rich media output.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Qt-based console for Jupyter with support for rich media output.

This package contains tests for %oname.

%prep
%setup

%prepare_sphinx3 docs
ln -s ../objects.inv docs/source/

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=$PWD
%make -C docs html

%check
export PYTHONPATH=$PWD
# from openSUSE:
# test skips: https://github.com/jupyter/qtconsole/issues/443
# now with test_input too. But does not seem to happen on the build server, only locally.
xvfb-run py.test3 -vv -ra -k "not (test_00 and (test_scroll or test_debug or test_input))"

%files
%doc *.md docs/build/html
%_bindir/*
%python3_sitelibdir/%oname-%version-py*.egg-info
%python3_sitelibdir/%oname/
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%changelog
* Wed Feb 02 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 5.2.2-alt1
- Updated to upstream version 5.2.2.

* Fri Oct 08 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 5.1.1-alt2
- Updated build dependencies.

* Mon Aug 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 5.1.1-alt1
- Updated to upstream version 5.1.1.
- Enabled tests.

* Thu Jun 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.3-alt3
- Updated build dependencies.

* Fri Oct 23 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.3-alt2
- Updated build dependencies.

* Tue Apr 09 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.3-alt1
- Updated to latest upstream release.
- Disabled build for python-2.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0.1-alt1.1
- NMU: Use buildreq for BR.

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Initial build for Sisyphus

