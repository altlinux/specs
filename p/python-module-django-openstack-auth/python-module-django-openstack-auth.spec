
Name:           python-module-django-openstack-auth
Version:        1.1.9
Release:        alt2.post42
Summary:        Django authentication backend for OpenStack Keystone
Group:          Development/Python

License:        BSD
URL:            http://pypi.python.org/pypi/django_openstack_auth/
Source0:        %name-%version.tar
Patch0:         0001-remove-runtime-dep-to-python-pbr.patch
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
 
Requires:       python-module-keystoneclient

%description
Django OpenStack Auth is a pluggable Django authentication backend that
works with Django's ``contrib.auth`` framework to authenticate a user against
OpenStack's Keystone Identity API.

The current version is designed to work with the
Keystone V2 API.

%prep
%setup
%patch0 -p1

# remove unnecessary .po files
find . -name "django.po" -exec rm -f '{}' \;

sed -i s/RPMVERSION/%{version}/ openstack_auth/__init__.py

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -f {test-,}requirements.txt

%build
%python_build

# generate html docs
PYTHONPATH=.:$PYTHONPATH sphinx-build doc/source html

%install
%python_install

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

