
Name: libopensync-plugin-file
Version: 0.36
Release: alt1

Summary: File sync. plugin for OpenSync
License: %lgpl2plus
Group: System/Libraries
URL: http://www.opensync.org/
Packager: Mobile Development Team <mobile@packages.altlinux.org>

Source: %name-%version.tar.bz2

Requires: libopensync = %version

BuildRequires: cmake gcc-c++ glib2-devel libxml2-devel pkg-config zlib-devel rpm-build-licenses
BuildRequires: libopensync-devel = %version

%description
This plugin allows applications using OpenSync to synchronise to and from
files stored on disk.

%prep
%setup -q

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
%doc AUTHORS COPYING
%_libdir/opensync-1.0/plugins/file-sync.so
%_datadir/opensync-1.0/defaults/file-sync

%changelog
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

* Tue Oct 03 2006 Alexey Shabalin <shaba@altlinux.ru> 0.19-alt2
- release 0.19
- disable fam suport in upstream

* Thu Sep 21 2006 Alexey Shabalin <shaba@altlinux.ru> 0.19-alt1cvs20060921
- svn version 20060921

* Tue Jul 18 2006 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt3cvs20060718
- svn version 20060718

* Mon May 29 2006 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt3cvs20060529
- svn version 20060529

* Tue Jan 31 2006 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt2
- change fam support to gamin

* Tue Nov 22 2005 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt1
- 0.18 release
- build for Sisyphus
- add Packager SynCE Development Team

* Fri Sep 30 2005 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt0.1.cvs20050930
- Initial package
