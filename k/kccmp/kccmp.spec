Name: kccmp
Version: 0.2
Release: alt2

Summary: Kernel configuration comparison
License: GPL
Group: Development/Kernel
Url: http://stoopidsimple.com/kccmp

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source: http://stoopidsimple.com/files/%name-%version.tar.gz
Patch0: %name-0.2-alt-compile-fix.patch

BuildPreReq: gcc-c++
BuildRequires(pre): libqt3-devel

%description
kccmp is a simple tool for comparing two linux kernel ".config" files.
It has the following features:
 1. Displays the configuration variables with different values in a
table form.
 2. Displays the configuration variables and values which are found in
only one of the compared files.

%prep
%setup
%patch0 -p1
%__subst 's|^LIBS.*|#\0|' %name.pro

%build
export PATH=$PATH:%_qt3dir/bin
qmake
%make_build CXXFLAGS="%optflags"

%install
mkdir -p %buildroot%_bindir/
install -p %name %buildroot%_bindir/

%files
%_bindir/*
%doc README

%changelog
* Sun Oct 26 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.2-alt2
- fix build

* Mon Oct 03 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.2-alt1
- initial build
