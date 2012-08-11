Name: wipefreespace
Version: 1.6.1
Release: alt3

Summary: Program for secure cleaning of free space on file systems
License: GPLv2
Group: File tools

Url: http://wipefreespace.sf.net
Source: %name-%version.tar.gz
Patch: wipefreespace-1.6.1-infodir.patch
Packager: Michael Shigorin <mike@altlinux.org>

Requires: xfsprogs
BuildRequires: glibc-kernheaders
BuildRequires: libe2fs-devel
#BuildRequires: libxfs-devel

%description
The wipefreespace is a program which securely cleans free space on given
file systems, making confidential removed data recovery impossible.

It also removes deleted files' names so that no trace is left.

WARNING: it is REQUIRED to specify a --method, otherwise you might think
the data is purged but it's still there actually.

%if 1
Supported file systems are: ext2/3/4 (for this exact package)
%else
Supported file systems are: ext2/3/4, NTFS, XFS, ReiserFSv3/4,
FAT12/16/32, MinixFSv1/2, JFS, HFS+ and OCFS.
%endif

%prep
%setup
%patch -p1

%build
%configure --disable-XFS
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_infodir/%name.*
%_man1dir/%name.1*
%doc AUTHORS ChangeLog README

%changelog
* Sat Aug 11 2012 Michael Shigorin <mike@altlinux.org> 1.6.1-alt3
- added upstream proposed patch to add info-dir entry

* Thu Aug 09 2012 Michael Shigorin <mike@altlinux.org> 1.6.1-alt2
- enabled info file installation (needs fixup though)

* Thu Aug 09 2012 Michael Shigorin <mike@altlinux.org> 1.6.1-alt1
- initial build for ALT Linux Sisyphus
