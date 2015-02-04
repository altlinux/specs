# -*- mode: RPM-SPEC; tab-width: 8; fill-column: 70; -*- 

%define _altdata_dir %_datadir/alterator

Name: alterator-bird
Version: 0.0.2
Release: alt1

Summary: Alterator module for Bird server setup
License: GPL
Group: System/Configuration/Other

Source:%name-%version.tar

Requires: alterator >= 4.7-alt1 alterator-sh-functions >= 0.6-alt5
Requires: alterator-l10n >= 2.9-alt1
Requires: augeas >= 1.2.0
Requires: bird >= 1.4.3-alt0.M70P.2
Requires: lsof
Requires: alterator-service-functions >= 2.0.0
BuildArch: noarch
BuildRequires: alterator

%description
Alterator module for Bird server setup
Bird is dynamic IP routing daemon

%prep
%setup -q

%build
%make_build

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*
%_alterator_backend3dir/*

%changelog
* Wed Feb 04 2015 Andriy Stepanov <stanv@altlinux.ru> 0.0.2-alt1
- Remove show/hide effect
  Add checkbox "start at boot"
  Add buttons: start/stop service

* Wed Jul 02 2014 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt1
- Initial build
