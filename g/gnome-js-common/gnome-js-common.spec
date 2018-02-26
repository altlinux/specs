%undefine _configure_target
%define ver_major 0.1
%def_enable seed
%def_enable gjs

Name: gnome-js-common
Version: %ver_major.2
Release: alt1

Summary: Common JavaScript modules for GNOME
License: GPLv3
Group: Development/Other
Url: http://www.gnome.org

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.bz2

BuildArch: noarch

# Automatically added by buildreq on Mon Sep 21 2009
BuildRequires: glibc-devel-static intltool

BuildRequires: intltool perl-XML-Parser
%{?_enable_seed:BuildRequires: libseed-devel}
%{?_enable_gjs:BuildRequires: libgjs-devel}

%description
gnome-js-common is a module holding tests and JavaScript code useful
or common to both Seed and gjs.

%prep
%setup -q

%build
%configure %{subst_enable gjs} \
	 %{subst_enable seed}

%make_build

%install
%make  \
	DESTDIR=%buildroot \
	gnome_js_commondocdir=%_docdir/%name-%version \
	libdir=%_datadir \
	install

#mkdir -p %buildroot%_libdir/gnome-js

%files
%_datadir/gnome-js/
%_datadir/pkgconfig/gnome-js-common.pc
#%dir %_libdir/gnome-js
%doc %_docdir/%name-%version

%changelog
* Sun Jan 03 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- new version

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- first build for Sisyphus

