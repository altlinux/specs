%global		pypi_name django-appconf

%define oname django-appconf
%def_with python3

Name:		python-module-%oname
Version:	1.0.2
Release:	alt1

Summary:	A helper class for handling configuration defaults of packaged apps gracefully

Group:		Development/Python
License:	BSD
URL:		http://django-appconf.readthedocs.org

BuildArch:	noarch

Source0:	%name-%version.tar

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-psycopg2 python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python3 python3-base
BuildRequires: python-module-alabaster python-module-django python-module-docutils python-module-html5lib python3-module-setuptools rpm-build-python3 time

#BuildRequires:	python-devel
#BuildRequires:	python-module-sphinx
#BuildRequires:	python-module-six
#BuildRequires:	python-module-objects.inv
#BuildRequires:	python-module-django
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPReReq: python3-devel python3-module-setuptools
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
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc html README.rst LICENSE
%python3_sitelibdir/*
%endif

%changelog
* Wed Mar 01 2017 Alexey Shabalin <shaba@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6-alt4.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6-alt4.1.1
- NMU: Use buildreq for BR.

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
