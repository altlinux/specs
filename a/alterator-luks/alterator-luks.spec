Name: alterator-luks
Version: 0.1
Release: alt1

Source:%name-%version.tar

Packager: Timur Aitov <timonbl4@altlinux.org>

Summary: alterator module for change LUKS passphrase
License: GPL
Group: System/Configuration/Other
BuildArch: noarch

BuildRequires: alterator

Requires: alterator
Requires: alterator-l10n

%description
alterator module for for change LUKS passphrase

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/
%_alterator_backend3dir/*

%changelog
* Wed Dec 19 2012 Timur Aitov <timonbl4@altlinux.org> 0.1-alt1
- initial build
