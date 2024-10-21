%define oname wtforms

%def_with check

Name: python3-module-%oname
Version: 3.2.0
Release: alt1

Summary: Form validation and rendering for Python web development

License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/WTForms
Vcs: https://github.com/wtforms/wtforms.git

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-babel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-markupsafe
BuildRequires: python3-module-email-validator
%endif

%description
WTForms is a flexible forms validation and rendering library for python
web development.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Mon Oct 21 2024 Anton Vyatkin <toni@altlinux.org> 3.2.0-alt1
- New version 3.2.0.

* Sun Sep 01 2024 Anton Vyatkin <toni@altlinux.org> 3.1.2-alt2
- Fixed FTBFS.
- Build without docs.

* Sun Jan 07 2024 Andrey Cherepanov <cas@altlinux.org> 3.1.2-alt1
- New version.

* Fri Nov 03 2023 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1
- New version.

* Wed Oct 11 2023 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- New version.

* Sat May 06 2023 Anton Zhukharev <ancieg@altlinux.org> 3.0.1-alt3
- Fixed %%check BR.

* Wed Jan 18 2023 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt2
- Built with pyproject macros.
- Built with check.

* Sat May 28 2022 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt1
- Automatically updated to 3.0.1.

* Fri Jul 31 2020 Andrey Cherepanov <cas@altlinux.org> 2.3.3-alt1
- New version.

* Sun Apr 26 2020 Andrey Cherepanov <cas@altlinux.org> 2.3.1-alt1
- New version.

* Wed Apr 22 2020 Andrey Cherepanov <cas@altlinux.org> 2.3.0-alt1
- New version.

* Tue Apr 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.2.1-alt2
- Build for python2 disabled.

* Tue Mar 24 2020 Andrey Cherepanov <cas@altlinux.org> 2.2.1-alt1
- New version.
- Fix License tag according to SPDX.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1-alt1
- Updated to upstream version 2.1.

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1.dev.git20141210
- New snapshot

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1.dev.git20140718
- Initial build for Sisyphus

