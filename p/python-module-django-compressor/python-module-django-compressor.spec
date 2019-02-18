%define pypi_name django_compressor

%define oname django-compressor

Name: python-module-%oname
Version: 2.2
Release: alt1

Summary: Compresses linked and inline JavaScript or CSS into single cached files

Group: Development/Python
License: MIT
Url: https://pypi.org/project/%pypi_name

BuildArch: noarch

Source: %pypi_name-%version.tar.gz

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-django
BuildRequires: python-module-versiontools
BuildRequires: python-module-rcssmin >= 1.0.6
BuildRequires: python-module-rjsmin >= 1.0.12

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-django
BuildRequires: python3-module-versiontools
BuildRequires: python3-module-rcssmin >= 1.0.6
BuildRequires: python3-module-rjsmin >= 1.0.12

Requires: python-module-django-appconf >= 1.0
Requires: python-module-versiontools
Requires: python-module-rcssmin  >= 1.0.6
Requires: python-module-rjsmin >= 1.0.12

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
Requires: python-module-%oname = %EVR

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
Requires: python3-module-django-appconf >= 1.0
Requires: python3-module-versiontools
Requires: python3-module-rcssmin  >= 1.0.6
Requires: python3-module-rjsmin >= 1.0.12

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
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Django Compressor combines and compresses linked and inline Javascript
or CSS in a Django templates into cacheable static files by using the
``compress`` template tag.  HTML in between ``{%% compress js/css %%}``
and ``{%% endcompress %%}`` is parsed and searched for CSS or JS. These
styles and scripts are subsequently processed with optional,
configurable compilers and filters.

This package contein tests.

%prep
%setup -n %pypi_name-%version

# Remove bundled egg-info
rm -rf %pypi_name.egg-info

cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc README.rst LICENSE
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/test_settings.py

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/test_settings.py

%files -n python3-module-%oname
%doc README.rst LICENSE
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/test_settings.py

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/test_settings.py

%changelog
* Mon Feb 18 2019 Alexey Shabalin <shaba@altlinux.org> 2.2-alt1
- 2.2

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
