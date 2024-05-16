%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rubocop

Name:          gem-rubocop
Version:       1.63.1
Release:       alt1
Summary:       A Ruby static code analyzer and formatter
License:       MIT
Group:         Development/Ruby
Url:           https://www.rubocop.org/
Vcs:           https://github.com/rubocop-hq/rubocop.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(asciidoctor) >= 0
BuildRequires: gem(bump) >= 0
BuildRequires: gem(bundler) >= 1.15.0
BuildRequires: gem(memory_profiler) >= 0
BuildRequires: gem(prism) >= 0.25.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.7
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(rubocop-rake) >= 0.6.0
BuildRequires: gem(rubocop-rspec) >= 2.4.0
BuildRequires: gem(stackprof) >= 0
BuildRequires: gem(test-queue) >= 0
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(json) >= 2.3
BuildRequires: gem(language_server-protocol) >= 3.17.0
BuildRequires: gem(parallel) >= 1.10
BuildRequires: gem(parser) >= 3.3.0.2
BuildRequires: gem(rainbow) >= 2.2.2
BuildRequires: gem(regexp_parser) >= 1.8
BuildRequires: gem(rexml) >= 3.2.5
BuildRequires: gem(rubocop-ast) >= 1.7.0
BuildRequires: gem(ruby-progressbar) >= 1.7
BuildRequires: gem(unicode-display_width) >= 2.4.0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 3
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(json) >= 3
BuildConflicts: gem(parallel) >= 2
BuildConflicts: gem(rainbow) >= 4
BuildConflicts: gem(regexp_parser) >= 3.0
BuildConflicts: gem(rexml) >= 4.0
BuildConflicts: gem(rubocop-ast) >= 2
BuildConflicts: gem(ruby-progressbar) >= 2
BuildConflicts: gem(unicode-display_width) >= 3.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency rubocop-ast >= 1.7.0,rubocop-ast < 2
%ruby_use_gem_dependency rubocop-rake >= 0.6.0,rubocop-rake < 1
Requires:      gem(json) >= 2.3
Requires:      gem(language_server-protocol) >= 3.17.0
Requires:      gem(parallel) >= 1.10
Requires:      gem(parser) >= 3.3.0.2
Requires:      gem(rainbow) >= 2.2.2
Requires:      gem(regexp_parser) >= 1.8
Requires:      gem(rexml) >= 3.2.5
Requires:      gem(rubocop-ast) >= 1.7.0
Requires:      gem(ruby-progressbar) >= 1.7
Requires:      gem(unicode-display_width) >= 2.4.0
Requires:      gem-regexp-parser >= 1.7.1-alt1.1
Requires:      gem-parser >= 2.7.1.4-alt1.1
Conflicts:     gem(json) >= 3
Conflicts:     gem(parallel) >= 2
Conflicts:     gem(rainbow) >= 4
Conflicts:     gem(regexp_parser) >= 3.0
Conflicts:     gem(rexml) >= 4.0
Conflicts:     gem(rubocop-ast) >= 2
Conflicts:     gem(ruby-progressbar) >= 2
Conflicts:     gem(unicode-display_width) >= 3.0
Provides:      gem(rubocop) = 1.63.1


%description
A Ruby static code analyzer and formatter, based on the community Ruby style
guide.


%package       -n rubocop
Version:       1.63.1
Release:       alt1
Summary:       A Ruby static code analyzer and formatter executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rubocop
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop) = 1.63.1

%description   -n rubocop
A Ruby static code analyzer and formatter executable(s).

A Ruby static code analyzer and formatter, based on the community Ruby style
guide.
%description   -n rubocop -l ru_RU.UTF-8
Исполнямка для самоцвета rubocop.


%if_enabled    doc
%package       -n gem-rubocop-doc
Version:       1.63.1
Release:       alt1
Summary:       A Ruby static code analyzer and formatter documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop) = 1.63.1

%description   -n gem-rubocop-doc
A Ruby static code analyzer and formatter documentation files.

A Ruby static code analyzer and formatter, based on the community Ruby style
guide.
%description   -n gem-rubocop-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop.
%endif


%if_enabled    devel
%package       -n gem-rubocop-devel
Version:       1.63.1
Release:       alt1
Summary:       A Ruby static code analyzer and formatter development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop) = 1.63.1
Requires:      gem(asciidoctor) >= 0
Requires:      gem(bump) >= 0
Requires:      gem(bundler) >= 1.15.0
Requires:      gem(memory_profiler) >= 0
Requires:      gem(prism) >= 0.25.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.7
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(rubocop-rake) >= 0.6.0
Requires:      gem(rubocop-rspec) >= 2.4.0
Requires:      gem(stackprof) >= 0
Requires:      gem(test-queue) >= 0
Requires:      gem(yard) >= 0.9
Requires:      gem(webmock) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 3
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(yard) >= 1

%description   -n gem-rubocop-devel
A Ruby static code analyzer and formatter development package.

A Ruby static code analyzer and formatter, based on the community Ruby style
guide.
%description   -n gem-rubocop-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop.
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

%files         -n rubocop
%doc README.md
%_bindir/rubocop

%if_enabled    doc
%files         -n gem-rubocop-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rubocop-devel
%doc README.md
%endif


%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 1.63.1-alt1
- ^ 1.36.0 -> 1.63.1

* Wed Sep 21 2022 Pavel Skrylev <majioa@altlinux.org> 1.36.0-alt1
- ^ 1.27.0 -> 1.36.0

* Sat Apr 16 2022 Pavel Skrylev <majioa@altlinux.org> 1.27.0-alt1
- ^ 1.15.0 -> 1.27.0

* Sun May 30 2021 Pavel Skrylev <majioa@altlinux.org> 1.15.0-alt1
- ^ 1.13.0 -> 1.15.0

* Fri Apr 23 2021 Pavel Skrylev <majioa@altlinux.org> 1.13.0-alt1
- ^ 0.88.0 -> 1.13.0

* Fri Jul 17 2020 Pavel Skrylev <majioa@altlinux.org> 0.88.0-alt1.1
- ! dep to gem-regexp-parser, and gem-parser (closes #38650)
- ! spec syntax

* Tue Jul 14 2020 Pavel Skrylev <majioa@altlinux.org> 0.88.0-alt1
- ^ 0.74.0 -> 0.88.0
- ! executable runnning (closes #38650)

* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.74.0-alt1.1
- ! spec according to changelog rules

* Sat Aug 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.74.0-alt1
- ^ v0.74.0
- ! spec

* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 0.66.0-alt1
- Bump to 0.66.0

* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 0.65.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
