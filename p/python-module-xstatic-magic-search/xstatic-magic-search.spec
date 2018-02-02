%define mname xstatic
%define oname %mname-magic-search
%define pypi_name XStatic-Magic-Search

%def_with python3
Name: python-module-%oname
Version: 0.2.5.1
Release: alt2.1
Group: Development/Python
Summary: Magic-Search (XStatic packaging standard)
License: ASL 2.0
Url: https://pypi.python.org/pypi/%pypi_name/
Source: %pypi_name-%version.tar.gz
BuildArch: noarch

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-%mname
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-%mname
%endif

%py_provides %mname.pkg.magic_search
%py_requires %mname.pkg

%description
MagicSearch is an AngularJS directive that provides a UI for both faceted
filtering and as-you-type filtering. It is intended for filtering tables,
such as an AngularJS smart-table, but it can be used in any situation
where you can provide it with facets/options and consume its events.

%package -n python3-module-%oname
Summary: Magic-Search (XStatic packaging standard)
Group: Development/Python3
%py3_provides %mname.pkg.magic_search
%py3_requires %mname.pkg

%description -n python3-module-%oname
MagicSearch is an AngularJS directive that provides a UI for both faceted
filtering and as-you-type filtering. It is intended for filtering tables,
such as an AngularJS smart-table, but it can be used in any situation
where you can provide it with facets/options and consume its events.

%prep
%setup -n %pypi_name-%version

%if_with python3
cp -fR . ../python3
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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt
%python_sitelibdir/%mname/pkg/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/*.pth

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/%mname/pkg/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/*.pth
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.5.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 14 2017 Alexey Shabalin <shaba@altlinux.ru> 0.2.5.1-alt2
- build as noarch

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.5.1-alt1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.5.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.5.1-alt1.1
- NMU: Use buildreq for BR.

* Thu Nov 05 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2.5.1-alt1
- 0.2.5.1
- update spec as other ALTLinux python-module-xstatic packages

* Wed Sep 09 2015 Lenar Shakirov <snejok@altlinux.ru> 0.2.0.1-alt1
- First build for ALT (based on Fedora 0.2.0.1-2.fc23.src)
