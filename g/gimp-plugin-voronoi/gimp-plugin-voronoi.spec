%define gimpplugindir %(gimptool --gimpplugindir)

Name: gimp-plugin-voronoi
Version: 2.2
Release: alt2

Summary: The ultimate Gimp Voronoi pattern generator
License: GPLv2+
Group: Graphics

# Upstream domain was hijacked by jackals^Wdomainers
Url: http://replay.waybackmachine.org/20070912230133/http://trific.ath.cx/software/gimp-plugins/voronoi/
Source: voronoi-2.2.tar.bz2

Requires: gimp >= 2.2

# Automatically added by buildreq on Tue Apr 12 2011
BuildRequires: libgimp-devel

%description
The ultimate Gimp pattern generator. Technically it generates 2D Voronoi
diagrams of various semi-random sets of points and then visualizes them
somehow.

%prep
%setup -n voronoi-%version

%build
subst 's/^LDFLAGS =/LDLIBS =/' Makefile
subst 's/-O2 -march=`uname -m`/%optflags/' Makefile
%make_build

%install
%makeinstall_std

%files
%gimpplugindir/plug-ins/*

%changelog
* Tue Apr 12 2011 Victor Forsiuk <force@altlinux.org> 2.2-alt2
- Fix to build with --as-needed and get rid of overlinked libraries.

* Tue Sep 04 2007 Victor Forsyuk <force@altlinux.org> 2.2-alt1
- Initial build.
