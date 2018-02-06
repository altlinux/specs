%define _unpackaged_files_terminate_build 1
%define oname docutils
%def_with python3

Summary: Docutils -- Python Documentation Utilities
Version: 0.14
Release: alt1.1
%setup_python_module %oname
Name: %packagename
License: public domain, Python, BSD, GPL (see COPYING.txt)
Group: Development/Python
BuildArch: noarch

URL: http://docutils.sourceforge.net/
Packager: Python Development Team <python@packages.altlinux.org>

# git://repo.or.cz/docutils.git
Source: %{oname}-%{version}.tar.gz
Patch: docutils-ALT-disable_assert.patch

Conflicts: Zope-docutils

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python-tools-2to3
%add_python3_req_skip pygments
%add_python3_req_skip pygments.formatter
%endif
%add_python_req_skip pygments

%description
Docutils is a modular system for processing documentation
into useful formats, such as HTML, XML, and LaTeX.  For
input Docutils supports reStructuredText, an easy-to-read,
what-you-see-is-what-you-get plaintext markup syntax.

%if_with python3
%package -n python3-module-%oname
Summary: Docutils -- Python 3 Documentation Utilitie
Group: Development/Python3

%description -n python3-module-%oname
Docutils is a modular system for processing documentation
into useful formats, such as HTML, XML, and LaTeX.  For
input Docutils supports reStructuredText, an easy-to-read,
what-you-see-is-what-you-get plaintext markup syntax.

%package -n python3-module-%oname-tests
Summary: Tests for Docutils -- Python 3 Documentation Utilitie
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Docutils is a modular system for processing documentation
into useful formats, such as HTML, XML, and LaTeX.  For
input Docutils supports reStructuredText, an easy-to-read,
what-you-see-is-what-you-get plaintext markup syntax.

This package contains tests for Docutils.
%endif

%prep
%setup -q -n %{oname}-%{version}
%patch -p2

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
find -type f -name '*.py' -exec sed -i 's|%_bindir/python|%_bindir/python3|' -- '{}' +
find -type f -name '*.py' -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in *; do
	mv $i py3_$i
done
popd
%endif
%python_install --optimize=2
mkdir -p %buildroot%_datadir/%modulename
cp -a tools %buildroot%_datadir/%modulename

#install -p -m644 docutils/utils/roman.py \
#	%buildroot%python_sitelibdir

%check
#export LC_ALL=en_US.UTF-8
#python test/alltests.py
#if_with python3
%if 0
pushd ../python3
python3 %buildroot%python3_sitelibdir/test/alltests.py
popd
%endif

%files
%doc docs *.txt
%_datadir/%modulename
%python_sitelibdir/*
%_bindir/rst*
%if_with python3
%exclude %_bindir/py3_*

%files -n python3-module-%oname
%_bindir/py3_*
%python3_sitelibdir/*
#exclude %python3_sitelibdir/test
%exclude %python3_sitelibdir/%modulename/examples.py*
#exclude %python3_sitelibdir/tools/editors/emacs/tests
#exclude %python3_sitelibdir/tools/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/%modulename/examples.py*
#python3_sitelibdir/tools/editors/emacs/tests
#python3_sitelibdir/tools/test
%endif

%changelog
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
