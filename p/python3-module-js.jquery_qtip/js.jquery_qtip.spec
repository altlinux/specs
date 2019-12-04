%define oname js.jquery_qtip

Name: python3-module-%oname
Version: 1.0.0
Release: alt2

Summary: Fanstatic packaging of jquery.qTip
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/js.jquery_qtip/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-fanstatic python3-module-js.jquery

%py3_provides %oname
%py3_requires js fanstatic js.jquery


%description
This library packages jquery.qTip for fanstatic.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
%__python3 setup.py test
%__python3 -c "from js.jquery_qtip import qtip; qtip.need()"

%files
%doc *.txt
%python3_sitelibdir/js/*
%python3_sitelibdir/*.egg-info


%changelog
* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

