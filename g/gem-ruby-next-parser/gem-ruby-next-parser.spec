%define        _unpackaged_files_terminate_build 0
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ruby-next-parser

Name:          gem-ruby-next-parser
Version:       3.4.0.2
Release:       alt1
Summary:       A Ruby parser written in pure Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/whitequark/parser
Vcs:           https://github.com/whitequark/parser.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.15
BuildRequires: gem(cliver) >= 0.3.2
BuildRequires: gem(gauntlet) >= 0
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(minitest) >= 5.10
BuildRequires: gem(parser) >= 3.0.3.1
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(racc) >= 1.8.1
BuildRequires: gem(rake) >= 13.0.1
BuildRequires: gem(simplecov) >= 0.15.1
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(ast) >= 2.5
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(cliver) >= 0.4
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(simplecov) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency racc >= 1.8.1,racc < 2
%ruby_ignore_names parser
Requires:      ruby >= 2.0.0
Requires:      gem(ast) >= 1.1
Requires:      gem(parser) >= 3.0.3.1
Requires:      gem(racc) >= 1.8.1
Conflicts:     gem(ast) >= 3.0
Provides:      gem(ruby-next-parser) = 3.4.0.2

%description
A Ruby parser written in pure Ruby.


%if_enabled    doc
%package       -n gem-ruby-next-parser-doc
Version:       3.4.0.2
Release:       alt1
Summary:       A Ruby parser written in pure Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-next-parser
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(ruby-next-parser) = 3.4.0.2

%description   -n gem-ruby-next-parser-doc
A Ruby parser written in pure Ruby documentation files.

%description   -n gem-ruby-next-parser-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-next-parser.
%endif


%if_enabled    devel
%package       -n gem-ruby-next-parser-devel
Version:       3.4.0.2
Release:       alt1
Summary:       A Ruby parser written in pure Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-next-parser
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(ruby-next-parser) = 3.4.0.2
Requires:      gem(bundler) >= 1.15
Requires:      gem(cliver) >= 0.3.2
Requires:      gem(gauntlet) >= 0
Requires:      gem(kramdown) >= 0
Requires:      gem(minitest) >= 5.10
Requires:      gem(rake) >= 13.0.1
Requires:      gem(simplecov) >= 0.15.1
Requires:      gem(yard) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(cliver) >= 0.4
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rake) >= 14
Conflicts:     gem(simplecov) >= 1

%description   -n gem-ruby-next-parser-devel
A Ruby parser written in pure Ruby development package.

%description   -n gem-ruby-next-parser-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-next-parser.
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
%doc CHANGELOG.md CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-ruby-next-parser-doc
%doc CHANGELOG.md CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ruby-next-parser-devel
%doc CHANGELOG.md CONTRIBUTING.md LICENSE.txt README.md
%endif


%changelog
* Tue Dec 09 2025 Pavel Skrylev <majioa@altlinux.org> 3.4.0.2-alt1
- ^ 3.2.2.4 -> 3.4.0.2

* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 3.2.2.4-alt1
- + packaged gem with Ruby Policy 2.0
