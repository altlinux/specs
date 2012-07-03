# vim: set ft=spec: -*- rpm-spec -*-

%define ruby_major 1.8

Name: ruby%{ruby_major}-redcloth
Version: 4.2.2
Release: alt2

Summary: Textile parser for Ruby
Group: Development/Ruby
License: BSD
Url: http://rubyforge.org/projects/redcloth/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: RedCloth-%version.tar
Patch: RedCloth-%version-%release.patch

# Automatically added by buildreq on Sat Jul 26 2008 (-bi)
BuildRequires: libruby%{ruby_major}-devel ruby-tool-setup

%description
RedCloth is a module for using Textile in Ruby. Textile is a text format.
A very simple text format. Another stab at making readable text that can 
be converted to HTML.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n RedCloth-%version
%patch -p1
%update_setup_rb
# WTF?
rm -rf lib/tasks
find . -name '._*' -print0 |
	xargs -r0 rm -rvf --

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc ext/redcloth_scan/*.c lib/

%files
%_bindir/*
%ruby_sitearchdir/*
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/RedCloth*

%changelog
* Thu Apr 28 2011 Timur Aitov <timonbl4@altlinux.org> 4.2.2-alt2
- Rebuild for ruby1.8

* Fri Jul 24 2009 Alexey I. Froloff <raorn@altlinux.org> 4.2.2-alt1
- [4.2.2]
- Do not package useless rake tasks

* Sat Jun 27 2009 Alexey I. Froloff <raorn@altlinux.org> 4.2.1-alt1
- [4.2.1]

* Fri Jul 25 2008 Sir Raorn <raorn@altlinux.ru> 4.0.1-alt1
- [4.0.1]

* Tue Mar 28 2006 Kirill A. Shutemov <kas@altlinux.ru> 3.0.4-alt1
- first build
