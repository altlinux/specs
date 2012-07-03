# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname kirbybase

Name: ruby-%pkgname
Version: 2.6
Release: alt2

Summary: Small, plain-text, dbms written in Ruby
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/kirbybase/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Thu Jul 02 2009 (-bi)
BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-rdoc ruby-tool-setup

%description
A small, plain-text, dbms written in Ruby.  It can be used either embedded 
or client/server.

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
%ruby_test_unit -Ilib:test test/ts_*.rb

%install
%ruby_install
%rdoc lib/

%files
%doc README
%ruby_sitelibdir/*

%files doc
%doc examples images kirbybaserubymanual.html
%ruby_ri_sitedir/KirbyBase*

%changelog
* Mon Nov 29 2010 Alexey I. Froloff <raorn@altlinux.org> 2.6-alt2
- Fix build with Ruby 1.9.2

* Thu Jul 02 2009 Alexey I. Froloff <raorn@altlinux.org> 2.6-alt1
- Built for Sisyphus

