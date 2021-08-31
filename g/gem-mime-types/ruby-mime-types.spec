%define        gemname mime-types

Name:          gem-mime-types
Version:       3.3.1
Release:       alt1
Summary:       Manages a MIME Content-Type database
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mime-types/ruby-mime-types
Vcs:           https://github.com/mime-types/ruby-mime-types/.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(mime-types-data) >= 3.2015 gem(mime-types-data) < 4
BuildRequires: gem(minitest) >= 5.14 gem(minitest) < 6
BuildRequires: gem(hoe-doofus) >= 1.0 gem(hoe-doofus) < 2
BuildRequires: gem(hoe-gemspec2) >= 1.1 gem(hoe-gemspec2) < 2
BuildRequires: gem(hoe-git) >= 1.6 gem(hoe-git) < 2
BuildRequires: gem(hoe-rubygems) >= 1.0 gem(hoe-rubygems) < 2
BuildRequires: gem(hoe-travis) >= 1.2 gem(hoe-travis) < 2
BuildRequires: gem(minitest-autotest) >= 1.0 gem(minitest-autotest) < 2
BuildRequires: gem(minitest-focus) >= 1.0 gem(minitest-focus) < 2
BuildRequires: gem(minitest-bonus-assertions) >= 3.0 gem(minitest-bonus-assertions) < 4
BuildRequires: gem(minitest-hooks) >= 1.4 gem(minitest-hooks) < 2
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14
BuildRequires: gem(fivemat) >= 1.3 gem(fivemat) < 2
BuildRequires: gem(minitest-rg) >= 5.2 gem(minitest-rg) < 6
BuildRequires: gem(simplecov) >= 0.7 gem(simplecov) < 1
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(hoe) >= 3.22 gem(hoe) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Requires:      gem(mime-types-data) >= 3.2015 gem(mime-types-data) < 4
Obsoletes:     ruby-mime-types < %EVR
Provides:      ruby-mime-types = %EVR
Provides:      gem(mime-types) = 3.3.1


%description
Manages a MIME Content-Type database that will return the Content-Type
for a given filename.

MIME::Types for Ruby originally based on and synchronized with MIME::Types for
Perl by Mark Overmeer, copy right 2001 - 2009. As of version 1.15, the data
format for the MIME::Type list has changed and the synchronization will no
longer happen.


%package       -n gem-mime-types-doc
Version:       3.3.1
Release:       alt1
Summary:       Manages a MIME Content-Type database documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mime-types
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mime-types) = 3.3.1

%description   -n gem-mime-types-doc
Manages a MIME Content-Type database documentation files.

Manages a MIME Content-Type database that will return the Content-Type
for a given filename.

MIME::Types for Ruby originally based on and synchronized with MIME::Types for
Perl by Mark Overmeer, copy right 2001 - 2009. As of version 1.15, the data
format for the MIME::Type list has changed and the synchronization will no
longer happen.

%description   -n gem-mime-types-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mime-types.


%package       -n gem-mime-types-devel
Version:       3.3.1
Release:       alt1
Summary:       Manages a MIME Content-Type database development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mime-types
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mime-types) = 3.3.1
Requires:      gem(minitest) >= 5.14 gem(minitest) < 6
Requires:      gem(hoe-doofus) >= 1.0 gem(hoe-doofus) < 2
Requires:      gem(hoe-gemspec2) >= 1.1 gem(hoe-gemspec2) < 2
Requires:      gem(hoe-git) >= 1.6 gem(hoe-git) < 2
Requires:      gem(hoe-rubygems) >= 1.0 gem(hoe-rubygems) < 2
Requires:      gem(hoe-travis) >= 1.2 gem(hoe-travis) < 2
Requires:      gem(minitest-autotest) >= 1.0 gem(minitest-autotest) < 2
Requires:      gem(minitest-focus) >= 1.0 gem(minitest-focus) < 2
Requires:      gem(minitest-bonus-assertions) >= 3.0 gem(minitest-bonus-assertions) < 4
Requires:      gem(minitest-hooks) >= 1.4 gem(minitest-hooks) < 2
Requires:      gem(rake) >= 10.0 gem(rake) < 14
Requires:      gem(fivemat) >= 1.3 gem(fivemat) < 2
Requires:      gem(minitest-rg) >= 5.2 gem(minitest-rg) < 6
Requires:      gem(simplecov) >= 0.7 gem(simplecov) < 1
Requires:      gem(rdoc) >= 4.0 gem(rdoc) < 7
Requires:      gem(hoe) >= 3.22 gem(hoe) < 4

%description   -n gem-mime-types-devel
Manages a MIME Content-Type database development package.

Manages a MIME Content-Type database that will return the Content-Type
for a given filename.

MIME::Types for Ruby originally based on and synchronized with MIME::Types for
Perl by Mark Overmeer, copy right 2001 - 2009. As of version 1.15, the data
format for the MIME::Type list has changed and the synchronization will no
longer happen.

%description   -n gem-mime-types-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mime-types.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-mime-types-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-mime-types-devel
%doc README.rdoc


%changelog
* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 3.3.1-alt1
- ^ 3.3 -> 3.3.1

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
