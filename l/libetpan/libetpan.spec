Name: libetpan
Version: 1.1
Release: alt1

Summary: This mail library  provide a portable, efficient middleware for different kinds of mail access.
License: %bsdstyle
Group: Development/C

Url: http://%name.sourceforge.net/

Source: %name-%version.tar

%def_with gnutls
%def_without openssl

BuildRequires(pre): rpm-build-licenses

# FIXME: Is it really needed g++?
BuildRequires: gcc-c++

%{?_with_gnutls:BuildRequires: libgnutls-devel libgcrypt-devel libgpg-error-devel zlib-devel}
%{?_with_openssl:BuildRequires: libssl-devel}
BuildRequires: libsasl2-devel libdb4.7-devel
BuildRequires: liblockfile-devel libexpat-devel libcurl-devel

%package devel
Summary: Development environment for %name library.
Group: Development/C
Requires: %name = %version-%release
%{?_with_gnutls:Requires: libgnutls-devel libgcrypt-devel libgpg-error-devel zlib-devel}
%{?_with_gnutls:Requires: libssl-devel}
Requires: libsasl2-devel libdb4.7-devel
Requires: liblockfile-devel

%description
The purpose of this mail library is to provide a portable, efficient
middleware for different kinds of mail access. When using the drivers
interface, the interface is the same for all kinds of mail access,
remote and local mailboxes.

%description devel
This package contains the header files and libraries for building
program which use lib%name.

%prep
%setup

%build
%configure \
	--disable-static \
	%{subst_with openssl} \
	%{subst_with gnutls} \
	--enable-ipv6
%make_build

%install
%makeinstall_std

%files
%doc ChangeLog NEWS COPYRIGHT README AUTHORS
%_libdir/%name.so.*

%files devel
%_bindir/%name-config
%dir %_includedir/%name
%_includedir/%name/*.h
%_includedir/%name.h
%_libdir/%name.so

%changelog
* Mon Jul 02 2012 Mikhail Efremov <sem@altlinux.org> 1.1-alt1
- Fix License.
- Updated to 1.1.

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.58-alt2
- Rebuilt for soname set-versions

* Mon Aug 10 2009 Alexey Rusakov <ktirf@altlinux.org> 0.58-alt1.1
- now really fixed ALT #10833.
- updated buildreqs slightly.

* Sun Aug 09 2009 Alexey Rusakov <ktirf@altlinux.org> 0.58-alt1
- 0.58
- removed obsolete post/postun macros.
- fixed -devel subpackage requires (closing ALT #10833).

* Thu Oct 16 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.57-alt1.1
-  build with new GnuTLS.

* Fri Oct 10 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.57-alt1
-  0.57.

* Mon Oct 06 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.56-alt1
-  0.56.

* Mon Aug 11 2008 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.54-alt1
-  0.54.

* Thu Sep 27 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.52-alt1
-  0.52.

* Fri May 11 2007 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.49-alt1
-  0.49.

* Wed Nov 29 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.48-alt1
-  0.48.

* Wed Oct 25 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.47cvs5-alt1
-  0.47.

* Mon Aug 28 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.46-alt1
-  0.46.

* Fri Jun 16 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.45-alt1.1
-  rebuild with new gnutls.

* Tue Mar 28 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.45-alt1
-  0.45.

* Mon Mar 20 2006 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.43-alt1
-  0.43.

* Wed Dec 07 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.41-alt1
-  0.41.

* Wed Nov 09 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.40-alt1
-  0.40.

* Tue Oct 04 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.39.1-alt1
- 0.39. 

* Mon Aug 01 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.38-alt1
-  0.38.

* Wed Jul 13 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.37-alt0.2
-  missing requires added.

* Wed Jul 13 2005 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 0.37-alt0.1
-  initial build.


