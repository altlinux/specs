%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname mini_racer

Name:          gem-mini-racer
Version:       0.16.0
Release:       alt1
Summary:       Minimal embedded v8 for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/discourse/mini_racer
Vcs:           https://github.com/discourse/mini_racer.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%ifarch i586 x86_64
BuildRequires: libv8-3.14-devel
%endif
BuildRequires: gcc-c++
BuildRequires: node-devel
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(libv8-node) >= 0
BuildConflicts: gem(libv8-node) >= 23
%if_enabled check
BuildRequires: gem(execjs) >= 0
BuildRequires: gem(m) >= 0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(rake) >= 12
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(uglifier) >= 0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency libv8-node >= 22.0,libv8-node < 23
%ruby_alias_names mini_racer,mini-racer
%ruby_ignore_names libv8-node
Requires:      ruby >= 3.1
Requires:      gem(libv8-node) >= 18.19.0.0
Conflicts:     gem(libv8-node) >= 23
Provides:      mini_racer = %EVR
Provides:      gem(mini_racer) = 0.16.0

%ruby_use_gem_version mini_racer:0.16.0

%description
Minimal embedded v8 engine for Ruby


%if_enabled    doc
%package       -n gem-mini-racer-doc
Version:       0.16.0
Release:       alt1
Summary:       Minimal embedded v8 for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mini_racer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mini_racer) = 0.16.0

%description   -n gem-mini-racer-doc
Minimal embedded v8 for Ruby documentation files.

Minimal embedded v8 engine for Ruby

%description   -n gem-mini-racer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mini_racer.
%endif


%if_enabled    devel
%package       -n gem-mini-racer-devel
Version:       0.16.0
Release:       alt1
Summary:       Minimal embedded v8 for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mini_racer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mini_racer) = 0.16.0
Requires:      gem(bundler) >= 0
Requires:      gem(m) >= 0
Requires:      gem(minitest) >= 5.0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rake-compiler) >= 0
Conflicts:     gem(minitest) >= 6

%description   -n gem-mini-racer-devel
Minimal embedded v8 for Ruby development package.

Minimal embedded v8 engine for Ruby

%description   -n gem-mini-racer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mini_racer.
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
%doc CHANGELOG CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-mini-racer-doc
%doc CHANGELOG CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-mini-racer-devel
%doc CHANGELOG CODE_OF_CONDUCT.md LICENSE.txt README.md
%_includedir/mini_racer_extension
%endif


%changelog
* Sun Jan 19 2025 Pavel Skrylev <majioa@altlinux.org> 0.16.0-alt1
- ^ 0.12.0 -> 0.16.0

* Thu Jul 25 2024 Pavel Skrylev <majioa@altlinux.org> 0.12.0-alt1
- ^ 0.6.3 -> 0.12.0

* Mon Jan 30 2023 Pavel Skrylev <majioa@altlinux.org> 0.6.3-alt1
- + packaged gem with Ruby Policy 2.0
