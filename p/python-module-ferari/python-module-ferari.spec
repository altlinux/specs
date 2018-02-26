%define origname FErari

Name:           python-module-ferari
Version:        1.0.0
Release:        alt1.bzr20111207
Summary:        Optimizer for finite element code
Group:          Development/Python
License:        LGPLv3+
URL:            http://fenics.org/wiki/FErari
Source:         %origname-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel
%setup_python_module %origname
%py_provides %origname
#py_requires ffc
# for bootstrap
%add_python_req_skip ffc

%description
FErari (Finite Element rearrangement to automatically reduce instructions)
generates optimized code for evaluation of the element tensor (element stiffness
matrix) and functions as an optimizing backend for FFC.

%prep
%setup

%build
%python_build

%install
%python_build_install --optimize=2

%files
%doc AUTHORS ChangeLog README TODO
%python_sitelibdir/*

%changelog
* Tue Jan 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.bzr20111207
- Version 1.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.0-alt1.bzr20110602.1
- Rebuild with Python-2.7

* Wed Aug 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.bzr20110602
- New snapshot

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.bzr20100906.1
- Rebuilt

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.bzr20100906
- New snapshot

* Wed Jun 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.bzr20100212
- Version 0.2.0

* Fri Jan 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt2.bzr20070807.2
- Avoided LinearAlgebra of Numeric

* Thu Dec 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt2.bzr20070807.1
- Rebuild without python-module-Numeric

* Wed Dec 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt2.bzr20070807
- Changed upstream repository: hg -> bzr

* Sun Dec 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.hg20090831.2
- Added requirement on python2.6(ffc)

* Tue Nov 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.hg20090831.1
- Rebuilt with python 2.6

* Mon Aug 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.hg20090831
- Snapshot 20090831

* Wed Aug 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.hg20090819
- New version

* Tue May 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt3
- Remove dependence on util (this is really pg)

* Sat Apr 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt2
- Add requirement on python2.5(ffc)

* Sat Apr 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1
- Initial build for Sisyphus
