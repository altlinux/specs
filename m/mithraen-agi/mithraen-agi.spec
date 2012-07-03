Name: mithraen-agi
Group: Development/Other
License: GPL
Version: 0.0.3
Release: alt1
Summary: Some Asterisk AGI scripts

BuildArch: noarch

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

# Automatically added by buildreq on Sun Apr 11 2010 (-bb)
BuildRequires: perl-asterisk-perl

%description
%summary

%prep
%setup
%build
%install
%make install DESTDIR=%buildroot
%files
/usr/lib/asterisk/agi-bin/callback
/usr/lib/asterisk/agi-bin/callback2

%changelog
* Sun Apr 18 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.3-alt1
- fix install

* Sun Apr 18 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.2-alt1
- Add callback2.pl

* Sun Apr 11 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt3
- small fix: we really need /usr/lib instead of %%_libdir

* Sun Apr 11 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt2
- build as noarch

* Sun Apr 11 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- initial build for ALT Linux Sisyphus

