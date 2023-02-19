%define        gemname berkshelf

Name:          gem-berkshelf
Version:       8.0.5
Release:       alt1
Summary:       A Chef Cookbook manager
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/berkshelf/berkshelf
Vcs:           https://github.com/berkshelf/berkshelf.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 10.1
BuildRequires: gem(aruba) >= 0.10
BuildRequires: gem(cucumber-expressions) = 5.0.13
BuildRequires: gem(chef-zero) >= 4.0
BuildRequires: gem(dep_selector) >= 1.0
BuildRequires: gem(fuubar) >= 2.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rspec-its) >= 1.2
BuildRequires: gem(webmock) >= 1.11
BuildRequires: gem(http) >= 0.9.8
BuildRequires: gem(chefstyle) >= 0
BuildRequires: gem(mixlib-shellout) >= 2.0
BuildRequires: gem(cleanroom) >= 1.0
BuildRequires: gem(minitar) >= 0.6
BuildRequires: gem(retryable) >= 2.0
BuildRequires: gem(solve) >= 4.0
BuildRequires: gem(thor) >= 0.20
BuildRequires: gem(octokit) >= 4.0
BuildRequires: gem(mixlib-archive) >= 1.1.4
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildRequires: gem(chef) >= 15.7.32
BuildRequires: gem(chef-config) >= 0
BuildRequires: gem(mixlib-config) >= 2.2.5
BuildConflicts: gem(aruba) >= 1
BuildConflicts: gem(cucumber) >= 4.0
BuildConflicts: gem(mixlib-shellout) >= 4.0
BuildConflicts: gem(cleanroom) >= 2
BuildConflicts: gem(retryable) >= 4.0
BuildConflicts: gem(solve) >= 5
BuildConflicts: gem(octokit) >= 6
BuildConflicts: gem(mixlib-archive) >= 2.0
BuildConflicts: gem(concurrent-ruby) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency octokit >= 5.6.1,octokit < 6
Requires:      gem(mixlib-shellout) >= 2.0
Requires:      gem(cleanroom) >= 1.0
Requires:      gem(minitar) >= 0.6
Requires:      gem(retryable) >= 2.0
Requires:      gem(solve) >= 4.0
Requires:      gem(thor) >= 0.20
Requires:      gem(octokit) >= 4.0
Requires:      gem(mixlib-archive) >= 1.1.4
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(chef) >= 15.7.32
Requires:      gem(chef-config) >= 0
Requires:      gem(mixlib-config) >= 2.2.5
Conflicts:     gem(mixlib-shellout) >= 4.0
Conflicts:     gem(cleanroom) >= 2
Conflicts:     gem(retryable) >= 4.0
Conflicts:     gem(solve) >= 5
Conflicts:     gem(octokit) >= 6
Conflicts:     gem(mixlib-archive) >= 2.0
Conflicts:     gem(concurrent-ruby) >= 2
Obsoletes:     ruby-berkshelf < %EVR
Provides:      ruby-berkshelf = %EVR
Provides:      gem(berkshelf) = 8.0.5


%description
A Chef Cookbook manager


%package       -n berks
Version:       8.0.5
Release:       alt1
Summary:       A Chef Cookbook manager executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета berkshelf
Group:         Documentation
BuildArch:     noarch

Requires:      gem(berkshelf) = 8.0.5

%description   -n berks
A Chef Cookbook manager executable(s).

%description   -n berks -l ru_RU.UTF-8
Исполнямка для самоцвета berkshelf.


%package       -n gem-berkshelf-doc
Version:       8.0.5
Release:       alt1
Summary:       A Chef Cookbook manager documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета berkshelf
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(berkshelf) = 8.0.5

%description   -n gem-berkshelf-doc
A Chef Cookbook manager documentation files.

%description   -n gem-berkshelf-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета berkshelf.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc spec/fixtures/cookbooks/example_cookbook-0.5.0/README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n berks
%doc spec/fixtures/cookbooks/example_cookbook-0.5.0/README.md
%_bindir/berks

%files         -n gem-berkshelf-doc
%doc spec/fixtures/cookbooks/example_cookbook-0.5.0/README.md
%ruby_gemdocdir


%changelog
* Mon Jan 30 2023 Pavel Skrylev <majioa@altlinux.org> 8.0.5-alt1
- ^ 7.0.8 -> 8.0.5 (no devel)

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 7.0.8-alt1
- ^ 7.0.7 -> 7.0.8

* Tue Feb 19 2019 Pavel Skrylev <majioa@altlinux.org> 7.0.7-alt1
- > Ruby Policy 2.0
- ^ 7.0.4 -> 7.0.7

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 7.0.4-alt1
- New version.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 7.0.3-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 7.0.2-alt1
- Initial build for Sisyphus
