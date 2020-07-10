# -*- coding: utf-8 -*-
%define _unpackaged_files_terminate_build 1

Name: python3-module-patiencediff
Version: 0.2.0
Release: alt1

Summary: This package contains the implementation of the patiencediff algorithm, as first described by Bram Cohen.
License: GPLv2
Group: Development/Python

Url: https://github.com/breezy-team/patiencediff
Packager: Anatoly Kitaikin <cetus@altlinux.org>

Source: patiencediff-%version.tar

BuildRequires(pre): rpm-build-python3

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

This module is built for python %__python_version

%package tests
Summary: patiencediff tests
Group: Development/Other

Requires: %name = %version-%release

%description tests
This package contains tools and test suites for testing patiencediff python module.

%prep
%setup -n patiencediff-%version

%build
%python3_build

%install
%python3_install --install-lib %python3_sitelibdir

%files
%python3_sitelibdir/patiencediff
%exclude %python3_sitelibdir/patiencediff/test*
%python3_sitelibdir/*.egg-info
%doc AUTHORS README.rst

%files tests
%python3_sitelibdir/patiencediff/test*

%changelog
* Fri Jul 10 2020 Anatoly Kitaikin <cetus@altlinux.org> 0.2.0-alt1
- First build


