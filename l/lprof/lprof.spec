Summary:        Open source color profiler
Name:           lprof
Version:        1.11.4.1
Release:       	alt6.20100921.1
License:        GPL
Group:          Graphics
Url:		http://www.mozilla.org/projects/security/pki/nss
Packager: Alexandra Panyukova <mex3@altlinux.ru>

Source0:	%name.tar

# Automatically added by buildreq on Wed Feb 13 2008 (-bi)
BuildRequires: scons gcc4.1-c++ libvigra-devel libX11-devel libusb-devel libjpeg-devel libusb-compat-devel libvigra strace vim
BuildRequires: qt4-devel libqt4-assistant-devel

BuildPreReq: libXxf86vm-devel libXdmcp-devel

%description
LProf is an open source color profiler that creates ICC compliant profiles for devices such as cameras, scanners and monitors.

%prep
%setup -q -c

%build
cd lprof
scons

%install
mkdir -p %buildroot
mkdir -p %buildroot/usr
cd lprof
scons install PREFIX=%buildroot/usr

%files
%_bindir/*
%_datadir/applications/*
%_datadir/pixmaps/*
%_datadir/lprof

%changelog
* Mon Jul 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.4.1-alt6.20100921.1
- Fixed build

* Tue Sep 23 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.11.4.1-alt6.20100921
- BuildRequires: libqt4-assistant-devel

* Thu Sep 21 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.11.4.1-alt5.20100921
- latest version from cvs
- fixed build requires

* Fri Jan 01 2010 Alexandra Panyukova <mex3@altlinux.ru> 1.11.4.1-alt4.20090722
- latest version from cvs

* Thu Jul 02 2009 Alexandra Panyukova <mex3@altlinux.ru> 1.11.4.1-alt4.20090218
- require: libusb-compat-devel

* Thu Feb 19 2009 Alexandra Panyukova <mex3@altlinux.ru> 1.11.4.1-alt3.20090218
- initial build for ALT Linux.

