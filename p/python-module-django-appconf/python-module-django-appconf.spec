%global		pypi_name django-appconf

%define oname django-appconf
%def_with python3

Name:		python-module-%oname
Version:	0.6
Release:	alt4.1

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
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPReReq: python3-devel python3-module-setuptools
%endif

%description
A helper class for handling configuratio defaults of packaged Django
apps gracefully.

%package -n python3-module-%oname
Summary: A helper class for handling configuration defaults of packaged apps gracefully
Group: Development/Python3

%description -n python3-module-%oname
A helper class for handling configuratio defaults of packaged Django
apps gracefully.

%prep
%setup
# Remove bundled egg-info
rm -rf %pypi_name.egg-info

%if_with python3
cp -fR . ../python3
%endif

# generate html docs
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

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
%doc html README.rst LICENSE
%python_sitelibdir/appconf
%python_sitelibdir/django_appconf-%version-py?.?.egg-info

%if_with python3
%files -n python3-module-%oname
%doc html README.rst LICENSE
%python3_sitelibdir/appconf
%python3_sitelibdir/django_appconf*.egg-info
%endif

%changelog
* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt4.1
- Added module for Python 3

* Mon Sep 30 2013 Pavel Shilovsky <piastry@altlinux.org> 0.6-alt4
- Fix build

* Mon Aug 26 2013 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt3
- cleanup spec, drop direct install requires

* Fri Jul 19 2013 Pavel Shilovsky <piastry@altlinux.org> 0.6-alt2
- Respect Autoimports/Sisyphus version

* Mon Jul 15 2013 Pavel Shilovsky <piastry@altlinux.org> 0.6-alt1
- Initial release for Sisyphus (based on Fedora)
