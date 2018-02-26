Name: nipy-data
Version: 0.2
Release: alt3.1
Summary: Data files for NIPY (Neuroimaging in Python)
License: MIT
Group: Graphics
Url: http://neuroimaging.scipy.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://nipy.sourceforge.net/data-packages/nipy-data-0.2.tar.gz
Source1: http://nipy.sourceforge.net/data-packages/nipy-templates-0.2.tar.gz
BuildArch: noarch

BuildPreReq: python-devel

%description
The neuroimaging in python (NIPY) project is an environment for the
analysis of structural and functional neuroimaging data. It currently
has a full system for general linear modeling of functional magnetic
resonance imaging (fMRI).

This package contains data files for NIPY.

%prep
%setup
tar -xf %SOURCE1

%build
#%python_build
#pushd nipy-templates
#%python_build
#popd

%install
%python_install --record=INSTALL_FILES
pushd nipy-templates-0.2
%python_install --record=../INSTALL_FILES2
popd
cat INSTALL_FILES2 >>INSTALL_FILES

%files -f INSTALL_FILES

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt3.1
- Rebuild with Python-2.7

* Thu Jul 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt3
- Updated nipy-templates to version 0.2

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Rebuilt with python 2.6

* Mon Sep 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

