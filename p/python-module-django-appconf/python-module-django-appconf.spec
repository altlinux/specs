%global		pypi_name django-appconf

Name:		python-module-django-appconf
Version:	0.6
Release:	alt4

Summary:	A helper class for handling configuration defaults of packaged apps gracefully

Group:		Development/Python
License:	BSD
URL:		http://pypi.python.org/pypi/django-appconf/0.6

BuildArch:	noarch

Source0:	%name-%version.tar

BuildRequires:	python-devel
BuildRequires:	python-module-sphinx
BuildRequires:	python-module-six
BuildRequires:	python-module-objects.inv
BuildRequires:	python-module-django

%description
A helper class for handling configuratio defaults of packaged Django
apps gracefully.

%prep
%setup
# Remove bundled egg-info
rm -rf %pypi_name.egg-info

# generate html docs
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%build
%python_build

%install
%python_install

%files
%doc html README.rst LICENSE
%python_sitelibdir/appconf
%python_sitelibdir/django_appconf-%version-py?.?.egg-info

%changelog
* Mon Sep 30 2013 Pavel Shilovsky <piastry@altlinux.org> 0.6-alt4
- Fix build

* Mon Aug 26 2013 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt3
- cleanup spec, drop direct install requires

* Fri Jul 19 2013 Pavel Shilovsky <piastry@altlinux.org> 0.6-alt2
- Respect Autoimports/Sisyphus version

* Mon Jul 15 2013 Pavel Shilovsky <piastry@altlinux.org> 0.6-alt1
- Initial release for Sisyphus (based on Fedora)
