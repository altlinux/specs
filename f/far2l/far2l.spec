Name: far2l
Version: 2.3.2
Release: alt1

Summary: Linux port of FAR v2

Group: File tools
License: GPLv2
Url: https://github.com/elfmz/far2l

# Source-url: https://github.com/elfmz/far2l/archive/refs/tags/v_%version.tar.gz
Source: %name-%version.tar

BuildRequires: cmake gcc-c++ glib2-devel
BuildRequires: libwxGTK3.0-devel
BuildRequires: libuchardet-devel
BuildRequires: libspdlog-devel
BuildRequires: libarchive-devel
BuildRequires: libpcre2-devel
BuildRequires: libssl-devel
BuildRequires: libssh-devel
BuildRequires: libnfs-devel
BuildRequires: libsmbclient-devel
BuildRequires: libneon-devel
BuildRequires: libxerces-c-devel

# multiarc/src/arcread.cpp:184:30: error: cast from 'ArcItemUserData*' to 'DWORD_PTR' {aka 'unsigned int'} loses precision [-fpermissive]
ExcludeArch: ppc64le

%description
Linux port of FAR v2.
ALPHA VERSION - Currently interesting only for enthusiasts!!!
Plug-ins that are currently working: NetRocks 
(SFTP/SCP/FTP/FTPS/SMB/NFS/WebDAV), colorer, multiarc, tmppanel,
align, autowrap, drawline, editcase, SimpleIndent, Calculator,
Python (optional scripting support).

Used code from projects:
FAR for Windows
WINE
ANSICON
Portable UnRAR
7z ANSI-C Decoder

%prep
%setup

%build
%cmake_insource -DPCRE_INCLUDE_DIR=%_includedir/pcre -DPYTHON=no
%make_build
# FIXME: NEW bad_elf_symbols detected during build on ALT Linux build system
rm -rf install/Plugins/{farftp,multiarc}/

%install
mkdir -p %buildroot%_bindir/
mkdir -p %buildroot%_libexecdir/%name/
cp -a install/* %buildroot%_libexecdir/%name/
ln -s ../../%_libexecdir/%name/far2l %buildroot%_bindir/%name

%files
%_bindir/%name
%_libexecdir/%name/

%changelog
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
