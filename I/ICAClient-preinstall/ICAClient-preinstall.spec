
Name:    ICAClient-preinstall
Version: 13.0.0.256735
Release: alt1

Summary: Set correct environment for Citrix Reseiver downloaded from http://www.citrix.com/
License: GPL
Group:   System/Libraries
URL:     http://www.citrix.com/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   citrix-client-libs.txt

ExclusiveArch: %ix86

BuildRequires(pre): libcurl

BuildRequires: libalsa
BuildRequires: libfreetype
BuildRequires: libGL
BuildRequires: libgst-plugins
BuildRequires: libgtk+2
BuildRequires: libpng12
BuildRequires: libspeex
BuildRequires: libvorbis
BuildRequires: libXaw
BuildRequires: libwebkitgtk2
BuildRequires: libxerces-c

Requires: nspluginwrapper

Provides: libcurl.so.4 = %{get_version libcurl}

%description
Set correct environment for Citrix Reseiver downloaded from http://www.citrix.com/

Tested with ICAClient-13.0.0.256735

%install
mkdir -p %buildroot/lib/citrix-client
cat %SOURCE0 | grep '=> /lib' | sed -ne 's/^[[:space:]]*\(lib[^ ]*\.so[0-9.]*\).*$/\1/p' | sort -u | xargs -ri ln -s /lib/{} %buildroot/lib/citrix-client/
mkdir -p %buildroot/usr/lib/citrix-client
cat %SOURCE0 | grep '=> /usr/lib' | sed -ne 's/^[[:space:]]*\(lib[^ ]*\.so[0-9.]*\).*$/\1/p' | sort -u | xargs -ri ln -s /usr/lib/{} %buildroot/usr/lib/citrix-client/

%files
/lib/citrix-client
/usr/lib/citrix-client

%changelog
* Thu Mar 20 2014 Andrey Cherepanov <cas@altlinux.org> 13.0.0.256735-alt1
- Initial build for ALT Linux
