%global pypi_name jsonpointer
%global github_name python-json-pointer
%global commit c1ec3dfd171b242e23b3fe078a99f0e23fb0c6ea
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%def_with python3

Name:           python-module-%{pypi_name}
Version:        1.6
Release:        alt1.1
Summary:        Resolve JSON Pointers in Python
Group:          Development/Python

License:        BSD
URL:            https://github.com/stefankoegl/%{github_name}
# pypi tarball does not contain COPYING
Source0:        %{name}-%{version}.tar

BuildArch:      noarch
BuildRequires:  python-devel python-module-setuptools
%if_with python3
BuildRequires:  rpm-build-python3 python3-module-setuptools
%endif

%description
Library to resolve JSON Pointers according to RFC 6901.

%if_with python3
%package -n python3-module-%{pypi_name}
Summary:        Resolve JSON Pointers in Python
Group:          Development/Python
%description -n python3-module-%{pypi_name}
Library to resolve JSON Pointers according to RFC 6901.
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
%if_with python3
pushd ../python3
%{__python3} tests.py
popd
%endif
%{__python} tests.py

%files
%doc README.md COPYING AUTHORS
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%{python_sitelibdir}/%{pypi_name}.py*
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info

%if_with python3
%files -n python3-module-%{pypi_name}
%doc README.md COPYING AUTHORS
%_bindir/*.py3
%{python3_sitelibdir}/__pycache__/*
%{python3_sitelibdir}/%{pypi_name}.py*
%{python3_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1
- Version 1.6

* Wed Jul 23 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0-alt1
- First build for ALT (based on Fedora 1.0-5.fc21.src)

