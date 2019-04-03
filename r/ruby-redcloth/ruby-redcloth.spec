# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname redcloth
%define        gemname RedCloth

Name:          ruby-%pkgname
Version:       4.3.2
Release:       alt2
Summary:       Textile parser for Ruby
Group:         Development/Ruby
License:       MIT
Url:           https://redcloth.org/
# VCS:         https://github.com/jgarber/redcloth.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Source:        %name-%version.tar
BuildArch:     noarch

BuildRequires(pre): rpm-build-ruby

%description
RedCloth is a module for using Textile in Ruby. Textile is a text format.
A very simple text format. Another stab at making readable text that can
be converted to HTML.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem


%package       -n %pkgname
Summary:       RedCloth executables for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n %pkgname
%summary.


%prep
%setup

%build
%gem_build --use=RedCloth --alias=redcloth

%install
%gem_install

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         -n %pkgname
%_bindir/%pkgname

%changelog
* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 4.3.2-alt2
- Use Ruby Policy 2.0
- Fix 4.3.2 gem version

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
