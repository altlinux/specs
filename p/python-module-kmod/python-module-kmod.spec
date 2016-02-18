%global pypi_name kmod
%def_with python3

Name:           python-module-%{pypi_name}
License:        LGPLv2+
Group:          Development/Python
Summary:        Python module to work with kernel modules
Version:        0.9
Release:        alt1.1
URL:            https://github.com/agrover/python-kmod/
Source0:        %{name}-%{version}.tar
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-json python-modules-xml python3 python3-base python3-dev python3-module-zope
BuildRequires: libkmod-devel python-module-Cython python3-module-Cython rpm-build-python3

#BuildRequires:  python-devel
#BuildRequires:  python-module-setuptools
#BuildRequires:  python-module-Cython
#BuildRequires:  kmod-devel

%description
Python module to allow listing, loading, and unloading
Linux kernel modules, using libkmod.


%if_with python3
%package -n python3-module-%{pypi_name}
Summary:        Python module to work with kernel modules
Group:		Development/Python
#BuildRequires:  rpm-build-python3 python3-dev
#BuildRequires:  python3-module-setuptools
#BuildRequires:  python3-module-Cython

%description -n python3-module-%{pypi_name}
Python module to allow listing, loading, and unloading
Linux kernel modules, using libkmod.

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

%files
%{python_sitelibdir}/kmod/*
%{python_sitelibdir}/kmod*.egg-info
%doc COPYING.LESSER README

%if_with python3
%files -n python3-module-%{pypi_name}
%doc COPYING.LESSER README
%{python3_sitelibdir}/kmod/*
%{python3_sitelibdir}/kmod*.egg-info
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9-alt1.1
- NMU: Use buildreq for BR.

* Thu Jul 31 2014 Lenar Shakirov <snejok@altlinux.ru> 0.9-alt1
- First build for ALT (based on Fedora 0.9-4.fc21.src)
