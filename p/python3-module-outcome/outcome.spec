%define  modulename outcome

%def_with check

Name:    python3-module-%modulename
Version: 1.2.0
Release: alt1

Summary: Capture the outcome of Python function calls
License: MIT or Apache-2.0
Group:   Development/Python
URL:     https://github.com/python-trio/outcome

Packager: Evgeny Sinelnikov <sin@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

Source:  %name-%version.tar

%description
Capture the outcome of Python function calls. Extracted from the Trio project.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%tox_create_default_config
%tox_check

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version-py%_python3_version.egg-info
%doc *.md *.rst

%changelog
* Wed Feb 08 2023 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt1
- Automatically updated to 1.2.0.
- Build with check.

* Tue Jan 15 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
