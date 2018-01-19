%define oname texttable
%def_with python3

Name: python-module-%oname
Version: 1.2.1
Release: alt1

Summary: Module for creating simple ASCII tables

License: %lgpl3only
Group: Development/Python
Url: https://github.com/foutaise/texttable

Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
BuildPreReq: rpm-build-python
BuildRequires: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%setup_python_module %oname

%description
texttable is a module to generate a formatted text table, using ASCII characters.

%if_with python3
%package -n python3-module-%oname
Summary: Module for creating simple ASCII tables (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
texttable is a module to generate a formatted text table, using ASCII characters.
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
%doc LICENSE
%python_sitelibdir/%oname.*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%oname.*
%python3_sitelibdir/*.egg-*
%python3_sitelibdir/__pycache__/*
%endif

%changelog
* Wed Jan 17 2018 Vladimir Didenko <cow@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Wed Jul 5 2017 Vladimir Didenko <cow@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Fri Apr 7 2017 Vladimir Didenko <cow@altlinux.ru> 0.8.8-alt1
- 0.8.8

* Fri Dec 16 2016 Vladimir Didenko <cow@altlinux.ru> 0.8.7-alt1
- 0.8.7

* Wed Oct 12 2016 Vladimir Didenko <cow@altlinux.ru> 0.8.5-alt1
- 0.8.5

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.4-alt1.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 8 2016 Vladimir Didenko <cow@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Mon Sep 14 2015 Vladimir Didenko <cow@altlinux.ru> 0.8.3-alt1
- 0.8.3
