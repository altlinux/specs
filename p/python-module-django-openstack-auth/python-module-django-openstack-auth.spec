
Name:           python-module-django-openstack-auth
Version:        2.4.2
Release:        alt1
Summary:        Django authentication backend for OpenStack Keystone
Group:          Development/Python

License:        BSD
URL:            http://pypi.python.org/pypi/django_openstack_auth/
Source0:        %name-%version.tar

BuildArch:      noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-django >= 1.8
BuildRequires: python-module-oslo.config >= 3.14.0
BuildRequires: python-module-oslo.policy >= 1.9.0
BuildRequires: python-module-keystoneclient >= 2.0.0
BuildRequires: python-module-keystoneauth1 >= 2.10.0

BuildRequires: python-module-django-dbbackend-sqlite3

Requires: python-module-django
Requires: python-module-oslo.config >= 3.14.0
Requires: python-module-oslo.policy >= 1.9.0
Requires: python-module-keystoneclient >= 2.0.0
Requires: python-module-keystoneauth1 >= 2.10.0

%description
Django OpenStack Auth is a pluggable Django authentication backend that
works with Django's ``contrib.auth`` framework to authenticate a user against
OpenStack's Keystone Identity API.

The current version is designed to work with the
Keystone V2 API.

%prep
%setup

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

# don't include tests in the RPM
rm -rf %buildroot/%python_sitelibdir/openstack_auth/tests
# 
# %check
# %{__python} setup.py test

%files -f django.lang
%doc LICENSE
%python_sitelibdir/*

%changelog
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

