Name:          python-module-pyme
Version:       0.8.1
Release:       alt2.2.1.1
%setup_python_module pyme

Group:         Development/Python
Summary:       PyMe is a python interface to GPGME library
Url:           http://pyme.sourceforge.net/
License:       %gpllgpl2only

Source0:       pyme-%version.tar
Patch0:        %name-%version-%release.patch

Packager:      Yury Yurevich <anarresti@altlinux.org>

BuildRequires(pre): rpm-build-licenses rpm-macros-make
BuildRequires: libgpgme-devel swig python-devel

%description
Pyme is, for the most part, a direct interface to the C GPGME library.
However, it is re-packaged in a more Pythonic way -- object-oriented
with classes and modules.

Features:

- Feature-rich, full implementation of the GPGME library. Supports
  all GPGME features except interactive editing (coming soon).
- Callback functions may be written in pure Python.
- Ability to sign, encrypt, decrypt, and verify data.
- Ability to list keys, export and import keys, and manage the keyring.
- Fully object-oriented with convenient classes and modules.

PyMe's development model is GPGME + Python + SWIG combination
which means that most of the functions and types are converted
from C into Python automatically by SWIG. In short, to be able
to use PyMe you need to be familiar with GPGME.

#--------------------------------------------------------------------

%prep
%setup -n pyme-%version
%patch -p1

%build
%make_ext
%make docs

%install
%make install DESTDIR=%buildroot

%files
%doc examples doc COPYING COPYING.LESSER
%python_sitelibdir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1-alt2.2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1-alt2.2.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt2.2
- Rebuilt for debuginfo

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt2.1
- Rebuilt with python 2.6

* Fri Jul 17 2009 Yury Yurevich <anarresti@altlinux.org> 0.8.1-alt2
- Add large file support to build with gpgme-1.2.0

* Sun May 24 2009 Yury Yurevich <anarresti@altlinux.org> 0.8.1-alt1
- Initial build for ALT Linux
