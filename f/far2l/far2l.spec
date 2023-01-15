Name: far2l
Version: 2.5.0
Release: alt1

Summary: Linux port of FAR v2

Group: File tools
License: GPLv2
Url: https://github.com/elfmz/far2l

# Source-url: https://github.com/elfmz/far2l/archive/refs/tags/v_%version.tar.gz
Source: %name-%version.tar

BuildRequires: cmake gcc-c++ glib2-devel
BuildRequires: libwxGTK3.2-devel
BuildRequires: libuchardet-devel
BuildRequires: libspdlog-devel
BuildRequires: libarchive-devel
BuildRequires: libpcre-devel
BuildRequires: libssl-devel
BuildRequires: libssh-devel
BuildRequires: libnfs-devel
BuildRequires: libsmbclient-devel
BuildRequires: libneon-devel
BuildRequires: libxerces-c-devel
BuildRequires: libXi-devel
BuildRequires: libX11-devel

# skip optional requires from /usr/share/far2l scripts
%filter_from_requires /^sudo/d
%filter_from_requires /^rpm/d
%filter_from_requires /^dpkg/d
%filter_from_requires /^pandoc/d
%filter_from_requires /^catdoc/d
%filter_from_requires /^poppler/d
%filter_from_requires /^notify-send/d
%filter_from_requires /^fdisk/d
%filter_from_requires /^gdisk/d
%filter_from_requires /^gnupg/d
%filter_from_requires /^universal-ctags/d
%filter_from_requires /^perl-Image-ExifTool/d

%description
Linux port of FAR v2.
BETA VERSION.
Use on your own risk!
Plug-ins that are currently working: NetRocks (SFTP/SCP/FTP/FTPS/SMB/NFS/WebDAV),
colorer, multiarc, tmppanel, align, autowrap, drawline, editcase, SimpleIndent,
Calculator, Python (optional scripting support)

Used code from projects:
- FAR for Windows and some of its plugins
- WINE
- ANSICON
- Portable UnRAR
- 7z ANSI-C Decoder
- utf-cpp by ww898

%prep
%setup
%autopatch -p1

%build
%cmake \
	-DPCRE_INCLUDE_DIR=%_includedir/pcre \
	-DPYTHON=no

%cmake_build

%install
%cmake_install

%files
%_bindir/%name
%_libexecdir/%name/
%_datadir/%name/
%_desktopdir/far2l.desktop
%_iconsdir/hicolor/*/apps/*.svg
%_iconsdir/far2l.svg
%_mandir/ru/man1/far2l.*
%_man1dir/far2l.*

%changelog
* Sun Jan 15 2023 Anton Midyukov <antohami@altlinux.org> 2.5.0-alt1
- new version (2.5.0) with rpmgs script
- build with wxGTK3.2
- add man1 pages

* Sat Apr 02 2022 Vitaly Lipatov <lav@altlinux.ru> 2.4.0-alt3
- skip optional requires from /usr/share/far2l scripts

* Thu Jan 20 2022 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt2
- add upstream patch for build on e2k (Closes: 41745)

* Wed Jan 12 2022 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt1
- new version (2.4.0) with rpmgs script
- cleanup spec

* Sun Jan 02 2022 Anton Midyukov <antohami@altlinux.org> 2.3.2-alt1
- new version (2.3.2) with rpmgs script (Closes: 41647)

* Sun Oct 10 2021 Igor Vlasenko <viy@altlinux.org> 2.0-alt4.89d986a
- NMU: added explicit ExcludeArch: ppc64le for rebuild to not fail

* Sat Sep 15 2018 Anton Midyukov <antohami@altlinux.org> 2.0-alt3.89d986a
- rebuilt with libwxGTK3.0

* Sat Jul 07 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt2.89d986a
- new git build 89d986a

* Wed Jan 04 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt2.4d33a48
- new git build 4d33a48

* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1.4198cd5
- new git build 4198cd5

* Sat Aug 20 2016 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- initial build for ALT Linux Sisyphus
