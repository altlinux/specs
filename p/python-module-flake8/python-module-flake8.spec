%def_disable check

%global oname flake8

Name: python-module-%oname
Version: 3.5.0
Release: alt2.1

Summary: Code checking using pep8 and pyflakes
Group: Development/Python
License: MIT
URL: http://pypi.python.org/pypi/flake8
# https://gitlab.com/pycqa/flake8.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: python-module-mccabe python-module-mock python-module-nose
BuildRequires: python-module-pytest python-module-pytest-runner
BuildRequires: python2.7(pycodestyle) python2.7(pyflakes) python2.7(enum)
BuildRequires: python2.7(configparser) python2.7(mock)

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-html5lib python3-module-mccabe python3-module-nose
BuildPreReq: python3-module-unittest2 python3-pyflakes python3-module-pbr
BuildPreReq: python3-module-pytest python3-module-pytest-runner
BuildPreReq: python3(pycodestyle) python3(pyflakes) python3(enum) python3(mock)

%py_requires multiprocessing setuptools mccabe pycodestyle pyflakes


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
%py3_requires setuptools mccabe pycodestyle pyflakes

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
find ../python3 -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
%python_build

pushd ../python3
%python3_build
popd

%install
unset PYTHONPATH

# Must do the python3 install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
pushd ../python3
%python3_install
mv %buildroot%_bindir/flake8 %buildroot%_bindir/python3-flake8
popd

%python_install

%if_with check
%check
PYTHONPATH=%buildroot%python_sitelibdir py.test -vv

pushd ../python3
PYTHONPATH=%buildroot%python3_sitelibdir py.test3 -vv
popd
%endif

%files
%doc README.rst CONTRIBUTORS.txt
%_bindir/%oname
%python_sitelibdir/%{oname}*

%files -n python3-module-%oname
%doc README.rst CONTRIBUTORS.txt
%_bindir/python3-%oname
%python3_sitelibdir/%{oname}*


%changelog
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
