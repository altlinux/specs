%define oname hiredis
%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt1

Summary: Python wrapper for hiredis

License: BSD
Group: Development/Python
Url: https://github.com/redis/hiredis-py

Source: %oname-%version.tar

BuildRequires: python-module-setuptools python3-devel python3-module-setuptools rpm-build-python3

%if_with python3
BuildRequires(pre): rpm-build-python3
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
* Fri Sep 27 2019 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0-alt1.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Jun 29 2015 Vladimir Didenko <cow@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Fri Nov 28 2014 Vladimir Didenko <cow@altlinux.ru> 0.1.5-alt1
- 0.1.5

* Tue Jun 24 2014 Vladimir Didenko <cow@altlinux.ru> 0.1.3-alt1
- initial build for Sisyphus
