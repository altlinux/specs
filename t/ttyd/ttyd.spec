%define _unpackaged_files_terminate_build 1

Name:     ttyd
Version:  1.7.7
Release:  alt1

Summary:  Share your terminal over the web
License:  MIT
Group:    Terminals
Url:      https://github.com/tsl0922/ttyd
Vcs:      https://github.com/tsl0922/ttyd

Source:   %name-%version.tar
Patch0:   ttyd-1.7.7-fedora-use-system-libuv.patch

BuildRequires: libjson-c-devel
BuildRequires: cmake
BuildRequires: vim-common
BuildRequires: libssl-devel
BuildRequires: libwebsockets-devel
BuildRequires: gcc-c++
BuildRequires: zlib-devel
BuildRequires: libuv-devel
BuildRequires: libev-devel

%description
ttyd is a simple command-line tool for sharing terminal over the web.

%prep
%setup
%patch0 -p0

%build
%cmake -DLWS_WITH_LIBUV=ON
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md
%_bindir/*
%_man1dir/*


%changelog
* Fri Aug 14 2026 Anton Meleshnikov <alton@altlinux.org> 1.7.7-alt1
- 1.7.7 released (thanks fedora for the patch)
- switched to use .gear/tags
- added vcs tag

* Tue Apr 25 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.3-alt1
- 1.7.3 released

* Mon Dec 26 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.2-alt1
- 1.7.2 released

* Mon Jun 27 2022 Dmitry Lyalyaev <fruktime@altlinux.org> 1.6.3-alt1
- Initial build for ALTLinux

