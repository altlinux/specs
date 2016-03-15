%global pypi_name jsonpatch
%global github_name python-json-patch
%global commit f6f3cd235337209fc96b71316215a40d1cd3026c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%def_with python3

Name:           python-module-%{pypi_name}
Version:        1.9
Release:        alt1.1
Summary:        Applying JSON Patches in Python
Group:          Development/Python

License:        BSD
URL:            https://github.com/stefankoegl/%{github_name}
#Source0:        https://pypi.python.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# pypi tarball does not contain README.md and tests.py
Source0:        %{name}-%{version}.tar

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-module-setuptools
BuildRequires:  python-modules-json
BuildRequires:  python-module-jsonpointer
Requires:       python-module-jsonpointer

%description
Library to apply JSON Patches according to RFC 6902.

%if_with python3
%package -n python3-module-%{pypi_name}
Summary:        Applying JSON Patches in Python
Group:		Development/Python
BuildArch:      noarch
BuildRequires:  rpm-build-python3
BuildRequires:  python3-module-setuptools
BuildRequires:  python3-module-jsonpointer
Requires:       python3-module-jsonpointer

%description -n python3-module-%{pypi_name}
Library to apply JSON Patches according to RFC 6902.

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
export LC_ALL=en_US.UTF-8
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
export LC_ALL=en_US.UTF-8
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
%{__python} tests.py

%if_with python3
pushd ../python3
%{__python3} tests.py
popd
%endif

%files
%doc README.md COPYING
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%{python_sitelibdir}/%{pypi_name}.py*
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info

%if_with python3
%files -n python3-module-%{pypi_name}
%doc README.md COPYING
%_bindir/*.py3
%{python3_sitelibdir}/%{pypi_name}.py*
%{python3_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9-alt1
- Version 1.9

* Wed Jul 23 2014 Lenar Shakirov <snejok@altlinux.ru> 1.2-alt1
- First build for ALT (based on Fedora 1.2-3.fc21.src)

