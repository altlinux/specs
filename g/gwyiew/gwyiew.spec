Name: gwyiew
Url: http://gwyddion.net/apps/#gwyiew
Version: 2.0
Release: alt1
License: GPL
Packager: Boris Savelev <boris@altlinux.org>

Source: %name-%version.tar.bz2
Group: Sciences/Other
Summary: Simple standalone SPM file viewer that makes use of Gwyddion libraries


# Automatically added by buildreq on Sat Jul 04 2009
BuildRequires: libgwyddion-devel

%description
gwyiew is a very simple standalone SPM file viewer that makes use of Gwyddion libraries.
Its primary purpose is to serve as a comprehensible example ? its source code has only slightly over 200 lines.

It can display any SPM file Gwyddion can (except raw and pixmap files that have to imported manually to Gwyddion)
and it supports multiple channels even though it only displays one at a time - use PageUp/PageDown to cycle through channels.

%prep
%setup

%build
%make_build

%install
%makeinstall_std PREFIX=%_prefix

%files
%doc README
%_bindir/%name

%changelog
* Sat Jul 04 2009 Boris Savelev <boris@altlinux.org> 2.0-alt1
- initial build for Sisyphus

