%define _altdata_dir %_datadir/alterator

Name: alterator-asterisk-gateway
Version: 0.0.3
Release: alt1

BuildArch: noarch

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source:%name-%version.tar

Summary: alterator module for E1<->SIP gateway setup
License: GPL
Group: System/Configuration/Other
Requires: alterator
Requires: alterator-l10n
Requires(pre): asterisk-user

BuildPreReq: alterator >= 4.7-alt1

# Automatically added by buildreq on Mon Jul 11 2005 (-bi)
BuildRequires: alterator

%description
%summary

%prep
%setup -q

%build
%make_build
touch GATEWAY_IP

%install
%makeinstall
install -m 0644 -D GATEWAY_IP %buildroot/etc/asterisk/GATEWAY_IP

%files
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*
%_alterator_backend3dir/*
%_datadir/alterator/help/*/*.html
%config(noreplace) %attr(0644,_asterisk,pbxadmin) /etc/asterisk/GATEWAY_IP

%changelog
* Fri Nov 27 2009 Stanislav Ievlev <inger@altlinux.org> 0.0.3-alt1
- use workflow 'none'

* Thu Oct 15 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.2-alt1
- fix typo in backend (thanks to misha@)

* Fri Sep 18 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- first build for Sisyphus

