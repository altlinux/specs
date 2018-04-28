%define modname django-formtools

Name: python-module-%modname
Version: 2.1
Release: alt1
Summary: A set of high-level abstractions for Django forms
Group: Development/Python

License: BSD
URL: http://django-formtools.readthedocs.org/en/latest/
# https://github.com/django/django-formtools
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-sphinx
BuildRequires: python-module-django >= 1.7
# Required for testing
BuildRequires: python-module-flake8
BuildRequires: python-module-coverage

Requires: python-module-django >= 1.7


%description
Django's "formtools" is a set of high-level abstractions for Django forms.
Currently for form previews and multi-step forms.

%package -n %name-doc
Summary: A set of high-level abstractions for Django forms - documentation
Group: Development/Documentation

Requires: %name = %version-%release

%description -n %name-doc
Django's "formtools" is a set of high-level abstractions for Django forms.

This is the associated documentation.

%package -n python3-module-%modname
Summary: A set of high-level abstractions for Django forms
Group: Development/Python

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
BuildPreReq: python3-module-sphinx
BuildPreReq: python3-module-django >= 1.7
# Required for testing
BuildPreReq: python3-module-flake8
BuildPreReq: python3-module-coverage

Requires: python3-module-django >= 1.7

%description -n python3-module-%modname
Django's "formtools" is a set of high-level abstractions for Django forms.
Currently for form previews and multi-step forms.

%package -n python3-module-%modname-doc
Summary: A set of high-level abstractions for Django forms - documentation
Group: Development/Documentation

Requires: python3-module-%modname = %version-%release

%description -n python3-module-%modname-doc
Django's "formtools" is a set of high-level abstractions for Django forms.

This is the associated documentation.

%prep
%setup

rm -rf ../python3
cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

%find_lang django py2lang

pushd ../python3
%python3_install
%find_lang django py3lang
popd

export PYTHONPATH=$PWD
make -C docs man

%files -n python-module-%modname -f py2lang.lang
%doc README.rst LICENSE
%python_sitelibdir/formtools
%python_sitelibdir/django_formtools-%version-py?.?.egg-info

%files -n python-module-%modname-doc
%doc docs/_build/*

%files -n python3-module-%modname -f ../python3/py3lang.lang
%doc README.rst LICENSE
%python3_sitelibdir/formtools
%python3_sitelibdir/django_formtools-%version-py?.?.egg-info
# find_lang will find both python2 and python3 locale files
%exclude %python_sitelibdir/formtools/locale

%files -n python3-module-%modname-doc
%doc docs/_build/*


%changelog
* Sat Apr 28 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.1-alt1
- Updated version to 2.1

* Fri May 26 2017 Lenar Shakirov <snejok@altlinux.ru> 1.0-alt1
- Initial build for ALT (based on 1.0-10.fc26.src)
