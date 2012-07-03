Name: synbak
Version: 1.3.2
Release: alt1

Summary: Synbak - Universal Backup System

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL
Group: File tools
Url: http://www.initzero.it/products/opensource/synbak

Source: http://www.initzero.it/products/opensource/synbak/download/%name-%version.tar

BuildArch: noarch

Requires: rsync, tar, gawk, sed, netcat, bc, mktemp >= 1.5, bash >= 2.0

# Automatically added by buildreq on Sat May 14 2011
BuildRequires: netcat

%description
Synbak is an application designed to unify several backup methods. Synbak
provides a powerful reporting system and a very simple interface for
configuration files.
Synbak is a wrapper for several existing backup programs suppling the
end user with common method for configuration that will manage the
execution logic for every single backup and will give detailed reports
of backups result.

Synbak can make backups using:
- RSync over ssh, rsync daemon, smb and cifs protocols (automount functions)
- Tar archives (tar, tar.gz and tar.bz2)
- Tape devices (using multi loader changer tapes too)
- LDAP databases
- MySQL databases
- Oracle databases
- CD-RW/DVD-RW
- Wget to mirror HTTP/FTP servers
- and more...

Synbak can make reports using:
- Email
- Html pages
- RSS feeds
- and more...

Moreover, if you are a developer and want to contribute,
the modular nature of synbak will allow you to easly write
new backup methods, reports, and translations.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_docdir/%name-%version/
%_bindir/%name
%_datadir/%name/

%changelog
* Sat May 14 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.2-alt1
- new version 1.3.2 (with rpmrb script)

* Sun Dec 07 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt2
- small fixes (apply patches from Vitaly Ostanin vyt@)

* Thu Dec 04 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.2-alt1
- new version 1.2.2 (with rpmrb script)

* Wed Jul 02 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)
- cleanup spec

* Sun Dec 10 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0.11-alt0.1
- new version 1.0.11 (with rpmrb script)

* Sun Jul 30 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt0.1
- initial build for ALT Linux Sisyphus

* Sat Feb 18 2006 Ugo Viti <ugo.viti@initzero.it> 1.0.0-1
- First public release!
- Complete rewrite from scratch

