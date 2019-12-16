%define _unpackaged_files_terminate_build 1
%define oname jupyter_console

%def_without docs

Name: python3-module-%oname
Version: 6.0.0
Release: alt2

Summary: Jupyter Terminal Console
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/jupyter_console
BuildArch: noarch

# https://github.com/jupyter/jupyter_console.git
# Source-url: https://pypi.io/packages/source/j/%oname/%oname-%version.tar.gz
Source: %name-%version.tar
Patch1: %oname-5.2.0-alt-docs.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: /dev/pts
%if_with docs
BuildRequires: python3-module-sphinx_rtd_theme
BuildRequires: python3-module-sphinxcontrib_github_alt
%endif
BuildRequires: python3-module-vine >= 1.3.0
BuildRequires: python3-module-jupyter_client ipython3
BuildRequires: python3-module-ipykernel python3-module-mock
BuildRequires: python3-module-pexpect python3-module-nose
BuildRequires: python3-module-coverage python3-module-traitlets-tests
BuildRequires: python3-module-ipython_genutils-tests
BuildRequires: python3(pathlib2) python3(PIL)

%py3_provides %oname
%py3_requires jupyter_client IPython ipykernel


%description
A terminal-based console frontend for Jupter kernels. This code is based
on the single-process IPython terminal.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A terminal-based console frontend for Jupter kernels. This code is based
on the single-process IPython terminal.

This package contains tests for %oname.

%prep
%setup
%patch1 -p1

%if_with docs
sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile
%endif

sed -i 's|#!/usr/bin/env python.*|#!/usr/bin/env python3|' \
    $(find ./ -type f \( -name '*.py' -o -name 'jupyter-console' \))

%build
%python3_build_debug

%install
%python3_install

%if_with docs
export PYTHONPATH=$PWD
%make -C docs html
%endif

%check
%if 0
JUPYTER_CONSOLE_TEST=yes nosetests3 -vv --with-coverage --cover-package=%oname %oname
%endif

%files
%doc *.md
%if_with docs
%doc docs/_build/html
%endif
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Mon Dec 16 2019 Andrey Bychkov <mrdrew@altlinux.org> 6.0.0-alt2
- build for python2 disabled

* Tue Jun 04 2019 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt1
- new version 6.0.0 (with rpmrb script)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 5.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Nov 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.2.0-alt1
- Updated to upstream version 5.2.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.dev.git20150812.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1.dev.git20150812
- Initial build for Sisyphus

