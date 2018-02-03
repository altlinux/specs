
Name:           python-module-django-openstack-auth
Version:        3.1.1
Release:        alt1.1
Summary:        Django authentication backend for OpenStack Keystone
Group:          Development/Python

License:        BSD
URL:            http://pypi.python.org/pypi/django_openstack_auth/
Source0:        django_openstack_auth-%version.tar.gz

BuildArch:      noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-django >= 1.8
BuildRequires: python-module-oslo.config >= 3.14.0
BuildRequires: python-module-oslo.policy >= 1.17.0
BuildRequires: python-module-keystoneclient >= 3.8.0
BuildRequires: python-module-keystoneauth1 >= 2.18.0

BuildRequires: python-module-django-dbbackend-sqlite3

Requires: python-module-django
Requires: python-module-oslo.config >= 3.14.0
Requires: python-module-oslo.policy >= 1.17.0
Requires: python-module-keystoneclient >= 3.8.0
Requires: python-module-keystoneauth1 >= 2.18.0

%description
Django OpenStack Auth is a pluggable Django authentication backend that
works with Django's ``contrib.auth`` framework to authenticate a user against
OpenStack's Keystone Identity API.

The current version is designed to work with the
Keystone V2 API.


%package tests
Summary: Tests for Django authentication backend for OpenStack Keystone
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for Django authentication backend for OpenStack Keystone.

%prep
%setup -n django_openstack_auth-%version

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -f {test-,}requirements.txt

%build
# generate translations
cd openstack_auth && django-admin compilemessages && cd ..

# remove unnecessary .po files
find . -name "django.po" -exec rm -f '{}' \;

%python_build

# generate html docs
PYTHONPATH=.:$PYTHONPATH sphinx-build doc/source html

%install
%python_install

cp -r openstack_auth/locale %buildroot%python_sitelibdir/openstack_auth

%find_lang django

# %check
# %{__python} setup.py test

%files -f django.lang
%doc LICENSE
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jun 01 2017 Alexey Shabalin <shaba@altlinux.ru> 3.1.1-alt1
- 3.1.1
- add tests package

* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 2.4.2-alt1
- 2.4.2

* Mon Oct 24 2016 Alexey Shabalin <shaba@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Tue Apr 19 2016 Alexey Shabalin <shaba@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Thu Nov 05 2015 Alexey Shabalin <shaba@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Tue Oct 13 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- 1.2.0
- add patches from fedora

* Wed Apr 01 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.9-alt2.post42
- upstream snapshot

* Tue Mar 17 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.9-alt1
- 1.1.9

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 1.1.5-alt1
- New version (based on Fedora 1.1.5-3.fc21.src)

* Mon Aug 26 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0.11-alt2
- cleanup spec

* Mon Jul 15 2013 Pavel Shilovsky <piastry@altlinux.org> 1.0.11-alt1
- Initial release for Sisyphus (based on Fedora)

