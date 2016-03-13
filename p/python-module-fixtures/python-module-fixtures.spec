%global pypi_name fixtures
%def_with python3
%def_disable check

Name:           python-module-%{pypi_name}
Version:        1.3.1
Release:        alt2.1
Summary:        Fixtures, reusable state for writing clean tests and more

Group:		Development/Python
License:        ASL 2.0 or BSD
URL:            https://launchpad.net/python-fixtures
Source0:        %{name}-%{version}.tar
BuildArch:      noarch

#BuildRequires:  python-devel python-module-mock
#BuildRequires:  python-module-setuptools-tests
#BuildRequires:  python-module-mimeparse

#Requires:       python-module-testtools
BuildRequires: python-module-mimeparse python-module-pbr python-module-pytest python-module-unittest2

%description
Fixtures defines a Python contract for reusable state / support logic,
primarily for unit testing. Helper and adaption logic is included to
make it easy to write your own fixtures using the fixtures contract.
Glue code is provided that makes using fixtures that meet the Fixtures
contract in unittest compatible test cases easy and straight forward.

%if_with python3
%package -n python3-module-%{pypi_name}
Summary:        Fixtures, reusable state for writing clean tests and more
Group:		Development/Python
BuildArch:      noarch
BuildRequires(pre):  rpm-build-python3
#BuildRequires:  python3-module-setuptools python3-module-mock
#BuildRequires:  python3-module-setuptools-tests
#BuildRequires:  python3-module-mimeparse
#Requires:       python3-module-testtools
BuildRequires: python3-module-html5lib python3-module-mimeparse python3-module-pbr python3-module-pytest python3-module-unittest2

%description -n python3-module-%{pypi_name}
Fixtures defines a Python contract for reusable state / support logic,
primarily for unit testing. Helper and adaption logic is included to
make it easy to write your own fixtures using the fixtures contract.
Glue code is provided that makes using fixtures that meet the Fixtures
contract in unittest compatible test cases easy and straight forward.

%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc README GOALS NEWS Apache-2.0 BSD COPYING
%{python_sitelibdir}/%{pypi_name}
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info

%if_with python3
%files -n python3-module-%{pypi_name}
%doc README GOALS NEWS Apache-2.0 BSD COPYING
%{python3_sitelibdir}/%{pypi_name}
%{python3_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 1.3.1-alt2
- Rebuild with "def_disable check"
- Clean buildreq

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Version 1.3.1

* Mon Jul 14 2014 Lenar Shakirov <snejok@altlinux.ru> 0.3.14-alt1
- First build for ALT (based on Fedora 0.3.14-3.fc21.src)
