%define oname gupnp-vala

Name: lib%oname
Version: 0.10.3
Release: alt1
Summary: GUPnP is a uPnP framework. This adds vala language bindings

Group: Development/Other
License: LGPLv2+
Url: http://www.gupnp.org/
Packager: Alexey Shabalin <shaba@altlinux.ru>

Source: http://www.gupnp.org/sources/bindings/%name-%version.tar

%define vala_ver 0.11.3
%define gssdp_ver 0.11.0
%define gupnp_ver 0.18.0
%define gupnp_av_ver 0.9.0
%define gupnp_dlna_ver 0.5.1

BuildRequires: vala >= %vala_ver vala-tools >= %vala_ver libvala-devel >= %vala_ver
BuildRequires: libgssdp-devel >= %gssdp_ver
BuildRequires: libgupnp-devel >= %gupnp_ver
BuildRequires: libgupnp-av-devel >= %gupnp_av_ver
BuildRequires: libgupnp-dlna-devel >= %gupnp_dlna_ver

%description
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

This package adds vala language bindings

%prep
%setup -q

%build
%autoreconf
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%check
%make_build check

%files
%doc AUTHORS COPYING
%_datadir/vala/vapi/*
%_pkgconfigdir/*.pc

%changelog
* Tue Mar 13 2012 Alexey Shabalin <shaba@altlinux.ru> 0.10.3-alt1
- 0.10.3

* Wed Sep 21 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.2-alt1
- 0.10.2

* Thu Jun 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.0-alt1
- 0.9.0

* Tue May 17 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Tue Oct 19 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.12-alt1
- 0.6.12

* Mon May 17 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.6-alt1
- 0.6.6

* Wed Mar 17 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.4-alt1
- 0.6.4

* Fri Dec 04 2009 Alexey Shabalin <shaba@altlinux.ru> 0.6.2-alt1
- Initial release
