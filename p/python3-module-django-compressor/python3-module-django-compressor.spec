%define pypi_name django_compressor

%define oname django-compressor

Name: python3-module-%oname
Version: 2.4.1
Release: alt1

Summary: Compresses linked and inline JavaScript or CSS into single cached files

Group: Development/Python3
License: MIT
Url: https://pypi.org/project/%pypi_name

BuildArch: noarch

Source: %pypi_name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-django-appconf >= 1.0.3
BuildRequires: python3-module-rcssmin >= 1.0.6
BuildRequires: python3-module-rjsmin >= 1.1.0

Requires: python3-module-django-appconf >= 1.0.3
Requires: python3-module-rcssmin  >= 1.0.6
Requires: python3-module-rjsmin >= 1.1.0

%description
Django Compressor combines and compresses linked and inline Javascript
or CSS in a Django templates into cacheable static files by using the
``compress`` template tag.  HTML in between ``{%% compress js/css %%}``
and ``{%% endcompress %%}`` is parsed and searched for CSS or JS. These
styles and scripts are subsequently processed with optional,
configurable compilers and filters.

%package tests
Summary: Tests of %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
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
#rm -rf %pypi_name.egg-info

%build
%python3_build

%install
%python3_install

%files
%doc README.rst LICENSE
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/test_settings.py

%files tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/test_settings.py

%changelog
* Tue Jul 13 2021 Alexey Shabalin <shaba@altlinux.org> 2.4.1-alt1
- 2.4.1

* Tue May 25 2021 Grigory Ustinov <grenka@altlinux.org> 2.2-alt2
- Drop python2 support

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
