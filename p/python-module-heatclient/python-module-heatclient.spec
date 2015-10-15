%def_with python3

Name: python-module-heatclient
Version: 0.4.0
Release: alt1
Summary: Python API and CLI for OpenStack Heat

Group: Development/Python
License: ASL 2.0
Url: http://pypi.python.org/pypi/python-heatclient
Source0: %name-%version.tar

#
# patches_base=0.2.9
#
Patch0001: 0001-Nuke-pbr-requirements-handling.patch
Patch0002: 0002-Remove-runtime-dependency-on-python-pbr.patch

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr
BuildRequires: python-module-d2to1
BuildRequires: python-module-argparse
BuildRequires: python-module-iso8601 >= 0.1.9
BuildRequires: python-module-prettytable >= 0.7
BuildRequires: python-module-requests >= 2.2.0
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-oslo.serialization >= 1.4.0
BuildRequires: python-module-oslo.utils >= 1.4.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-keystoneclient >= 1.1.0
BuildRequires: python-module-swiftclient >= 2.2.0
BuildRequires: python-module-yaml >= 3.1.0
BuildRequires: python-module-babel >= 1.3
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-argparse
BuildRequires: python3-module-iso8601 >= 0.1.9
BuildRequires: python3-module-prettytable >= 0.7
BuildRequires: python3-module-requests >= 2.2.0
BuildRequires: python3-module-oslo.i18n >= 1.3.0
BuildRequires: python3-module-oslo.serialization >= 1.4.0
BuildRequires: python3-module-oslo.utils >= 1.4.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-keystoneclient >= 1.1.0
BuildRequires: python3-module-swiftclient >= 2.2.0
BuildRequires: python3-module-yaml >= 3.1.0
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
%endif


%description
This is a client for the OpenStack Heat API. There's a Python API (the
heatclient module), and a command-line script (heat). Each implements 100 percent of
the OpenStack Heat API.

%if_with python3
%package -n python3-module-heatclient
Summary:    Python API and CLI for OpenStack Heat
Group: Development/Python3

%description -n python3-module-heatclient
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

%patch0001 -p1
%patch0002 -p1

# We provide version like this in order to remove runtime dep on pbr.
sed -i s/REDHATHEATCLIENTVERSION/%version/ heatclient/__init__.py

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
%files -n python3-module-heatclient
%_bindir/python3-heat
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Wed Mar 11 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt1
- 0.3.0
- add python package

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 0.2.9-alt1
- First build for ALT (based on Fedora 0.2.9-1.fc21.src)

