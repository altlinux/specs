%define oname pytest-aiohttp

Name: python-module-%oname
Version: 0.1.3
Release: alt2.1
Summary: pytest plugin for aiohttp support
License: ASL 2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-aiohttp

Source: https://pypi.python.org/packages/89/b1/a486d9e969de578c373bb48ca907cbfa337653dd9fb8b8f61143053399b3/%oname-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools python3-module-pytest-runner python3(aiohttp) python3(aiohttp.test_utils)
BuildRequires: python3-module-chardet

%description
pytest plugin for aiohttp support

%package -n python3-module-%oname
Summary: pytest plugin for aiohttp support
Group: Development/Python3
%add_python3_req_skip aiohttp.pytest_plugin

%description -n python3-module-%oname
pytest plugin for aiohttp support

%prep
%setup -n %oname-%version

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files -n python3-module-%oname
%doc *.rst LICENSE
%python3_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.3-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Nov 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.3-alt2
- Updated build dependencies.

* Sun Jan 15 2017 Anton Midyukov <antohami@altlinux.org> 0.1.3-alt1
- Initial build for ALT Linux Sisyphus.
