Name: intercal
Version: 0.29
Release: alt1.git20140828

Summary: The language that kills the weak and drives mad the strong
License: GPL, except for ick-wrap.c
Group: Development/Other
Url: http://www.catb.org/~esr/intercal/

# git://gitorious.org/intercal/intercal.git
Source: %url/%name-%version.tar.gz

BuildPreReq: flex groff-base groff-ps tidy

Requires: gcc

%description
An implementation of the language INTERCAL, legendary for
its perversity and horribleness (this version adds COME FROM
for extra flavor).  Comes with language manual and examples
including possibly the entire extant body of INTERCAL code.
Now supports i18n and l14n (to Ancient Roman locale only)
Now with fix patch by Donald Knuth.

%prep
%setup

%build
%autoreconf
%configure
%make_build
pushd doc
%make_build all
%__rm -f Makefile intercal.refs.tmp
popd

%install
%makeinstall_std

cp -a pit examples
rm -fr examples/{lib,Makefile}

%files
%_bindir/*
%_libdir/*.a
%_includedir/*
%_datadir/ick*
%_infodir/*
%_mandir/man?/*
%doc BUGS NEWS README HISTORY doc/ examples/ etc/%name.el

%changelog
* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.29-alt1.git20140828
- Version 0.29

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.24-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Sep 26 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.24-alt1
- initial build
