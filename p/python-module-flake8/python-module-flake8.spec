%def_with python3

%global modname flake8

Name:             python-module-%{modname}
Version:          2.4.1
Release:          alt1.git20150710.1.1
Summary:          Code checking using pep8 and pyflakes

Group:            Development/Python
License:          MIT
URL:              http://pypi.python.org/pypi/%{modname}
# https://gitlab.com/pycqa/flake8.git
Source0:          %{name}-%{version}.tar
#Patch0: flake8-2.4.0-alt-requirements.patch

BuildArch:        noarch
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-funcsigs python-module-pbr python-module-setuptools python-module-six python-module-unittest2 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-mccabe python-module-mock python-module-nose python-tools-pep8 python3-module-html5lib python3-module-mccabe python3-module-nose python3-module-pbr python3-module-unittest2 python3-pyflakes python3-tools-pep8 rpm-build-python3

#BuildRequires:    python-devel python-modules-multiprocessing
#BuildRequires:    python-module-nose
#BuildRequires:    python-module-setuptools
#BuildRequires:    python-module-mccabe >= 0.2
#BuildRequires:    python-tools-pep8 >= 1.4.3
#BuildRequires:    pyflakes >= 0.6.1
#BuildRequires:    python-module-mock
Requires:    python-module-mccabe >= 0.2
Requires:    python-tools-pep8 >= 1.4.3
Requires:    pyflakes >= 0.6.1
Requires:    python-module-setuptools
%if_with python3
BuildRequires(pre):    rpm-build-python3
#BuildRequires:    python3-module-setuptools
#BuildRequires:    python3-module-nose
#BuildRequires:    python3-module-mccabe >= 0.2
#BuildRequires:    python3-tools-pep8 >= 1.4.3
#BuildRequires:    python3-pyflakes >= 0.6.1
#BuildRequires:    python3-module-mock
%endif

%py_requires multiprocessing

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
%package -n python3-module-%{modname}
Summary:        Code checking using pep8 and pyflakes
Group:          Development/Python

Requires:    python3-module-setuptools
Requires:    python3-module-mccabe >= 0.2
Requires:    python3-tools-pep8 >= 1.4.3
Requires:    python3-pyflakes >= 0.6.1

%description -n python3-module-%{modname}
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
#patch0 -p2

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
mv %{buildroot}%{_bindir}/flake8 %{buildroot}%{_bindir}/python3-flake8
popd
%endif

%python_install


%check
%{__python} setup.py nosetests --verbosity=2
%if_with python3
%{__python3} setup.py nosetests --verbosity=2
%endif

%files
%doc README.rst CONTRIBUTORS.txt

%{_bindir}/%{modname}
%{python_sitelibdir}/%{modname}*

%if_with python3
%files -n python3-module-%{modname}
%doc README.rst CONTRIBUTORS.txt
%{_bindir}/python3-flake8
%{python3_sitelibdir}/%{modname}*
%endif


%changelog
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

