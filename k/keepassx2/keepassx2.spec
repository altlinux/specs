%define _name keepassx

Name: %{_name}2
Version:  2.0.3
Release:  alt1
Summary: KeePassX Password Safe - light-weight cross-platform password manager
Group: File tools
License: %gpl2plus
URL: http://www.keepassx.org/

Source: %name-%version.tar

Conflicts: %_name < %version

BuildRequires(pre): rpm-build-licenses
BuildRequires: cmake ctest gcc-c++
BuildRequires: libqt4-devel >= 4.6.0
BuildRequires: libgcrypt-devel >= 1.6.0
BuildRequires: zlib-devel >= 1.2.0
BuildRequires: libXi-devel libXtst-devel libX11-devel

%description
KeePassX  is  a cross platform port  of the windows  application
"Keepass Password Safe". It is an OpenSource password safe which
helps you to manage your passwords in an easy and secure way. It
uses a highly encrypted database locked with one master key.

KeePassX saves many different information: user names, passwords,
urls, comments and  file attachments in one single database.  The
entries could be  sorted in groups, with user-defined  titles and
icons specified for each entry or group. Also KeePassX  offers an 
utility for secure password generation.

The complete database is always encrypted either with AES  (alias
Rijndael) or  Twofish  encryption algorithm using  a 256 bit key.
The database format  of KeePassX  is compatible with the one used
in KeePass Password Safe.

%prep
%setup -n %name-%version

%build
%cmake \
  -DWITH_CXX11=ON

%cmake_build VERBOSE=1

%install
%cmakeinstall_std

%files
%_bindir/*
%_libdir/%_name/libkeepassx-autotype-x11.so
%_desktopdir/%_name.desktop
%_datadir/mime/packages/%_name.xml
%_iconsdir/hicolor/*/*/*
%_datadir/%_name

%changelog
* Tue Dec 20 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.3-alt1
- 2.0.3

* Tue Apr 19 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Tue Dec 08 2015 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1
- 2.0 release

* Mon Nov 16 2015 Alexey Shabalin <shaba@altlinux.ru> 1.9.92-alt1.beta2
- 2.0 beta2

* Mon Oct 06 2014 Alexey Shabalin <shaba@altlinux.ru> 1.9.85-alt1.alpha6
- Initial build upstream snapshot
