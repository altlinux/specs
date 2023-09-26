Name: fvwm3
Version: 1.0.8
Release: alt1

Summary: F(?) Virtual Window Manager, the successor to fvwm2
License: GPLv2+
Group: Graphical desktop/FVWM based
Url: http://www.fvwm.org/

# https://github.com/fvwmorg/fvwm3
Source: %name-%version.tar

BuildRequires: asciidoctor /usr/bin/pod2man
BuildRequires: libbson-devel libevent-devel libfribidi-devel
BuildRequires: libXcursor-devel libXpm-devel libXrandr-devel libXt-devel libXft-devel
BuildRequires: libpng-devel librsvg-devel libcairo-devel libreadline-devel
BuildRequires: perl-Tk rpm-build-python3

%description
fvwm3 window manager, the successor to fvwm2.

Fvwm is a virtual window manager for the X windows system. It was
originally a feeble fork of TWM by Robert Nation in 1993 (fvwm history),
and has evolved into the fantastic, fabulous, famous, flexible, and so
on, window manager we have today.

Fvwm is ICCCM-compliant and highly configurable. Starting from a minimal
configuration, Fvwm can be configured with both internal tools and third
party software to customize most aspects of a desktop.

Currently, your existing fvwm2 config will work with fvwm3, but over time
this will change.

%package scripts
Summary: F(?) Virtual Window Manager, the successor to fvwm2, additional scripts
Group: Graphical desktop/FVWM based
BuildArch: noarch
%description scripts
This package contains the FvwmPerl module, fvwm Perl library and other
scripts for fvwm3 window manager, the successor to fvwm2.


%prep
%setup -q

%build
%autoreconf
%configure --enable-mandoc
%make

%install
%makeinstall_std
mv %buildroot/%_bindir/FvwmCommand         %buildroot/%_bindir/Fvwm3Command
mv %buildroot/%_bindir/fvwm-convert-2.6    %buildroot/%_bindir/fvwm3-convert-2.6
mv %buildroot/%_bindir/fvwm-menu-desktop   %buildroot/%_bindir/fvwm3-menu-desktop
mv %buildroot/%_bindir/fvwm-menu-directory %buildroot/%_bindir/fvwm3-menu-directory
mv %buildroot/%_bindir/fvwm-menu-xlock     %buildroot/%_bindir/fvwm3-menu-xlock
mv %buildroot/%_bindir/fvwm-perllib        %buildroot/%_bindir/fvwm3-perllib
mv %buildroot/%_mandir/man1/FvwmPerl.1     %buildroot/%_mandir/man1/Fvwm3Perl.1
mv %buildroot/%_mandir/man1/fvwm-convert-2.6.1 %buildroot/%_mandir/man1/fvwm3-convert-2.6.1

# install additional docs
install -p -D -m644 COPYING NEWS *.md -t $RPM_BUILD_ROOT%_docdir/%name-%version/

%define _perl_lib_path %perl_vendor_privlib:%_datadir/fvwm3/perllib

%find_lang --output=%name.lang fvwm FvwmScript

%files -f %name.lang
%_bindir/fvwm3
%_bindir/fvwm-root
%dir %_libexecdir/fvwm3/
%dir %_libexecdir/fvwm3/%version/
%_libexecdir/fvwm3/%version/*
%exclude %_libexecdir/fvwm3/%version/FvwmPerl
%dir %_datadir/fvwm3/
%_datadir/fvwm3/*
%exclude %_datadir/fvwm3/perllib/
%exclude %_datadir/fvwm3/fvwm-script-ComExample.pl

%_mandir/man?/*
%exclude %_mandir/man1/fvwm3-convert-2.6.1*
%exclude %_mandir/man1/fvwm-menu-desktop.1*
%exclude %_mandir/man1/fvwm-menu-directory.1*
%exclude %_mandir/man1/fvwm-menu-xlock.1*
%exclude %_mandir/man1/fvwm-perllib.1*
%exclude %_mandir/man1/Fvwm3Perl.1*
%_docdir/%name-%version

%files scripts
%_bindir/Fvwm3Command
%_bindir/fvwm3-convert-2.6
%_bindir/fvwm3-menu-desktop
%_bindir/fvwm3-menu-directory
%_bindir/fvwm3-menu-xlock
%_bindir/fvwm3-perllib
%_libexecdir/fvwm3/%version/FvwmPerl
%dir %_libexecdir/fvwm3
%dir %_libexecdir/fvwm3/%version
%_datadir/fvwm3/perllib/
%_datadir/fvwm3/fvwm-script-ComExample.pl
%_mandir/man1/fvwm3-convert-2.6.1*
%_mandir/man1/fvwm-menu-desktop.1*
%_mandir/man1/fvwm-menu-directory.1*
%_mandir/man1/fvwm-menu-xlock.1*
%_mandir/man1/fvwm-perllib.1*
%_mandir/man1/Fvwm3Perl.1*

%changelog
* Tue Sep 26 2023 Vladislav Zavjalov <slazav@altlinux.org> 1.0.8-alt1
- 1.0.8

* Wed Oct 19 2022 Vladislav Zavjalov <slazav@altlinux.org> 1.0.5-alt2
- rename scripts and perl libraries to avoid collisions with old fvwm

* Wed Oct 19 2022 Vladislav Zavjalov <slazav@altlinux.org> 1.0.5-alt1
- 1.0.5

* Mon Sep 20 2021 Vladislav Zavjalov <slazav@altlinux.org> 1.0.4-alt1
- 1.0.4

* Tue Dec 22 2020 Vladislav Zavjalov <slazav@altlinux.org> 1.0.2-alt2
- Rename perl modules to avoid duplicated provides

* Mon Dec 21 2020 Vladislav Zavjalov <slazav@altlinux.org> 1.0.2-alt1
- 1.0.2, first build for Altlinux
