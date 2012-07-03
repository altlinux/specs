
Name: libssh
Version: 0.5.2
Release: alt1

Group: System/Libraries
Summary: C library to authenticate in a simple manner to one or more SSH servers
Url: http://www.libssh.org/
License: LGPL

# svn checkout svn://svn.berlios.de/libssh/trunk libssh
Source: http://www.libssh.org/files/%name-%version.tar.gz
Source1: version-script.libssh
Source2: compat.lds
Patch1: version-script.patch

BuildRequires: cmake doxygen gcc-c++ ghostscript-utils graphviz latex2html
BuildRequires: libgcrypt-devel libssl-devel zlib-devel kde-common-devel

%description
The ssh library was designed to be used by programmers needing a working
SSH implementation by the mean of a library. The complete control of the
client is made by the programmer. With libssh, you can remotely execute
programs, transfer files, use a secure and transparent tunnel for your
remote programs. With its Secure FTP implementation, you can play with
remote files easily, without third-party programs others than libcrypto
(from openssl). libssh features :

    * Full C library functions for manipulating a client-side SSH
      connection
    * Lesser GPL licensing -SSH2 protocol compliant
    * Fully configurable sessions
    * Support for AES-128,AES-192,AES-256,blowfish, in cbc mode
    * Use multiple SSH connections in a same process, at same time
    * Use multiple channels in the same connection
    * Thread safety when using different sessions at same time
    * Basic but correct SFTP implementation (secure file transfer)
    * RSA and DSS server public key supported
    * Compression support (with zlib)
    * Public key (RSA and DSS), password and keyboard-interactive
      authentication
    * Complete documentation about its API
    * Runs and tested under amd64, x86, arm, sparc32, ppc under Linux,
      BSD, MacosX and Solaris
    * A developer listening to you
    * It's free (LGPL)!


%package devel
Summary: Development files for %name
Group: System/Libraries
Requires: %name = %version-%release
Provides: ssh-devel = %version-%release
%description devel
This package contains the development files for %name.


%prep
%setup -q
%patch1 -p1
install -m 0644 %SOURCE1 ./
install -m 0644 %SOURCE2 ./

%build
%Kcmake
%Kmake

%install
%Kinstall

%files
%_libdir/*.so.*


%files devel
%_pkgconfigdir/%name.pc
%_pkgconfigdir/libssh_threads.pc
%_includedir/%name
%_libdir/*.so

%changelog
* Wed Jun 13 2012 Sergey V Turchin <zerg@altlinux.org> 0.5.2-alt1
- new version

* Wed Aug 31 2011 Sergey V Turchin <zerg@altlinux.org> 0.5.1-alt0.M60P.1
- built for M60P

* Wed Aug 31 2011 Sergey V Turchin <zerg@altlinux.org> 0.5.1-alt1
- new version

* Mon Jun 06 2011 Sergey V Turchin <zerg@altlinux.org> 0.5.0-alt1
- new version

* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 0.4.8-alt1
- new version

* Tue Oct 05 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.6-alt1
- new version

* Thu Aug 26 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.5-alt1
- new version
- add versioning

* Tue Apr 06 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.2-alt0.M51.1
- built for M51

* Tue Apr 06 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.2-alt1
- new version

* Tue Mar 30 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.1-alt0.M51.1
- built for M51

* Wed Mar 03 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.1-alt1
- new version

* Tue Jan 19 2010 Sergey V Turchin <zerg@altlinux.org> 0.4.0-alt1
- built for ALT

