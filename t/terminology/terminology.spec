%def_disable snapshot
%define ver_major 1.0

Name: terminology
Version: %ver_major.0
Release: alt1

Summary: EFL terminal emulator
License: BSD
Group: Terminals
Url: http://www.enlightenment.org/p.php?p=about/terminology

%if_disabled snapshot
Source: http://download.enlightenment.org/rel/apps/%name/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif
Patch: %name-1.0.0-alt-default_font.patch

Requires: fonts-bitmap-terminus
Provides: xvt

BuildRequires: intltool
# BuildRequires: libevas-devel edje embryo_cc libedje-devel libemotion-devel libethumb-devel
# for efl >= 1.8.0
Conflicts: libelementary < 1.8.0
BuildRequires: efl-libs-devel
BuildRequires: libelementary-devel >= 1.8.0

%description
An EFL terminal emulator with some extra bells and whistles. It's brand
new and was only started near the begining of June 2012, so expecting it
to do everything a mature terminal emulator does is a bit premature, but
considering it's young age, it does a lot.

%prep
%setup
%patch -b .def_font

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
%_altdir/%name
%_iconsdir/%name.png
%_man1dir/%name.1*
%doc AUTHORS ChangeLog COPYING README

%changelog
* Thu Jan 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Mon Dec 21 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt2
- updated to v0.9.1-51-gf731ff6

* Sat Sep 19 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- 0.9.1

* Mon Sep 07 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- 0.9.0

* Mon May 04 2015 Yuri N. Sedunov <aris@altlinux.org> 0.8.99-alt0.1
- 0.8.99_27179b65

* Mon Feb 16 2015 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

* Sun Sep 21 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.99-alt1
- 0.6.99_a61c3499

* Thu Sep 18 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt2
- rebuilt with efl/elementary-1.11.2

* Tue Jul 08 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Thu Jul 03 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Mon Mar 10 2014 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Sun Dec 08 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0 for E18

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Wed Jan 23 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt0.2
- used Terminus 18 as default font

* Sat Dec 15 2012 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt0.1
- first preview build for Sisyphus

