%define _unpackaged_files_terminate_build 1
%define pypi_name flickrapi
%define mod_name %pypi_name

Name: python3-module-%pypi_name
Version: 2.4.0
Release: alt3

Summary: The official Python interface to the Flickr API
License: Python
Group: Development/Python3
Url: https://pypi.org/project/flickrapi/
Vcs: https://github.com/sybrenstuvel/flickrapi/
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
The easiest to use, most complete, and most actively developed Python
interface to the Flickr API.It includes support for authorized and
non-authorized access, uploading and replacing photos, and all Flickr
API functions.

%prep
%setup
%pyproject_deps_resync_build

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE.txt
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Jul 20 2023 Stanislav Levin <slev@altlinux.org> 2.4.0-alt3
- Fixed FTBFS (missing build dependency on six).

* Fri Dec 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.4.0-alt2
- build for python2 disabled

* Tue Mar 27 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.4.0-alt1
- Version 2.4.0
  Fixed deps in setup.py

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4-alt1
- Initial build for Sisyphus
