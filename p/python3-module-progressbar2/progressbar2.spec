%define oname progressbar2

Name: python3-module-%oname
Version: 3.55.0
Release: alt1

Summary: Text progress bar library for Python
License: LGPLv2.1+ or BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/progressbar2/

BuildArch: noarch

# https://github.com/WoLpH/python-progressbar.git
Source: %name-%version.tar
Patch1: %oname-3.34.4-alt-doc.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-runner
BuildRequires: python3-module-python_utils

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
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=$PWD
py.test3 progressbar tests ||:

%files
%doc examples.py *.rst
%python3_sitelibdir/*

%changelog
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

