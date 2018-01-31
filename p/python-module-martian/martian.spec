%define _unpackaged_files_terminate_build 1
%define mname martian

Name: python-module-%mname
Version: 1.1
Release: alt1%ubt

Summary: A library to grok configuration from Python code
License: ZPLv2.1
Group: Development/Python
# Source-git: https://github.com/zopefoundation/martian.git
Url: http://pypi.python.org/pypi/martian

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools
#for tests
BuildRequires: python-module-tox
BuildRequires: python-module-virtualenv
BuildRequires: python-module-zope.testrunner
BuildRequires: python-module-coverage
BuildRequires: python3-module-tox
BuildRequires: python3-module-virtualenv
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-coverage
#
BuildArch: noarch

%description
Martian is a library that allows the embedding of configuration
information in Python code. Martian can then grok the system and do the
appropriate configuration registrations. One example of a system that
uses Martian is the system where it originated: Grok
(http://grok.zope.org)

%package -n python3-module-%mname
Summary: A library to grok configuration from Python3 code
Group: Development/Python3

%description -n python3-module-%mname
Martian is a library that allows the embedding of configuration
information in Python3 code. Martian can then grok the system and do the
appropriate configuration registrations. One example of a system that
uses Martian is the system where it originated: Grok
(http://grok.zope.org)

%prep
%setup

rm -rf ../python3
cp -a . ../python3

# from src/martian/testing_compat3.py :
# """ Just python classes that only work in
#     python3. In python < 3 you will get a syntax error.
# """
rm -f src/%mname/testing_compat3.py

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
export PIP_INDEX_URL=http://host.invalid./
export PYTHONPATH=%buildroot%python_sitelibdir_noarch:%python_sitelibdir_noarch:%_libdir/python%_python_version/site-packages
TOX_TESTENV_PASSENV='PYTHONPATH' tox -e py27 -v

pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch:%python3_sitelibdir_noarch:%_libdir/python3/site-packages
TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 -e py35 -v
popd

%files
%doc *.txt *.rst
%python_sitelibdir/%mname
%python_sitelibdir/%mname-%version-*.egg-info

%files -n python3-module-%mname
%doc *.txt *.rst
%python3_sitelibdir/%mname
%python3_sitelibdir/%mname-%version-*.egg-info

%changelog
* Thu Jan 25 2018 Stanislav Levin <slev@altlinux.org> 1.1-alt1%ubt
- 0.14 -> 1.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.14-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.14-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt2
- Added necessary requirements

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt1
- Initial build for Sisyphus

