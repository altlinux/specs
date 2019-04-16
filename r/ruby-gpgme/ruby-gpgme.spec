# vim: set ft=spec: -*- rpm-spec -*-

%define        pkgname gpgme

Name:          ruby-%pkgname
Version:       2.0.18
Release:       alt1
Summary:       Ruby interface to GnuPG Made Easy
Group:         Development/Ruby
License:       LGPLv2.1+
Url:           http://github.com/ueno/ruby-gpgme
# VCS:         http://github.com/ueno/ruby-gpgme.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libgpgme-devel
BuildRequires: gem(mini_portile2)

%description
Ruby interface to GnuPG Made Easy (GPGME).


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-%pkgname-doc
Obsoletes:     ruby-%pkgname-doc

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
* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 2.0.18-alt1
- Bump to 2.0.18
- Use Ruby Policy 2.0

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.16-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.16-alt1.1
- Rebuild with Ruby 2.5.0

* Thu Jan 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.16-alt1
- New version.

* Wed Dec 20 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.15-alt1
- New version.

* Mon Oct 30 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.14-alt1
- New version

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.13-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.13-alt1.1
- Rebuild with Ruby 2.4.1

* Wed Jul 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.13-alt1
- New version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.12-alt2
- Rebuild with new %%ruby_sitearchdir location

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 2.0.12-alt1
- new version 2.0.12

* Wed Mar 19 2014 Led <led@altlinux.ru> 1.0.6-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Wed Dec 05 2012 Led <led@altlinux.ru> 1.0.6-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.6-alt1
- [1.0.6]
- License changed to LGPLv2.1+

* Sat Dec 27 2008 Sir Raorn <raorn@altlinux.ru> 1.0.1-alt1
- [1.0.1]

* Tue Aug 31 2004 Sir Raorn <raorn@altlinux.ru> 0.2-alt1
- Built for Sisyphus
