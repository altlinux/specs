%define _unpackaged_files_terminate_build 1

Name: mscp
Version: 0.2.4
Release: alt1

Summary: Transfer files over multiple SSH (SFTP) connections
License: GPL-3.0
Group: Networking/File transfer

Url: https://github.com/upa/mscp
VCS: https://github.com/upa/mscp.git
Source0: %name-%version.tar
Source1: libssh-%name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: zlib-devel
BuildRequires: libssl-devel

%description
mscp, a variant of scp, copies files over multiple SSH (SFTP) connections 
by multiple threads. It enables transferring (1) multiple files 
simultaneously and (2) a large file in parallel, reducing the transfer 
time for a lot of/large files over networks.

%prep
%setup
tar -xf %SOURCE1 -C libssh --strip-components 1
patch -d libssh -p1 < patch/libssh-0.11.2.patch

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/%name
%_man1dir/*

%changelog
* Tue Aug 11 2026 Andrey Alekseev <parovoz@altlinux.org> 0.2.4-alt1
- initial build for ALT Sisyphus
