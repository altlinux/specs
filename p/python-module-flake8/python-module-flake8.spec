%def_with python3

%global oname flake8

Name:             python-module-%oname
Version:          3.5.0
Release:          alt1
Summary:          Code checking using pep8 and pyflakes

Group:            Development/Python
License:          MIT
BuildArch:        noarch
URL:              http://pypi.python.org/pypi/flake8

# https://gitlab.com/pycqa/flake8.git
Source:           %name-%version.tar

BuildRequires: python-module-mccabe python-module-mock python-module-nose
BuildRequires: python-module-pytest-runner python2.7(pycodestyle) python2.7(pyflakes)
BuildRequires: python2.7(configparser)
%if_with python3
BuildRequires(pre):    rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-mccabe python3-module-nose python3-module-pbr
BuildRequires: python3-module-unittest2 python3-pyflakes
BuildRequires: python3-module-pytest-runner python3(pycodestyle) python3(pyflakes)
%endif

%py_requires multiprocessing setuptools mccabe pycodestyle pyflakes

%description
Flake8 is a wrapper around these tools:

- PyFlakes - pep8 - Ned's McCabe script

Flake8 runs all tools by launching the single 'flake8' script, but ignores
pep8 and PyFlakes extended options and just uses defaults. It displays the
warnings in a per-file, merged output.

It also adds a few features:

- files that contains with this header are skipped::

# flake8: noqa

- lines that contains a "# NOQA" comment at the end will not issue a
warning. - a Mercurial hook.

- a McCabe complexity checker.


%if_with python3
%package -n python3-module-%oname
Summary:        Code checking using pep8 and pyflakes
Group:          Development/Python

%py3_requires setuptools mccabe pycodestyle pyflakes

%description -n python3-module-%oname
Flake8 is a wrapper around these tools:

- PyFlakes - pep8 - Ned's McCabe script

Flake8 runs all tools by launching the single 'flake8' script, but ignores
pep8 and PyFlakes extended options and just uses defaults. It displays the
warnings in a per-file, merged output.

It also adds a few features:

- files that contains with this header are skipped::

# flake8: noqa

- lines that contains a "# NOQA" comment at the end will not issue a
warning. - a Mercurial hook.

- a McCabe complexity checker.

This is version of the package running with Python 3.

%endif


%prep
%setup

#sed -i -e '/^#!\s*\/.*bin\/.*python/d' flake8/pep8.py
#chmod -x flake8/pep8.py

%if_with python3
rm -rf ../python3
cp -a . ../python3
find ../python3 -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%endif


%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
unset PYTHONPATH

# Must do the python3 install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if_with python3
pushd ../python3
%python3_install
mv %buildroot%_bindir/flake8 %buildroot%_bindir/python3-flake8
popd
%endif

%python_install


%check
PYTHONPATH=%buildroot%python_sitelibdir py.test -vv

%if_with python3
pushd ../python3
PYTHONPATH=%buildroot%python3_sitelibdir py.test3 -vv
popd
%endif

%files
%doc README.rst CONTRIBUTORS.txt
%_bindir/%oname
%python_sitelibdir/%{oname}*

%if_with python3
%files -n python3-module-%oname
%doc README.rst CONTRIBUTORS.txt
%_bindir/python3-%oname
%python3_sitelibdir/%{oname}*
%endif

%changelog
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

