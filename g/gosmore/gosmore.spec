Name: gosmore
Version: 0.0.0.20101111
Release: alt4.svn.24204
Summary: Openstreetmap.org viewer / wayfinder / search client
License: GPLv2+
Group: Sciences/Geosciences
Url: http://sourceforge.net/projects/gosmore/
Packager: Egor Glukhov <kaman@altlinux.org>
Source0: %name-%version.tar

BuildRequires: gcc-c++ libcurl-devel libgtk+2-devel libxml2-devel

%description
Openstreetmap.org viewer with searching and routing capabilities
Gosmore is a openstreetmap.org viewer. It uses it's own binary format that
facilitate interactive searching and routing. It has many of the features
found in modern handheld GPS receivers.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc README
%_bindir/*
%_man1dir/%name.1.gz
%_datadir/%name
%_pixmapsdir/%name.xpm
%_desktopdir/%name.desktop

%changelog
* Tue Jul 05 2011 Egor Glukhov <kaman@altlinux.org> 0.0.0.20101111-alt4.svn.24204
- Fixed build

* Tue Feb 15 2011 Egor Glukhov <kaman@altlinux.org> 0.0.0.20101111-alt3.svn.24204
- Fixed build

* Wed Dec 08 2010 Egor Glukhov <kaman@altlinux.org> 0.0.0.20101111-alt2.svn.24204
- Fixed freedesktop categories

* Thu Nov 18 2010 Egor Glukhov <kaman@altlinux.org> 0.0.0.20101111-alt1.svn.24204
- Initial build for Sisyphus

