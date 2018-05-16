%global pypi_name jsonpatch
%global github_name python-json-patch
%def_without bootstrap

Name:           python-module-%{pypi_name}
Version:        1.9
Release:        alt1.2

Summary:        Applying JSON Patches in Python
Group:          Development/Python
License:        BSD
URL:            https://github.com/stefankoegl/%{github_name}
BuildArch:      noarch

Source0:        %{name}-%{version}.tar

BuildRequires:  python-devel
BuildRequires:  python-module-setuptools
BuildRequires:  python-modules-json
BuildRequires:  python-module-jsonpointer

BuildRequires(pre):  rpm-build-python3
BuildPreReq:  python3-module-setuptools
BuildPreReq:  python3-module-jsonpointer


%description
Library to apply JSON Patches according to RFC 6902.

%package -n python3-module-%{pypi_name}
Summary:        Applying JSON Patches in Python
Group:		Development/Python

%description -n python3-module-%{pypi_name}
Library to apply JSON Patches according to RFC 6902.

%prep
%setup

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
export LC_ALL=en_US.UTF-8
%python3_build
popd

%install
pushd ../python3
export LC_ALL=en_US.UTF-8
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

%python_install

%if_with bootstrap
%check
%{__python} tests.py

pushd ../python3
%{__python3} tests.py
popd
%endif

%files
%doc README.md COPYING
%_bindir/*
%exclude %_bindir/*.py3
%{python_sitelibdir}/%{pypi_name}.py*
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-module-%{pypi_name}
%doc README.md COPYING
%_bindir/*.py3
%{python3_sitelibdir}/%{pypi_name}.py*
%{python3_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.9-alt1.2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9-alt1
- Version 1.9

* Wed Jul 23 2014 Lenar Shakirov <snejok@altlinux.ru> 1.2-alt1
- First build for ALT (based on Fedora 1.2-3.fc21.src)
