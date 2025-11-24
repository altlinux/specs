%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname berkshelf

Name:          gem-berkshelf
Version:       8.1.6
Release:       alt1
Summary:       A Chef Cookbook manager
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/berkshelf/berkshelf
Vcs:           https://github.com/berkshelf/berkshelf.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 10.1
%if_enabled check
BuildRequires: gem(appbundler) >= 0
BuildRequires: gem(aruba) >= 2.3
BuildRequires: gem(chef) >= 18.0.0
BuildRequires: gem(chef-cleanroom) >= 1.0
BuildRequires: gem(chef-config) >= 0
BuildRequires: gem(chef-zero) >= 4.0
BuildRequires: gem(chefstyle) >= 0
BuildRequires: gem(concurrent-ruby) >= 1.0
BuildRequires: gem(cucumber) >= 9.2
BuildRequires: gem(cucumber-cucumber-expressions) >= 17.1
BuildRequires: gem(debug) >= 0
BuildRequires: gem(dep_selector) >= 1.0
BuildRequires: gem(ffi) >= 1.15.5
BuildRequires: gem(fuubar) >= 2.0
BuildRequires: gem(http) >= 0.9.8
BuildRequires: gem(minitar) >= 1.0
BuildRequires: gem(mixlib-archive) >= 1.1.4
BuildRequires: gem(mixlib-config) >= 2.2.5
BuildRequires: gem(mixlib-shellout) >= 2.0
BuildRequires: gem(octokit) >= 4.0
BuildRequires: gem(retryable) >= 2.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rspec-its) >= 1.2
BuildRequires: gem(solve) >= 4.0
BuildRequires: gem(syslog) >= 0.3
BuildRequires: gem(thor) >= 1.2.1
BuildRequires: gem(webmock) >= 1.11
BuildConflicts: gem(aruba) >= 3
BuildConflicts: gem(chef-cleanroom) >= 2
BuildConflicts: gem(concurrent-ruby) >= 2
BuildConflicts: gem(cucumber) >= 10
BuildConflicts: gem(cucumber-cucumber-expressions) >= 18
BuildConflicts: gem(ffi) >= 2
BuildConflicts: gem(minitar) >= 2
BuildConflicts: gem(mixlib-archive) >= 2.0
BuildConflicts: gem(mixlib-shellout) >= 4.0
BuildConflicts: gem(octokit) >= 9
BuildConflicts: gem(retryable) >= 4.0
BuildConflicts: gem(solve) >= 5
BuildConflicts: gem(syslog) >= 1
BuildConflicts: gem(thor) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency thor >= 1.2.1,thor < 2
%ruby_use_gem_dependency chef >= 19.0.85,chef < 20
%ruby_use_gem_dependency ffi >= 1.17.0,ffi < 2
%ruby_use_gem_dependency octokit >= 8.1.0,octokit < 9
Requires:      ruby >= 3.1.0
Requires:      rubygems >= 2.0.0
Requires:      gem(chef) >= 18.0.0
Requires:      gem(chef-cleanroom) >= 1.0
Requires:      gem(chef-config) >= 0
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(ffi) >= 1.15.5
Requires:      gem(minitar) >= 1.0
Requires:      gem(mixlib-archive) >= 1.1.4
Requires:      gem(mixlib-config) >= 2.2.5
Requires:      gem(mixlib-shellout) >= 2.0
Requires:      gem(octokit) >= 4.0
Requires:      gem(retryable) >= 2.0
Requires:      gem(solve) >= 4.0
Requires:      gem(syslog) >= 0.3
Requires:      gem(thor) >= 1.2.1
Conflicts:     gem(chef-cleanroom) >= 2
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(ffi) >= 2
Conflicts:     gem(minitar) >= 2
Conflicts:     gem(mixlib-archive) >= 2.0
Conflicts:     gem(mixlib-shellout) >= 4.0
Conflicts:     gem(octokit) >= 9
Conflicts:     gem(retryable) >= 4.0
Conflicts:     gem(solve) >= 5
Conflicts:     gem(syslog) >= 1
Conflicts:     gem(thor) >= 2
Obsoletes:     ruby-berkshelf < %EVR
Provides:      ruby-berkshelf = %EVR
Provides:      gem(berkshelf) = 8.1.6

