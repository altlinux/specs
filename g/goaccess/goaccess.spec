Summary: Is an open source real-time web log analyzer
Name: goaccess
Version: 1.1.1
Release: alt1
Url: http://goaccess.prosoftcorp.com/
Source: %name-%version.tar
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License: GPLv2
Group: Other

BuildRequires: glib2-devel libncurses-devel libGeoIP-devel

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
%configure --enable-geoip
%make

%install
install -D -m 755 goaccess %buildroot%_sbindir/goaccess
install -D -m 644 goaccess.1 %buildroot%_man1dir/goaccess.1

%files
%_sbindir/goaccess
%_man1dir/goaccess*

%doc AUTHORS ChangeLog NEWS COPYING README TODO

%changelog
* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.1.1-alt1
- New version (ALT 32790)

* Fri Jun 10 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 0.9.8-alt1
- New version

* Mon Feb 29 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 0.9.7-alt1
- New version

* Tue Sep 15 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 0.9.4-alt1
- New version

* Mon Aug 31 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 0.9.3-alt1
- New version

* Tue Apr 28 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 0.9-alt1
- New version

* Wed Dec 10 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.8.5-alt1
- New version

* Thu Sep 11 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.8.4-alt1
- New version

* Fri Aug 01 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.8.3-alt1
- New version

* Thu Jun 19 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.8.1-alt1
- New version

* Tue Dec 17 2013 Valentin Rosavitskiy <valintinr@altlinux.org> 0.6.2-alt2
- Builded with geoip support

* Fri Nov 08 2013 Valentin Rosavitskiy <valintinr@altlinux.org> 0.6.2-alt1
- Builded for t6

* Fri Aug 09 2013 Valentin Rosavitskiy <valintinr@altlinux.org> 0.6.1-alt1
- New version

* Mon Jun 24 2013 Valentin Rosavitskiy <valintinr@altlinux.org> 0.5.1-alt2
- Add doc files

* Wed Jun 12 2013 Valentin Rosavitskiy <valintinr@altlinux.org> 0.5.1-alt1
- Initial build


