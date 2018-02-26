%define distname obexfs

Name: fuse-obexfs
Version: 0.11
Release: alt0.rc3.qa1

Summary: FUSE based filesystem using ObexFTP
Group: System/Kernel and hardware
License: GPL
Url: http://dev.zuckschwerdt.org/openobex/wiki/ObexFs
Packager: L.A. Kostis <lakostis@altlinux.ru>

Source0: http://downloads.sourceforge.net/openobex/obexfs-%{version}rc3.tar.gz

BuildRequires: obexftp-devel libfuse-devel pkgconfig

Requires: fuse

%description
FUSE based filesystem using ObexFTP (currently beta).

The caching layer has been removed as it is provided by the ObexFTP library
now. Actually ObexFS is just a thin layer wrapping a basic ObexFTP client into
FUSE callbacks. 

%prep
%setup -q -n %distname-%{version}rc3

%build
%configure
%make

%install
%makeinstall

%files
%doc AUTHORS COPYING ChangeLog NEWS README

%_bindir/obexfs
%_bindir/obexautofs

%changelog
* Tue May 17 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.11-alt0.rc3.qa1
- NMU (by repocop): the following fixes applied:
  * specfile-macros-get_dep-is-deprecated for fuse-obexfs

* Sun Nov 11 2007 L.A. Kostis <lakostis@altlinux.ru> 0.11-alt0.rc3
- initial build for ALTLinux.


