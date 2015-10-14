
Name:           python-module-django-openstack-auth
Version:        1.2.0
Release:        alt1
Summary:        Django authentication backend for OpenStack Keystone
Group:          Development/Python

License:        BSD
URL:            http://pypi.python.org/pypi/django_openstack_auth/
Source0:        %name-%version.tar

Patch0001: 0001-remove-runtime-dep-to-python-pbr.patch
Patch0002: 0002-Set-default-value-for-new-token-attributes.patch
Patch0003: 0003-Add-missing-_-import-to-plugin-base.py.patch
Patch0004: 0004-Prepend-WEBROOT-to-redirect-URL-for-WebSSO.patch
Patch0005: 0005-Fix-Login-form-s-fields-sorting-for-Django-1.7.patch
Patch0006: 0006-Use-unscoped-token-for-scoping-to-project.patch
Patch0007: 0007-Configurable-token-hashing.patch
Patch0008: 0008-Extend-User-from-AbstractBaseUser-and-AnonymousUser.patch
Patch0009: 0009-initialize-the-hasher-for-unscoped-token.patch
Patch0010: 0010-Replace-default-User-model-PK.patch
Patch0011: 0011-doa-does-not-work-with-mysql.patch

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-module-setuptools
BuildRequires:  python-module-sphinx
BuildRequires:  python-module-oslosphinx
BuildRequires:  python-module-six >= 1.9.0
BuildRequires:  python-module-keystoneclient >= 1.1.0
BuildRequires:  python-module-pbr >= 0.6
BuildRequires:  python-module-oslo.config >= 1.9.3

Requires:   python-module-django
BuildRequires:   python-module-django
 
Requires: python-module-keystoneclient

%description
Django OpenStack Auth is a pluggable Django authentication backend that
works with Django's ``contrib.auth`` framework to authenticate a user against
OpenStack's Keystone Identity API.

The current version is designed to work with the
Keystone V2 API.

%prep
%setup
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1
%patch0009 -p1
%patch0010 -p1
%patch0011 -p1


# Remove bundled egg-info
rm -rf django_openstack_auth.egg-info

sed -i s/RPMVERSION/%{version}/ openstack_auth/__init__.py

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

