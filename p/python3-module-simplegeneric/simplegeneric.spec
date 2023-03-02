%global modname simplegeneric

Name:           python3-module-%{modname}
Version:        0.8.1
Release:        alt4
Summary:        Simple generic functions (similar to Python's own len(), pickle.dump(), etc.)

Group:          Development/Python3
License:        Python or ZPLv2.1
URL:            http://cheeseshop.python.org/pypi/simplegeneric
Source0:        %{modname}-%{version}.zip

BuildArch:      noarch
BuildRequires:  unzip
BuildRequires:  rpm-build-python3

%description
The simplegeneric module lets you define simple single-dispatch generic
functions, akin to Python's built-in generic functions like len(), iter() and
so on. However, instead of using specially-named methods, these generic
functions use simple lookup tables, akin to those used by e.g. pickle.dump()
and other generic functions found in the Python standard library.

%prep
%setup -n %{modname}-%{version}

    sed -i "s/file(/open(/g" setup.py
find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
%python3_build

%install
%python3_install

%check
PYTHONPATH=$(pwd) %{__python3} setup.py test

%files
%doc README.txt
%{python3_sitelibdir}/__pycache__/simplegeneric.cpython*
%{python3_sitelibdir}/simplegeneric.py*
%{python3_sitelibdir}/simplegeneric-%version-py%_python3_version.egg-info

%changelog
* Thu Mar 02 2023 Anton Vyatkin <toni@altlinux.org> 0.8.1-alt4
- (NMU) Fix BuildRequires, drop 2to3

* Thu Jun 16 2022 Grigory Ustinov <grenka@altlinux.org> 0.8.1-alt3
- Fixed FTBFS.

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 0.8.1-alt2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.1-alt1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.1-alt1.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Aug 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1
- Version 0.8.1

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 0.8-alt1
- First build for ALT (based on Fedora 0.8-9.fc21.src)

