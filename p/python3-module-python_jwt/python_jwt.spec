%define  modulename python_jwt

# needs stale pyvows
%def_without check

Name:    python3-module-%modulename
Version: 3.3.2
Release: alt1

Summary: Module for generating and verifying JSON Web Tokens

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/python-jwt

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

%description
%summary.

%prep
%setup
# Remove bundled egg-info
rm -rf %modulename.egg-info

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=$PWD
%__python3 ./test/run/run_pyvows.py -v test

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version-py%_python3_version.egg-info
%doc LICENCE *.md

%changelog
* Thu Jun 02 2022 Grigory Ustinov <grenka@altlinux.org> 3.3.2-alt1
- Initial build for Sisyphus.
