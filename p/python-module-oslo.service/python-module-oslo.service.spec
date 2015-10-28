%global pypi_name oslo.service

%def_with python3

Name: python-module-%pypi_name
Version: 0.9.0
Release: alt1
Summary: Oslo service library
Group: Development/Python
License: ASL 2.0
Url: http://launchpad.net/oslo
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.3
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-oslo-i18n
BuildRequires: python-module-oslo.utils >= 2.0.0
BuildRequires: python-module-oslo.concurrency >= 2.3.0
BuildRequires: python-module-oslo.config >= 2.3.0
BuildRequires: python-module-oslo.log >= 1.8.0
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-paste
BuildRequires: python-module-PasteDeploy >= 1.5.0
BuildRequires: python-module-eventlet >= 0.17.4
BuildRequires: python-module-greenlet >= 0.3.2
BuildRequires: python-module-monotonic >= 0.3
BuildRequires: python-module-six >= 1.9.0

%description
Library for running OpenStack services


%if_with python3
%package -n python3-module-%pypi_name
Summary: Oslo service library
Group: Development/Python3

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.3
BuildRequires: python3-module-oslo-i18n
BuildRequires: python3-module-oslo.utils >= 2.0.0
BuildRequires: python3-module-oslo.concurrency >= 2.3.0
BuildRequires: python3-module-oslo.config >= 2.3.0
BuildRequires: python3-module-oslo.log >= 1.8.0
BuildRequires: python3-module-oslo.i18n >= 1.5.0
BuildRequires: python3-module-paste
BuildRequires: python3-module-PasteDeploy >= 1.5.0
BuildRequires: python3-module-eventlet >= 0.17.4
BuildRequires: python3-module-greenlet >= 0.3.2
BuildRequires: python3-module-monotonic >= 0.3
BuildRequires: python3-module-six >= 1.9.0

%description -n python3-module-%pypi_name
Library for running OpenStack services
%endif

%package doc
Summary: Oslo service documentation
Group: Development/Documentation
%description doc
Documentation for oslo.service


%prep
%setup
# Remove bundled egg-info
rm -rf %pypi_name.egg-info
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
popd
%endif
%python_install

rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc README.rst
%python_sitelibdir/oslo*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%pypi_name
%doc README.rst
%python3_sitelibdir/oslo*
%python3_sitelibdir/*.egg-info
%endif

%files doc
%doc html

%changelog
* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 0.9.0-alt1
- Initial package.
