%def_with python3

Name:       python-module-keystoneclient
Version:    1.7.2
Release:    alt1
Summary:    Client library for OpenStack Identity API
License:    ASL 2.0
URL:        http://pypi.python.org/pypi/%{name}
Source:    %name-%version.tar
Group:      Development/Python

BuildArch:  noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-d2to1
BuildRequires: python-module-argparse
BuildRequires: python-module-iso8601 >= 0.1.9
BuildRequires: python-module-prettytable >= 0.7
BuildRequires: python-module-requests >= 2.5.2
BuildRequires: python-module-oslo.config >= 2.3.0
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-oslo.serialization >= 1.4.0
BuildRequires: python-module-oslo.utils >= 2.0.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-netaddr >= 0.7.12
BuildRequires: python-module-babel >= 1.3
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-stevedore >= 1.5.0
BuildRequires: python-module-debtcollector >= 0.3.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-argparse
BuildRequires: python3-module-iso8601 >= 0.1.9
BuildRequires: python3-module-prettytable >= 0.7
BuildRequires: python3-module-requests >= 2.5.0
BuildRequires: python3-module-oslo.config >= 2.3.0
BuildRequires: python3-module-oslo.i18n >= 1.5.0
BuildRequires: python3-module-oslo.serialization >= 1.4.0
BuildRequires: python3-module-oslo.utils >= 2.0.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-netaddr >= 0.7.12
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-stevedore >= 1.5.0
BuildRequires: python3-module-debtcollector >= 0.3.0
%endif

%description
Client library and command line utility for interacting with Openstack
Identity API.

%if_with python3
%package -n python3-module-keystoneclient
Summary:    Client library for OpenStack Identity API
Group: Development/Python3

%description -n python3-module-keystoneclient
Client library and command line utility for interacting with Openstack
Identity API.
%endif

%package doc
Summary:    Documentation for OpenStack Identity API Client
Group:  Development/Documentation

%description doc
Documentation for the client library for interacting with Openstack
Identity API.

%prep
%setup

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

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
mv %buildroot%_bindir/keystone %buildroot%_bindir/python3-keystone
%endif

%python_install
install -p -D -m 644 tools/keystone.bash_completion %buildroot%_sysconfdir/bash_completion.d/keystone.bash_completion

# Delete tests
rm -fr %buildroot%python_sitelibdir/keystoneclient/tests
rm -fr %buildroot%python3_sitelibdir/keystoneclient/tests


# Build HTML docs and man page
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html
sphinx-build -b man doc/source man
install -p -D -m 644 man/keystone.1 %buildroot%_man1dir/keystone.1

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%files
%doc LICENSE README.rst
%_bindir/keystone
%_sysconfdir/bash_completion.d/keystone.bash_completion
%python_sitelibdir/*
%_man1dir/keystone.1*

%if_with python3
%files -n python3-module-keystoneclient
%_bindir/python3-keystone
%python3_sitelibdir/*
%endif

%files doc
%doc LICENSE html

%changelog
* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Fri Mar 06 2015 Alexey Shabalin <shaba@altlinux.ru> 0.11.2-alt1
- 0.11.2
- add python3 package

* Mon Jul 21 2014 Lenar Shakirov <snejok@altlinux.ru> 0.9.0-alt1
- New build for ALT (based on Fedora 0.9.0-2.fc21.src)

* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 0.1.2-alt1
- Initial release for Sisyphus (based on Fedora)

