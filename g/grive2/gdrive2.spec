Name: grive2
Version: 0.5.0
Release: alt1
License: GPLv2
Group: Networking/File transfer
Url: http://yourcmc.ru/wiki/Grive2
Summary: Google Drive client with the support for the new Drive REST API and partial sync
Source: v%version.tar.gz
# Automatically added by buildreq on Wed Jul 26 2017
# optimized out: boost-devel boost-devel-headers cmake-modules glibc-kernheaders-x86 libgpg-error libgpg-error-devel libstdc++-devel pkg-config python-base
BuildRequires: boost-filesystem-devel boost-program_options-devel cmake gcc-c++ glibc-kernheaders-generic libcurl-devel libexpat-devel libgcrypt-devel libyajl-devel zlib-devel

%description
This is the fork of original "Grive" (https://github.com/Grive/grive) Google Drive client with the support for the new Drive REST API and partial sync.

Grive can be considered still beta or pre-beta quality. It simply downloads all the files in your Google Drive into the current directory. After you make some changes to the local files, run grive again and it will upload your changes back to your Google Drive. New files created locally or in Google Drive will be uploaded or downloaded respectively. Deleted files will also be "removed". Currently Grive will NOT destroy any of your files: it will only move the files to a directory named .trash or put them in the Google Drive trash. You can always recover them.

%prep
%setup -n %name-%version

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*
%_man1dir/*

%changelog
* Wed Jul 26 2017 Fr. Br. George <george@altlinux.ru> 0.5.0-alt1
- Autobuild version bump to 0.5.0

* Wed Jul 26 2017 Fr. Br. George <george@altlinux.ru> 0.4.2-alt1
- Initial build for ALT

