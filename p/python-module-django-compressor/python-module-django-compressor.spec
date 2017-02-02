%global		pypi_name django_compressor

%define oname django-compressor
%def_with python3

Name:		python-module-%oname
Version:	2.1.1
Release:	alt1

Summary:	Compresses linked and inline JavaScript or CSS into single cached files

Group:		Development/Python
License:	MIT
URL:		http://pypi.python.org/pypi/django_compressor/1.2

BuildArch:	noarch

Source0:	%name-%version.tar

BuildRequires:	python-devel
BuildRequires:	python-module-setuptools
BuildRequires:	python-module-django
BuildRequires:	python-module-versiontools
BuildRequires:	python-module-rcssmin >= 1.0.6
BuildRequires:	python-module-rjsmin >= 1.0.12

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq:python3-devel python3-module-setuptools python3-module-django
%endif

Requires:	python-module-django-appconf >= 1.0
Requires:	python-module-versiontools
Requires:	python-module-rcssmin  >= 1.0.6
Requires:	python-module-rjsmin >= 1.0.12

%description
Django Compressor combines and compresses linked and inline Javascript
or CSS in a Django templates into cacheable static files by using the
``compress`` template tag.  HTML in between ``{%% compress js/css %%}``
and ``{%% endcompress %%}`` is parsed and searched for CSS or JS. These
styles and scripts are subsequently processed with optional,
configurable compilers and filters.

%package tests
Summary: Tests of %oname
Group: Development/Python
Requires:	python-module-%oname = %EVR

%description tests
Django Compressor combines and compresses linked and inline Javascript
or CSS in a Django templates into cacheable static files by using the
``compress`` template tag.  HTML in between ``{%% compress js/css %%}``
and ``{%% endcompress %%}`` is parsed and searched for CSS or JS. These
styles and scripts are subsequently processed with optional,
configurable compilers and filters.

This package contein tests.

%package -n python3-module-%oname
Summary: Compresses linked and inline JavaScript or CSS into single cached files
Group: Development/Python3
Requires:	python3-module-django-appconf
Requires:	python3-module-versiontools

%description -n python3-module-%oname
Django Compressor combines and compresses linked and inline Javascript
or CSS in a Django templates into cacheable static files by using the
``compress`` template tag.  HTML in between ``{%% compress js/css %%}``
and ``{%% endcompress %%}`` is parsed and searched for CSS or JS. These
styles and scripts are subsequently processed with optional,
configurable compilers and filters.

%package -n python3-module-%oname-tests
Summary: Tests of %oname
Group: Development/Python3
Requires:	python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Django Compressor combines and compresses linked and inline Javascript
or CSS in a Django templates into cacheable static files by using the
``compress`` template tag.  HTML in between ``{%% compress js/css %%}``
and ``{%% endcompress %%}`` is parsed and searched for CSS or JS. These
styles and scripts are subsequently processed with optional,
configurable compilers and filters.

This package contein tests.

%prep
%setup

# Remove bundled egg-info
rm -rf %pypi_name.egg-info

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
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/test_settings.py

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/test_settings.py

%if_with python3
%files -n python3-module-%oname
%doc README.rst LICENSE
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/test_settings.py

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/test_settings.py
%endif

%changelog
* Thu Feb 02 2017 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Tue Apr 19 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1
- 2.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 14 2015 Lenar Shakirov <snejok@altlinux.ru> 1.5-alt2
- Fixed build

* Thu Sep 10 2015 Lenar Shakirov <snejok@altlinux.ru> 1.5-alt1
- Version 1.5

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Version 1.4
- Added module for Python 3

* Mon Aug 26 2013 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt3
- cleanup spec, remove direct python-module-django requires

* Fri Jul 19 2013 Pavel Shilovsky <piastry@altlinux.org> 1.3-alt2
- Respect Autoimports/Sisyphus version

* Mon Jul 15 2013 Pavel Shilovsky <piastry@altlinux.org> 1.3-alt1
- Initial release for Sisyphus (based on Fedora)
