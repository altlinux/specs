Name: grapherAD
Url: http://gwyddion.net/apps/grapherAD.php
Version: 1.0
Release: alt1
License: GPL
Packager: Boris Savelev <boris@altlinux.org>

Source: %name-%version.tar.bz2
Group: Sciences/Other
Summary: Graphing monitor for a custom spectroscopic ellipsometry and spectrophotometry

# Automatically added by buildreq on Sat Jul 04 2009
BuildRequires: libgwyddion-devel

%description
grapherAD is a graphing monitor for a custom spectroscopic ellipsometry
and spectrophotometry data fitting software used at
Department of Physical Electronics of Faculty of Science, Masaryk University.

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
* Sat Jul 04 2009 Boris Savelev <boris@altlinux.org> 1.0-alt1
- initial build for Sisyphus

