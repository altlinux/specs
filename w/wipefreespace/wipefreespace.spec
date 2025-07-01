Name: wipefreespace
Version: 3.0
Release: alt1

Summary: Program for secure cleaning of free space on file systems
License: GPL-2.0-or-later
Group: File tools

URL: https://wipefreespace.sourceforge.io
VCS: https://github.com/bogdro/wipefreespace.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

#Requires: xfsprogs
BuildRequires: glibc-kernheaders
BuildRequires: libe2fs-devel
BuildRequires: libxfs-devel xfsprogs
BuildRequires: libntfs-3g-devel
BuildRequires: libuuid-devel
BuildRequires: libcap-devel
BuildRequires: makeinfo

%description
The wipefreespace is a program which securely cleans free space on given
file systems, making confidential removed data recovery impossible.

It also removes deleted files' names so that no trace is left.

WARNING: it is REQUIRED to specify a --method, otherwise you might think
the data is purged but it's still there actually.

Supported file systems are: ext2/3/4, NTFS, XFS.
#, ReiserFSv3/4,
#FAT12/16/32, MinixFSv1/2, JFS, HFS+ and OCFS.

%prep
%setup
%autopatch -p1

%build
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_infodir/%name.*
%_man1dir/%name.1*
%doc AUTHORS ChangeLog README README.md

%changelog
* Tue Jul 01 2025 Anton Midyukov <antohami@altlinux.org> 3.0-alt1
- new version 3.0
- update URL, add VCS, clean Packager, update build dependencies.

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt4.1
- NMU: added BR: texinfo

* Wed Aug 15 2012 Michael Shigorin <mike@altlinux.org> 1.6.1-alt4
- moved %_bindir/%name to /bin

* Sat Aug 11 2012 Michael Shigorin <mike@altlinux.org> 1.6.1-alt3
- added upstream proposed patch to add info-dir entry

* Thu Aug 09 2012 Michael Shigorin <mike@altlinux.org> 1.6.1-alt2
- enabled info file installation (needs fixup though)

* Thu Aug 09 2012 Michael Shigorin <mike@altlinux.org> 1.6.1-alt1
- initial build for ALT Linux Sisyphus
