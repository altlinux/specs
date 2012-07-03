
Name: libopensync-plugin-opie
Version: 0.36
Release: alt1.1

Summary: Opie plugin for OpenSync
License: %lgpl2plus
Group: System/Libraries
URL: http://www.opensync.org/
Packager: Mobile Development Team <mobile@packages.altlinux.org>

Source: %name-%version.tar.bz2
Patch: %name-curl-7.21.7.patch

Requires: libcurl
Requires: libopensync = %version

BuildRequires: cmake gcc-c++ glib2-devel libcurl-devel libxml2-devel rpm-build-licenses
BuildRequires: libopensync-devel = %version

%description
This plugin allows applications using Opie to synchronise.

%prep
%setup -q
%patch0 -p2

%build
mkdir build
cd build
cmake -D CMAKE_INSTALL_PREFIX:PATH=%_prefix \
	-D OPENSYNC_LIBEXEC_DIR=%_libexecdir/opensync-1.0 \
%if %{_lib} == lib64
	-D LIB_SUFFIX=64 \
%endif
    -D CMAKE_SKIP_RPATH:BOOL=TRUE ../

%make_build

%install
pushd build
%make_install install DESTDIR=%buildroot
popd

%files
%_libdir/opensync-1.0/plugins/opie-sync.so
%_libdir/opensync-1.0/formats/opie.so
%_datadir/opensync-1.0/defaults/opie-sync

%changelog
* Mon Aug 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.36-alt1.1
- Rebuilt with curl 7.21.7

* Tue Jan 29 2008 Alexey Shabalin <shaba@altlinux.ru> 0.36-alt1
- 0.36 release for developers

* Mon Jan 21 2008 Alexey Shabalin <shaba@altlinux.ru> 0.35-alt1
- 0.35 release for developers

* Mon Apr 02 2007 Alexey Shabalin <shaba@altlinux.ru> 0.22-alt1
- 0.22

* Mon Feb 12 2007 Alexey Shabalin <shaba@altlinux.ru> 0.21-alt1
- 0.21
- cleanup spec(drop cvs)

* Wed Nov 08 2006 Alexey Shabalin <shaba@altlinux.ru> 0.20-alt1
- release 0.20

* Wed Oct 25 2006 Alexey Shabalin <shaba@altlinux.ru> 0.19-alt2
- release 0.19

* Thu Sep 21 2006 Alexey Shabalin <shaba@altlinux.ru> 0.19-alt1cvs20060921
- Initial package
