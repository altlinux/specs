Name: kccmp
Version: 0.3
Release: alt1

Summary: Kernel configuration comparison
License: GPL
Group: Development/Kernel
Url: http://stoopidsimple.com/kccmp

Source: http://stoopidsimple.com/files/%name-%version.tar.gz

BuildPreReq: gcc-c++
BuildRequires(pre): libqt4-devel

%description
kccmp is a simple tool for comparing two linux kernel ".config" files.
It has the following features:
 1. Displays the configuration variables with different values in a
table form.
 2. Displays the configuration variables and values which are found in
only one of the compared files.

%prep
%setup
subst 's|^LIBS.*|#\0|' %name.pro

%build
export PATH=$PATH:%_qt4dir/bin
qmake
%make_build CXXFLAGS="%optflags"

%install
mkdir -p %buildroot%_bindir/
install -p %name %buildroot%_bindir/

%files
%_bindir/*
%doc README

%changelog
* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Version 0.3

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.2-alt2.qa1
- NMU: rebuilt for debuginfo.

* Sun Oct 26 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.2-alt2
- fix build

* Mon Oct 03 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.2-alt1
- initial build
