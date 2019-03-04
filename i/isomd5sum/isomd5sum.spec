# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: isomd5sum
Version: 1.2.3
Release: alt1

Summary: Utilities to implant/verify md5sum in ISO images
License: %gpl2plus
Group: System/Base
Url: https://github.com/rhinstaller/isomd5sum
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses rpm-build-python3
BuildRequires: libpopt-devel python3-devel

%description
This package contains utilities for implanting and verifying
MD5 checksum in an ISO9660 image.

%package -n python3-module-%name
Summary: Python module for isomd5sum
Group: Development/Python
Requires: %name = %EVR

%description -n python3-module-%name
This package contains python module for implanting and verifying
MD5 checksum in an ISO9660 image.

%package devel
Summary: Development headers and library for isomd5sum
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains header files and a library for implanting
and verifying MD5 checksum in an ISO9660 image.

%prep
%setup

%build
PYTHON=%__python3 make checkisomd5 implantisomd5 pyisomd5sum.so

%install
PYTHON=%__python3 %makeinstall_std

%files
%doc COPYING
%_bindir/implantisomd5
%_bindir/checkisomd5
%_mandir/man*/*

%files -n python3-module-%name
%python3_sitelibdir/pyisomd5sum.so

%files devel
%_includedir/*.h
%_libdir/*.a
%_datadir/pkgconfig/isomd5sum.pc

%changelog
* Mon Mar 04 2019 Anton Midyukov <antohami@altlinux.org> 1.2.3-alt1
- 1.2.3

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.12-alt1.1
- NMU: added URL

* Mon Mar 31 2014 Michael Shigorin <mike@altlinux.org> 1.0.12-alt1
- 1.0.12
- switched to upstream git
- separate python subpackage
- spec cleanup

* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt0.20080218.2
- Fixed build

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.4-alt0.20080218.1.1
- Rebuild with Python-2.7

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt0.20080218.1
- Rebuilt with python 2.6

* Mon Feb 18 2008 Andriy Stepanov <stanv@altlinux.ru> 1.0.4-alt0.20080218
- sources from fedora git repository 2008 Feb 18
