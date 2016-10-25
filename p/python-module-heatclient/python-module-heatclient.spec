%def_with python3
%define sname heatclient

Name: python-module-%sname
Version: 1.5.0
Release: alt1
Summary: Python API and CLI for OpenStack Heat

Group: Development/Python
License: ASL 2.0
Url: http://pypi.python.org/pypi/python-%sname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-cliff >= 1.15.0
BuildRequires: python-module-iso8601 >= 0.1.11
BuildRequires: python-module-osc-lib >= 1.0.2
BuildRequires: python-module-prettytable >= 0.7
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.utils >= 3.16.0
BuildRequires: python-module-keystoneauth1 >= 2.10.0
BuildRequires: python-module-swiftclient >= 2.2.0
BuildRequires: python-module-yaml >= 3.1.0
BuildRequires: python-module-requests >= 2.10.0
BuildRequires: python-module-six >= 1.9.0


BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-cliff >= 1.15.0
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-osc-lib >= 1.0.2
BuildRequires: python3-module-prettytable >= 0.7
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0
BuildRequires: python3-module-oslo.utils >= 3.16.0
BuildRequires: python3-module-keystoneauth1 >= 2.10.0
BuildRequires: python3-module-swiftclient >= 2.2.0
BuildRequires: python3-module-yaml >= 3.1.0
BuildRequires: python3-module-requests >= 2.10.0
BuildRequires: python3-module-six >= 1.9.0
%endif

%description
This is a client for the OpenStack Heat API. There's a Python API (the
heatclient module), and a command-line script (heat). Each implements 100 percent of
the OpenStack Heat API.

%if_with python3
%package -n python3-module-%sname
Summary:    Python API and CLI for OpenStack Heat
Group: Development/Python3

%description -n python3-module-%sname
This is a client for the OpenStack Heat API. There's a Python API (the
heatclient module), and a command-line script (heat). Each implements 100 percent of
the OpenStack Heat API.
%endif

%package doc
Summary: Documentation for OpenStack Heat API Client
Group: Development/Documentation

%description doc
This is a client for the OpenStack Heat API. There's a Python API (the
heatclient module), and a command-line script (heat). Each implements 100 percent of
the OpenStack Heat API.

This package contains auto-generated documentation.

%prep
%setup

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config.
rm -rf {test-,}requirements.txt tools/{pip,test}-requires
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
mv %buildroot%_bindir/heat %buildroot%_bindir/python3-heat
%endif

%python_install
echo "%version" > %buildroot%python_sitelibdir/heatclient/versioninfo
echo "%version" > %buildroot%python3_sitelibdir/heatclient/versioninfo

# Delete tests
rm -fr %buildroot%python_sitelibdir/heatclient/tests
rm -fr %buildroot%python3_sitelibdir/heatclient/tests

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%files
%doc LICENSE README.rst
%_bindir/heat
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%_bindir/python3-heat
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Nov 03 2015 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Wed Mar 11 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt1
- 0.3.0
- add python package

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 0.2.9-alt1
- First build for ALT (based on Fedora 0.2.9-1.fc21.src)

