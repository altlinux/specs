%define oname progressbar2
%def_with check

Name: python3-module-%oname
Version: 4.5.0
Release: alt1

Summary: Text progress bar library for Python

License: LGPLv2.1+ or BSD
Group: Development/Python3
URL: https://pypi.org/project/progressbar2
VCS: https://github.com/WoLpH/python-progressbar

Source: %name-%version.tar
Patch1: %oname-3.34.4-alt-doc.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-freezegun
BuildRequires: python3-module-python_utils
BuildRequires: python3-module-dill
%endif

BuildArch: noarch

Conflicts: python3-module-progressbar

%description
A text progress bar is typically used to display the progress of a long
running operation, providing a visual cue that processing is underway.

The ProgressBar class manages the current progress, and the format of
the line is given by a number of widgets. A widget is an object that may
display differently depending on the state of the progress bar.

%prep
%setup
%patch1 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
sed -i '/cov/d' pytest.ini
%pyproject_run_pytest

%files
%doc LICENSE examples.py *.rst
%_bindir/progressbar
%python3_sitelibdir/progressbar
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Wed Sep 25 2024 Grigory Ustinov <grenka@altlinux.org> 4.5.0-alt1
- Automatically updated to 4.5.0.

* Tue Mar 05 2024 Grigory Ustinov <grenka@altlinux.org> 4.4.2-alt1
- Automatically updated to 4.4.2.

* Tue Feb 27 2024 Grigory Ustinov <grenka@altlinux.org> 4.4.1-alt1
- Automatically updated to 4.4.1.

* Tue Jan 23 2024 Grigory Ustinov <grenka@altlinux.org> 4.3.2-alt1
- Automatically updated to 4.3.2.

* Thu Oct 27 2022 Grigory Ustinov <grenka@altlinux.org> 4.2.0-alt1
- Automatically updated to 4.2.0.

* Wed Oct 19 2022 Grigory Ustinov <grenka@altlinux.org> 4.1.1-alt1
- Automatically updated to 4.1.1.

* Fri Oct 14 2022 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt1
- Automatically updated to 4.0.0.

* Mon Sep 05 2022 Evgeny Sinelnikov <sin@altlinux.org> 3.55.0-alt1
- Update to new version with support of python-3.8 and later.

* Tue Apr 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.34.4-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.34.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 22 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.34.4-alt1
- Updated to upstream version 3.34.4.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.6.9-alt1.git20141119.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.6.9-alt1.git20141119.1
- NMU: Use buildreq for BR.

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.9-alt1.git20141119
- Initial build for Sisyphus

