# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname xmpp4r

Name: ruby-%pkgname
Version: 0.5
Release: alt2.2

Summary: XMPP/Jabber library for Ruby
License: GPLv2/Ruby
Group: Development/Ruby

# see also https://github.com/ln/xmpp4r
Url: http://home.gna.org/xmpp4r/
Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

Obsoletes: xmpp4r
BuildArch: noarch

BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-rdoc ruby-tool-setup

%description
XMPP4R is an XMPP/Jabber library for Ruby. Its goal is to provide
a complete framework to develop Jabber-related applications or
scripts in Ruby.

 * Fully object-oriented
 * Aims at being XMPP compliant
 * Threaded, events-based
 * Well unit-tested and documented code
 * Uses well-known and well-tested software like REXML, instead
   of reinventing the wheel
 * Very easy to extend

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

%install
%ruby_install
%rdoc lib/

%files
%doc CHANGELOG README.rdoc
%ruby_sitelibdir/*

%files doc
%doc data/doc/xmpp4r/examples
%ruby_ri_sitedir/Jabber*

%changelog
* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.5-alt2.2
- Rebuild with Ruby 2.4.1
- Disable tests

* Fri Nov 30 2012 Led <led@altlinux.ru> 0.5-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Sat Jun 11 2011 Michael Shigorin <mike@altlinux.org> 0.5-alt2
- fixed build by dropping failing tests
- spec tags rearranged a bit (see ALT Packaging HOWTO)

* Sat Jun 27 2009 Alexey I. Froloff <raorn@altlinux.org> 0.5-alt1
- [0.5]

* Mon Sep 01 2008 Sir Raorn <raorn@altlinux.ru> 0.4-alt1
- 0.4

* Thu Jul 20 2006 Sir Raorn <raorn@altlinux.ru> 0.3-alt1
- [0.3]

* Wed Jul 12 2006 Sir Raorn <raorn@altlinux.ru> 0.2-alt1
- Built for Sisyphus

