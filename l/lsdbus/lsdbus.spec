Name: lsdbus
Version: 0.1
Release: alt1

Summary: utility to scan the system and session message bus
License: GPLv2
Group: Monitoring

Source0: %name-%version.tgz

Patch0: lsdbus-as-needed.patch

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Mon Apr 14 2008
BuildRequires: libdbus-glib-devel

%description
utility to scan the system and session message bus for participants
and prints their names an unique bus identifiers.


%prep
%setup -q
%patch0 -p0

%build
%make_build CFLAGS="%optflags"

%install
mkdir -p %buildroot{%_bindir,%_man1dir}/
install -m755 lsdbus %buildroot%_bindir/
install -m644 lsdbus.1 %buildroot%_man1dir/

%files
%doc README
%_bindir/lsdbus
%_man1dir/*

%changelog
* Mon Apr 14 2008 Igor Zubkov <icesik@altlinux.org> 0.1-alt1
- build for Sisyphus

