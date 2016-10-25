%define sname osprofiler

%def_with python3

Name: python-module-%sname
Version: 1.4.0
Release: alt1
Summary: OpenStack cross-project profiling library
Group: Development/Python
License: ASL 2.0
Url: https://github.com/openstack/%sname
Source: %name-%version.tar

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-oslo.messaging >= 5.2.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-oslo.utils >= 3.4.0
BuildRequires: python-module-webob >= 1.2.3
BuildRequires: python-module-oslo.config >= 3.2.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-oslo.messaging >= 5.2.0
BuildRequires: python3-module-oslo.utils >= 3.4.0
BuildRequires: python3-module-webob >= 1.2.3
BuildRequires: python3-module-oslo.config >= 3.2.0
%endif

BuildArch: noarch

%description
OSProfiler is an OpenStack cross-project profiling library.

%if_with python3
%package -n python3-module-%sname
Summary: OpenStack cross-project profiling library
Group: Development/Python3

%description -n python3-module-%sname
OSProfiler is an OpenStack cross-project profiling library.
%endif


%package doc
Summary: Documentation for OpenStack cross-project profiling library
Group: Development/Documentation

%description doc
Documentation for OSProfiler is an OpenStack cross-project profiling library.

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

# disabling git call for last modification date from git repo
sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py
python setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%if_with python3
pushd ../python3
%python3_install
mv %buildroot%_bindir/%sname %buildroot%_bindir/python3-%sname
popd
%endif
%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc AUTHORS ChangeLog LICENSE PKG-INFO README.rst
%python_sitelibdir/*
%_bindir/%sname

%if_with python3
%files -n python3-module-%sname
%python3_sitelibdir/*
%_bindir/python3-%sname
%endif

%files doc
%doc doc/build/html

%changelog
* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Mar 12 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt1
- Initial release
