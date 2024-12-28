Name: alterator-python-functions

Version: 1.0.0
Release: alt1

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

Requires: gettext

Conflicts: alterator < 3.4-alt1

BuildArch: noarch

Source: %name-%version.tar

Summary: Binding functions for Alterator Python based backends
License: GPLv3
Group: Development/Python3

%description
Binding functions for Alterator Python based backends.
Note that the module is `alterator_bindings.backend3`

%prep
%setup -q

%build
%pyproject_build

%check
%pyproject_run_unittest

%install
%pyproject_install

%files
%python3_sitelibdir_noarch/alterator_bindings/*
%doc README.md

%changelog
* Fri Dec 27 2024 Sergey Konev <darisishe@altlinux.org> 1.0.0-alt1
- Initial version
