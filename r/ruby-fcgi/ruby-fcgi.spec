%define        pkgname fcgi

Name:          ruby-%pkgname
Version:       0.9.2.1
Release:       alt3
Summary:       FastCGI for ruby
Group:         Development/Ruby
License:       MIT
Url:           https://github.com/alphallc/ruby-fcgi-ng
# VCS:         https://github.com/alphallc/ruby-fcgi-ng.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libfcgi-devel

%description
FastCGI is a language independent, scalable, open extension to CGI
that provides high performance without the limitations of server
specific APIs.

MoonWolf developed a library for FastCGI in
http://www.moonwolf.com/ruby/archive/. But now, he is MIA.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%changelog
* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.2.1-alt3
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.2.1-alt2.5
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.2.1-alt2.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.2.1-alt2.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.2.1-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.2.1-alt2.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.2.1-alt2
- Rebuild with new %%ruby_sitearchdir location

* Thu Sep 22 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.2.1-alt1
- New version 0.9.2.1

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.8.8-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Wed Dec 05 2012 Led <led@altlinux.ru> 0.8.8-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Thu Jul 15 2010 Alexey I. Froloff <raorn@altlinux.org> 0.8.8-alt1
- [0.8.8]

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 0.8.7-alt2
- Rebuilt with Ruby 1.9

* Wed Apr 02 2008 Sir Raorn <raorn@altlinux.ru> 0.8.7-alt1
- [0.8.7]

* Tue Mar 28 2006 Kirill A. Shutemov <kas@altlinux.ru> 0.8.6-alt1
- first build
