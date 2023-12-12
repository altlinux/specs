%define        _unpackaged_files_terminate_build 1
%define        gemname automatiek

Name:          gem-automatiek
Version:       0.3.0
Release:       alt1
Summary:       Vendor your gem's dependencies in retro style
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/segiddins/automatiek
Vcs:           https://github.com/segiddins/automatiek.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.10
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(rspec) >= 0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
Provides:      gem(automatiek) = 0.3.0


%description
A gem to vendor other gems, for situations where dependency resolution just
isn't an option. Extracted from Bundler's Rakefile


%package       -n gem-automatiek-doc
Version:       0.3.0
Release:       alt1
Summary:       Vendor your gem's dependencies in retro style documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета automatiek
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(automatiek) = 0.3.0

%description   -n gem-automatiek-doc
Vendor your gem's dependencies in retro style documentation files.

A gem to vendor other gems, for situations where dependency resolution just
isn't an option. Extracted from Bundler's Rakefile

%description   -n gem-automatiek-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета automatiek.


%package       -n gem-automatiek-devel
Version:       0.3.0
Release:       alt1
Summary:       Vendor your gem's dependencies in retro style development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета automatiek
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(automatiek) = 0.3.0
Requires:      gem(bundler) >= 1.10
Requires:      gem(rake) >= 10.0
Requires:      gem(rspec) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14

%description   -n gem-automatiek-devel
Vendor your gem's dependencies in retro style development package.

A gem to vendor other gems, for situations where dependency resolution just
isn't an option. Extracted from Bundler's Rakefile

%description   -n gem-automatiek-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета automatiek.


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

%files         -n gem-automatiek-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-automatiek-devel
%doc README.md


%changelog
* Fri Dec 01 2023 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- + packaged gem with Ruby Policy 2.0
