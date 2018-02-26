Name: rpm-build-mediawiki
Version: 0.3
Release: alt1

Summary: RPM helper scripts for package mediawiki extensions
License: GPL
Group: Development/Other

URL: http://www.freesource.info/wiki/Altlinux/Policy/Fonts
Source: ftp://download.etersoft.ru/pub/Etersoft/BuildFarm/sources/tarball/%name-%version.tar

BuildArch: noarch

%description
RPM helper scripts for package mediawiki extensions.
It introduced mediawiki_ext_install macro.

See %url for detailed mediawiki extension packaging policy.

%prep
%setup

%install
install -D -m644 macros %buildroot/%_rpmmacrosdir/mediawiki

%files
%doc EXAMPLE.ALT
%_rpmmacrosdir/mediawiki

%changelog
* Sat May 15 2010 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- do not pack temp. *.files file

* Tue Feb 02 2010 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- fix spec, fix generated path to extension

* Tue Feb 02 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
