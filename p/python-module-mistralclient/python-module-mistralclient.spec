%def_with python3
%define sname mistralclient

Name:       python-module-%sname
Version:    2.1.1
Release:    alt1
Summary:    Client Library for OpenStack Mistral Workflow Service API
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
BuildRequires: python-module-keystoneclient >= 2.0.0
BuildRequires: python-module-requests >= 2.5.2
BuildRequires: python-module-cliff >= 1.15.0
BuildRequires: python-module-osc-lib >= 1.0.2
BuildRequires: python-module-oslo.utils >= 3.16.0
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
BuildRequires: python3-module-keystoneclient >= 1.6.0
BuildRequires: python3-module-requests >= 2.5.2
BuildRequires: python3-module-cliff >= 1.14.0
BuildRequires: python3-module-osc-lib >= 1.0.2
BuildRequires: python3-module-oslo.utils >= 3.16.0
BuildRequires: python3-module-yaml >= 3.1.0
%endif

%description
There is a Python library for accessing the API (mistralclient module),
and a command-line script (mistral).

%if_with python3
%package -n python3-module-%sname
Summary:    Client Library for OpenStack Mistral Workflow Service API
Group: Development/Python3

%description -n python3-module-%sname
Client library and command line utility for interacting with Openstack
MistralAPI.
%endif

%package doc

Summary: Documentation for OpenStack Mistral Workflow Service API
Group:  Development/Documentation

%description doc
Documentation for the client library for interacting with Openstack
Mistral Workflow Service API.

%prep
%setup

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

# Remove bundled egg-info
rm -rf *.egg-info
# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

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
mv %buildroot%_bindir/mistral %buildroot%_bindir/python3-mistral
%endif

%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests


# Build HTML docs and man page
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%files
%doc LICENSE README.rst
%_bindir/mistral
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%_bindir/python3-mistral
%python3_sitelibdir/*
%endif

%files doc
%doc LICENSE html

%changelog
* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- Initial release for Sisyphus
