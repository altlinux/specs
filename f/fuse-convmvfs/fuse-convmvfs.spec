Name:           fuse-convmvfs
Version:        0.2.6
Release: 	alt1
Summary:        FUSE-Filesystem to convert filesystem encodings

Group:          System/Kernel and hardware
License:        GPL
URL:            http://fuse-convmvfs.sourceforge.net/
Source0:        http://dl.sourceforge.net/sourceforge/fuse-convmvfs/%name-%version.tar.gz

# Automatically added by buildreq on Mon Jun 18 2007
BuildRequires: gcc-c++ libfuse-devel

BuildRequires:  libfuse-devel >= 2.5.0
BuildPreReq: libattr-devel

%description
This is a filesystem client use the FUSE(Filesystem in
USErspace) interface to convert file name from one charset
to another. Inspired by convmv.

%prep
%setup


%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/convmvfs
%doc README* COPYING ChangeLog AUTHORS NEWS THANKS


%changelog
* Sun Sep 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.6-alt1
- Version 0.2.6

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.2.4-alt1.qa1
- NMU: rebuilt for debuginfo.

* Thu Mar 06 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.2.4-alt1
- new version

* Mon Jun 18 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.2.3-alt0.1
- first build

