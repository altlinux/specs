Name: isomd5sum
Version: 1.0.12
Release: alt1.1

Summary: Utilities to implant/verify md5sum in ISO images
License: %gpl2plus
Group: System/Base
Url: https://github.com/rhinstaller/isomd5sum

#Url: http://git.fedorahosted.org/git/?p=isomd5sum.git;a=summary
#Source: http://fedorahosted.org/releases/i/s/isomd5sum/%name-%version.tar.bz2
Source: %name-%version.tar
Packager: Andriy Stepanov <stanv@altlinux.ru>

# Automatically added by buildreq on Tue Feb 19 2008
BuildRequires: libpopt-devel python-devel
BuildPreReq: rpm-build-licenses

%description
This package contains utilities for implanting and verifying
MD5 checksum in an ISO9660 image.

%package -n python-module-%name
Summary: Python module for isomd5sum
Group: Development/Python
Requires: %name = %version-%release

%description -n python-module-%name
This package contains python module for implanting and verifying
MD5 checksum in an ISO9660 image.

%package devel
Summary: Development headers and library for isomd5sum
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains header files and a library for implanting
and verifying MD5 checksum in an ISO9660 image.

%prep
%setup

%build
%make

%install
%makeinstall_std

%files
%doc COPYING
%_bindir/implantisomd5
%_bindir/checkisomd5
%_mandir/man*/*

%files -n python-module-%name
%python_sitelibdir/pyisomd5sum.so

%files devel
%_includedir/*.h
%_libdir/*.a

%changelog
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
