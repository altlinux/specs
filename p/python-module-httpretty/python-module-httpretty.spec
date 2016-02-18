%global pypi_name httpretty
%def_with python3

Name:           python-module-%{pypi_name}
Version:        0.8.10
Release:        alt1.1
Summary:        HTTP client mock for Python
License:        MIT
Group:		Development/Python
Url:            http://github.com/gabrielfalcao/httpretty
Source:         %{name}-%{version}.tar

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-pyasn1 python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-ndg-httpsclient python-module-ntlm python3-module-setuptools rpm-build-python3

#BuildRequires:  python-devel
#BuildRequires:  python-module-setuptools
#BuildRequires:  python-module-urllib3
#BuildRequires:  python-modules-json
Requires:       python-module-urllib3

BuildArch:      noarch

%description
This libary allows mocking of http protocol based
unit tests.

%if_with python3
%package -n python3-module-%{pypi_name}
Summary:        HTTP client mock for Python
Group:		Development/Python
BuildArch:      noarch
#BuildRequires:  rpm-build-python3
#BuildRequires:  python3-module-setuptools
Requires:       python3-module-testtools

%description -n python3-module-%{pypi_name}
This libary allows mocking of http protocol based
unit tests.

%endif


%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%{python_sitelibdir}/*

%if_with python3
%files -n python3-module-%{pypi_name}
%{python3_sitelibdir}/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.10-alt1.1
- NMU: Use buildreq for BR.

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.10-alt1
- Version 0.8.10

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.5-alt1
- Version 0.8.5

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt1
- Version 0.8.4

* Mon Jul 21 2014 Lenar Shakirov <snejok@altlinux.ru> 0.8.0-alt1
- First build for ALT (based on Suse 0.8.0-1.1.src)

