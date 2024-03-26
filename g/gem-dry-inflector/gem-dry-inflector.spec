%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname dry-inflector

Name:          gem-dry-inflector
Version:       1.0.0
Release:       alt1
Summary:       String inflections for dry-rb
License:       MIT
Group:         Development/Ruby
Url:           https://dry-rb.org/gems/dry-inflector
Vcs:           https://github.com/dry-rb/dry-inflector.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-cobertura) >= 0
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(warning) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Provides:      gem(dry-inflector) = 1.0.0


%description
dry-inflector is an inflector gem for Ruby, which provides a configurable
inflector object, rather than using a singleton.


%if_enabled    doc
%package       -n gem-dry-inflector-doc
Version:       1.0.0
Release:       alt1
Summary:       String inflections for dry-rb documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dry-inflector
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dry-inflector) = 1.0.0

%description   -n gem-dry-inflector-doc
String inflections for dry-rb documentation files.

dry-inflector is an inflector gem for Ruby, which provides a configurable
inflector object, rather than using a singleton.
%description   -n gem-dry-inflector-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dry-inflector.
%endif


%if_enabled    devel
%package       -n gem-dry-inflector-devel
Version:       1.0.0
Release:       alt1
Summary:       String inflections for dry-rb development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dry-inflector
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dry-inflector) = 1.0.0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-cobertura) >= 0
Requires:      gem(rexml) >= 0
Requires:      gem(warning) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(bundler) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(byebug) >= 0
Requires:      gem(yard) >= 0
Conflicts:     gem(rubocop) >= 2

%description   -n gem-dry-inflector-devel
String inflections for dry-rb development package.

dry-inflector is an inflector gem for Ruby, which provides a configurable
inflector object, rather than using a singleton.
%description   -n gem-dry-inflector-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dry-inflector.
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
%files         -n gem-dry-inflector-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-dry-inflector-devel
%doc README.md
%endif


%changelog
* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- ^ 0.2.1 -> 1.0.0

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.1-alt1
- ^ 0.1.2 -> 0.2.1

* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
