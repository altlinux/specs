%define oname aiohttp-wsgi

%def_with check

Name: python3-module-%oname
Version: 0.10.0
Release: alt1

Summary: WSGI adapter for aiohttp
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/aiohttp-wsgi/
Vcs: https://github.com/etianen/aiohttp-wsgi.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-aiohttp
%endif

%py3_provides aiohttp_wsgi
%py3_requires aiohttp

%description
aiohttp-wsgi is a WSGI adapter for aiohttp.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%tox_create_default_config
%tox_check

%files
%doc *.rst LICENSE
%_bindir/*
%python3_sitelibdir/aiohttp_wsgi
%python3_sitelibdir/aiohttp_wsgi-%version-*.egg-info


%changelog
* Thu Apr 06 2023 Anton Vyatkin <toni@altlinux.org> 0.10.0-alt1
- New version 0.10.0

* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 0.6.3-alt2
- Drop python2 support.

* Tue Jan 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.git20150331.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1.git20150331.1
- NMU: Use buildreq for BR.

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150331
- Initial build for Sisyphus

