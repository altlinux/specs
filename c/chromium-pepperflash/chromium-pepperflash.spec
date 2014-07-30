Name: 	  chromium-pepperflash
Version:  1.5
Release:  alt1

Summary:  Pepper Flash Player - browser plugin for Chromium
License:  GPLv3+
Group:    Networking/WWW
Url: 	  http://altlinux.org/PepperFlash

Packager: Andrey Cherepanov <cas@altlinux.org>

Source1:  update-pepperflash

BuildRequires: curl wget gzip xml-utils glibc-utils
Requires: chromium
Requires: curl wget gzip xml-utils glibc-utils
BuildArch: noarch

%description
This package will download Chrome from Google, and unpack it to make the
included Pepper Flash Player available for use with Chromium.  The end
user license agreement is available at Google.

%prep

%install
install -D -m 0755 %SOURCE1 %buildroot%_sbindir/update-pepperflash

%preun
%_sbindir/update-pepperflash --uninstall --quiet ||:
exit 0

%post
%_sbindir/update-pepperflash --install --quiet ||:

%files
%_sbindir/update-pepperflash

%changelog
* Tue Jul 29 2014 Andrey Cherepanov <cas@altlinux.org> 1.5-alt1
- Initial build in Sisyphus adapted from Debian

