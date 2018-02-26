# vim: set ft=spec: -*- rpm-spec -*-

%define ruby_major 1.8
%define pkgname rubytree

Name: ruby%{ruby_major}-%pkgname
Version: 0.5.2
Release: alt2

Summary: Simple implementation of the generic Tree data structure
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/rubytree/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Sat Nov 28 2009 (-bi)
BuildRequires: ruby%{ruby_major} rpm-build-ruby ruby%{ruby_major}-stdlibs ruby%{ruby_major}-tool-rdoc ruby-tool-setup

%description
Rubytree is a simple implementation of the generic Tree data structure.
This implementation is node-centric, where the individual nodes on the
tree are the primary objects and drive the structure.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

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
%rdoc lib/

%files
%doc README
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/Tree*

%changelog
* Fri Apr 29 2011 Timur Aitov <timonbl4@altlinux.org> 0.5.2-alt2
- Rebuild for ruby1.8

* Sat Nov 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.5.2-alt1
- Built for Sisyphus

