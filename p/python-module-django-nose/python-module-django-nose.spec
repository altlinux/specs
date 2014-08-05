%global pkgname django-nose
%def_with python3

Name:           python-module-django-nose
Version:        1.2
Release:        alt1
Summary:        Django test runner that uses nose
Group:          Development/Python

License:        BSD
URL:            http://github.com/jbalogh/django-nose
Source0:        %{name}-%{version}.tar

BuildArch:      noarch
BuildRequires:  python-devel python-module-setuptools
Requires:       python-module-nose
Requires:       python-module-django

%description
Django test runner that uses nose.

%if_with python3
%package -n python3-module-%{pkgname}
Summary:        Django test runner that uses nose
Group:		Development/Python
BuildArch:      noarch
BuildRequires:  rpm-build-python3 python3-module-setuptools
Requires:       python3-module-nose
Requires:       python3-module-django

%description -n python3-module-%{pkgname}
Django test runner that uses nose.

%endif

%prep
%setup

# remove egg-info
rm -rf django_nose.egg-info

%if_with python3
rm -rf ../python3
cp -a . ../python3
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
%doc LICENSE README.rst
%{python_sitelibdir}/django_nose
%{python_sitelibdir}/django_nose-%{version}-py?.?.egg-info

%if_with python3
%files -n python3-module-%{pkgname}
%doc LICENSE README.rst
%{python3_sitelibdir}/django_nose
%{python3_sitelibdir}/django_nose-%{version}-py?.?.egg-info
%endif

%changelog
* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 1.2-alt1
- First build for ALT (based on Fedora 1.2-2.fc21.src)

