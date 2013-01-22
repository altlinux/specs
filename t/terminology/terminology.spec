%define ver_major 0.2

Name: terminology
Version: %ver_major.0
Release: alt0.2

Summary: EFL terminal emulator
License: BSD
Group: Terminals
Url: http://www.enlightenment.org/p.php?p=about/terminology

#Source: %name-%version.tar
Source: http://download.enlightenment.org/releases/%name-%version.tar.xz
Patch: %name-0.2-sl-theme.patch
Patch1: %name-0.2-up.patch
Patch2: %name-0.2-alt-default_font.patch

Requires: fonts-bitmap-terminus
Provides: xvt

BuildRequires: intltool
BuildRequires: libevas-devel edje embryo_cc libedje-devel libemotion-devel libelementary-devel >= 1.7.3

%description
An EFL terminal emulator with some extra bells and whistles. It's brand
new and was only started near the begining of June 2012, so expecting it
to do everything a mature terminal emulator does is a bit premature, but
considering it's young age, it does a lot.

%prep
%setup -q
%patch -p1
%patch1 -p1
%patch2 -b .def_font

%build
%autoreconf
%configure

%make_build

%install
%makeinstall_std

# alternatives
mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_bindir/xvt	%_bindir/%name	30
EOF

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/applications/*
%_datadir/%name/
#%%exclude %_datadir/%name/fonts
%_altdir/%name
%_iconsdir/%name.png
%doc AUTHORS ChangeLog COPYING README

%changelog
* Wed Jan 23 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt0.2
- used Terminus 18 as default font

* Sat Dec 15 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt0.1
- first preview build for Sisyphus

