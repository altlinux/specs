%def_enable snapshot

%define _name kqoauth
%define git_ver 7c31a120

Name: lib%_name-qt5
Version: 0.98
Release: alt1.%git_ver

Summary: Qt OAuth support library
Group: System/Libraries
License: LGPLv2.1+
Url: https://github.com/kypeli/kQOAuth

%if_disabled snapshot
Source: kQOAuth-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

Conflicts: lib%_name

BuildRequires(Pre): qt5-base-devel
BuildRequires: gcc-c++ libssl-devel

%description
kQOAuth is a OAuth 1.0 library written for Qt in C++. The goals for the
library have been to provide easy integration to existing Qt5 applications
utilizing Qt5 signals describing the OAuth process, and to provide a
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
%setup -n %_name-%version
subst 's@\/usr\/lib@"%_libdir"@' kqoauth.prf
find ./ -name "*.pro" -print0| xargs -r0 subst 's@\/lib@/"%_lib"@' --

# Fix pkgconfig file
sed -i 's|QtCore QtNetwork|Qt5Core Qt5Network|g' src/pcfile.sh

%build
%qmake_qt5 KQOAUTH_LIBDIR=%_libdir
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%make check

%files
%_libdir/lib%_name.so.*
%doc CHANGELOG README

%files devel
%_includedir/QtKOAuth/
%_libdir/lib%_name.so
%_pkgconfigdir/%_name.pc

%exclude %_libdir/lib%_name.prl
%exclude %_libdir/qt5/mkspecs/features/%_name.prf

%changelog
* Mon Jun 27 2016 Yuri N. Sedunov <aris@altlinux.org> 0.98-alt1.7c31a120
- first build for Sisyphus (0.98-6-g7c31a12)


