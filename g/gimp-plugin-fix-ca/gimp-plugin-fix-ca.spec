%define gimpplugindir %(gimptool-2.0 --gimpplugindir)

Name: gimp-plugin-fix-ca
Version: 3.0.2
Release: alt1

Summary: Fix Chromatic Aberration Gimp Plug-In
License: GPLv2+
Group: Graphics

URL: http://kcd.sourceforge.net/fix-ca.php
Source0: http://kcd.sourceforge.net/fix-ca.c

Requires: gimp2 >= 2.2

# Automatically added by buildreq on Fri Sep 14 2007
BuildRequires: libgimp-devel

%description
Fix-CA is able to fix lateral CA caused by lens and colored fringing caused
by light travel through dense material such as glass and water (which is
called directional CA in the program).

%prep
%setup -q -c -T
cp %SOURCE0 .

%build
# TODO: benchmark build with CFLAGS below
#export CFLAGS="%optflags -ffast-math -funroll-loops"
gimptool-2.0 --build fix-ca.c

%install
export DESTDIR=%buildroot
gimptool-2.0 --install-admin-bin fix-ca

%files
%gimpplugindir/plug-ins/*

%changelog
* Wed Mar 05 2008 Victor Forsyuk <force@altlinux.org> 3.0.2-alt1
- 3.0.2

* Fri Sep 14 2007 Victor Forsyuk <force@altlinux.org> 3.0.1-alt1
- Initial build.
