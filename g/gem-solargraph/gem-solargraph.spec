%define        _unpackaged_files_terminate_build 1
%define        gemname solargraph

Name:          gem-solargraph
Version:       0.49.0
Release:       alt1
Summary:       A Ruby language server
License:       MIT
Group:         Development/Ruby
Url:           https://solargraph.org
Vcs:           https://github.com/castwide/solargraph.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(pry) >= 0
BuildRequires: gem(public_suffix) >= 3.1
BuildRequires: gem(rspec) >= 3.5
BuildRequires: gem(simplecov) >= 0.14
BuildRequires: gem(webmock) >= 3.6
BuildRequires: gem(backport) >= 1.2
BuildRequires: gem(benchmark) >= 0
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(diff-lcs) >= 1.4
BuildRequires: gem(e2mmap) >= 0
BuildRequires: gem(jaro_winkler) >= 1.5
BuildRequires: gem(kramdown) >= 2.3
BuildRequires: gem(kramdown-parser-gfm) >= 1.1
BuildRequires: gem(parser) >= 3.0
BuildRequires: gem(rbs) >= 2.0
BuildRequires: gem(reverse_markdown) >= 2.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(thor) >= 1.0
BuildRequires: gem(tilt) >= 2.0
BuildRequires: gem(yard) >= 0.9
BuildConflicts: gem(public_suffix) >= 5
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(backport) >= 2
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(diff-lcs) >= 2
BuildConflicts: gem(jaro_winkler) >= 2
BuildConflicts: gem(kramdown) >= 3
BuildConflicts: gem(kramdown-parser-gfm) >= 2
BuildConflicts: gem(parser) >= 4
BuildConflicts: gem(rbs) >= 3
BuildConflicts: gem(reverse_markdown) >= 3
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(thor) >= 2
BuildConflicts: gem(tilt) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency public_suffix >= 4.0.3,public_suffix < 5
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
Requires:      gem(backport) >= 1.2
Requires:      gem(benchmark) >= 0
Requires:      gem(bundler) >= 2.0
Requires:      gem(diff-lcs) >= 1.4
Requires:      gem(e2mmap) >= 0
Requires:      gem(jaro_winkler) >= 1.5
Requires:      gem(kramdown) >= 2.3
Requires:      gem(kramdown-parser-gfm) >= 1.1
Requires:      gem(parser) >= 3.0
Requires:      gem(rbs) >= 2.0
Requires:      gem(reverse_markdown) >= 2.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(thor) >= 1.0
Requires:      gem(tilt) >= 2.0
Requires:      gem(yard) >= 0.9
Conflicts:     gem(backport) >= 2
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(diff-lcs) >= 2
Conflicts:     gem(jaro_winkler) >= 2
Conflicts:     gem(kramdown) >= 3
Conflicts:     gem(kramdown-parser-gfm) >= 2
Conflicts:     gem(parser) >= 4
Conflicts:     gem(rbs) >= 3
Conflicts:     gem(reverse_markdown) >= 3
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(thor) >= 2
Conflicts:     gem(tilt) >= 3
Provides:      gem(solargraph) = 0.49.0


%description
IDE tools for code completion, inline documentation, and static analysis


%package       -n solargraph
Version:       0.49.0
Release:       alt1
Summary:       A Ruby language server executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета solargraph
Group:         Other
BuildArch:     noarch

Requires:      gem(solargraph) = 0.49.0

%description   -n solargraph
A Ruby language server executable(s).

IDE tools for code completion, inline documentation, and static analysis

%description   -n solargraph -l ru_RU.UTF-8
Исполнямка для самоцвета solargraph.


%package       -n gem-solargraph-doc
Version:       0.49.0
Release:       alt1
Summary:       A Ruby language server documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета solargraph
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(solargraph) = 0.49.0

%description   -n gem-solargraph-doc
A Ruby language server documentation files.

IDE tools for code completion, inline documentation, and static analysis

%description   -n gem-solargraph-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета solargraph.


%package       -n gem-solargraph-devel
Version:       0.49.0
Release:       alt1
Summary:       A Ruby language server development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета solargraph
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(solargraph) = 0.49.0
Requires:      gem(pry) >= 0
Requires:      gem(public_suffix) >= 3.1
Requires:      gem(rspec) >= 3.5
Requires:      gem(simplecov) >= 0.14
Requires:      gem(webmock) >= 3.6
Conflicts:     gem(public_suffix) >= 5
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(webmock) >= 4

%description   -n gem-solargraph-devel
A Ruby language server development package.

IDE tools for code completion, inline documentation, and static analysis

%description   -n gem-solargraph-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета solargraph.


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

%files         -n solargraph
%doc README.md
%_bindir/solargraph

%files         -n gem-solargraph-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-solargraph-devel
%doc README.md


%changelog
* Wed Jun 21 2023 Pavel Skrylev <majioa@altlinux.org> 0.49.0-alt1
- + packaged gem with Ruby Policy 2.0
