%define sname retrying
%def_with python3

Name: python-module-%sname
Version: 1.3.3
Release: alt1.1.1
Summary: Retrying library
Group: Development/Python
License: ASL 2.0
Url:  https://github.com/rholder/retrying
Source: %name-%version.tar

BuildArch: noarch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools
#BuildRequires: python-module-six >= 1.7.0

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-six >= 1.7.0
%endif

%description
Simplify the task of adding retry behavior to just about anything.

%if_with python3
%package -n python3-module-%sname
Summary: Retrying library
Group: Development/Python3

%description -n python3-module-%sname
Simplify the task of adding retry behavior to just about anything.
%endif

%prep
%setup

# Remove bundled egg-info
rm -rf %sname.egg-info
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


%files
%doc README.rst LICENSE AUTHORS.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.3-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.3-alt1.1
- NMU: Use buildreq for BR.

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.3-alt1
- initial build
