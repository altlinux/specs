%define oname usersettings

%def_with check

Name: python3-module-%oname
Version: 1.1.5
Release: alt2

Summary: Portable Local Settings Storage
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/usersettings/
VCS: https://github.com/glvnst/usersettings.git

Source: %name-%version.tar
Patch: usersettings-1.1.5-replace-readfp-alt-fix.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-appdirs
BuildRequires: python3-module-pytest
%endif

%description
"usersettings" is a python module for easily managing persistent
settings using an editable format and stored in an OS-appropriate
location (windows/os x/linux are supported).

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc *.md docs/* examples
%python3_sitelibdir/%oname.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%oname-%version.dist-info


%changelog
* Sun Jan 21 2024 Anton Vyatkin <toni@altlinux.org> 1.1.5-alt2
- Fixed FTBFS.

* Fri Feb 24 2023 Anton Vyatkin <toni@altlinux.org> 1.1.5-alt1
- new version 1.1.5

* Mon Jan 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.7-alt3
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.7-alt2.git20130531.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Mar 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt2.git20130531
- Fixed build

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt1.git20130531
- Initial build for Sisyphus

