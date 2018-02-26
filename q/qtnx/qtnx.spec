Name: qtnx
Version: 0.9
Release: alt2

Summary: Freenx application/thin-client client
Group: Networking/Remote access
License: GPLv2
URL: http://freenx.berlios.de

Packager: Boris Savelev <boris@altlinux.org>

Source0: %name.tar.bz2
Patch0: %name-key-path.patch
Patch11: scroll.patch
Patch12: keymap.patch
Patch13: dodnx.patch
Patch14: keychooser.patch
Patch15: sessionfiles.patch
Patch16: ssh_dnserror.patch

Requires: libnxcl >= 1:0.9-alt2

# Automatically added by buildreq on Fri Jun 13 2008
BuildRequires: gcc-c++ libnxcl-devel libqt4-devel

%description
This is an update of the experimental QtNX client which was based on the
now deprecated NXClientLib backend library. This is an experimental port
to Seb James' nxcl library.

%prep
%setup -n %name
%patch0 -p1

%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

%build
qmake-qt4
%make

%install
%makeinstall_std
mkdir -p %buildroot%_bindir/
mkdir -p %buildroot%_datadir/%name
install -m 755 %name %buildroot%_bindir/
install -m 644 id.key %buildroot%_datadir/%name/id.key
%files
%doc README
%_bindir/*
%_datadir/%name/id.key

%changelog
* Sun Sep 27 2009 Boris Savelev <boris@altlinux.org> 0.9-alt2
- add patches from nx-mobile (Fabian Franz)

* Fri Jun 13 2008 Boris Savelev <boris@altlinux.org> 0.9-alt1
- initial build
