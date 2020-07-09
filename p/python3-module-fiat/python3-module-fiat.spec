%define _unpackaged_files_terminate_build 1

%define origname FIAT

Name: python3-module-fiat
Version: 2019.1.0
Release: alt1
Summary: FInite element Automatic Tabulator
Group: Development/Python3
License: LGPLv3+
URL: https://fenicsproject.org/

BuildArch: noarch

# https://bitbucket.org/fenics-project/fiat.git
Source: %name-%version.tar


BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
FIAT is a FInite element Automatic Tabulator.

%prep
%setup

%build
%python3_build

%install
%python3_build_install --optimize=2

%files
%doc COPYING COPYING.LESSER
%doc AUTHORS ChangeLog.rst README.rst
%python3_sitelibdir/*

%changelog
* Thu Jul 09 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2019.1.0-alt1
- Updated to upstream version 2019.1.0.
- Switched to python-3.

* Tue Mar 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.0-alt2.dev.git20150429
- Updated build dependencies.

* Sat May 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.dev.git20150429
- Version 1.6.0dev

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.git20140730
- Version 1.4.0

* Wed May 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20140214
- Version 1.3.0

* Tue May 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20130411
- New snapshot

* Thu Jan 31 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.bzr20130108
- Version 1.1.0

* Mon Oct 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2.bzr20121001
- New snapshot

* Mon Aug 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2.bzr20120610
- New snapshot

* Sun May 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2.bzr20111207
- Rebuilt with updated NumPy

* Tue Jan 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.bzr20111207
- Version 1.0.0

* Tue Dec 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.beta.bzr20110811
- Version 1.0-beta

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.9-alt1.bzr20110625.1
- Rebuild with Python-2.7

* Wed Aug 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt1.bzr20110625
- New snapshot

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt1.bzr20110223
- Version 0.9.9

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.bzr20101018
- New snapshot

* Tue Aug 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.bzr20100701
- Version 0.9.2

* Mon Jul 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.bzr20100304.1
- Rebuilt

* Wed Jun 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.bzr20100304
- Version 0.9.1

* Wed Dec 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt4.bzr20091124
- New snapshot

* Tue Nov 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt3.hg20090831.1
- Rebuilt with python 2.6

* Mon Aug 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt3.hg20090831
- Snapshot 20090831

* Tue Jul 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt3.hg20090819
- New snapshot

* Fri Apr 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt2
- Build as noarch package

* Fri Apr 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1
- Initial build for Sisyphus
