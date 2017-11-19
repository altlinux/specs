%define oname async-timeout

Name: python-module-%oname
Version: 1.4
Release: alt1
Summary: Timeout context manager for asyncio programs
License: ASL 2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/async_timeout

Source: https://pypi.python.org/packages/29/f6/eeac39dfadd3a7610bb33842cf611a1f09fcd2e445ab76e4c951efde0c2b/%oname-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-pytest-runner
#BuildRequires: python3-module-setuptools-tests python3-module-pytest-aiohttp

%description
Timeout context manager for asyncio programs.

%package -n python3-module-%oname
Summary: Timeout context manager for asyncio programs
Group: Development/Python3

%description -n python3-module-%oname
Timeout context manager for asyncio programs.

%prep
%setup -n %oname-%version

%build
%python3_build_debug

%install
%python3_install

%check
#python3 setup.py test

%files -n python3-module-%oname
%doc *.rst LICENSE
%python3_sitelibdir/*

%changelog
* Sun Nov 19 2017 Anton Midyukov <antohami@altlinux.org> 1.4-alt1
- New version 1.4

* Sat Jan 21 2017 Anton Midyukov <antohami@altlinux.org> 1.1-alt1
- Initial build for ALT Linux Sisyphus.
