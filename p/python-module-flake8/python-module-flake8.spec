%define _unpackaged_files_terminate_build 1
%define oname flake8

%def_with check

Name: python-module-%oname
Version: 3.6.0
Release: alt1

Summary: Code checking using pep8 and pyflakes
Group: Development/Python
License: MIT
Url: http://pypi.python.org/pypi/flake8
# https://gitlab.com/pycqa/flake8.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-pytest-runner
BuildRequires: python3-module-pytest-runner

%if_with check
BuildRequires: python-module-pytest
BuildRequires: python-module-tox
BuildRequires: python-module-coverage
BuildRequires: python-module-pyflakes
BuildRequires: python-module-mock
BuildRequires: python-module-mccabe
BuildRequires: python-module-configparser
BuildRequires: python-module-pycodestyle
BuildRequires: python3-module-pytest
BuildRequires: python3-module-tox
BuildRequires: python3-module-coverage
BuildRequires: python3-module-pyflakes
BuildRequires: python3-module-mock
BuildRequires: python3-module-mccabe
BuildRequires: python3-module-pycodestyle
%endif

%py_requires mccabe
%py_requires pyflakes
%py_requires pycodestyle

%description
Flake8 is a wrapper around these tools:

- PyFlakes - pep8 - Ned's McCabe script

Flake8 runs all tools by launching the single 'flake8' script, but ignores
pep8 and PyFlakes extended options and just uses defaults. It displays the
warnings in a per-file, merged output.

It also adds a few features:

- files that contains with this header are skipped::

- lines that contains a "# NOQA" comment at the end will not issue a
warning. - a Mercurial hook.

- a McCabe complexity checker.

%package -n python3-module-%oname
Summary: Code checking using pep8 and pyflakes
Group: Development/Python3
%py3_requires mccabe
%py3_requires pycodestyle
%py3_requires pyflakes

%description -n python3-module-%oname
Flake8 is a wrapper around these tools:

- PyFlakes - pep8 - Ned's McCabe script

Flake8 runs all tools by launching the single 'flake8' script, but ignores
pep8 and PyFlakes extended options and just uses defaults. It displays the
warnings in a per-file, merged output.

It also adds a few features:

- files that contains with this header are skipped::

- lines that contains a "# NOQA" comment at the end will not issue a
warning. - a Mercurial hook.

- a McCabe complexity checker.

This is version of the package running with Python 3.

%prep
%setup

rm -rf ../python3
cp -a . ../python3
find ../python3 -name '*.py' | xargs sed -i '1s|^#!python|#!%__python3|'

%build
%python_build

pushd ../python3
%python3_build
popd

%install
pushd ../python3
%python3_install
mv %buildroot%_bindir/{flake8,python3-flake8}
popd

%python_install

%check
export PIP_INDEX_URL=http://host.invalid./

export PYTHONPATH="$(pwd)"/src
# copy nessecary exec deps
TOX_TESTENV_PASSENV='PYTHONPATH' %_bindir/tox \
--sitepackages -e py%{python_version_nodots python} --notest
cp -f %_bindir/coverage .tox/py%{python_version_nodots python}/bin/

TOX_TESTENV_PASSENV='PYTHONPATH' %_bindir/tox \
--sitepackages -e py%{python_version_nodots python} -v -- -v

pushd ../python3
export PYTHONPATH="$(pwd)"/src
# copy nessecary exec deps
TOX_TESTENV_PASSENV='PYTHONPATH' %_bindir/tox.py3 \
--sitepackages -e py%{python_version_nodots python3} --notest
cp -f %_bindir/coverage3 .tox/py%{python_version_nodots python3}/bin/coverage

TOX_TESTENV_PASSENV='PYTHONPATH' %_bindir/tox.py3 \
--sitepackages -e py%{python_version_nodots python3} -v -- -v
popd

%files
%doc README.rst LICENSE
%_bindir/flake8
%python_sitelibdir/flake8/
%python_sitelibdir/flake8-*.egg-info/

%files -n python3-module-%oname
%doc README.rst LICENSE
%_bindir/python3-flake8
%python3_sitelibdir/flake8/
%python3_sitelibdir/flake8-*.egg-info/

%changelog
* Sat Oct 27 2018 Stanislav Levin <slev@altlinux.org> 3.6.0-alt1
- 3.5.0 -> 3.6.0.

* Fri May 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.5.0-alt2.1
- rebuild with python3.6

* Fri Feb 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.0-alt2
- Updated build dependencies.

* Fri Dec 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.0-alt1
- Updated to upstream version 3.5.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.4.1-alt1.git20150710.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.4.1-alt1.git20150710.1
- NMU: Use buildreq for BR.

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt1.git20150710
- Snapshot from git

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt1
- Version 2.4.1

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1
- Version 2.4.0

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1
- Version 2.3.0

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.5-alt1
- Version 2.2.5

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 2.1.0-alt1
- First build for ALT (based on Fedora 2.1.0-3.fc21.src)
