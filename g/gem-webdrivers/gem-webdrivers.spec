%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname webdrivers

Name:          gem-webdrivers
Version:       5.3.1
Release:       alt1
Summary:       Easy download and use of browser drivers
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/titusfortner/webdrivers
Vcs:           https://github.com/titusfortner/webdrivers/tree/v5.3.1.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(ffi) >= 1.0
BuildRequires: gem(rake) >= 12.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 0.89
BuildRequires: gem(rubocop-packaging) >= 0.5.0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rspec) >= 1.42
BuildRequires: gem(simplecov) >= 0.16
BuildRequires: gem(nokogiri) >= 1.6
BuildRequires: gem(rubyzip) >= 1.3.0
BuildRequires: gem(selenium-webdriver) >= 4.0
BuildConflicts: gem(ffi) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-packaging) >= 1
BuildConflicts: gem(rubocop-rspec) >= 3
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(selenium-webdriver) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency rubocop-packaging >= 0.5.2,rubocop-packaging < 1
Requires:      gem(nokogiri) >= 1.6
Requires:      gem(rubyzip) >= 1.3.0
Requires:      gem(selenium-webdriver) >= 4.0
Conflicts:     gem(nokogiri) >= 2
Conflicts:     gem(selenium-webdriver) >= 5
Provides:      gem(webdrivers) = 5.3.1


%description
Run Selenium tests more easily with install and updates for all supported
webdrivers.


%if_enabled    doc
%package       -n gem-webdrivers-doc
Version:       5.3.1
Release:       alt1
Summary:       Easy download and use of browser drivers documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета webdrivers
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(webdrivers) = 5.3.1

%description   -n gem-webdrivers-doc
Easy download and use of browser drivers documentation files.

Run Selenium tests more easily with install and updates for all supported
webdrivers.
%description   -n gem-webdrivers-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета webdrivers.
%endif


%if_enabled    devel
%package       -n gem-webdrivers-devel
Version:       5.3.1
Release:       alt1
Summary:       Easy download and use of browser drivers development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета webdrivers
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(webdrivers) = 5.3.1
Requires:      gem(ffi) >= 1.0
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 0.89
Requires:      gem(rubocop-packaging) >= 0.5.0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rspec) >= 1.42
Requires:      gem(simplecov) >= 0.16
Conflicts:     gem(ffi) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-packaging) >= 1
Conflicts:     gem(rubocop-rspec) >= 3
Conflicts:     gem(simplecov) >= 1

%description   -n gem-webdrivers-devel
Easy download and use of browser drivers development package.

Run Selenium tests more easily with install and updates for all supported
webdrivers.
%description   -n gem-webdrivers-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета webdrivers.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-webdrivers-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-webdrivers-devel
%doc README.md
%endif


%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 5.3.1-alt1
- + packaged gem with Ruby Policy 2.0
