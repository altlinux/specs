%define        gemname manageiq-style

Name:          gem-manageiq-style
Version:       1.3.2
Release:       alt1
Summary:       Style and linting configuration for ManageIQ projects
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ManageIQ/manageiq-style
Vcs:           https://github.com/manageiq/manageiq-style.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(more_core_extensions) >= 0
BuildRequires: gem(optimist) >= 0
BuildRequires: gem(rubocop) >= 1.13 gem(rubocop) < 2
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rails) >= 0
BuildRequires: gem(rake) >= 12.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(simplecov) >= 0.17

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      gem(more_core_extensions) >= 0
Requires:      gem(optimist) >= 0
Requires:      gem(rubocop) >= 1.13 gem(rubocop) < 2
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rails) >= 0
Provides:      gem(manageiq-style) = 1.3.2


%description
Style and linting configuration for ManageIQ projects.


%package       -n manageiq-style
Version:       1.3.2
Release:       alt1
Summary:       Style and linting configuration for ManageIQ projects executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета manageiq-style
Group:         Other
BuildArch:     noarch

Requires:      gem(manageiq-style) = 1.3.2

%description   -n manageiq-style
Style and linting configuration for ManageIQ projects executable(s).

%description   -n manageiq-style -l ru_RU.UTF-8
Исполнямка для самоцвета manageiq-style.


%package       -n gem-manageiq-style-doc
Version:       1.3.2
Release:       alt1
Summary:       Style and linting configuration for ManageIQ projects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета manageiq-style
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(manageiq-style) = 1.3.2

%description   -n gem-manageiq-style-doc
Style and linting configuration for ManageIQ projects documentation files.

%description   -n gem-manageiq-style-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета manageiq-style.


%package       -n gem-manageiq-style-devel
Version:       1.3.2
Release:       alt1
Summary:       Style and linting configuration for ManageIQ projects development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета manageiq-style
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(manageiq-style) = 1.3.2
Requires:      gem(rake) >= 12.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(simplecov) >= 0.17

%description   -n gem-manageiq-style-devel
Style and linting configuration for ManageIQ projects development package.

%description   -n gem-manageiq-style-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета manageiq-style.


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

%files         -n manageiq-style
%doc README.md
%_bindir/manageiq-style

%files         -n gem-manageiq-style-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-manageiq-style-devel
%doc README.md


%changelog
* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 1.3.2-alt1
- + packaged gem with Ruby Policy 2.0
