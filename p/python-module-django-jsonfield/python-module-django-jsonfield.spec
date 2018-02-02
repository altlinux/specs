%global pypi_name jsonfield

%def_with python3

Name:           python-module-django-%pypi_name
Version:        1.0.1
Release:        alt1.1
Epoch:          1
Summary:        A reusable Django field that allows you to store validated JSON in your model
Group:          Development/Python

License:        BSD
URL:            https://github.com/bradjasper/django-jsonfield
Source0:        %name-%version.tar

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-module-setuptools python-module-setuptools
BuildRequires:  python-module-django
%if_with python3
BuildRequires:  python3-devel rpm-build-python3
BuildRequires:  python3-module-setuptools python3-module-setuptools
BuildRequires:  python3-module-django
%endif

%description
django-jsonfield is a reusable Django field that allows you to store validated
JSON in your model. It silently takes care of serialization. To use, simply
add the field to one of your models.

%if_with python3
%package -n python3-module-django-%pypi_name
Summary:        %summary
Group:          Development/Python

%description -n python3-module-django-%pypi_name
django-jsonfield is a reusable Django field that allows you to store validated
JSON in your model. It silently takes care of serialization. To use, simply
add the field to one of your models.
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

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README.rst LICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-django-%pypi_name
%doc README.rst LICENSE
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:1.0.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 30 2017 Lenar Shakirov <snejok@altlinux.ru> 1:1.0.1-alt1
- Build correct source (Epoch version up)

* Fri May 26 2017 Lenar Shakirov <snejok@altlinux.ru> 1.0.3-alt1
- Initial build for ALT (based on 1.0.3-4.fc26.src)
