%define mname xstatic
%define oname %mname-magic-search

%def_with python3
Name: python-module-%oname
Version: 0.2.5.1
Release: alt1.1.1
Group: Development/Python
Summary: Magic-Search (XStatic packaging standard)
License: ASL 2.0
Url: https://pypi.python.org/pypi/XStatic-Magic-Search

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-%mname
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-%mname
%endif

%py_provides %mname.pkg.magic_search
%py_requires %mname.pkg

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools-tests python-module-xstatic python3-module-setuptools-tests python3-module-xstatic rpm-build-python3

%description
MagicSearch is an AngularJS directive that provides a UI for both faceted
filtering and as-you-type filtering. It is intended for filtering tables,
such as an AngularJS smart-table, but it can be used in any situation
where you can provide it with facets/options and consume its events.

%if_with python3
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
%endif

%prep
%setup

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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
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
