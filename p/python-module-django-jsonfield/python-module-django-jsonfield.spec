%global pypi_name jsonfield

%def_with python3

Name:           python-module-django-%pypi_name
Version:        1.0.3
Release:        alt1
Summary:        A reusable Django field that allows you to store validated JSON in your model
Group:          Development/Python

License:        BSD
URL:            https://github.com/bradjasper/django-jsonfield
Source0:        %name-%version.tar
Source1:        https://raw.githubusercontent.com/bradjasper/django-jsonfield/master/LICENSE
# for Patch0 info check https://github.com/bradjasper/django-jsonfield/issues/169
Patch0:         test.patch

BuildArch:      noarch

# for testing purposes
BuildRequires:  sqlite3

BuildRequires:  python-devel
BuildRequires:  python-module-setuptools
BuildRequires:  python-module-django python-module-django-tests
BuildRequires:  python-module-django-formtools python-module-django-dbbackend-sqlite3
%if_with python3
BuildRequires:  python3-devel rpm-build-python3
BuildRequires:  python3-module-setuptools
BuildRequires:  python3-module-django python3-module-django-tests
BuildRequires:  python3-module-django-formtools python3-module-django-dbbackend-sqlite3
%endif

%description
django-jsonfield is a reusable Django field that allows you to store validated
JSON in your model. It silently takes care of serialization. To use, simply
add the field to one of your models.

%if_with python3
%package -n python3-module-django-%pypi_name
Summary:        %summary
Group:          Development/Python
Requires:  python3-module-django
Requires:  python3-module-django-formtools

%description -n python3-module-django-%pypi_name
django-jsonfield is a reusable Django field that allows you to store validated
JSON in your model. It silently takes care of serialization. To use, simply
add the field to one of your models.
%endif

%prep
%setup
cp %SOURCE1 .
%patch0 -p1

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

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
sqlite3 FILETEMP
export DB_ENGINE=sqlite3
export DB_NAME="mydb"
%__python setup.py test
%__python3 setup.py test

%files
%doc README.rst LICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-django-%pypi_name
%doc README.rst LICENSE
%python3_sitelibdir/*
%endif

%changelog
* Fri May 26 2017 Lenar Shakirov <snejok@altlinux.ru> 1.0.3-alt1
- Initial build for ALT (based on 1.0.3-4.fc26.src)

