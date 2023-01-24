%define _unpackaged_files_terminate_build 1
%define pypi_name cloudpickle

%def_with check

Name: python3-module-%pypi_name
Version: 2.2.1
Release: alt1
Summary: Extended pickling support for Python objects
Group: Development/Python
License: BSD

Url: https://pypi.org/project/cloudpickle
VCS: https://github.com/cloudpipe/cloudpickle

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# synced to dev-requirements.txt
BuildRequires: python3(pytest)
BuildRequires: python3(psutil)
# for psutil
BuildRequires: /proc
BuildRequires: python3(tornado)
%endif

%description
cloudpickle makes it possible to serialize Python constructs
not supported by the default pickle module from the Python standard
library. cloudpickle is especially useful for cluster computing where
Python expressions are shipped over the network to execute on remote
hosts, possibly close to the data. Among other things, cloudpickle
supports pickling for lambda expressions, functions and classes defined
interactively in the __main__ module.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# _cloudpickle_testpkg should be actually built and installed
export PYTHONPATH=tests/cloudpickle_testpkg

# file_handles tests fail, TypeError: cannot pickle '_io.FileIO' object
# GH issue: https://github.com/cloudpipe/cloudpickle/issues/114
%pyproject_run_pytest -vra -k "not file_handles"

%files
%doc README.md
%python3_sitelibdir/cloudpickle/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Jan 24 2023 Stanislav Levin <slev@altlinux.org> 2.2.1-alt1
- 2.0.0 -> 2.2.1.

* Mon Nov 14 2022 Stanislav Levin <slev@altlinux.org> 2.0.0-alt2
- Fixed FTBFS (pytest 7.2).

* Thu Feb 03 2022 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt1
- New version 2.0.0
- fix packaging with python >= 3.10

* Sun May 24 2020 Anton Midyukov <antohami@altlinux.org> 1.4.1-alt1
- New version 1.4.1

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1.qa1
- NMU: applied repocop patch

* Fri Oct 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.0-alt1
- Initial build for ALT.

* Wed Aug 09 2017 Lumir Balhar <lbalhar@redhat.com> - 0.3.1-1
- Initial package.
