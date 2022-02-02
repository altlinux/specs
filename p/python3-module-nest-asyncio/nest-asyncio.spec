%define _unpackaged_files_terminate_build 1

%define oname nest_asyncio
%define pkgname nest-asyncio

Name: python3-module-%pkgname
Version: 1.5.4
Release: alt1
Summary: Patch asyncio to allow nested event loops 
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/nest-asyncio/

BuildArch: noarch

# https://github.com/erdewit/nest_asyncio
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: /usr/bin/py.test3

%description
By design asyncio does not allow its event loop to be nested.
This presents a practical problem: When in an environment
where the event loop is already running it's impossible to run tasks
and wait for the result. Trying to do so will give the error
"RuntimeError: This event loop is already running".

The issue pops up in various environments, such as web servers,
GUI applications and in Jupyter notebooks.

This module patches asyncio to allow nested use of asyncio.run
and loop.run_until_complete.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
py.test3 -vv tests

%files
%doc LICENSE
%doc README.rst
%python3_sitelibdir/%oname.py
%python3_sitelibdir/__pycache__/%{oname}.*
%python3_sitelibdir/%oname-%version-py3*.egg-info

%changelog
* Wed Feb 02 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.4-alt1
- Updated to upstream version 1.5.4.

* Mon Aug 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.1-alt1
- Updated to upstream version 1.5.1.

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.0-alt1
- Initial build for ALT.
