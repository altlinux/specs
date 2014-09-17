Name: 	  chromium-pepperflash
Version:  1.5.1
Release:  alt1

Summary:  Pepper Flash Player - browser plugin for Chromium
License:  GPLv3+
Group:    Networking/WWW
Url: 	  http://altlinux.org/PepperFlash

Packager: Andrey Cherepanov <cas@altlinux.org>

Source1:  update-pepperflash

BuildRequires: curl wget gzip xml-utils
Requires: chromium
Requires: curl wget gzip xml-utils

%description
This package will download Chrome from Google, and unpack it to make the
included Pepper Flash Player available for use with Chromium.  The end
user license agreement is available at Google.

%prep

%install
install -D -m 0755 %SOURCE1 %buildroot%_sbindir/update-pepperflash
mkdir -p %buildroot%_libdir/browser-plugins
mkdir -p %buildroot%_libdir/pepper-plugins
touch %buildroot%_libdir/pepper-plugins/libpepflashplayer.so
mkdir -p %buildroot%_cachedir/pepperflash

%preun
%_sbindir/update-pepperflash --uninstall --quiet ||:
exit 0

%post
%_sbindir/update-pepperflash --install --quiet ||:

%files
%_sbindir/update-pepperflash
%ghost %_libdir/pepper-plugins/libpepflashplayer.so
%dir %_cachedir/pepperflash

%changelog
* Tue Sep 16 2014 Andrey Cherepanov <cas@altlinux.org> 1.5.1-alt1
- Fix version detect in new plugin versions
- Add arguments --clean and --version
- Change plugin location to %%_libdir/pepper-plugins

* Mon Sep 01 2014 Andrey Cherepanov <cas@altlinux.org> 1.5-alt3
- Remove unnecessary require of glibc-utils

* Fri Aug 29 2014 Andrey Cherepanov <cas@altlinux.org> 1.5-alt2
- Mark plugin file as %%ghost file (ALT #30225)
- Package cache directory

* Tue Jul 29 2014 Andrey Cherepanov <cas@altlinux.org> 1.5-alt1
- Initial build in Sisyphus adapted from Debian

