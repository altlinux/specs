Name: goaccess

Summary: Is an open source real-time web log analyzer
Version: 1.8.1
Release: alt1

URL: https://goaccess.io/
#URL: http://goaccess.prosoftcorp.com/

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License: %mit
Group: Other

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Jul 20 2021
# optimized out: glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libncurses-devel libtinfo-devel perl python3 python3-base python3-module-paste ruby ruby-stdlibs sh4 shared-mime-info tzdata xz
BuildRequires: glib2-devel libGeoIP-devel libncursesw-devel libssl-devel


%description
GoAccess is an open source real-time web log analyzer
and interactive viewer that runs in a terminal in *nix
systems. It provides fast and valuable HTTP statistics
for system administrators that require a visual server
report on the fly.

%prep
%setup
%patch0 -p1

%build
%autoreconf
#%%add_optflags -fcommon
%configure --with-getline \
           --with-openssl \
           --enable-geoip=legacy \
           --enable-utf8  \
           %nil
%make

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS COPYING README TODO

%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/goaccess.conf
%config %_sysconfdir/%name/browsers.list
%config %_sysconfdir/%name/podcast.list

%_bindir/goaccess
%_man1dir/goaccess*


%changelog
* Tue Nov 07 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.8.1-alt1
- New version

* Sat Oct 21 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.8-alt1
- New version

* Wed Aug 09 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.7.2-alt1
- New version

* Sun Nov 07 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.5.2-alt1
- New version

* Tue Jul 20 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.5.1-alt1
- New version
  - lot of new features
  - incrementally logs processing through the on-disk persistence option
  - fixes for overflows, segfaults, etc
- Update project URL
- Fix license

* Tue Apr 06 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.1-alt2
- Fixed FTBFS with -fcommon.

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


