%define oname async-timeout

Name: python-module-%oname
Version: 3.0.1
Release: alt1
Summary: Timeout context manager for asyncio programs
License: ASL 2.0
Group: Development/Python
Url: https://github.com/aio-libs/async_timeout/

Source: %oname-%version.tar
BuildArch: noarch

%description
Timeout context manager for asyncio programs.

%package -n python3-module-%oname
Summary: Timeout context manager for asyncio programs
Group: Development/Python3

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description -n python3-module-%oname
Timeout context manager for asyncio programs.

%prep
%setup -n %oname-%version

%build
%python3_build_debug

%install
%python3_install

%files -n python3-module-%oname
%doc *.rst LICENSE
%python3_sitelibdir/*

%changelog
* Sun Apr 07 2019 Anton Midyukov <antohami@altlinux.org> 3.0.1-alt1
- New version 3.0.1
- switch to git
- cleanup spec

* Sun Nov 19 2017 Anton Midyukov <antohami@altlinux.org> 1.4-alt1
- New version 1.4

* Sat Jan 21 2017 Anton Midyukov <antohami@altlinux.org> 1.1-alt1
- Initial build for ALT Linux Sisyphus.
