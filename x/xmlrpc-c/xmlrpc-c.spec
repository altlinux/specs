%define libname libxmlrpc
# libxml2 backend is broken
%def_disable libxml2

Name: xmlrpc-c
Version: 1.54.06
Release: alt2

Summary: XML-RPC C library - an implementation of the xmlrpc protocol
License: BSD-3-Clause AND MIT
Group: System/Libraries

Url: http://xmlrpc-c.sourceforge.net/

Source: %name-%version.tar


Patch1: %name-1.12.00-alt-configure-fixes.patch
Patch2: 0001-cleanup-and-fix-libxml2-backend.patch

# Patches from fedora
Patch101: 0001-xmlrpc_server_abyss-use-va_args-properly.patch
Patch102: 0002-Use-proper-datatypes-for-long-long.patch
Patch103: 0003-allow-30x-redirections.patch

# Patches from OpenNebula
Patch201: xml_parse_huge.patch

BuildRequires: gcc-c++
BuildRequires: libcurl-devel
%{?_enable_libxml2:BuildRequires: libxml2-devel}
BuildRequires: libncurses-devel libreadline-devel
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

%package -n %libname-client
Summary: C client libraries for xmlrpc-c
Group: System/Libraries
Requires: %libname = %version-%release

%description -n %libname-client
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.

This library provides a modular implementation of XML-RPC for C
clients.

%package -n %libname-devel
Summary: Files for developing applications that use %libname
Requires: %libname = %version-%release
Requires: %libname++ = %version-%release
Requires: %libname-client = %version-%release
Requires: %libname-client++ = %version-%release
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

%package -n %libname-client++
Summary: C++ client libraries for xmlrpc-c
Group: System/Libraries
Requires: %libname-client = %version-%release
Requires: %libname++ = %version-%release

%description -n %libname-client++
XML-RPC is a quick-and-easy way to make procedure calls over the
Internet. It converts the procedure call into XML document, sends it
to a remote server using HTTP, and gets back the response as XML.

This library provides a modular implementation of XML-RPC for C++
clients.

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
%patch1 -p1
%if_enabled libxml2
%patch2 -p1
%endif
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch201 -p1

%build
autoconf
%configure \
	--disable-wininet-client \
	%{?_enable_libxml2:--enable-libxml2-backend}

%make
%make -C tools

%install
%makeinstall_std
%makeinstall_std -C tools
rm -f %buildroot%_libdir/*.a

%files
%doc README doc/*
%doc tools/xmlrpc_transport/xmlrpc_transport.html
%_man1dir/*
%_bindir/*
%exclude %_bindir/xmlrpc-c-config

%files -n %libname
%_libdir/libxmlrpc.so.*
%_libdir/libxmlrpc_*.so.*
%exclude %_libdir/libxmlrpc_cpp.so.*
%exclude %_libdir/libxmlrpc_*++.so.*
%exclude %_libdir/libxmlrpc_client.so.*

%files -n %libname-client
%_libdir/libxmlrpc_client.so.*

%files -n %libname++
%_libdir/libxmlrpc_cpp.so.*
%_libdir/libxmlrpc++.so.*
%_libdir/libxmlrpc_*++.so.*
%exclude %_libdir/libxmlrpc_client++.so.*

%files -n %libname-client++
%_libdir/libxmlrpc_client++.so.*

%files -n %libname-devel
%_bindir/xmlrpc-c-config
%_includedir/xmlrpc-c/
%_includedir/*.h
%_pkgconfigdir/*.pc
%_libdir/*.so

%changelog
* Fri Jan 27 2023 Alexey Shabalin <shaba@altlinux.org> 1.54.06-alt2
- apply xml_parse_huge.patch for OpenNebula

* Thu Sep 29 2022 Alexey Shabalin <shaba@altlinux.org> 1.54.06-alt1
- 1.54.06

* Mon Jul 19 2021 Alexey Shabalin <shaba@altlinux.org> 1.51.07-alt1
- 1.51.07

* Wed Apr 08 2020 Alexey Shabalin <shaba@altlinux.org> 1.51.06-alt1
- 1.51.06

* Tue Jan 22 2019 Alexey Shabalin <shaba@altlinux.org> 1.51.03-alt1.svn3018
- 1.51.03

* Wed Sep 26 2018 Alexey Shabalin <shaba@altlinux.org> 1.51.02-alt1.svn3011
- 1.51.02

* Thu Mar 01 2018 Alexey Shabalin <shaba@altlinux.ru> 1.43.06-alt1.svn2912
- 1.43.06

* Wed Aug 30 2017 Alexey Shabalin <shaba@altlinux.ru> 1.39.12-alt1.svn2910
- 1.39.12

* Tue Jul 21 2015 Vitaly Lipatov <lav@altlinux.ru> 1.32.5-alt2.svn2451
- use cmake macros
- rebuild with new libstdc++

* Tue Mar 11 2014 Timur Aitov <timonbl4@altlinux.org> 1.32.5-alt1.svn2451
- 1.32.5

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