%description
A Chef Cookbook manager


%package       -n berks
Version:       8.1.6
Release:       alt1
Summary:       A Chef Cookbook manager executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета berkshelf
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(berkshelf) = 8.1.6
Requires:      gem(appbundler) >= 0

%description   -n berks
A Chef Cookbook manager executable(s).

%description   -n berks -l ru_RU.UTF-8
Исполнямка для самоцвета berkshelf.


%if_enabled    doc
%package       -n gem-berkshelf-doc
Version:       8.1.6
Release:       alt1
Summary:       A Chef Cookbook manager documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета berkshelf
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(berkshelf) = 8.1.6

%description   -n gem-berkshelf-doc
A Chef Cookbook manager documentation files.

%description   -n gem-berkshelf-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета berkshelf.
%endif


%if_enabled    devel
%package       -n gem-berkshelf-devel
Version:       8.1.6
Release:       alt1
Summary:       A Chef Cookbook manager development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета berkshelf
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(berkshelf) = 8.1.6
Requires:      gem(appbundler) >= 0
Requires:      gem(aruba) >= 2.3
Requires:      gem(chef) >= 18.0.0
Requires:      gem(chef-cleanroom) >= 1.0
Requires:      gem(chef-config) >= 0
Requires:      gem(chef-zero) >= 4.0
Requires:      gem(chefstyle) >= 0
Requires:      gem(concurrent-ruby) >= 1.0
Requires:      gem(cucumber) >= 9.2
Requires:      gem(cucumber-cucumber-expressions) >= 17.1
Requires:      gem(debug) >= 0
Requires:      gem(dep_selector) >= 1.0
Requires:      gem(ffi) >= 1.15.5
Requires:      gem(fuubar) >= 2.0
Requires:      gem(http) >= 0.9.8
Requires:      gem(minitar) >= 1.0
Requires:      gem(mixlib-archive) >= 1.1.4
Requires:      gem(mixlib-config) >= 2.2.5
Requires:      gem(mixlib-shellout) >= 2.0
Requires:      gem(octokit) >= 4.0
Requires:      gem(retryable) >= 2.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rspec-its) >= 1.2
Requires:      gem(solve) >= 4.0
Requires:      gem(syslog) >= 0.3
Requires:      gem(thor) >= 1.2.1
Requires:      gem(webmock) >= 1.11
Conflicts:     gem(aruba) >= 3
Conflicts:     gem(chef-cleanroom) >= 2
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(cucumber) >= 10
Conflicts:     gem(cucumber-cucumber-expressions) >= 18
Conflicts:     gem(ffi) >= 2
Conflicts:     gem(minitar) >= 2
Conflicts:     gem(mixlib-archive) >= 2.0
Conflicts:     gem(mixlib-shellout) >= 4.0
Conflicts:     gem(octokit) >= 9
Conflicts:     gem(retryable) >= 4.0
Conflicts:     gem(solve) >= 5
Conflicts:     gem(syslog) >= 1
Conflicts:     gem(thor) >= 2

%description   -n gem-berkshelf-devel
A Chef Cookbook manager development package.

%description   -n gem-berkshelf-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета berkshelf.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc LICENSE CHANGELOG.legacy.md CHANGELOG.md CONTRIBUTING.md README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n berks
%doc LICENSE CHANGELOG.legacy.md CHANGELOG.md CONTRIBUTING.md README.md
%_bindir/berks

%if_enabled    doc
%files         -n gem-berkshelf-doc
%doc LICENSE CHANGELOG.legacy.md CHANGELOG.md CONTRIBUTING.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-berkshelf-devel
%doc LICENSE CHANGELOG.legacy.md CHANGELOG.md CONTRIBUTING.md README.md
%endif


%changelog
* Thu Nov 20 2025 Pavel Skrylev <majioa@altlinux.org> 8.1.6-alt1
- ^ 8.0.5 -> 8.1.6

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
