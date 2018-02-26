# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname bzip2-ruby

Name: %pkgname
Version: 0.2.6
Release: alt1

Summary: Ruby C bindings to libbzip2
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/bzip2-ruby/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Sun Apr 11 2010 (-bi)
BuildRequires: bzlib-devel libruby-devel ruby-tool-setup

%description
Ruby C bindings to libbzip2.

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install

%files
%doc README.rdoc
%ruby_sitelibdir/*
%ruby_sitearchdir/*

%changelog
* Sun Apr 11 2010 Alexey I. Froloff <raorn@altlinux.org> 0.2.6-alt1
- Built for Sisyphus

