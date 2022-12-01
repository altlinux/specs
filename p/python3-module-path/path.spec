%define _unpackaged_files_terminate_build 1
%define pypi_name path

%def_with check

Name: python3-module-%pypi_name
Version: 16.6.0
Release: alt1

Summary: A module wrapper for os.path
License: MIT
Group: Development/Python
Url: https://pypi.org/project/path/
VCS: https://github.com/jaraco/path

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(appdirs)
BuildRequires: python3(packaging)
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name
Provides: python3-module-path.py = %EVR
Obsoletes: python3-module-path.py < %EVR

%description
path implements a path objects as first-class entities, allowing
common operations on files to be invoked on those path objects directly.

%prep
%setup
%patch -p1

# if build from git source tree
# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM. These files will be packaged unless filtered by MANIFEST.in.
git init
git config user.email author@example.com
git config user.name author
git add .
git commit -m 'release'
git tag '%version'

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject -- -vra

%files
%doc *.rst
%python3_sitelibdir/path/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Dec 01 2022 Stanislav Levin <slev@altlinux.org> 16.6.0-alt1
- 16.5.0 -> 16.6.0.

* Mon Oct 24 2022 Stanislav Levin <slev@altlinux.org> 16.5.0-alt1
- 16.4.0 -> 16.5.0.

* Tue Apr 05 2022 Stanislav Levin <slev@altlinux.org> 16.4.0-alt1
- 16.3.0 -> 16.4.0.

* Tue Jan 11 2022 Stanislav Levin <slev@altlinux.org> 16.3.0-alt1
- 16.0.0 -> 16.3.0.

* Tue Jul 20 2021 Stanislav Levin <slev@altlinux.org> 16.0.0-alt1
- 13.2.0 -> 16.0.0.

* Sun May 23 2021 Michael Shigorin <mike@altlinux.org> 13.2.0-alt2
- Fixed BR:

* Tue Apr 21 2020 Stanislav Levin <slev@altlinux.org> 13.2.0-alt1
- 12.0.1 -> 13.2.0.

* Tue Aug 06 2019 Stanislav Levin <slev@altlinux.org> 12.0.1-alt2
- Fixed testing against Pytest 5.

* Mon Apr 22 2019 Stanislav Levin <slev@altlinux.org> 12.0.1-alt1
- 11.5.0 -> 12.0.1.

* Fri Jan 25 2019 Stanislav Levin <slev@altlinux.org> 11.5.0-alt1
- 7.2 -> 11.5.0.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 7.2-alt1.git20150122.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 7.2-alt1.git20150122.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.2-alt1.git20150122
- Version 7.2

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt1.git20140823
- Version 5.3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.2.990-alt1.1
- Rebuild with Python-2.7

* Tue Jun 07 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.2.2.990-alt1
- Initial build for Sisyphus.
