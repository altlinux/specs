%def_with python3

%global modname simplegeneric

Name:           python-module-%{modname}
Version:        0.8.1
Release:        alt1.1.1.1
Summary:        Simple generic functions (similar to Python's own len(), pickle.dump(), etc.)

Group:          Development/Python
License:        Python or ZPLv2.1
URL:            http://cheeseshop.python.org/pypi/simplegeneric
Source0:        %{name}-%{version}.zip

BuildArch:      noarch
BuildRequires:  python-devel unzip
BuildRequires:  python-module-setuptools
BuildRequires:  python-module-setuptools

%description
The simplegeneric module lets you define simple single-dispatch generic
functions, akin to Python's built-in generic functions like len(), iter() and
so on. However, instead of using specially-named methods, these generic
functions use simple lookup tables, akin to those used by e.g. pickle.dump()
and other generic functions found in the Python standard library.


%if_with python3
%package -n python3-module-%{modname}
Summary:        Simple generic functions (similar to Python's own len(), pickle.dump(), etc.)

Group:          Development/Python
License:        Python or ZPLv2.1

BuildRequires:  rpm-build-python3
BuildRequires:  python3-module-setuptools
BuildRequires:  python3-module-setuptools
BuildRequires:  python-tools-2to3

%description -n python3-module-%{modname}
The simplegeneric module lets you define simple single-dispatch generic
functions, akin to Python's built-in generic functions like len(), iter() and
so on. However, instead of using specially-named methods, these generic
functions use simple lookup tables, akin to those used by e.g. pickle.dump()
and other generic functions found in the Python standard library.
%endif


%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
pushd ../python3
    2to3 --write --nobackups .
    sed -i "s/file(/open(/g" setup.py
popd
find ../python3 -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%check
%if_with python3
pushd ../python3
PYTHONPATH=$(pwd) %{__python3} setup.py test
popd
%endif

PYTHONPATH=$(pwd) %{__python} setup.py test

%files
%doc README.txt
%{python_sitelibdir}/simplegeneric.py*
%{python_sitelibdir}/simplegeneric-%{version}-py?.?.egg-info

%if_with python3
%files -n python3-module-%{modname}
%doc README.txt
%{python3_sitelibdir}/__pycache__/simplegeneric.cpython*
%{python3_sitelibdir}/simplegeneric.py*
%{python3_sitelibdir}/simplegeneric-%{version}-py?.?.egg-info
%endif

%changelog
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

