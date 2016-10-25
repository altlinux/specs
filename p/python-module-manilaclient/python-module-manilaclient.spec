%def_with python3
%define sname manilaclient

Name:       python-module-%sname
Version:    1.11.0
Release:    alt1
Summary:    Client Library for OpenStack Manila shared file system service API
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
BuildRequires: python-module-reno
BuildRequires: python-module-oslo.config >= 3.14.0
BuildRequires: python-module-oslo.log >= 1.14.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.utils >= 3.16.0
BuildRequires: python-module-prettytable >= 0.7
BuildRequires: python-module-requests >= 2.10.0
BuildRequires: python-module-simplejson >= 2.2.0
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-keystoneclient >= 2.0.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-requests >= 2.10.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-keystoneclient >= 2.0.0
BuildRequires: python3-module-oslo.config >= 3.14.0
BuildRequires: python3-module-oslo.log >= 1.14.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0
BuildRequires: python3-module-oslo.utils >= 3.16.0
BuildRequires: python3-module-prettytable >= 0.7
BuildRequires: python3-module-simplejson >= 2.2.0
%endif

%description
There is a Python library for accessing the API (manilaclient module),
and a command-line script (manilac).

%if_with python3
%package -n python3-module-%sname
Summary:    Client Library for OpenStack  Manila shared file system service API
Group: Development/Python3

%description -n python3-module-%sname
Client library and command line utility for interacting with Openstack
Manila API.
%endif

%package doc

Summary:    Documentation for OpenStack  Manila shared file system service API
Group:  Development/Documentation

%description doc
Documentation for the client library for interacting with Openstack
Manila shared file system service API.

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
mv %buildroot%_bindir/manila %buildroot%_bindir/python3-manila
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
%_bindir/manila
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%_bindir/python3-manila
%python3_sitelibdir/*
%endif

%files doc
%doc LICENSE html

%changelog
* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- Initial release for Sisyphus
