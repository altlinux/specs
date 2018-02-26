# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname yajl-ruby

Name: %pkgname
Version: 0.7.5
Release: alt1

Summary: YAJL C Bindings for Ruby
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/yajl-ruby/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Sun Apr 11 2010 (-bi)
BuildRequires: libruby-devel ruby-tool-setup

%description
This package is a C binding to the excellent YAJL JSON parsing and
generation library.

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%files
%doc README.rdoc
%ruby_sitelibdir/*
%ruby_sitearchdir/*

%files doc
%ruby_ri_sitedir/Yajl*

%changelog
* Sun Apr 11 2010 Alexey I. Froloff <raorn@altlinux.org> 0.7.5-alt1
- Built for Sisyphus

