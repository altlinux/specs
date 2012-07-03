%define oname lftpfs
Name: fuse-lftpfs
Version: 0.4.2
Release: alt1

Summary: filesystem with caching for smart mirror of sites based on FUSE and LFTP
License: GPL
Group: System/Kernel and hardware
Url: http://lftpfs.sourceforge.net/

# Automatically added by buildreq on Wed Dec 02 2009
BuildRequires: perl-Fuse perl-IPC-Run perl-devel

Packager: Ilya Shpigor <elly@altlinux.org>

Source: http://prdownloads.sf.net/%oname/%oname-%version.tar

%description
LftpFS is a read-only network filesystem with caching for smart mirror of sites. Useful for mirroring of Linux repositories. It's based on FUSE and LFTP client, which supports FTP, HTTP, FISH, SFTP, HTTPS, FTPS protocols and works over proxies. LftpFS is a fork from unmaintained FuseFTP.

%prep
%setup -n %oname-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/%oname

%changelog
* Wed Dec 02 2009 Ilya Shpigor <elly@altlinux.org> 0.4.2-alt1
- initial build for ALT Linux Sisyphus

