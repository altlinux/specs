%global pypi_name django_openstack_auth

Name:           python-module-django-openstack-auth
Version:        1.1.5
Release:        alt1
Summary:        Django authentication backend for OpenStack Keystone
Group:          Development/Python

License:        BSD
URL:            http://pypi.python.org/pypi/django_openstack_auth/
Source0:        %{name}-%{version}.tar
Patch0:         0001-remove-runtime-dep-to-python-pbr.patch
BuildArch:      noarch
 
BuildRequires:  python-devel
BuildRequires:  python-module-setuptools
BuildRequires:  python-module-sphinx
BuildRequires:  python-module-mox
BuildRequires:  python-module-keystoneclient
BuildRequires:  python-module-iso8601
BuildRequires:  python-module-pbr
BuildRequires:  python-module-netaddr
BuildRequires:  python-module-oslo-sphinx

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
# Remove bundled egg-info
# rm -rf %{pypi_name}.egg-info

# remove unnecessary .po files
find . -name "django.po" -exec rm -f '{}' \;

sed -i s/RPMVERSION/%{version}/ openstack_auth/__init__.py

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -f {test-,}requirements.txt

# make doc build compatible with python-oslo-sphinx RPM
sed -i 's/oslosphinx/oslo.sphinx/' doc/source/conf.py

%build
%python_build

# generate html docs
PYTHONPATH=.:$PYTHONPATH sphinx-build doc/source html

%install
%python_install

%find_lang django

# don't include tests in the RPM
rm -rf %{buildroot}/%{python_sitelibdir}/openstack_auth/tests
# 
# %check
# %{__python} setup.py test

%files -f django.lang
%doc LICENSE
%dir %{python_sitelibdir}/openstack_auth
%{python_sitelibdir}/openstack_auth/
%{python_sitelibdir}/openstack_auth/locale/openstack_auth.pot
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 1.1.5-alt1
- New version (based on Fedora 1.1.5-3.fc21.src)

* Mon Aug 26 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0.11-alt2
- cleanup spec

* Mon Jul 15 2013 Pavel Shilovsky <piastry@altlinux.org> 1.0.11-alt1
- Initial release for Sisyphus (based on Fedora)

