%define gimpdatadir %(gimptool-2.0 --gimpdatadir)

Name: gimp-script-vintage-look
Version: 0.2
Release: alt1

Summary: Gimp script to simulate a vintage look
License: GPLv2+
Group: Graphics

Url: http://registry.gimp.org/node/1348
Source: http://registry.gimp.org/files/vintage-look_0.scm

BuildArch: noarch

Requires: gimp

# Automatically added by buildreq on Thu Oct 01 2009
BuildRequires: libgimp-devel

%description
This script-fu for The Gimp is an attempt to simulate a vintage look.

%prep

%build

%install
install -pD -m644 %_sourcedir/vintage-look_0.scm %buildroot%gimpdatadir/scripts/vintage-look.scm

%files
%gimpdatadir/scripts/*

%changelog
* Thu Oct 01 2009 Victor Forsyuk <force@altlinux.org> 0.2-alt1
- Initial build.
