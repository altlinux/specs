%define libname libxmlrpc

Name: xmlrpc-c
Version: 1.27.0
Release: alt1.svn2145

Summary: XML-RPC C library - an implementation of the xmlrpc protocol
License: BSD-style
Group: System/Libraries

Url: http://xmlrpc-c.sourceforge.net/
Source: %name-%version.tar
Patch0: %name-cmake.patch
Patch1: %name-1.12.00-alt-configure-fixes.patch
Patch2: %name-30x-redirect.patch
Patch3: %name-uninit-curl.patch
Patch4: %name-curl-types.h.patch
Patch5: %name-longlong.patch
Patch6: %name-check-vasprintf-return-value.patch
Patch7: %name-include-string_int.h.patch
Patch8: %name-printf-size_t.patch

BuildRequires: libcurl-devel libxml2-devel gcc-c++ cmake
BuildRequires: libncurses-devel libncursesxx-devel
BuildRequires: libssl-devel zlib-devel

%description
XML-RPC for C/C++ is programming libraries and related tools to help you
write an XML-RPC server or client in C or C++.

%package -n %libname
Summary: XML-RPC C library - an implementation of the xmlrpc protocol
Group: System/Libraries

%description -n %libname
XML-RPC for C/C++ is programming libraries and related tools to help you
write an XML-RPC server or client in C or C++.


%package -n %libname-devel
Summary: Files for developing applications that use %libname
Requires: %libname = %version-%release
Requires: libcurl-devel libexpat-devel libssl-devel w3c-libwww-devel libxml2-devel
Group: Development/C

%description -n %libname-devel
The header file for developing applications that use
%name.


%package -n %libname++
Summary: XML-RPC C++ library - an implementation of the xmlrpc protocol
Group: System/Libraries
Requires: %libname = %version-%release

%description -n %libname++
XML-RPC for C/C++ is programming libraries and related tools to help you
write an XML-RPC server or client in C or C++.

This package contains C++ bindings for %libname.


%package -n %libname++-devel
Summary: Files for developing applications that use %libname++
Requires: %libname++ = %version-%release
Requires: %libname-devel = %version-%release
Group: Development/C++

%description -n %libname++-devel
The header file for developing applications that use
%libname++.


%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
mkdir -p build
cd build
export CFLAGS="$RPM_OPT_FLAGS -Wno-uninitialized -Wno-unknown-pragmas"
export CXXFLAGS="$RPM_OPT_FLAGS"
cmake .. \
	-D_lib:STRING=%_libdir \
	-DMUST_BUILD_CURL_CLIENT:BOOL=ON \
	-DMUST_BUILD_LIBWWW_CLIENT:BOOL=OFF \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DENABLE_TOOLS:BOOL=ON
%make_build VERBOSE=1

%install
cd build
%makeinstall_std
rm -f %buildroot%_libdir/*.a
mkdir -p %buildroot%_pkgconfigdir
mv %buildroot%prefix%_pkgconfigdir/*.pc %buildroot%_pkgconfigdir

%files
%doc README doc/*
%doc tools/xmlrpc/xmlrpc.html
%doc tools/xmlrpc_transport/xmlrpc_transport.html
%_man1dir/*
%_bindir/xmlrpc
%_bindir/xmlrpc_transport
%_bindir/xml-rpc-api2cpp
%_bindir/xmlrpc_cpp_proxy
%exclude %_bindir/xml-rpc-api2txt

%files -n %libname
%_libdir/*.so.3*

%files -n %libname-devel
%_bindir/xmlrpc-c-config
%_includedir/xmlrpc-c
%_includedir/*.h
%_pkgconfigdir/*.pc
%_libdir/*.so

%files -n %libname++
%_libdir/*.so.7*


%changelog
* Wed Sep 28 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 1.27.0-alt1.svn2145
- update to 1.27.0 (svn2145) (ALT#26363)
- enable cplusplus, abyss-server, cgi-server (ALT#26364)

* Tue Jul 05 2011 Dmitry V. Levin <ldv@altlinux.org> 1.12.00-alt11
- Fixed build with new libcurl-devel.

* Mon Apr 18 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.12.00-alt10
- fix build

* Fri Oct 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.00-alt9
- Rebuilt for soname set-versions

* Thu Nov 20 2008 Andrey Rahmatullin <wrar@altlinux.ru> 1.12.00-alt8
- remove update_*/clean_* invocations

* Thu Sep 11 2008 Andrey Rahmatullin <wrar@altlinux.ru> 1.12.00-alt7
- recognize linux-gnueabi as linux (kas@)

* Sun May 11 2008 Andrey Rahmatullin <wrar@altlinux.ru> 1.12.00-alt6
- libxmlrpc-devel should also require libxml2-devel because of xmlrpc-c-config

* Mon Apr 14 2008 Andrey Rahmatullin <wrar@altlinux.ru> 1.12.00-alt5
- fix building with new curl (Gentoo)

* Sun Jan 20 2008 Andrey Rahmatullin <wrar@altlinux.ru> 1.12.00-alt4
- correctly fix building with new autotools, now including x86_64 (authors
  seem to have no brain)

* Sat Dec 29 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.12.00-alt3
- fix building with new autotools

* Sat Oct 27 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.12.00-alt2
- fix x86_64 build (damir@), again
- fix broken symlinks in /usr/include

* Mon Oct 22 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.12.00-alt1
- 1.12.00
- disable optional server components
- disable C++ bindings

* Thu Apr 12 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.10.00-alt2
- fix License (#11485)
- put docs in one directory

* Fri Mar 30 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.10.00-alt1
- 1.10.0

* Wed Jan 03 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.09.00-alt1
- 1.09.00

* Fri Dec 08 2006 Andrey Rahmatullin <wrar@altlinux.ru> 1.08.00-alt4
- fix x86_64 build (damir@)

* Tue Dec 05 2006 Andrey Rahmatullin <wrar@altlinux.ru> 1.08.00-alt3
- package C++ bindings separately

* Thu Nov 23 2006 Andrey Rahmatullin <wrar@altlinux.ru> 1.08.00-alt2
- fix requires for devel subpackage according to 
  `xmlrpc-c-config client --libs' output

* Thu Nov 23 2006 Andrey Rahmatullin <wrar@altlinux.ru> 1.08.00-alt1
- 1.08.00

* Wed Aug 23 2006 Andrey Rahmatullin <wrar@altlinux.ru> 1.06.02-alt0.3
- Sisyphus build

* Sun Aug 13 2006 Damir Shayhutdinov <damir@altlinux.ru> 1.06.02-alt0.2
- Use automake for building.

* Mon Aug 07 2006 Andrey Rahmatullin <wrar@altlinux.ru> 1.06.02-alt0.1
- initial build
