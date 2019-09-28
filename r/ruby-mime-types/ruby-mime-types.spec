# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname mime-types

Name:          ruby-%pkgname
Version:       3.3
Release:       alt1
Summary:       Manages a MIME Content-Type database
Group:         Development/Ruby
License:       MIT
Url:           https://github.com/mime-types/ruby-mime-types
%vcs           https://github.com/mime-types/ruby-mime-types.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary.
Manages a MIME Content-Type database that will return the Content-Type for
a given filename.

MIME::Types for Ruby originally based on and synchronized with
MIME::Types for Perl by Mark Overmeer, copy right 2001 - 2009. As of
version 1.15, the data format for the MIME::Type list has changed and
the synchronization will no longer happen.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --use=%gemname --version-replace=%version

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 3.3-alt1
- update (^) 3.2.2 -> 3.3
- update to (^) Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.2-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Mar 30 2017 Andrey Cherepanov <cas@altlinux.org> 3.1-alt1
- New version

* Mon Oct 19 2015 Andrey Cherepanov <cas@altlinux.org> 2.6.2-alt1
- New version
- Update homepage to https://github.com/mime-types/ruby-mime-types

* Fri Dec 07 2012 Led <led@altlinux.ru> 1.18-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Wed Apr 18 2012 Igor Zubkov <icesik@altlinux.org> 1.18-alt1
- 1.16 -> 1.18
- Fix repocop warning

* Sat Dec 12 2009 Igor Zubkov <icesik@altlinux.org> 1.16-alt1
- build for Sisyphus



