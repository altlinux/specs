# vim: set ft=spec: -*- rpm-spec -*-

%define ruby_major 1.8

Name: libxml-ruby%{ruby_major}
Version: 1.1.3
Release: alt2

Summary: Ruby language bindings for the GNOME Libxml2 XML toolkit
Group: Development/Ruby
License: MIT
Url: http://libxml.rubyforge.org/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Patch1: libxml-1.1.3-alt-tests.patch

# Automatically added by buildreq on Sat Nov 01 2008 (-bi)
BuildRequires: db2latex-xsl libruby%{ruby_major}-devel libxml2-devel ruby%{ruby_major}-stdlibs ruby-tool-setup zlib-devel

%description
The LibXML/Ruby project provides Ruby language bindings for the
GNOME Libxml2 XML toolkit. It is free software, released under the
MIT License.

Libxml-ruby's primary advantage over REXML is performance - if speed
is your need, these are good libraries to consider, as demonstrated
by the informal benchmark below.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -q
%patch -p1

#function 'force_encoding' miss in Ruby 1.8.7
%patch1 -p2

%update_setup_rb

%build
%ruby_config
%ruby_build
%ruby_test_unit -Ilib:ext/libxml:test test/test_suite.rb

%install
%ruby_install
%rdoc ext/libxml/*.c lib/

%files
%doc README
%ruby_sitearchdir/*
%ruby_sitelibdir/*

%files doc
%doc CHANGES
%doc %ruby_ri_sitedir/LibXML

%changelog
* Mon Apr 25 2011 Timur Aitov <timonbl4@altlinux.org> 1.1.3-alt2
- Rebuild for ruby1.8

* Fri May 08 2009 Alexey I. Froloff <raorn@altlinux.org> 1.1.3-alt1
- [1.1.3]

* Sat Nov 01 2008 Sir Raorn <raorn@altlinux.ru> 0.8.3-alt1
- [0.8.3]

* Fri Feb 02 2007 Sir Raorn <raorn@altlinux.ru> 0.3.8.4-alt1
- Built for Sisyphus

