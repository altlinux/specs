%define _unpackaged_files_terminate_build 1
%define oname simplejson

Name: python3-module-%oname
Version: 3.18.1
Release: alt1

Summary: Simplejson is a simple, fast, extensible JSON encoder/decoder for Python

License: MIT/X Consortium
Group: Development/Python3
Url: https://simplejson.readthedocs.io/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-sphinx-sphinx-build-symlink

%description
Simplejson is a simple, fast, complete, correct and extensible JSON
encoder and decoder for Python 2.3+. It is pure Python code with no
dependencies.

%package doc
Summary: Documentation for %name
Group: Development/Python
BuildArch: noarch

%description doc
Simplejson is a simple, fast, complete, correct and extensible JSON
encoder and decoder for Python 2.3+. It is pure Python code with no
dependencies.

This package contains documentation for simplejson.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

python3 ./scripts/make_docs.py

%install
%python3_install
# python2 compat only
rm -f %buildroot/%python3_sitelibdir/%oname/ordered_dict.py

%check
python3 setup.py test

%files
%python3_sitelibdir/%oname/
%exclude %python3_sitelibdir/%oname/tests
%python3_sitelibdir/*.egg-info

%files doc
%doc docs/*


%changelog
* Sun Jan 22 2023 Vitaly Lipatov <lav@altlinux.ru> 3.18.1-alt1
- new version 3.18.1 (with rpmrb script)

* Tue Apr 05 2022 Vitaly Lipatov <lav@altlinux.ru> 3.17.6-alt1
- new version 3.17.6 (with rpmrb script)

* Sun Jul 04 2021 Vitaly Lipatov <lav@altlinux.ru> 3.17.2-alt1
- build python3 module separately
- new version 3.17.2 (with rpmrb script)

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 3.15.0-alt3.qa1
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 3.15.0-alt2.qa1
- NMU: remove %ubt from release

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 3.15.0-alt1.qa1%ubt
- NMU: applied repocop patch

* Thu Jun 14 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.15.0-alt1%ubt
- Updated to upstream version 3.15.0.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.11.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.11.1-alt1
- Updated to upstream version 3.11.1.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.10.0-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.8.0-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Jul 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.0-alt1
- Version 3.8.0

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.5-alt1
- Version 3.6.5

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt1
- Version 3.5.3
- Added module for Python 3

* Wed Dec 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.1-alt1
- Version 3.3.1

* Mon Sep 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1
- Version 3.3.0

* Mon Apr 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1
- Version 2.5.0

* Tue Feb 07 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.3-alt1
- 2.1.3
- enable tests

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.2-alt2.1
- Rebuild with Python-2.7

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt2
- Rebuilt for debuginfo

* Sun Nov 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1
- Version 2.1.2

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1
- Version 2.1.1

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.9-alt1.1
- Rebuilt with python 2.6

* Fri May 29 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.9-alt1
- 2.0.9
- numerous spec fixes
- package documentation
- don't package tests

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 1.7.4-alt1.1
- Rebuilt with python-2.5.

* Thu Nov 15 2007 Gennady Kovalev <gik@altlinux.ru> 1.7.4-alt1
- 1.7.4 release

* Wed Mar 22 2006 Gennady Kovalev <gik@altlinux.ru> 1.1-alt1
- Initial build
