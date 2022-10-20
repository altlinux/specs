%define _unpackaged_files_terminate_build 1
%define pypi_name vine

%def_with check

Name: python3-module-%pypi_name
Version: 5.0.0
Release: alt2

Summary: Python promises

License: BSD
Group: Development/Python3
Url: https://pypi.org/project/vine/
VCS: https://github.com/celery/vine.git

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

%description
Promises, promises, promises.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
# override upstream's config (it's too much to patch)
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.rst
%python3_sitelibdir/vine/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 20 2022 Stanislav Levin <slev@altlinux.org> 5.0.0-alt2
- Repackaged 5.0.0 (1.3.0 -> 5.0.0).

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 5.0.0-alt1
- new version 5.0.0 (with rpmrb script)

* Tue Oct 13 2020 Stanislav Levin <slev@altlinux.org> 1.3.0-alt2
- Stopped Python2 package build(Python2 EOL).

* Sun Jun 09 2019 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)
- switch to build from tarball

* Wed Oct 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.4-alt1
- Initial build for ALT.
