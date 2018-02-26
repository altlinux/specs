# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname mkrf

Name: ruby-%pkgname
Version: 0.2.3
Release: alt2

Summary: making C extensions for Ruby a bit easier
Group: Development/Ruby
License: MIT
Url: http://rubyforge.org/projects/mkrf/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Thu Apr 03 2008 (-bi)
BuildRequires: rpm-build-ruby ruby-rake ruby-tool-rdoc ruby-tool-setup zlib-devel

%description
mkrf is a library for generating Rakefiles. It is primarily for
building C extensions for Ruby, but will be able to be used for
generic Rakefile generation as well. Main goals include simple
use and reuse in other projects.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build
%ruby_test_unit -Ilib test/unit/test_*.rb

%install
%ruby_install
%rdoc lib/

%files
%ruby_sitelibdir/*
%doc examples README TODO CHANGELOG

%files doc
%ruby_ri_sitedir/Mkrf*

%changelog
* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.2.3-alt2
- Rebuilt with Ruby 1.9

* Thu Apr 03 2008 Sir Raorn <raorn@altlinux.ru> 0.2.3-alt1
- Built for Sisyphus

