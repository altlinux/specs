%define ver_major 3.10

Name: gnome-getting-started-docs
Version: %ver_major.0.1
Release: alt1

Summary: Help for a new GNOME users
License: %fdl
Group: Graphical desktop/GNOME
Url: ftp://ftp.gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

BuildArch: noarch

%define yelp_ver 3.6.0

BuildRequires: rpm-build-gnome rpm-build-licenses
BuildRequires: intltool yelp-tools >= %yelp_ver xml-utils xsltproc xmllint

%description
This package contains a GNOME 'Getting Started' guide that can be viewed with
yelp. It is normally used together with gnome-initial-setup.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang --with-gnome --output=%name.lang getting-started gnome-help

%files -f %name.lang
%doc AUTHORS README NEWS

%changelog
* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0.1-alt1
- 3.10.0.1

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0.1-alt1
- 3.8.0.1

* Thu Feb 28 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.90-alt1
- first build for people/gnome

