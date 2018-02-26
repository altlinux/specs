Name:           fuse-convmvfs
Version:        0.2.4
Release: 	alt1
Summary:        FUSE-Filesystem to convert filesystem encodings

Group:          System/Kernel and hardware
License:        GPL
URL:            http://fuse-convmvfs.sourceforge.net/
Source0:        http://dl.sourceforge.net/sourceforge/fuse-convmvfs/%name-%version.tar.gz

# Automatically added by buildreq on Mon Jun 18 2007
BuildRequires: gcc-c++ libfuse-devel

BuildRequires:  libfuse-devel >= 2.5.0

%description
This is a filesystem client use the FUSE(Filesystem in
USErspace) interface to convert file name from one charset
to another. Inspired by convmv.

%prep
%setup


%build
%configure
%make_build

%install
make install DESTDIR=%buildroot

%files
%_bindir/convmvfs
%doc README* COPYING ChangeLog AUTHORS NEWS


%changelog
* Thu Mar 06 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.2.4-alt1
- new version

* Mon Jun 18 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.2.3-alt0.1
- first build

