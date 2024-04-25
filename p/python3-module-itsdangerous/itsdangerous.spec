%define oname itsdangerous

Name: python3-module-%oname
Version: 2.2.0
Release: alt1
Summary: Various helpers to pass trusted data to untrusted environments and back
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/itsdangerous/

# https://github.com/mitsuhiko/itsdangerous.git
Source: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-flit-core

%description
It's Dangerous
   ... so better sign this

Various helpers to pass data to untrusted environments and to get it
back safe and sound.

%prep
%setup -n %oname-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md docs/*.rst
%python3_sitelibdir/*

%changelog
* Thu Apr 25 2024 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- New version.
- Built using pyproject macros.

* Fri Mar 25 2022 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt1
- New version.

* Sat Mar 12 2022 Andrey Cherepanov <cas@altlinux.org> 2.1.1-alt1
- New version.

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

