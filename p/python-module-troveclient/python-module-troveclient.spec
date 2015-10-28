%def_with python3

Name: python-module-troveclient
Version: 1.3.0
Release: alt1
Summary: Client library for OpenStack DBaaS API
Group: Development/Python

License: ASL 2.0
Url: http://www.openstack.org/
Source0: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-d2to1
BuildRequires: python-module-argparse
BuildRequires: python-module-prettytable >= 0.7
BuildRequires: python-module-requests >= 2.5.2
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-oslo.utils >= 2.0.0
BuildRequires: python-module-keystoneclient >= 1.6.0
BuildRequires: python-module-simplejson >= 2.2.0
BuildRequires: python-module-babel >= 1.3
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-argparse
BuildRequires: python3-module-prettytable >= 0.7
BuildRequires: python3-module-requests >= 2.5.2
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-oslo.utils >= 2.0.0
BuildRequires: python3-module-keystoneclient >= 1.6.0
BuildRequires: python3-module-simplejson >= 2.2.0
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
%endif


%description
This is a client for the Trove API. There's a Python API (the
troveclient module), and a command-line script (trove). Each
implements 100 percent (or less ;) ) of the Trove API.

%if_with python3
%package -n python3-module-troveclient
Summary:   Client library for OpenStack DBaaS API
Group: Development/Python3

%description -n python3-module-troveclient
This is a client for the Trove API. There's a Python API (the
troveclient module), and a command-line script (trove). Each
implements 100 percent (or less ;) ) of the Trove API.
%endif

%package doc
Summary: Documentation for OpenStack DBaaS API
Group: Development/Documentation

%description doc
This is a client for the Trove API. There's a Python API (the
troveclient module), and a command-line script (trove). Each
implements 100 percent (or less ;) ) of the Trove API.

This package contains auto-generated documentation.


%prep
%setup

# Remove bundled egg-info
rm -rf %name.egg-info

# Let RPM handle the requirements
rm -f {test-,}requirements.txt

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
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/trove %buildroot%_bindir/python3-trove
%endif

%python_install
# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python_sitelibdir/*/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/*/tests

sphinx-build -b html doc/source html

# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%files
%doc README.rst LICENSE
%python_sitelibdir/*
%_bindir/trove

%if_with python3
%files -n python3-module-troveclient
%_bindir/python3-trove
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Tue Nov 03 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Wed Mar 11 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.8-alt1
- 1.0.8
- add python3 package

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.5-alt1
- First build for ALT (based on Fedora 1.0.5-1.fc21.src)

