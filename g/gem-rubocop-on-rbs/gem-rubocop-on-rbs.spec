%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rubocop-on-rbs

Name:          gem-rubocop-on-rbs
Version:       1.8.0
Release:       alt1
Summary:       RuboCop extension for RBS file
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ksss/rubocop-on-rbs
Vcs:           https://github.com/ksss/rubocop-on-rbs.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(lint_roller) >= 1.1
BuildRequires: gem(prism) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rbs) >= 3.5
BuildRequires: gem(rbs-inline) >= 0
BuildRequires: gem(repl_type_completor) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(steep) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(zlib) >= 0
BuildConflicts: gem(lint_roller) >= 2
BuildConflicts: gem(rbs) >= 4
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      ruby >= 3.2.0
Requires:      gem(activesupport) >= 0
Requires:      gem(lint_roller) >= 1.1
Requires:      gem(rbs) >= 3.5
Requires:      gem(rbs-inline) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(zlib) >= 0
Conflicts:     gem(lint_roller) >= 2
Conflicts:     gem(rbs) >= 4
Conflicts:     gem(rubocop) >= 2
Provides:      gem(rubocop-on-rbs) = 1.8.0

%description
RuboCop extension for RBS file.


%if_enabled    doc
%package       -n gem-rubocop-on-rbs-doc
Version:       1.8.0
Release:       alt1
Summary:       RuboCop extension for RBS file documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-on-rbs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-on-rbs) = 1.8.0

%description   -n gem-rubocop-on-rbs-doc
RuboCop extension for RBS file documentation files.

%description   -n gem-rubocop-on-rbs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-on-rbs.
%endif


%if_enabled    devel
%package       -n gem-rubocop-on-rbs-devel
Version:       1.8.0
Release:       alt1
Summary:       RuboCop extension for RBS file development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-on-rbs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-on-rbs) = 1.8.0
Requires:      gem(activesupport) >= 0
Requires:      gem(lint_roller) >= 1.1
Requires:      gem(prism) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rbs) >= 3.5
Requires:      gem(rbs-inline) >= 0
Requires:      gem(repl_type_completor) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(steep) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(zlib) >= 0
Conflicts:     gem(lint_roller) >= 2
Conflicts:     gem(rbs) >= 4
Conflicts:     gem(rubocop) >= 2

%description   -n gem-rubocop-on-rbs-devel
RuboCop extension for RBS file development package.

%description   -n gem-rubocop-on-rbs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-on-rbs.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rubocop-on-rbs-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rubocop-on-rbs-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE.txt README.md
%endif


%changelog
* Wed Oct 22 2025 Pavel Skrylev <majioa@altlinux.org> 1.8.0-alt1
- ^ 0.7.0 -> 1.8.0

* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt1
- + packaged gem with Ruby Policy 2.0
