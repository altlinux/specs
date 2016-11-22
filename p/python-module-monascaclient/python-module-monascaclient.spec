%def_with python3
%define sname monascaclient

Name:       python-module-%sname
Version:    1.2.0
Release:    alt1
Summary:    Python API and CLI for OpenStack Monasca
License:    ASL 2.0
URL:        http://pypi.python.org/pypi/python-%sname
Source:    %name-%version.tar
Group:      Development/Python

BuildArch:  noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-d2to1
BuildRequires: python-module-argparse
BuildRequires: python-module-requests >= 2.10.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-oslo.config >= 3.9.0
BuildRequires: python-module-oslo.concurrency >= 3.5.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.log >= 1.14.0
BuildRequires: python-module-oslo.middleware >= 3.0.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.service >= 1.0.0
BuildRequires: python-module-oslo.utils >= 3.5.0
BuildRequires: python-module-keystoneclient >= 1.7.0
BuildRequires: python-module-requests >= 2.5.2
BuildRequires: python-module-iso8601 >= 0.1.11
BuildRequires: python-module-prettytable  >= 0.7
BuildRequires: python-module-yaml >= 3.1.0



%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-argparse
BuildRequires: python3-module-requests >= 2.5.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-oslo.config >= 3.9.0
BuildRequires: python3-module-oslo.concurrency >= 3.5.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.log >= 1.14.0
BuildRequires: python3-module-oslo.middleware >= 3.0.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0
BuildRequires: python3-module-oslo.service >= 1.0.0
BuildRequires: python3-module-oslo.utils >= 3.5.0
BuildRequires: python3-module-keystoneclient >= 1.7.0
BuildRequires: python3-module-requests >= 2.5.2
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-prettytable  >= 0.7
BuildRequires: python3-module-yaml >= 3.1.0
%endif

%description
This is a client library for Monasca built to interface with the Monasca API. It
provides a Python API the monascaclient module and a command-line tool
monasca.

The Monasca Client was written using the OpenStack Heat Python client as a framework.

%if_with python3
%package -n python3-module-%sname
Summary:    Python API and CLI for OpenStack Monasca
Group: Development/Python3

%description -n python3-module-%sname
This is a client library for Monasca built to interface with the Monasca API. It
provides a Python API the monascaclient module and a command-line tool
monasca.

The Monasca Client was written using the OpenStack Heat Python client as a framework.
%endif

%package doc

Summary: Documentation for OpenStack Monasca API Client
Group:  Development/Documentation

%description doc
This is a client library for Monasca built to interface with the Monasca API. It
provides a Python API the monascaclient module and a command-line tool
monasca.

%prep
%setup

# Let RPM handle the dependencies
rm -f {,test-}requirements.txt

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
mv %buildroot%_bindir/monasca %buildroot%_bindir/python3-monasca
%endif

%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests


# Build HTML docs and man page
#export PYTHONPATH="$( pwd ):$PYTHONPATH"
#sphinx-build -b html doc/source html

# Fix hidden-file-or-dir warnings
#rm -fr html/.doctrees html/.buildinfo

%files
%doc LICENSE README.rst
%_bindir/monasca
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%_bindir/python3-monasca
%python3_sitelibdir/*
%endif

#%files doc
#%doc LICENSE html

%changelog
* Tue Nov 22 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- Initial release for Sisyphus
