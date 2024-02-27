%define _unpackaged_files_terminate_build 1

%define pypi_name filedepot
%define mod_name depot

%def_with check

Name: python3-module-%pypi_name
Version: 0.11.0
Release: alt1
Summary: Toolkit for storing files and attachments in web applications
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/filedepot/
Vcs: https://github.com/amol-/depot
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# boto is deprecated
%add_pyproject_deps_check_filter boto
# not packaged
%add_pyproject_deps_check_filter google-cloud-storage
%pyproject_builddeps_metadata_extra testing
%endif

%description
DEPOT is a framework for easily storing and serving files in web
applications on Python2.6+ and Python3.2+.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

# drop boto-based connector (boto was replaced with boto3)
rm depot/io/awss3.py

%build
%pyproject_build

%install
%pyproject_install

%check
# skip tests requiring running Mongo
export NO_MONGO=1
%pyproject_run_unittest discover -v

%files
%doc *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Feb 26 2024 Stanislav Levin <slev@altlinux.org> 0.11.0-alt1
- 0.8.0 -> 0.11.0.

* Wed Mar 09 2022 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1
- 0.7.1 -> 0.8.0.

* Wed Dec 04 2019 Anton Farygin <rider@altlinux.ru> 0.7.1-alt1
- 0.7.1
- disabled python2 version

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.0-alt1
- Updated to upstream version 0.5.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.3-alt1.git20150209.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.3-alt1.git20150209.1
- NMU: Use buildreq for BR.

* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20150209
- Initial build for Sisyphus

