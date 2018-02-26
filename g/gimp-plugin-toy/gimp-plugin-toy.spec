%define gimpplugindir %(gimptool-2.0 --gimpplugindir)

Name: gimp-plugin-toy
Version: 1.0.1
Release: alt1

Summary: GIMP plugin for simple tilt-shift fakes
License: BSD-like
Group: Graphics

Url: http://registry.gimp.org/node/25803
Source: http://registry.gimp.org/files/gimp-plugin-toy-%version.tar.gz

Requires: gimp
# Automatically added by buildreq on Sat Nov 12 2011
BuildRequires: intltool libgimp-devel

%description
This plug-in creates a toy effect or tilt-shift miniature faking on a selected layer.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang gimp20-toy

%files -f gimp20-toy.lang
%gimpplugindir/plug-ins/*
%_datadir/toy
%doc COPYING

%changelog
* Sat Nov 12 2011 Victor Forsiuk <force@altlinux.org> 1.0.1-alt1
- Initial build.
