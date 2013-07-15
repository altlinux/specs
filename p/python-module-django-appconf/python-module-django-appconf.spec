%global		pypi_name django-appconf

Name:		python-module-django-appconf
Version:	0.6
Release:	alt1
Summary:	A helper class for handling configuration defaults of packaged apps gracefully

Group:		Development/Python
License:	BSD
URL:		http://pypi.python.org/pypi/django-appconf/0.6
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	python-devel
BuildRequires:	python-module-sphinx
BuildRequires:	python-module-six
BuildRequires:	python-module-objects.inv
BuildRequires:	python-module-django

Requires:	python-module-django
Requires:	python-module-six

%description
A helper class for handling configuratio defaults of packaged Django
apps gracefully.

%prep
%setup -q -n %{name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# generate html docs
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%check
%{__python} setup.py test

%files
%doc html README.rst LICENSE
%{python_sitelibdir}/appconf
%{python_sitelibdir}/django_appconf-%{version}-py?.?.egg-info

%changelog
* Mon Jul 15 2013 Pavel Shilovsky <piastry@altlinux.org> 0.6-alt1
- Initial release for Sisyphus (based on Fedora)
