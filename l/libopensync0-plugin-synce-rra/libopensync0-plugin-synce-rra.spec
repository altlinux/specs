%define orig_name libopensync-plugin-synce-rra
Name: libopensync0-plugin-synce-rra
Version: 0.22.1
Release: alt1

Summary: SynCE WM5+ devices plugin for OpenSync
License: GPL
Group: System/Libraries
URL: http://www.synce.org
Packager: Mobile Development Team <mobile@packages.altlinux.org>

Source: %orig_name-%version.tar.gz

Provides: libopensync0-plugin-synce = %version
Obsoletes: libopensync0-plugin-synce

BuildRequires: gcc-c++ glib2-devel libmimedir libopensync0-devel libxml2-devel

BuildRequires: libsynce-devel > 0.13
BuildRequires: librapi-devel > 0.13
BuildRequires: librra-devel > 0.13

%description
This plugin allows applications using OpenSync to synchronise to and from WM5+ based devices.

%prep
%setup -q -n %orig_name-%version

%build
%autoreconf
%configure
%make

%install
%makeinstall install DESTDIR=%buildroot
rm -f %buildroot%_libdir/opensync/plugins/*.la

%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%_libdir/opensync/plugins/*.so
%_datadir/opensync/defaults/*

%changelog
* Tue Sep 08 2009 Alexey Shabalin <shaba@altlinux.ru> 0.22.1-alt1
- Initial package, based on libopensync-plugin-synce
- support WM5+ based devices
