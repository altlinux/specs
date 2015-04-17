%define _name kqoauth
%define git_ver 7c31a120

Name: lib%_name
Version: 0.98
Release: alt2.%git_ver

Summary: Qt OAuth support library
Group: System/Libraries
License: LGPLv2.1+
Url: https://github.com/kypeli/kQOAuth

#Source: kQOAuth-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): libqt4-devel
BuildRequires: gcc-c++

%description
kQOAuth is a OAuth 1.0 library written for Qt in C++. The goals for the
library have been to provide easy integration to existing Qt applications
utilizing Qt signals describing the OAuth process, and to provide a
convenient approach to OAuth authentication.

kQOAuth has support for retrieving the user authorization from the service
provider's website. kQOAuth will open the user's web browser to the
authorization page, give a local URL as the callback URL and setup a HTTP
server on this address to listen for the reply from the service and then
process it.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch -p1
subst 's@\/usr\/lib@"%_libdir"@' kqoauth.prf
find ./ -name "*.pro" -print0| xargs -r0 subst 's@\/lib@/"%_lib"@' --

%build
%qmake_qt4 KQOAUTH_LIBDIR=%_libdir
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%make check

%files
%_libdir/%name.so.*
%doc CHANGELOG README

%files devel
%_includedir/QtKOAuth/
%_libdir/%name.so
%_libdir/%name.prl
%_pkgconfigdir/%_name.pc
%_datadir/qt4/mkspecs/features/%_name.prf

%changelog
* Fri Apr 17 2015 Yuri N. Sedunov <aris@altlinux.org> 0.98-alt2.7c31a120
- updated to 0.98_7c31a120

* Mon Jan 06 2014 Yuri N. Sedunov <aris@altlinux.org> 0.98-alt1
- first build for Sisyphus

