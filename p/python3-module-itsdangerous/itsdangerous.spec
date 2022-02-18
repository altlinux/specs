%define oname itsdangerous

Name: python3-module-%oname
Version: 2.1.0
Release: alt1
Summary: Various helpers to pass trusted data to untrusted environments and back
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/itsdangerous/

# https://github.com/mitsuhiko/itsdangerous.git
Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

%description
It's Dangerous
   ... so better sign this

Various helpers to pass data to untrusted environments and to get it
back safe and sound.

%prep
%setup -n %oname-%version

%build
%python3_build_debug

%install
%python3_install

%files
%doc README.rst docs/*.rst
%python3_sitelibdir/*

%changelog
* Fri Feb 18 2022 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- New version.

* Thu May 20 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- New version.
- Build only for Python3.

* Wed May 12 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Tue Mar 24 2020 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version.
- Fix License tag according to SPDX.
- Build from upstream tag.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.24-alt1.git20140328.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.24-alt1.git20140328.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24-alt1.git20140328
- Initial build for Sisyphus

