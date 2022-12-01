%define _unpackaged_files_terminate_build 1
%define pypi_name zipp

%def_with check

Name: python3-module-%pypi_name
Version: 3.11.0
Release: alt1

Summary: A pathlib-compatible Zipfile object wrapper

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/zipp/
VCS: https://github.com/jaraco/zipp.git

BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(jaraco.itertools)
BuildRequires: python3(jaraco.functools)
BuildRequires: python3(more_itertools)
%endif

%description
A pathlib-compatible Zipfile object wrapper.

%prep
%setup
%autopatch -p1
# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM.
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc README.rst
%python3_sitelibdir/zipp/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Nov 30 2022 Stanislav Levin <slev@altlinux.org> 3.11.0-alt1
- 3.10.0 -> 3.11.0.

* Mon Oct 24 2022 Stanislav Levin <slev@altlinux.org> 3.10.0-alt1
- 3.9.1 -> 3.10.0.

* Mon Oct 10 2022 Stanislav Levin <slev@altlinux.org> 3.9.1-alt1
- 3.8.1 -> 3.9.1.

* Tue Aug 09 2022 Stanislav Levin <slev@altlinux.org> 3.8.1-alt1
- 3.7.0 -> 3.8.1.

* Wed Jan 12 2022 Stanislav Levin <slev@altlinux.org> 3.7.0-alt1
- 3.6.0 -> 3.7.0.

* Mon Oct 18 2021 Stanislav Levin <slev@altlinux.org> 3.6.0-alt1
- 3.5.1 -> 3.6.0.

* Wed Sep 29 2021 Stanislav Levin <slev@altlinux.org> 3.5.1-alt1
- 3.5.0 -> 3.5.1.

* Wed Jul 21 2021 Stanislav Levin <slev@altlinux.org> 3.5.0-alt1
- 1.0.0 -> 3.5.0.
- Reenabled testing.

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- new version 1.0.0 (with rpmrb script)

* Sun Apr 25 2021 Vitaly Lipatov <lav@altlinux.ru> 0.5.0-alt2
- NMU: build python3 module only, cleanup spec

* Tue May 14 2019 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1
- 0.4.0 -> 0.5.0.

* Fri May 03 2019 Stanislav Levin <slev@altlinux.org> 0.4.0-alt1
- 0.3.3 -> 0.4.0.

* Mon Jan 28 2019 Stanislav Levin <slev@altlinux.org> 0.3.3-alt1
- Initial build.
