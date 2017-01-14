%define oname aiohttp-cors

Name: python-module-%oname
Version: 0.5.0
Release: alt1
Summary: CORS support for aiohttp
License: ASL 2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/aiohttp_cors

Source: https://pypi.python.org/packages/93/e2/794d3933921402c92018f52929a1121b77208bfe9f64844b95825a29fdd5/%oname-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

%description
aiohttp_cors library implements Cross Origin Resource Sharing (CORS) support for
aiohttp asyncio-powered asynchronous HTTP server.

%package -n python3-module-%oname
Summary: CORS support for aiohttp
Group: Development/Python3

%description -n python3-module-%oname
aiohttp_cors library implements Cross Origin Resource Sharing (CORS) support for
aiohttp asyncio-powered asynchronous HTTP server.

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
* Sun Jan 15 2017 Anton Midyukov <antohami@altlinux.org> 0.5.0-alt1
- Initial build for ALT Linux Sisyphus.
