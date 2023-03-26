%define _unpackaged_files_terminate_build 1
%define oname requests-cache

# some problems with pymongo
%def_without check

Name: python3-module-%oname
Version: 1.0.1
Release: alt1

Summary: Persistent cache for requests library

License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/requests-cache/
BuildArch: noarch

# https://github.com/reclosedev/requests-cache.git
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry
%if_with check
BuildRequires: python3-module-timeout-decorator
BuildRequires: python3-module-url-normalize
BuildRequires: python3-module-cattrs
%endif

%py3_provides requests_cache
%py3_requires sqlite3


%description
Requests-cache is a transparent persistent cache for requests
(version >= 1.1.0) library.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md LICENSE
%python3_sitelibdir/*

%changelog
* Sun Mar 26 2023 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Automatically updated to 1.0.1.

* Fri Mar 03 2023 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt1
- Automatically updated to 1.0.0.

* Fri Jan 20 2023 Grigory Ustinov <grenka@altlinux.org> 0.9.8-alt1
- Build new version (Closes: #44977).

* Mon May 30 2022 Grigory Ustinov <grenka@altlinux.org> 0.4.13-alt3
- Fixed BuildRequires.

* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.13-alt2
- python2 disabled

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.13-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.9-alt1.git20150117.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.9-alt1.git20150117.1
- NMU: Use buildreq for BR.

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.9-alt1.git20150117
- Version 0.4.9

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt1.git20141219
- Initial build for Sisyphus

