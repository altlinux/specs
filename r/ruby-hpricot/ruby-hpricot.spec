# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname hpricot

Name: ruby-%pkgname
Version: 0.8
Release: alt1.2

Summary: A Fast, Enjoyable HTML Parser for Ruby
Group: Development/Ruby
License: MIT/Ruby
Url: http://wiki.github.com/why/hpricot

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
Group: Development/Documentation

%description doc
Documentation files for %name.


%prep
%setup -n %pkgname-%version
%patch -p1
sed -i -r -e '/ruby_digitmap\[\]/s/^([[:blank:]]*).*$/\1static const char digitmap[] = "0123456789";/' \
	-e '/=[[:blank:]]*ruby_digitmap\[/s/ruby_(digitmap)/\1/' \
	ext/fast_xs/fast_xs.c
%update_setup_rb


%build
%ruby_config
pushd ext/hpricot_scan
  ragel hpricot_scan.rl -G2 -o hpricot_scan.c
  ragel hpricot_css.rl -G2 -o hpricot_css.c
popd
%ruby_build


%install
%ruby_install
%rdoc lib/


%check
for t in test/test_*; do
  testrb -Iext/hpricot_scan:ext/fast_xs:lib "$t"
done


%files
%doc README
%ruby_sitelibdir/*
%ruby_sitearchdir/*


%files doc
%ruby_ri_sitedir/Hpricot*


%changelog
* Fri Mar 14 2014 Led <led@altlinux.ru> 0.8-alt1.2
- test: fixed for ruby >= 2.0

* Sun Dec 09 2012 Led <led@altlinux.ru> 0.8-alt1.1
- Rebuilt with ruby-1.9.3-alt1
- fix build with libruby 1.9.x

* Fri Jul 10 2009 Alexey I. Froloff <raorn@altlinux.org> 0.8-alt1
- 0.8-8-g38c781c

* Wed Aug 20 2008 Sir Raorn <raorn@altlinux.ru> 0.5.140-alt1
- Built for Sisyphus

