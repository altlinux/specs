%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname webpacker

Name:          gem-webpacker
Version:       5.4.4
Release:       alt1
Summary:       Use webpack to manage app-like JavaScript modules in Rails
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/webpacker
Vcs:           https://github.com/rails/webpacker/tree/v5.4.4.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.3.0
BuildRequires: gem(rubocop) >= 0.93.1
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rails) >= 0
BuildRequires: gem(rake) >= 11.1
BuildRequires: gem(rack-proxy) >= 0.6.1
BuildRequires: gem(semantic_range) >= 2.3.0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(activesupport) >= 5.2
BuildRequires: gem(railties) >= 5.2
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(minitest) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(rack-proxy) >= 0.6.1
Requires:      gem(semantic_range) >= 2.3.0
Requires:      gem(activesupport) >= 5.2
Requires:      gem(railties) >= 5.2
Provides:      gem(webpacker) = 5.4.4


%description
Use webpack to manage app-like JavaScript modules in Rails


%if_enabled    doc
%package       -n gem-webpacker-doc
Version:       5.4.4
Release:       alt1
Summary:       Use webpack to manage app-like JavaScript modules in Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета webpacker
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(webpacker) = 5.4.4

%description   -n gem-webpacker-doc
Use webpack to manage app-like JavaScript modules in Rails documentation files.

%description   -n gem-webpacker-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета webpacker.
%endif


%if_enabled    devel
%package       -n gem-webpacker-devel
Version:       5.4.4
Release:       alt1
Summary:       Use webpack to manage app-like JavaScript modules in Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета webpacker
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(webpacker) = 5.4.4
Requires:      gem(bundler) >= 1.3.0
Requires:      gem(rubocop) >= 0.93.1
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rails) >= 0
Requires:      gem(rake) >= 11.1
Requires:      gem(minitest) >= 5.0
Requires:      gem(byebug) >= 0
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(minitest) >= 6

%description   -n gem-webpacker-devel
Use webpack to manage app-like JavaScript modules in Rails development package.

%description   -n gem-webpacker-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета webpacker.
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
%files         -n gem-webpacker-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-webpacker-devel
%doc README.md
%endif


%changelog
* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 5.4.4-alt1
- + packaged gem with Ruby Policy 2.0
