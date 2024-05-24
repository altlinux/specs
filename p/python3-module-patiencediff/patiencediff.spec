Name: python3-module-patiencediff
Version: 0.2.15
Release: alt1

Summary: This package contains the implementation of the patiencediff algorithm, as first described by Bram Cohen

License: GPLv2
Group: Development/Python3
URL: https://pypi.org/project/patiencediff
VCS: https://github.com/breezy-team/patiencediff

Packager: Anatoly Kitaikin <cetus@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
This package contains the implementation of the patiencediff algorithm, as first described by Bram Cohen.

Like Python's difflib, this module provides both a convience unified_diff function for the generation of
unified diffs of text files as well as a SequenceMatcher that can be used on arbitrary lists.

Patiencediff provides a good balance of performance, nice output for humans, and implementation simplicity.

The code in this package was extracted from the Bazaar code base.

The package comes with two implementations:

 - A Python implementation (_patiencediff_py.py); this implementation only requires a Python interpreter and
   is the more readable version of the two
 - A C implementation implementation (_patiencediff_c.c); this implementation is faster, but requires a C compiler
   and is less readable

%package tests
Summary: patiencediff tests
Group: Development/Other

Requires: %name = %version-%release

%description tests
This package contains tools and test suites for testing patiencediff python module.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc AUTHORS README.rst
%_bindir/patiencediff
%python3_sitelibdir/patiencediff
%exclude %python3_sitelibdir/patiencediff/test*
%python3_sitelibdir/patiencediff-%version.dist-info

%files tests
%python3_sitelibdir/patiencediff/test*

%changelog
* Fri May 24 2024 Grigory Ustinov <grenka@altlinux.org> 0.2.15-alt1
- Automatically updated to 0.2.15.

* Fri Oct 21 2022 Anatoly Kitaykin <cetus@altlinux.org> 0.2.4-alt1
- Release 0.2.4

* Tue Jun 29 2021 Anatoly Kitaykin <cetus@altlinux.org> 0.2.2-alt1
- Release 0.2.2

* Tue Feb 02 2021 Anatoly Kitaykin <cetus@altlinux.org> 0.2.1-alt1
- Release 0.2.1

* Fri Jul 10 2020 Anatoly Kitaikin <cetus@altlinux.org> 0.2.0-alt1
- First build


