Name: CloudCross
Version: 1.4.5
Release: alt2
License: BSD
Group: Networking/File transfer
Summary: Syncronization of local files and folders with clouds
Source: v%version.tar.gz
Url: https://cloudcross.mastersoft24.ru/#usage

BuildRequires: gcc-c++ libcurl-devel qt5-base-devel qt5-tools-devel

%description
CloudCross it's open source software for the synchronization of local
files and folders with multiple cloud storages. On this moment
CloudCross supports sync with Yandex.Disk Google Drive Cloud mail.ru
OneDrive and Dropbox. This program was written in pure Qt, without any
third-party libraries.

%prep
%setup -n %name-%version

%build
%qmake_qt5
%make_build

%install
##install -D ccross %buildroot/%_bindir/ccross
%makeinstall INSTALL_ROOT=%buildroot
install -D ccross-app/doc/ccross %buildroot%_man1dir/ccross.1

%files
%doc ccross-app/doc/*.* README* CHANGES*
%_bindir/*
%_man1dir/*

%changelog
* Fri Nov 10 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.4.5-alt2
- NMU: trimmed dependencies according to project files.
  As a side effect package can be build for LoongArch.

* Sat Oct 26 2019 Fr. Br. George <george@altlinux.ru> 1.4.5-alt1
- Autobuild version bump to 1.4.5

* Tue Jan 29 2019 Fr. Br. George <george@altlinux.ru> 1.4.4-alt1
- Autobuild version bump to 1.4.4

* Mon Mar 19 2018 Fr. Br. George <george@altlinux.ru> 1.4.1-alt1
- Autobuild version bump to 1.4.1

* Wed Jul 26 2017 Fr. Br. George <george@altlinux.ru> 1.4.0-alt1
- Autobuild version bump to 1.4.0

* Wed Jul 26 2017 Fr. Br. George <george@altlinux.ru> 1.3.1-alt1
- Initial build for ALT

