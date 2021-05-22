%define oname pytest-aiohttp

Name: python3-module-%oname
Version: 0.3.0
Release: alt1
Summary: pytest plugin for aiohttp support
License: ASL 2.0
Group: Development/Python3
Url: https://github.com/aio-libs/pytest-aiohttp/
# Source-url: %url/archive/v%version/%oname-%version.tar.gz
Source: %oname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3(aiohttp)
BuildRequires: python3(cchardet)
BuildRequires: python3(aiohttp.test_utils)
#BuildRequires: python3-module-pytest-runner

%description
pytest plugin for aiohttp support

#%add_python3_req_skip aiohttp.pytest_plugin

%prep
%setup -n %oname-%version

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files -n python3-module-%oname
%doc *.rst LICENSE
%python3_sitelibdir/*

%changelog
* Sat May 22 2021 Anton Midyukov <antohami@altlinux.org> 0.3.0-alt1
- new version (0.3.0) with rpmgs script
- cleanup spec

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.3-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Nov 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.3-alt2
- Updated build dependencies.

* Sun Jan 15 2017 Anton Midyukov <antohami@altlinux.org> 0.1.3-alt1
- Initial build for ALT Linux Sisyphus.
