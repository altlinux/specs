%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-asyncio

%def_with check

Name: python3-module-%pypi_name
Version: 0.20.2
Release: alt1

Summary: Pytest support for asyncio
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/pytest-dev/pytest-asyncio
BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%py3_provides %pypi_name

%if_with check
# install_requires=
BuildRequires: python3(pytest)

BuildRequires: python3(hypothesis)
BuildRequires: python3(flaky)
%endif

%description
pyee supplies a BaseEventEmitter object that is similar to the EventEmitter
class from Node.js. It also supplies a number of subclasses with added support
for async and threaded programming in python, such as async/await as seen in
python 3.5+.

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
%doc *.rst LICENSE
%python3_sitelibdir/pytest_asyncio/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Nov 14 2022 Stanislav Levin <slev@altlinux.org> 0.20.2-alt1
- 0.20.1 -> 0.20.2.

* Mon Oct 24 2022 Stanislav Levin <slev@altlinux.org> 0.20.1-alt1
- 0.19.0 -> 0.20.1.

* Wed Jul 20 2022 Stanislav Levin <slev@altlinux.org> 0.19.0-alt1
- 0.17.2 -> 0.19.0.

* Thu Feb 03 2022 Stanislav Levin <slev@altlinux.org> 0.17.2-alt1
- 0.15.1 -> 0.17.2.

* Thu Oct 14 2021 Ivan A. Melnikov <iv@altlinux.org> 0.15.1-alt2
- NMU: Fix FTBFS by ignoring warnings in tests.

* Thu Apr 22 2021 Stanislav Levin <slev@altlinux.org> 0.15.1-alt1
- 0.15.0 -> 0.15.1.

* Mon Apr 19 2021 Stanislav Levin <slev@altlinux.org> 0.15.0-alt1
- 0.14.0 -> 0.15.0.

* Tue Sep 08 2020 Stanislav Levin <slev@altlinux.org> 0.14.0-alt1
- 0.10.0 -> 0.14.0.

* Tue Jan 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.10.0-alt1
- Initial build for Sisyphus

