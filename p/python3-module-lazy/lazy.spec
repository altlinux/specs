%define _unpackaged_files_terminate_build 1
%define pypi_name lazy
%define mod_name %pypi_name

Name: python3-module-%pypi_name
Version: 2.0
Release: alt1
Summary: Lazy attributes for Python objects
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/lazy/
Vcs: https://github.com/stefanholek/lazy
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
Lazy attributes are computed attributes that are evaluated only once,
the first time they are used. Subsequent uses return the results of the
first call. They come handy when code should run

* late, i.e. just before it is needed, and
* once, i.e. not twice, in the lifetime of an object.

You can think of it as deferred initialization. The possibilities are
endless.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build --backend-config-settings='{"--build-option": ["egg_info", "--tag-build=''", "--no-date"]}'

%install
%pyproject_install

%check
%pyproject_run_unittest discover

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jul 06 2026 Stanislav Levin <slev@altlinux.org> 2.0-alt1
- 1.6 -> 2.0

* Mon Jun 03 2024 Stanislav Levin <slev@altlinux.org> 1.6-alt1
- 1.3 -> 1.6.

* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.3-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3-alt1.git20140420.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt1.git20140420.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20140420
- Initial build for Sisyphus

