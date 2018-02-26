# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname hpricot

Name: ruby-%pkgname
Version: 0.8
Release: alt1

Summary: A Fast, Enjoyable HTML Parser for Ruby
Group: Development/Ruby
License: MIT/Ruby
Url: http://wiki.github.com/why/hpricot

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Fri Jul 10 2009 (-bi)
BuildRequires: libruby-devel ragel ruby-test-unit ruby-tool-setup

%description
Hpricot is a fast, flexible HTML parser written in C.  It's designed to
be very accommodating (like Tanaka Akira's HTree) and to have a very
helpful library (like some JavaScript libs -- JQuery, Prototype -- give
you.)  The XPath and CSS parser, in fact, is based on John Resig's JQuery.

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
pushd ext/hpricot_scan
  ragel hpricot_scan.rl -G2 -o hpricot_scan.c
  ragel hpricot_css.rl -G2 -o hpricot_css.c
popd
%ruby_build
for t in test/test_*; do
  testrb -Iext/hpricot_scan:ext/fast_xs:lib "$t"
done

%install
%ruby_install
%rdoc lib/

%files
%doc README
%ruby_sitelibdir/*
%ruby_sitearchdir/*

%files doc
%ruby_ri_sitedir/Hpricot*

%changelog
* Fri Jul 10 2009 Alexey I. Froloff <raorn@altlinux.org> 0.8-alt1
- 0.8-8-g38c781c

* Wed Aug 20 2008 Sir Raorn <raorn@altlinux.ru> 0.5.140-alt1
- Built for Sisyphus

