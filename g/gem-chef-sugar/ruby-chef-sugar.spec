%define  pkgname chef-sugar

Name:          gem-%pkgname
Version:       3.4.0
Release:       alt2
Summary:       Chef Sugar is a Gem & Chef Recipe
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/sethvargo/chef-sugar
Vcs:           https://github.com/sethvargo/chef-sugar.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
Chef Sugar is a Gem & Chef Recipe that includes series of helpful sugar of the
Chef core and other resources to make a cleaner, more lean recipe DSL, enforce
DRY principles, and make writing Chef recipes an awesome experience!


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
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Fri Mar 06 2020 Pavel Skrylev <majioa@altlinux.org> 3.4.0-alt2
- used (>) Ruby Policy 2.0
- fixed (!) spec

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Jun 27 2017 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus
