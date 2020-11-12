%define oname js.jquery

Name: python3-module-%oname
Version: 3.3.1
Release: alt1

Summary: fanstatic jQuery
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/js.jquery/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-fanstatic

%py3_requires js fanstatic shutilwhich

Obsoletes: python3-module-js.query
Provides: python3-module-js.query

%description
This library packages jQuery for fanstatic. It is aware of jQuery's
structure and different modes (normal, minified).

%prep
%setup

%build
%python3_build_debug

%install
%python3_install
%python3_prune

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
%__python3 setup.py test
%__python3 -c "from js.jquery import jquery; jquery.need()"

%files
%doc *.txt
%python3_sitelibdir/js/*
%python3_sitelibdir/js.jquery-*-nspkg.pth
%python3_sitelibdir/*.egg-info

%changelog
* Thu Nov 12 2020 Vitaly Lipatov <lav@altlinux.ru> 3.3.1-alt1
- new version 3.3.1 (with rpmrb script)
- obsoletes: python3-module-js.query (ALT bug 39269)

* Mon Apr 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.9.1-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.9.1-alt1.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.1-alt1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.9.1-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.1-alt1
- Initial build for Sisyphus

