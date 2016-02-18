%define oname hiredis
%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt1.1

Summary: Python wrapper for hiredis

License: BSD
Group: Development/Python
Url: https://github.com/redis/hiredis-py

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: https://pypi.python.org/packages/source/s/sanction/sanction-0.4.tar.gz
Source: %oname-%version.tar

#BuildPreReq: rpm-build-python
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-devel python3-module-setuptools rpm-build-python3

#BuildRequires: python-devel python-module-distribute
#BuildRequires: libhiredis-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-distribute
%endif

%setup_python_module %oname

%description
Python wrapper for hiredis.

%if_with python3
%package -n python3-module-%oname
Summary: Python wrapper for hiredis (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
Python wrapper for hiredis
%endif


%prep
%setup -n %oname-%version

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
%doc COPYING
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Jun 29 2015 Vladimir Didenko <cow@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Fri Nov 28 2014 Vladimir Didenko <cow@altlinux.ru> 0.1.5-alt1
- 0.1.5

* Tue Jun 24 2014 Vladimir Didenko <cow@altlinux.ru> 0.1.3-alt1
- initial build for Sisyphus
