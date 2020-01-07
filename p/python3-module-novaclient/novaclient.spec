%define oname novaclient

Name: python3-module-%oname
Version: 16.0.0
Release: alt1

Summary: Python API and CLI for OpenStack Nova

Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/python-%oname

Source: https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch: noarch

Requires: python3-module-simplejson >= 3.5.1
Requires: python3-module-keystoneclient

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-keystoneauth1 >= 3.5.0
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-prettytable >= 0.7.2
BuildRequires: python3-module-simplejson >= 3.5.1
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-babel >= 2.3.4

BuildRequires: python3-module-keystoneclient >= 3.8.0
BuildRequires: python3-module-cinderclient >= 3.3.0
BuildRequires: python3-module-glanceclient >= 2.8.0
BuildRequires: python3-module-neutronclient >= 6.7.0

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-sphinxcontrib-apidoc

%description
This is a client for the OpenStack Nova API. There's a Python API (the
novaclient module), and a command-line script (nova). Each implements 100 percent of
the OpenStack Nova API.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Nova API Client
Group: Development/Documentation

%description doc
This is a client for the OpenStack Nova API. There's a Python API (the
novaclient module), and a command-line script (nova). Each implements 100 percent of
the OpenStack Nova API.

This package contains auto-generated documentation.

%prep
%setup -n python-%oname-%version

# Remove bundled egg-info
rm -rf python_novaclient.egg-info

# Let RPM handle the requirements
rm -f {,test-}requirements.txt

# Prevent doc build warnings from causing a build failure
sed -i '/warning-is-error/d' setup.cfg

%build
%python3_build

python3 setup.py build_sphinx
python3 setup.py build_sphinx -b html
python3 setup.py build_sphinx -b man
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%python3_install

mkdir -p %buildroot%_sysconfdir/bash_completion.d
install -pm 644 tools/nova.bash_completion \
    %buildroot%_sysconfdir/bash_completion.d/nova

#install -p -D -m 644 doc/build/man/nova.1 %buildroot%_man1dir/nova.1

%files
%doc README.rst
%doc LICENSE
%_bindir/nova
#%%_man1dir/nova.*
%_sysconfdir/bash_completion.d
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc build/sphinx/html build/sphinx/man

%changelog
* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 16.0.0-alt1
- Automatically updated to 16.0.0.
- Added watch file.
- Renamed spec file.

* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 15.1.0-alt1
- Automatically updated to 15.1.0.
- Build without python2.

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 11.0.0-alt1
- Updated to 11.0.0.

* Mon Mar 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 7.1.2-alt2
- Updated build dependencies.

* Thu Jun 22 2017 Alexey Shabalin <shaba@altlinux.ru> 7.1.2-alt1
- 7.1.2

* Tue May 30 2017 Alexey Shabalin <shaba@altlinux.ru> 7.1.1-alt1
- 7.1.1

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 6.0.0-alt1
- 6.0.0

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 3.3.1-alt1
- 3.3.1

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 2.30.2-alt1
- 2.30.2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.30.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.30.1-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 2.30.1-alt1
- 2.30.1

* Fri Oct 02 2015 Alexey Shabalin <shaba@altlinux.ru> 2.23.2-alt2
- drop Requires: python-module-keyring

* Tue Aug 25 2015 Alexey Shabalin <shaba@altlinux.ru> 2.23.2-alt1
- 2.23.2

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 2.23.0-alt1
- 2.23.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- 2.22.0
- add python3 package

* Thu Jul 24 2014 Lenar Shakirov <snejok@altlinux.ru> 2.17.0-alt1
- New version (based on Fedora 2.17.0-2.fc21.src)

* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 2.8.0.26-alt1
- Initial release for Sisyphus (based on Fedora)

