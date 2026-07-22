%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname dry-initializer

Name:          gem-dry-initializer
Version:       3.2.0
Release:       alt1
Summary:       DSL for declaring params and options of the initializer
License:       MIT
Group:         Development/Ruby
Url:           https://dry-rb.org/gems/dry-initializer
Vcs:           https://github.com/dry-rb/dry-initializer.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(dry-types) >= 0
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-cobertura) >= 0
BuildRequires: gem(warning) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.81.6,rubocop < 2
Requires:      ruby >= 3.1.0
Provides:      gem(dry-initializer) = 3.2.0

%description
DSL for declaring params and options of the initializer


%if_enabled    doc
%package       -n gem-dry-initializer-doc
Version:       3.2.0
Release:       alt1
Summary:       DSL for declaring params and options of the initializer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dry-initializer
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(dry-initializer) = 3.2.0

%description   -n gem-dry-initializer-doc
DSL for declaring params and options of the initializer documentation files.

%description   -n gem-dry-initializer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dry-initializer.
%endif


%if_enabled    devel
%package       -n gem-dry-initializer-devel
Version:       3.2.0
Release:       alt1
Summary:       DSL for declaring params and options of the initializer development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dry-initializer
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(dry-initializer) = 3.2.0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rspec) >= 0

%description   -n gem-dry-initializer-devel
DSL for declaring params and options of the initializer development package.

%description   -n gem-dry-initializer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dry-initializer.
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
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md changelog.yml
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-dry-initializer-doc
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md changelog.yml
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-dry-initializer-devel
%doc CHANGELOG.md LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md changelog.yml
%endif


%changelog
* Wed Jul 08 2026 Alexander Burmatov <thatman@altlinux.org> 3.2.0-alt1
- ^ 3.1.1 -> 3.2.0

* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 3.1.1-alt1
- + packaged gem with Ruby Policy 2.0
