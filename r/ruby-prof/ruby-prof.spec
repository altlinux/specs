# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname ruby-prof

Name: %pkgname
Version: 0.9.2
Release: alt1

Summary: Fast code profiler for Ruby
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/ruby-prof/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar

# Automatically added by buildreq on Mon Nov 10 2008 (-bi)
BuildRequires: libruby-devel ruby-tool-setup ruby-test-unit

%description
ruby-prof is a fast code profiler for Ruby.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build
# Results unreliable
#ruby -e '$LOAD_PATH.unshift(*%%w(lib ext test)); require "test_suite"'

%install
%ruby_install
%rdoc lib/ ext/*.c

%files
%doc README.rdoc
%_bindir/*
%ruby_sitelibdir/*
%ruby_sitearchdir/*

%files doc
%ruby_ri_sitedir/RubyProf*

%changelog
* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 0.9.2-alt1
- [0.9.2]

* Mon Jun 29 2009 Alexey I. Froloff <raorn@altlinux.org> 0.7.3-alt1
- [0.7.3]

* Mon Nov 10 2008 Sir Raorn <raorn@altlinux.ru> 0.6.1-alt1
- Built for Sisyphus

