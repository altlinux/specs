# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname pkg-config

Name: ruby-%pkgname
Version: 1.0.7
Release: alt3

Summary: pkg-config implementation by Ruby
Group: Development/Ruby
License: LGPLv2+
Url: https://github.com/rcairo/pkg-config

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Sun Jan 09 2011 (-bi)
BuildRequires: libruby-devel rpm-build-ruby ruby-test-unit ruby-tool-setup libcairo-devel libcairo-gobject-devel libpixman-devel xorg-dri2proto-devel xorg-glproto-devel libXau-devel libXdmcp-devel libXext-devel libXdamage-devel libpng-devel libudev-devel libXxf86vm-devel

%description
A pkg-config implementation by Ruby.

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build
%ruby_test_unit -Ilib:test test

%install
%ruby_install

%files
%doc NEWS README.rdoc
%ruby_sitelibdir/*

%changelog
* Thu Nov 10 2011 Timur Aitov <timonbl4@altlinux.org> 1.0.7-alt3
- Repair build

* Fri Apr 29 2011 Timur Aitov <timonbl4@altlinux.org> 1.0.7-alt2
- Repair build

* Sun Jan 09 2011 Alexey I. Froloff <raorn@altlinux.org> 1.0.7-alt1
- Built for Sisyphus

