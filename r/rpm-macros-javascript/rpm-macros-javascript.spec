Name: rpm-macros-javascript
Version: 0.2
Release: alt1

Summary: RPM helper scripts for packaging javascipt libraries
License: GPL
Group: Development/Other

Url: http://www.altlinux.org/JavaScript_Policy

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

%description
RPM helper scripts for package javascript libraries.

See %url for detailed javascript libraries packaging policy.

%prep
%setup

%install
install -D -m644 macros %buildroot/%_rpmmacrosdir/javascript

%files
#doc EXAMPLE.ALT
%_rpmmacrosdir/javascript

%changelog
* Fri Jan 27 2012 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- add _jquery, _jquerypluginsdir macros

* Tue Oct 11 2011 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
