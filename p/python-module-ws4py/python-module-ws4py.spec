%define oname ws4py
Name: python-module-ws4py
Version: 0.5.1
Release: alt2

Summary: WebSocket for Python (ws4py)

Url: https://github.com/Lawouach/WebSocket-for-Python
License: ASL 2.0
Group: Development/Python

Packager: Valentin Rosavitskiy <valintinr@altlinux.org>

# Source-url: https://pypi.io/packages/source/w/%oname/%oname-%version.tar.gz
Source: %name-%version.tar
Patch1: %oname-async-fix.patch

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
ws4py is a Python package implementing the WebSocket protocol as
defined in RFC 6455.

%package -n python3-module-%oname
Summary: WebSocket for Python (ws4py)
Group: Development/Python3

%description -n python3-module-%oname
ws4py is a Python package implementing the WebSocket protocol as
defined in RFC 6455.


%prep
%setup
%patch1 -p1


%build
%add_optflags -fno-strict-aliasing
%python3_build

%install
%python3_install


%files -n python3-module-%oname
%doc CHANGELOG.md LICENSE README.md
%python3_sitelibdir/*


%changelog
* Tue Oct 01 2019 Anton Farygin <rider@altlinux.ru> 0.5.1-alt2
- removed python2 support

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt1
- new version 0.5.1 (with rpmrb script)
- switch to build from tarball

* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 0.3.5.git.fd55907a-alt1
- New version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.4-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 30 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.3.4-alt1
- Initla build for ALT

