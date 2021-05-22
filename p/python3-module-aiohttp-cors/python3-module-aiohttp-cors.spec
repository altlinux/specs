%define oname aiohttp-cors

Name: python3-module-%oname
Version: 0.7.0
Release: alt2
Summary: CORS support for aiohttp
License: ASL 2.0
Group: Development/Python3
Url: https://github.com/aio-libs/aiohttp-cors

Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
aiohttp_cors library implements Cross Origin Resource Sharing (CORS)
support for aiohttp asyncio-powered asynchronous HTTP server.

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
* Sat May 22 2021 Anton Midyukov <antohami@altlinux.org> 0.7.0-alt2
- rename srpm to python3-module-aiohttp-cors

* Sun Apr 07 2019 Anton Midyukov <antohami@altlinux.org> 0.7.0-alt1
- New version 0.7.0

* Sat Nov 18 2017 Anton Midyukov <antohami@altlinux.org> 0.5.3-alt1
- New version 0.5.3

* Mon May 08 2017 Anton Midyukov <antohami@altlinux.org> 0.5.1-alt1
- New version 0.5.1

* Sun Jan 15 2017 Anton Midyukov <antohami@altlinux.org> 0.5.0-alt1
- Initial build for ALT Linux Sisyphus.
