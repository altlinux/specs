%define _unpackaged_files_terminate_build 1
%define pypi_name facebook-utils
%define mod_name facebook_utils

Name: python3-module-%mod_name
Version: 0.50.5
Release: alt2

Summary: Simple utilites for facebook integration
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/facebook_utils/
VCS: https://github.com/jvanasco/facebook_utils
BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

# well-known PyPI name
%py3_provides %pypi_name
Provides: python3-module-%pypi_name = %EVR

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
A collection of utilities for integrating user accounts with
Facebook.com.

Right now this handles oauth and graph operations.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc CHANGES.txt README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Feb 10 2023 Stanislav Levin <slev@altlinux.org> 0.50.5-alt2
- Fixed FTBFS (setuptools 67).

* Mon Nov 25 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.50.5-alt1
- version updated to 0.50.5
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.20.3-alt1.git20140717.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.20.3-alt1.git20140717.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20.3-alt1.git20140717
- Initial build for Sisyphus

