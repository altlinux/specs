%define oname zope.tal

%def_with check

Name: python3-module-%oname
Version: 5.0.1
Release: alt1

Summary: Zope3 Template Attribute Languate
License: ZPL-2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.tal/

VCS: https://github.com/zopefoundation/zope.tal.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-zope.i18nmessageid
BuildRequires: python3-module-zope.interface
BuildRequires: python3-module-zope.testrunner
%endif

%add_python3_req_skip cStringIO

%description
The Zope3 Template Attribute Languate (TAL) specifies the custom
namespace and attributes which are used by the Zope Page Templates
renderer to inject dynamic markup into a page. It also includes the
Macro Expansion for TAL (METAL) macro language used in page assembly.

The dynamic values themselves are specified using a companion language,
TALES (see the 'zope.tales' package for more).

%package tests
Summary: Tests for Zope 3 Template Attribute Languate (TAL)
Group: Development/Python3
Requires: %name = %EVR
Requires: python3-module-zope.testing

%description tests
The Zope3 Template Attribute Languate (TAL) specifies the custom
namespace and attributes which are used by the Zope Page Templates
renderer to inject dynamic markup into a page. It also includes the
Macro Expansion for TAL (METAL) macro language used in page assembly.

The dynamic values themselves are specified using a companion language,
TALES (see the 'zope.tales' package for more).

This package contains tests for Zope3 Template Attribute Languate.

%prep
%setup

%build
%python3_build

%install
%python3_install

%if "%_lib" == "lib64"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

%check
%tox_check

%files
%doc *.rst
%python3_sitelibdir/zope/tal
%python3_sitelibdir/%oname-%version-*.egg-info
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/runtest.*
%exclude %python3_sitelibdir/*/*/*/runtest.*

%files tests
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/runtest.*
%python3_sitelibdir/*/*/*/runtest.*


%changelog
* Wed Feb 22 2023 Anton Vyatkin <toni@altlinux.org> 5.0.1-alt1
- new version 5.0.1

* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.2.0-alt3
- python2 disabled

* Thu Feb 08 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.2.0-alt2
- fix lib/lib64 stupidity

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Aug 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.0-alt1
- Updated to upstream version 4.2.0.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.2-alt1.dev0.git10150605.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt1.dev0.git10150605
- Version 4.1.2.dev0

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git10141229
- Version 4.1.1.dev0

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1.dev.git10140113
- Version 4.0.1dev

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Version 4.0.0

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a1
- Version 4.0.0a1

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.6.1-alt1.1
- Rebuild with Python-3.3

* Tue Apr 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Version 3.6.1
- Added module for Python 3

* Thu Dec 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Version 3.6.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.2-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt3
- Added necesssary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt1
- Initial build for Sisyphus

