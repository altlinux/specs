# vim: set ft=spec: -*- rpm-spec -*-

%def_disable check

Name: libxml-ruby
Version: 1.1.3
Release: alt2

Summary: Ruby language bindings for the GNOME Libxml2 XML toolkit
Group: Development/Ruby
License: MIT
Url: http://libxml.rubyforge.org/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: rpm-build-ruby
BuildRequires: libruby-devel libxml2-devel ruby-tool-setup zlib-devel

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
%update_setup_rb
sed -i 's/Config:/Rb&/g' ext/libxml/extconf.rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc ext/libxml/*.c lib/

%check
%ruby_test_unit -Ilib:ext/libxml:test test/test_suite.rb

%files
%doc README
%ruby_sitearchdir/*
%ruby_sitelibdir/*

%files doc
%doc CHANGES
%doc %ruby_ri_sitedir/LibXML

%changelog
* Fri Dec 07 2012 Led <led@altlinux.ru> 1.1.3-alt2
- Rebuilt with ruby-1.9.3-alt1
- fixed build with ruby 1.9
- updated BuildRequires
- disabled check

* Fri May 08 2009 Alexey I. Froloff <raorn@altlinux.org> 1.1.3-alt1
- [1.1.3]

* Sat Nov 01 2008 Sir Raorn <raorn@altlinux.ru> 0.8.3-alt1
- [0.8.3]

* Fri Feb 02 2007 Sir Raorn <raorn@altlinux.ru> 0.3.8.4-alt1
- Built for Sisyphus

