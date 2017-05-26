%global pypi_name django-formtools

%def_with python3

Name:           python-module-%{pypi_name}
Version:        1.0
Release:        alt1
Summary:        A set of high-level abstractions for Django forms
Group:          Development/Python

License:        BSD
URL:            http://django-formtools.readthedocs.org/en/latest/
Source0:        %name-%version.tar
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-module-sphinx
BuildRequires:  python-module-django >= 1.7
# Required for testing
BuildRequires:  python-module-flake8
BuildRequires:  python-module-coverage

Requires:       python-module-django >= 1.7

%description
Django's "formtools" is a set of high-level abstractions for Django forms.
Currently for form previews and multi-step forms.

%package -n %name-doc
Summary:        A set of high-level abstractions for Django forms - documentation
Group:          Development/Documentation

Requires:       %name = %version-%release

%description -n %name-doc
Django's "formtools" is a set of high-level abstractions for Django forms.

This is the associated documentation.

%if_with python3
%package -n python3-module-%pypi_name
Summary:        A set of high-level abstractions for Django forms
Group:          Development/Python

BuildRequires:  python3-devel rpm-build-python3
BuildRequires:  python3-module-sphinx
BuildRequires:  python3-module-django >= 1.7
# Required for testing
BuildRequires:  python3-module-flake8
BuildRequires:  python3-module-coverage

Requires:       python3-module-django >= 1.7

%description -n python3-module-%pypi_name
Django's "formtools" is a set of high-level abstractions for Django forms.
Currently for form previews and multi-step forms.

%package -n python3-module-%pypi_name-doc
Summary:        A set of high-level abstractions for Django forms - documentation
Group:          Development/Documentation

Requires:       python3-module-%pypi_name = %version-%release

%description -n python3-module-%pypi_name-doc
Django's "formtools" is a set of high-level abstractions for Django forms.

This is the associated documentation.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%find_lang django py2lang
# generate html docs 
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%if_with python3
pushd ../python3
%python3_install
%find_lang django py3lang
popd
%endif

%files -n python-module-%pypi_name -f py2lang.lang
%doc README.rst LICENSE
%python_sitelibdir/formtools
%python_sitelibdir/django_formtools-%version-py?.?.egg-info

%files -n python-module-%pypi_name-doc
%doc html LICENSE

%if_with python3
%files -n python3-module-%pypi_name -f ../python3/py3lang.lang
%doc README.rst LICENSE
%python3_sitelibdir/formtools
%python3_sitelibdir/django_formtools-%version-py?.?.egg-info
# find_lang will find both python2 and python3 locale files
%exclude %python_sitelibdir/formtools/locale

%files -n python3-module-%pypi_name-doc
%doc html LICENSE
%endif

%changelog
* Fri May 26 2017 Lenar Shakirov <snejok@altlinux.ru> 1.0-alt1
- Initial build for ALT (based on 1.0-10.fc26.src)
