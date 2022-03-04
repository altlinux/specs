%define _unpackaged_files_terminate_build 1
%define oname distlib

%def_with check

Name: python3-module-%oname
Version: 0.3.4
Release: alt1

Summary: Low-level functions for packaging and distribution of Python software
License: Python
Group: Development/Python3
# Source-git: https://bitbucket.org/pypa/distlib.git
Url: https://pypi.org/project/distlib/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(tox)
%endif

BuildArch: noarch

%description
%oname is a library of packaging functionality which is intended to be used as
the basis for third-party packaging tools. Using a common layer will improve
interoperability and consistency of user experience across those tools which
use the library.

%prep
%setup
%patch -p1

# win files
rm -v distlib/*.exe

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
export SKIP_ONLINE=yes
export TOX_TESTENV_PASSENV='SKIP_ONLINE'
tox.py3 --sitepackages -vvr

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Fri Mar 04 2022 Stanislav Levin <slev@altlinux.org> 0.3.4-alt1
- 0.3.1 -> 0.3.4.

* Mon Oct 26 2020 Stanislav Levin <slev@altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus.

