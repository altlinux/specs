%define oname mdp

# 16 tests (test_dtype_consistency) fail on armh
%ifnarch armh
%def_with check
%else
%def_without check
%endif

Name: python3-module-%oname
Version: 3.6
Release: alt1

Summary: Modular toolkit for Data Processing

Group: Development/Python3
License: BSD-3-Clause
URL: https://pypi.org/project/MDP/
VCS: https://github.com/mdp-toolkit/mdp-toolkit

Source: %name-%version.tar
Source1: MDP-tutorial.pdf

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-future
BuildRequires: python3-module-numpy-testing
%endif

%add_python3_req_skip shogun UserDict pp libsvm.svmutil

%description
Modular toolkit for Data Processing (MDP) is a Python data processing
framework.

From the user's perspective, MDP is a collection of supervised and
unsupervised learning algorithms and other data processing units that
can be combined into data processing sequences and more complex
feed-forward network architectures.

From the scientific developer's perspective, MDP is a modular framework,
which can easily be expanded. The implementation of new algorithms is
easy and intuitive. The new implemented units are then automatically
integrated with the rest of the library.

The base of available algorithms is steadily increasing and includes, to
name but the most common, Principal Component Analysis (PCA and NIPALS),
several Independent Component Analysis algorithms (CuBICA, FastICA,
TDSEP, JADE, and XSFA), Slow Feature Analysis, Gaussian Classifiers,
Restricted Boltzmann Machine, and Locally Linear Embedding.

%package tests
Summary: Tests for Modular toolkit for Data Processing
Group: Development/Python3
Requires: %name = %EVR

%description tests
Modular toolkit for Data Processing (MDP) is a Python data processing
framework.

This package contains tests for MDP.

%package doc
Summary: Documentation for Modular toolkit for Data Processing
Group: Development/Documentation
BuildArch: noarch

%description doc
Modular toolkit for Data Processing (MDP) is a Python data processing
framework.

This package contains documentation for MDP.

%prep
%setup
install -p -m644 %SOURCE1 .

sed -i 's|#! /usr/bin/env python|#! /usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%check
%tox_create_default_config
%tox_check -- mdp
%tox_check -- bimdp

%files
%python3_sitelibdir/bimdp
%python3_sitelibdir/%oname
%python3_sitelibdir/MDP-%version-*.egg-info
%exclude %python3_sitelibdir/%oname/test
%exclude %python3_sitelibdir/bimdp/test

%files tests
%python3_sitelibdir/%oname/test
%python3_sitelibdir/bimdp/test

%files doc
%doc *.pdf CHANGES CHECKLIST COPYRIGHT
%doc README TODO


%changelog
* Mon Mar 13 2023 Anton Vyatkin <toni@altlinux.org> 3.6-alt1
- New version 3.6

* Sun Nov 22 2020 Vitaly Lipatov <lav@altlinux.ru> 3.5-alt2
- cleanup spec

* Fri Nov 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.5-alt1
- Version updated to 3.5
- disable python2, enable python3

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt2.git20140427
- Fixed build

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt1.git20140427
- New snapshot

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt1.git20130903
- Version 3.4

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3-alt1.git20111024
- Version 3.3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2-alt1.git20110415.1
- Rebuild with Python-2.7

* Thu May 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt1.git20110415
- Version 3.2

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1.git20101123
- New snapshot

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1.git20100725
- Version 2.6

* Thu Mar 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.svn20091007.2
- Extracted tests into separate packages
- Added
  + pickles package
  + examples

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.svn20091007.1
- Rebuilt with python 2.6

* Fri Oct 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.svn20091007
- Initial build for Sisyphus

