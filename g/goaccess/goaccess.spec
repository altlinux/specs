Summary: Is an open source real-time web log analyzer
Name: goaccess
Version: 0.5.1
Release: alt1
Url: http://goaccess.prosoftcorp.com/
Source: %name-%version.tar
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License: GPLv2
Group: Other

BuildRequires: glib2-devel

%description
GoAccess is an open source real-time web log analyzer
and interactive viewer that runs in a terminal in *nix
systems. It provides fast and valuable HTTP statistics
for system administrators that require a visual server
report on the fly.

%prep
%setup

%build
%autoreconf
%configure
%make

%install
install -D -m 755 goaccess %buildroot%_sbindir/goaccess
install -D -m 644 goaccess.1 %buildroot%_man1dir/goaccess.1

%files
%_sbindir/goaccess
%_man1dir/goaccess.1.gz
%changelog
* Wed Jun 12 2013 Valentin Rosavitskiy <valintinr@altlinux.org> 0.5.1-alt1
- Initial build


