%define _unpackaged_files_terminate_build 1

%define oname docutils
%def_enable check
Summary: Docutils -- Python Documentation Utilities
Version: 0.15.2
Release: alt1
Name: python3-module-%oname
License: public domain, Python, BSD, GPL (see COPYING.txt)
Group: Development/Python3
BuildArch: noarch

URL: http://docutils.sourceforge.net/
# https://pypi.org/project/docutils/
Source: %name-%version.tar
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%add_python3_req_skip pygments
%add_python3_req_skip pygments.formatter

%description 
Docutils is a modular system for processing documentation
into useful formats, such as HTML, XML, and LaTeX.  For
input Docutils supports reStructuredText, an easy-to-read,
what-you-see-is-what-you-get plaintext markup syntax.

%prep
%setup -q

%build
%python3_build

%install
%python3_install

%check
python3 test3/alltests.py

%files
%_bindir/*
%python3_sitelibdir/*

%changelog
* Tue Dec 17 2019 Anton Farygin <rider@altlinux.ru> 0.15.2-alt1
- 0.14 -> 0.15.2
- renamed to python3-module-docutils

* Fri Aug 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.14-alt2
- Renamed resulting binaries, removed .py suffix (Closes: #35274).
- Removed python3-module-docutils-tests subpackage.

* Tue Feb 06 2018 Stanislav Levin <slev@altlinux.org> 0.14-alt1.1
- (NMU) Fix Requires to pygments.formatter

* Wed Oct 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.14-alt1
- Updated to upstream version 0.14.

* Thu Mar 23 2017 Fr. Br. George <george@altlinux.ru> 0.13.1-alt2
- Comment out buggy assertion again

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.13.1-alt1
- automated PyPI update

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.13-alt4.git20150716.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.13-alt4.git20150716.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Mar 02 2016 Dmitry V. Levin <ldv@altlinux.org> 0.13-alt4.git20150716
- Remove pygments from requirements.
- Packages subdirectories.

* Thu Aug 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt3.git20150716
- Disabled bad assert

* Thu Aug 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt2.git20150716
- Snapshot from git

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.svn20150603
- New snapshot

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.svn20140708
- Version 0.13

* Mon Sep 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt1.svn20130917
- Version 0.12

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt2.svn20130117
- Use 'find... -exec...' instead of 'for ... $(find...'

* Wed Mar 20 2013 Aleksey Avdeev <solo@altlinux.ru> 0.11-alt1.svn20130117.1
- Rebuild with Python-3.3

* Fri Jan 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.svn20130117
- Version 0.11

* Wed Apr 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt3
- Extracted tests into separate package

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt2
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1
- Version 0.9, snapshot 20111212

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7-alt1.1
- Rebuild with Python-2.7

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Version 0.7

* Thu Jan 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.20100119-alt1
- Version 0.6, upstream snapshot 20100119

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.1
- Rebuilt with python 2.6

* Thu Apr 16 2009 Fr. Br. George <george@altlinux.ru> 0.5-alt1
- Version up
- tools and docs packaged

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.4-alt1.1
- Rebuilt with python-2.5.

* Tue Feb 07 2006 Ivan Fedorov <ns@altlinux.ru> 0.4-alt1
- Initial build for ALT Linux
