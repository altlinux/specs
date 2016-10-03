# vim: set ft=spec: -*- rpm-spec -*-

Name: ruby-redcloth
Version: 4.3.2
Release: alt1

Summary: Textile parser for Ruby
Group: Development/Ruby
License: BSD
Url: http://redcloth.org/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: redcloth-%version.tar

BuildRequires: libruby-devel ruby-tool-setup

BuildArch: noarch

%description
RedCloth is a module for using Textile in Ruby. Textile is a text format.
A very simple text format. Another stab at making readable text that can
be converted to HTML.

%package doc
Summary: Documentation files for %name
Group: Documentation
BuildArch: noarch

%description doc
Documentation files for %name

%prep
%setup -n redcloth-%version
%update_setup_rb

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
%ruby_sitelibdir/*

%files doc
%ruby_ri_sitedir/RedCloth*

%changelog
* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 4.3.2-alt1
- New version 4.3.2
- Build as noarch

* Wed Mar 19 2014 Led <led@altlinux.ru> 4.2.2-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Tue Dec 04 2012 Led <led@altlinux.ru> 4.2.2-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Fri Jul 24 2009 Alexey I. Froloff <raorn@altlinux.org> 4.2.2-alt1
- [4.2.2]
- Do not package useless rake tasks

* Sat Jun 27 2009 Alexey I. Froloff <raorn@altlinux.org> 4.2.1-alt1
- [4.2.1]

* Fri Jul 25 2008 Sir Raorn <raorn@altlinux.ru> 4.0.1-alt1
- [4.0.1]

* Tue Mar 28 2006 Kirill A. Shutemov <kas@altlinux.ru> 3.0.4-alt1
- first build
