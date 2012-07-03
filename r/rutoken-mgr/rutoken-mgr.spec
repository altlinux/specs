# vim: set ft=spec: -*- rpm-spec -*-

Name: rutoken-mgr
Version: 0.2
Release: alt1

Summary: Rutoken Manager
Group: Development/Ruby
License: GPL

BuildArch: noarch

Requires: opensc openssl openssl-engine_pkcs11

Source: %name-%version.tar

# Automatically added by buildreq on Fri Sep 25 2009 (-bi)
BuildRequires: rpm-build-ruby ruby-gettext-utils ruby-tool-setup

%description
Simple Rutoken Manager application.

%prep
%setup
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install

%find_lang %name

%files -f %name.lang
%_bindir/rutoken-mgr
%ruby_sitelibdir/*
%_datadir/%name
%_desktopdir/rutoken-mgr.desktop

%changelog
* Tue Oct 06 2009 Alexey I. Froloff <raorn@altlinux.org> 0.2-alt1
- [0.2]
  + fixed slot selection when generating certificate request
  + added busy indicator

* Fri Sep 25 2009 Alexey I. Froloff <raorn@altlinux.org> 0.1-alt1
- Built for Sisyphus

