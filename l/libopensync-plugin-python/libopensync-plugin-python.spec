
Name: libopensync-plugin-python
Version: 0.36
Release: alt1.2.1

Summary: Python plugin for OpenSync
License: %lgpl2plus
Group: System/Libraries
URL: http://www.opensync.org/
Packager: Mobile Development Team <mobile@packages.altlinux.org>

Source: %name-%version.tar.bz2

Requires: python-base  
Requires: libopensync = %version

BuildRequires: cmake gcc-c++ glib2-devel pkg-config python-devel
BuildRequires: python-modules-encodings rpm-build-licenses
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
		-D PYTHON_INCLUDE_PATH:PATH=%_includedir/python%__python_version \
		-D PYTHON_LIBRARY:FILEPATH=%_libdir/libpython%__python_version.so \
    -D CMAKE_SKIP_RPATH:BOOL=TRUE ../ \

%make_build

%install
pushd build
%make_install install DESTDIR=%buildroot
popd

%files
%_libdir/opensync-1.0/plugins/python-module.so
%_libdir/opensync-1.0/python-plugins/*

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.36-alt1.2.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.36-alt1.2
- Rebuilt with python 2.6

* Sun Feb 03 2008 Grigory Batalov <bga@altlinux.ru> 0.36-alt1.1
- Rebuilt with python-2.5.

* Tue Jan 29 2008 Alexey Shabalin <shaba@altlinux.ru> 0.36-alt1
- 0.36 release for developers

* Mon Jan 21 2008 Alexey Shabalin <shaba@altlinux.ru> 0.35-alt1
- 0.35 release for developers

* Mon Apr 02 2007 Alexey Shabalin <shaba@altlinux.ru> 0.22-alt1
- 0.22

* Mon Feb 12 2007 Alexey Shabalin <shaba@altlinux.ru> 0.21-alt1
- 0.21
- cleanip spec(drop cvs)

* Wed Nov 08 2006 Alexey Shabalin <shaba@altlinux.ru> 0.20-alt1
- release 0.20

* Tue Oct 03 2006 Alexey Shabalin <shaba@altlinux.ru> 0.19-alt2
- release 0.19

* Tue Jul 18 2006 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt2cvs20060718
- svn version 20060718

* Mon May 29 2006 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt2cvs20060529
- svn version 20060529

* Tue Nov 22 2005 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt1
- 0.18 release
- build for Sisyphus

* Fri Sep 30 2005 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt0.1.cvs20050930
- Initial package
