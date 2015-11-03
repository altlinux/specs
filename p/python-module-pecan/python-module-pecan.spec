%define pypi_name pecan
%def_with python3

Name: python-module-%pypi_name
Version: 1.0.3
Release: alt1
Summary: A lean WSGI object-dispatching web framework
Group: Development/Python

License: BSD
Url: http://github.com/dreamhost/%pypi_name
Source0: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-webob >= 1.2
BuildRequires: python-module-simplegeneric >= 0.8
BuildRequires: python-module-mako >= 0.4.0
BuildRequires: python-module-singledispatch
BuildRequires: python-module-webtest >= 1.3.1
BuildRequires: python-module-argparse
BuildRequires: python-module-logutils

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-webob >= 1.2
BuildRequires: python3-module-simplegeneric >= 0.8
BuildRequires: python3-module-mako >= 0.4.0
BuildRequires: python3-module-singledispatch
BuildRequires: python3-module-webtest >= 1.3.1
BuildRequires: python3-module-argparse
BuildRequires: python3-module-logutils
%endif

%description
A WSGI object-dispatching web framework, designed to be lean and
fast with few dependencies

%if_with python3
%package -n python3-module-%pypi_name
Summary: A lean WSGI object-dispatching web framework
Group: Development/Python3

%description -n python3-module-%pypi_name
A WSGI object-dispatching web framework, designed to be lean and
fast with few dependencies
%endif

%prep
%setup

# Remove bundled egg-info
rm -rf %pypi_name.egg-info

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%python_build

%install
%if_with python3
pushd ../python3
%python3_install
mv %buildroot%_bindir/pecan \
   %buildroot%_bindir/pecan3
mv %buildroot%_bindir/gunicorn_pecan \
   %buildroot%_bindir/gunicorn_pecan3
popd
%endif

%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/testing.py
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/testing.py
rm -fr %buildroot%python3_sitelibdir/*/tests


%files
%doc LICENSE README.rst
%_bindir/pecan
%_bindir/gunicorn_pecan
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%pypi_name
%_bindir/pecan3
%_bindir/gunicorn_pecan3
%python3_sitelibdir/*
%endif


%changelog
* Fri Oct 30 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1
- 1.0.3
- add python3 package
- delete tests

* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 0.4.5-alt1
- First build for ALT (based on Fedora 0.4.5-4.fc21)

