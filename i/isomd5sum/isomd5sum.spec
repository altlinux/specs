Summary: Utilities for working with md5sum implanted in ISO images
Name: isomd5sum
Version: 1.0.4
Release: alt0.20080218.2
License: %gpl2plus
Group: System/Base 
Packager:  Andriy Stepanov <stanv@altlinux.ru>
#URL: http://git.fedorahosted.org/git/?p=isomd5sum.git;a=summary
#URL: http://git.altlinux.org/people/stanv/packages/
#Source0: http://fedorahosted.org/releases/i/s/isomd5sum/%{name}-%{version}.tar.bz2
Source0: %{name}-%{version}.tar
Patch0: isomd5sum-1.0.4-alt-no-Werror.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# Automatically added by buildreq on Tue Feb 19 2008
BuildRequires: libpopt-devel python-devel
BuildPreReq: rpm-build-licenses

%description
The isomd5sum package contains utilities for implanting and verifying
an md5sum implanted into an ISO9660 image.

%package devel
Summary: Development headers and library for using isomd5sum 
Group: Development/C
Requires: %{name} = %{version}-%{release}

%description devel
This contains header files and a library for working with the isomd5sum
implanting and checking.

%prep
%setup -q
%patch0 -p2

%build
%make

%install
%make install DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING
%_bindir/implantisomd5
%_bindir/checkisomd5
%{_mandir}/man*/*
%{python_sitelibdir}/pyisomd5sum.so

%files devel
%defattr(-,root,root,-)
%{_includedir}/*.h
%{_libdir}/*.a

%changelog
* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt0.20080218.2
- Fixed build

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.4-alt0.20080218.1.1
- Rebuild with Python-2.7

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt0.20080218.1
- Rebuilt with python 2.6

* Mon Feb 18 2008 Andriy Stepanov <stanv@altlinux.ru> 1.0.4-alt0.20080218
- sources from fedora git repository 2008 Feb 18
