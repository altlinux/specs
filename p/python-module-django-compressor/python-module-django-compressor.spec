%global		pypi_name django_compressor

Name:		python-module-django-compressor
Version:	1.3
Release:	alt1
Summary:	Compresses linked and inline JavaScript or CSS into single cached files

Group:		Development/Python
License:	MIT
URL:		http://pypi.python.org/pypi/django_compressor/1.2
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	python-devel
BuildRequires:	python-module-distribute
BuildRequires:	python-module-django

Requires:	python-module-django-appconf >= 0.4
Requires:	python-module-versiontools
Requires:	python-module-django

%description
Django Compressor combines and compresses linked and inline Javascript
or CSS in a Django templates into cacheable static files by using the
``compress`` template tag.  HTML in between ``{% compress js/css %}``
and ``{% endcompress %}`` is parsed and searched for CSS or JS. These
styles and scripts are subsequently processed with optional,
configurable compilers and filters.

%prep
%setup -q -n %{name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# remove /usr/bin/env from scripts
for i in compressor/tests/precompiler.py \
         compressor/filters/cssmin/cssmin.py \
         compressor/filters/jsmin/rjsmin.py;
  do sed -i -e "1d" $i;
done

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst LICENSE
%{python_sitelibdir}/compressor
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Mon Jul 15 2013 Pavel Shilovsky <piastry@altlinux.org> 1.3-alt1
- Initial release for Sisyphus (based on Fedora)
