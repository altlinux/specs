Name: alterator-python-functions

Version: 1.0.0
Release: alt3

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

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
* Sat Feb 22 2025 Sergey Konev <darisishe@altlinux.org> 1.0.0-alt3
- Explicit build dependency on python3-module-wheel

* Mon Feb 17 2025 Sergey Konev <darisishe@altlinux.org> 1.0.0-alt2
- Proper 'translate' function implementation

* Fri Dec 27 2024 Sergey Konev <darisishe@altlinux.org> 1.0.0-alt1
- Initial version
