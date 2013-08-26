%global		pypi_name django_openstack_auth

Name:		python-module-django-openstack-auth
Version:	1.0.11
Release:	alt2

Summary:	Django authentication backend for OpenStack Keystone

Group:		Development/Python
License:	BSD
URL:		http://pypi.python.org/pypi/django_openstack_auth/1.0.11

BuildArch:	noarch

Source0:	%name-%version.tar

BuildRequires:	python-devel
BuildRequires:	python-module-sphinx
BuildRequires:	python-module-mox
BuildRequires:	python-module-keystoneclient
BuildRequires:	python-module-iso8601
BuildRequires:	python-module-django1.4

Requires:	python-module-django1.4
Requires:	python-module-keystoneclient

%description
Django OpenStack Auth is a pluggable Django authentication backend that
works with Django's ``contrib.auth`` framework to authenticate a user
against OpenStack's Keystone Identity API.

The current version is designed to work with the Keystone V2 API.

%prep
%setup
# Remove bundled egg-info
rm -rf %pypi_name.egg-info

# remove unnecessary .po files
find . -name "django.po" -exec rm -f '{}' \;

#sed -i 's/SECERT_KEY/SECRET_KEY/' openstack_auth/tests/settings.py

%build
%python_build

# generate html docs
PYTHONPATH=.:$PYTHONPATH sphinx-build docs html

%install
%python_install

%find_lang django

# don't include tests in the RPM
rm -rf %buildroot/%python_sitelibdir/openstack_auth/tests

#%check
#python setup.py test

%files -f django.lang
%doc README.rst LICENSE
%python_sitelibdir/openstack_auth/
%python_sitelibdir/%pypi_name-%version-py?.?.egg-info

%changelog
* Mon Aug 26 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0.11-alt2
- cleanup spec

* Mon Jul 15 2013 Pavel Shilovsky <piastry@altlinux.org> 1.0.11-alt1
- Initial release for Sisyphus (based on Fedora)
