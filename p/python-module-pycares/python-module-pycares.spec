%define module_name pycares
%def_with python3

Name: python-module-%module_name
Version: 0.6.3
Release: alt1.1

Summary: Python interface for c-ares
License: MIT
Group: Development/Python

Url: http://github.com/saghul/pycares
Source: %name-%version.tar

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python3 python3-base
BuildRequires: python-devel python3-devel rpm-build-python3

#BuildRequires: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-distribute
%endif

%description
pycares is a Python module which provides an interface to c-ares.
c-ares (http://c-ares.haxx.se/) c-ares is a C library that performs DNS requests and name resolves asynchronously.

%package -n python3-module-%module_name
Summary: Python interface for c-ares (Python3)
Group: Development/Python3

%description -n python3-module-%module_name
pycares is a Python module which provides an interface to c-ares.
c-ares (http://c-ares.haxx.se/) c-ares is a C library that performs DNS requests and name resolves asynchronously.

%prep
%setup -q

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif


%build
export LANG=en_US.UTF-8
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
export LANG=en_US.UTF-8
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/pycares*
%doc README.rst LICENSE ChangeLog

%if_with python3
%files -n python3-module-%module_name
%python3_sitelibdir/pycares*
%doc README.rst LICENSE ChangeLog
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.3-alt1.1
- NMU: Use buildreq for BR.

* Fri Feb 13 2015 Vladimir Didenko <cow@altlinux.ru> 0.6.3-alt1
- new version

* Tue Sep 10 2013 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- first build for Sisyphus

