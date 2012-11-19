Name: fuse-curlftpfs
Version: 0.9.2
Release: alt3

Summary: FTP filesystem, based on Curl and FUSE
License: GPL
Group: System/Kernel and hardware
Url: http://curlftpfs.sourceforge.net

Obsoletes: curlftpfs

BuildRequires: glib2-devel libcurl-devel libfuse-devel

Patch1: %name-fix-io-error.patch
Patch2: %name-fix-memory-leak.patch
Patch3: %name-fix-memory-leak-when-cache-is-disabled.patch

Source: %name-%version-%release.tar

%description
CurlFtpFS is a filesystem for accessing FTP hosts based on FUSE and
libcurl. CurlFtpFS differentiates itself from other FTP filesystems
because it features:
- SSLv3 and TLSv1 support
- connecting through tunneling HTTP proxies
- automatically reconnection if the server times out
- transform absolute symlinks to point back into the ftp file system

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files
%_bindir/curlftpfs
%_man1dir/curlftpfs.1.*

%changelog
* Mon Nov 19 2012 Pavel Shilovsky <piastry@altlinux.org> 0.9.2-alt3
- Add 0.9.2 version bugfix patch (taken from Debian)
- Rename package to fuse-curlftpfs

* Fri Nov 09 2012 Pavel Shilovsky <piastry@altlinux.org> 0.9.2-alt2
- Fix missed 0.9.2 sources

* Wed Aug 25 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.2-alt1
- 0.9.2 released

* Tue Dec 25 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.1-alt2
- fixed build with autofoo >= 2.60

* Sun Jul 15 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.1-alt1
- Initial build.
