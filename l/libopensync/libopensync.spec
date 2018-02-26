
Name: libopensync
Version: 0.36
Release: alt1.2.1

Summary: Synchronisation framework
License: %lgpl2plus
Group: System/Libraries
URL: http://www.opensync.org/
Packager: Mobile Development Team <mobile@packages.altlinux.org>

Source: %name-%version.tar.bz2

BuildRequires: gcc-c++ glib2-devel libsqlite3-devel libxml2-devel pkg-config cmake
BuildRequires: python-devel python-modules-encodings swig zlib-devel rpm-build-licenses
BuildPreReq: check

%description
OpenSync is a plugin-based application that basically provides a framework
for syncing groups which can have two or more members. These members could
be just about any kind of database we have a plugin like:

 - A folder filled with vcard files containing contacts (file-sync)
 - An LDAP server having a huge list of contacts (ldap-sync)
 - An application like Mozilla Sunbird or Google Calendar managing calendars
 - A PIM (Personal Information Management) like Ximian Evolution or KDE PIM
 - A mobile phone which hosts contacts/ calendars/ notes
     
OpenSync is not only limited to sync PIM data.

%package devel
Summary: Header files, libraries and development documentation for %name
Group: Development/C
Requires: %name = %version

%description devel
This package contains the header files, static libraries and development
documentation for %name. If you like to develop programs using %name,
you will need to install %name-devel.

%package tools
Summary: Tools for %name
Group: Development/Other
Requires: %name

%description tools
Tools to test and debug %name.

%package -n python-module-opensync
Summary: Python module for %name.
Group: Development/Python
Requires: %name

%description -n python-module-opensync
Python module for %name.

%prep
%setup -q

%build
#configure --disable-profiling --enable-tools --disable-unit-tests
cmake -D CMAKE_INSTALL_PREFIX:PATH=%_prefix \
	-D OPENSYNC_LIBEXEC_DIR=%_libexecdir/opensync-1.0 \
%if %{_lib} == lib64
         -D LIB_SUFFIX=64 \
%endif
	-D PYTHON_INCLUDE_PATH:FILEPATH=%_includedir/python%__python_version \
	-D PYTHON_LIBRARY:FILEPATH=%_libdir/libpython%__python_version.so \
	-D CMAKE_SKIP_RPATH:BOOL=TRUE .

%make_build

%install
make install DESTDIR=%buildroot
%__mkdir_p %buildroot%_datadir/opensync-1.0/defaults
%__mkdir_p %buildroot%_libdir/opensync-1.0/{python-,}plugins

%files
%doc AUTHORS COPYING README
%_libdir/*.so.*
%_libdir/opensync-1.0
%_datadir/opensync-1.0
%exclude %_datadir/opensync-1.0/cmake

%files devel
%_includedir/opensync-1.0
%_pkgconfigdir/*.pc
%_libdir/*.so
%_datadir/opensync-1.0/cmake

%files tools
%_bindir/*

%files -n python-module-opensync
%dir %python_sitelibdir/*

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.36-alt1.2.1
- Rebuild with Python-2.7

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.36-alt1.2
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
- cleanup spec (drop cvs)

* Wed Nov 08 2006 Alexey Shabalin <shaba@altlinux.ru> 0.20-alt1
- release 0.20

* Tue Oct 03 2006 Alexey Shabalin <shaba@altlinux.ru> 0.19-alt2
- release 0.19
- build puthon module
- fix spec (add in files %%_libexecdir/osplugin)
- fix BuildRequires

* Thu Sep 21 2006 Alexey Shabalin <shaba@altlinux.ru> 0.19-alt1cvs20060921
- svn version 20060921 

* Tue Jul 18 2006 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt2cvs20060718
- svn version 20060718

* Mon May 29 2006 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt2cvs20060529
- svn version 20060529
- set_verify_elf_method relaxed
- add directory %%_datadir/opensync/defaults

* Tue Nov 22 2005 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt1
- 0.18 release
- build for Sisyphus

* Fri Sep 30 2005 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt0.1.cvs20050930
- Initial package
