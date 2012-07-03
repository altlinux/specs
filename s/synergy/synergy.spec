Summary:	Mouse and keyboard sharing utility
Name:		synergy
Version:	1.3.7
Release:	alt1
License:	GPL
Group:		Accessibility
URL:		http://synergy-foss.org
Source0:	%name-%version.tar
Patch0:		%name-%version-%release.patch

Packager:	Evgeny Sinelnikov <sin@altlinux.ru>

# Automatically added by buildreq on Fri Sep 28 2007
BuildRequires: gcc-c++ libXtst-devel
BuildRequires: rpm-macros-cmake
BuildRequires: cmake

%description
Synergy lets you easily share a single mouse and keyboard between
multiple computers with different operating systems, each with its own
display, without special hardware. It's intended for users with
multiple computers on their desk since each system uses its own
display.

%prep
%setup -q
%patch0 -p0

%build
./configure
%make_build VERBOSE=1

%install
install -D bin/synergyc %buildroot%_bindir/synergyc
install -D bin/synergys %buildroot%_bindir/synergys
install -D -m0644 doc/synergy.conf.example %buildroot%_sysconfdir/synergy.conf
install -D -m0644 doc/synergys.man %buildroot/%_man1dir/synergys.1
install -D -m0644 doc/synergyc.man %buildroot/%_man1dir/synergyc.1

%files
%doc ChangeLog COPYING README
%doc doc/synergy.conf*
%_bindir/synergyc
%_bindir/synergys
%config(noreplace) %_sysconfdir/synergy.conf
%_man1dir/synergys*
%_man1dir/synergyc*

%changelog
* Sun Sep 11 2011 Evgeny Sinelnikov <sin@altlinux.ru> 1.3.7-alt1
- Build new version with bew scheme

* Fri Sep 28 2007 Eugene V. Horohorin <genix@altlinux.ru> 1.3.1-alt1
- initial build

