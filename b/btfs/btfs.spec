Name: btfs
Version: 3.1
Release: alt1

Summary: A bittorrent filesystem based on FUSE

License: GPLv2
Group: Communications
Url: https://github.com/johang/btfs

# Source-url: https://github.com/johang/btfs/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(fuse3) pkgconfig(libcurl) pkgconfig(libtorrent-rasterbar)
BuildRequires: rpm-build-python3

ExcludeArch: %ix86

%description
With BTFS, you can mount any .torrent file or magnet link and then use it
as any read-only directory in your file tree.
The contents of the files will be downloaded on-demand as they
are read by applications.
Tools like ls, cat and cp works as expected.
Applications like vlc and mplayer can also work without changes.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_bindir/btplay
%_bindir/btfsstat
%_man1dir/*

%changelog
* Sat Jan 10 2026 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt1
- new version 3.1
- switch to FUSE 3
- exclude i586 (FUSE 3 requires 64-bit off_t)

* Sat May 15 2021 Vitaly Lipatov <lav@altlinux.ru> 2.24-alt2
- add BR: rpm-build-python3

* Wed Feb 24 2021 Vitaly Lipatov <lav@altlinux.ru> 2.24-alt1
- new version 2.24 (with rpmrb script)

* Thu Jan 21 2021 Vitaly Lipatov <lav@altlinux.ru> 2.23-alt1
- new version 2.23 (with rpmrb script)

* Wed Sep 02 2020 Vitaly Lipatov <lav@altlinux.ru> 2.22-alt1
- new version 2.22 (with rpmrb script)

* Sat Sep 07 2019 Vitaly Lipatov <lav@altlinux.ru> 2.20-alt1
- new version 2.20 (with rpmrb script)

* Tue May 14 2019 Vitaly Lipatov <lav@altlinux.ru> 2.19-alt1
- new version 2.19 (with rpmrb script)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 2.18-alt1
- new version 2.18 (with rpmrb script)

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.13-alt3.1
- NMU: rebuilt with boost-1.67.0

* Wed Apr 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.13-alt3
- (NMU) Rebuilt with new libtorrent-rasterbar.

* Wed Aug 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.13-alt2
- Rebuild with new libtorrent-rasterbar.

* Wed Mar 15 2017 Vitaly Lipatov <lav@altlinux.ru> 2.13-alt1
- new version 2.13 (with rpmrb script)

* Fri Jul 29 2016 Vitaly Lipatov <lav@altlinux.ru> 2.10-alt1
- new version 2.10 (with rpmrb script)

* Thu Jun 23 2016 Vitaly Lipatov <lav@altlinux.ru> 2.9-alt1
- initial build for ALT Linux Sisyphus
