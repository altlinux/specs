%define sname oslo.policy

%def_with python3

Name: python-module-%sname
Version: 1.14.0
Release: alt1
Summary: RBAC policy enforcement library for OpenStack
Group: Development/Python
License: ASL 2.0
Url: http://launchpad.net/oslo.policy
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-requests >= 2.10.0
BuildRequires: python-module-oslo.config >= 3.14.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.utils >= 3.16.0
BuildRequires: python-module-six >= 1.9.0

BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-requests >= 2.10.0
BuildRequires: python3-module-oslo.config >= 3.14.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0
BuildRequires: python3-module-oslo.utils >= 3.16.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
%endif

%description
RBAC policy enforcement library for OpenStack

%if_with python3
%package -n python3-module-%sname
Summary: RBAC policy enforcement library for OpenStack
Group: Development/Python3

%description -n python3-module-%sname
RBAC policy enforcement library for OpenStack

%endif


%package doc
Summary: Documentation for the Oslo policy handling library
Group: Development/Documentation

%description doc
Documentation for the Oslo policy handling library.

%prep
%setup

# Remove bundled egg-info
#rm -rf %sname.egg-info

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

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%if_with python3
pushd ../python3
%python3_install
for bin_files in oslopolicy-list-redundant oslopolicy-policy-generator oslopolicy-sample-generator oslopolicy-checker; do
    mv %buildroot%_bindir/$bin_files %buildroot%_bindir/python3-$bin_files
done
popd
%endif
%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc CONTRIBUTING.rst HACKING.rst LICENSE PKG-INFO README.rst
%python_sitelibdir/*
%_bindir/*
%exclude %_bindir/python3-*

%if_with python3
%files -n python3-module-%sname
%python3_sitelibdir/*
%_bindir/python3-*
%endif

%files doc
%doc html

%changelog
* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.14.0-alt1
- 1.14.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.11.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 0.11.0-alt1
- 0.11.0

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- Initial release
