
Summary: Tools for managing the osinfo database
Name: osinfo-db-tools
Version: 1.0.0
Release: alt1
License: LGPLv2+
Group: Development/Tools
Source: %name-%version.tar
Url: http://libosinfo.org/

BuildRequires: intltool >= 0.40.0
BuildRequires: gnome-common gtk-doc
BuildRequires: glib2-devel libgio-devel
BuildRequires: libxml2-devel >= 2.6.0
BuildRequires: libxslt-devel >= 1.0.0
BuildRequires: libarchive-devel
BuildRequires: perl-podlators

Conflicts: libosinfo < 1.0.0

%description
This package provides tools for managing the osinfo database of
information about operating systems for use with virtualization

%prep
%setup

%build
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING.LIB NEWS README
%_bindir/*
%_man1dir/*

%changelog
* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt1
- 1.0.0

