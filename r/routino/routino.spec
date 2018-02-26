Name: routino
Version: 2.1.2
Release: alt1
Summary: Router for OpenStreetMap Data
License: AGPL 3.0
Group: Sciences/Geosciences
Url: http://routino.org/
Packager: Egor Glukhov <kaman@altlinux.org>
Source0: %name-%version.tar
BuildRequires: flex

%description
Routino is an application for finding a route between two points using
the dataset of topographical information collected by OpenStreetMap.

%prep
%setup

%build
%make_build

%install
%makeinstall_std

%files
%doc doc/*.txt doc/html
%exclude %_prefix/doc
%_bindir/*
%_datadir/%name

%changelog
* Sat Nov 19 2011 Egor Glukhov <kaman@altlinux.org> 2.1.2-alt1
- New version

* Tue Nov 23 2010 Egor Glukhov <kaman@altlinux.org> 1.5.1-alt1
- Initial build for Sisyphus
