%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname standard-minitest

Name:          gem-standard-minitest
Version:       1.0.0
Release:       alt1
Summary:       A Standard Ruby plugin that configures rubocop-minitest
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/kirillplatonov/standard-minitest
Vcs:           https://github.com/kirillplatonov/standard-minitest.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(lint_roller) >= 1.0
BuildRequires: gem(rubocop-minitest) >= 0
BuildConflicts: gem(lint_roller) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(lint_roller) >= 1.0
Requires:      gem(rubocop-minitest) >= 0
Conflicts:     gem(lint_roller) >= 2
Provides:      gem(standard-minitest) = 1.0.0


%description
A Standard Ruby plugin that configures rubocop-minitest


%if_enabled    doc
%package       -n gem-standard-minitest-doc
Version:       1.0.0
Release:       alt1
Summary:       A Standard Ruby plugin that configures rubocop-minitest documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета standard-minitest
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(standard-minitest) = 1.0.0

%description   -n gem-standard-minitest-doc
A Standard Ruby plugin that configures rubocop-minitest documentation files.

%description   -n gem-standard-minitest-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета standard-minitest.
%endif


%if_enabled    devel
%package       -n gem-standard-minitest-devel
Version:       1.0.0
Release:       alt1
Summary:       A Standard Ruby plugin that configures rubocop-minitest development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета standard-minitest
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(standard-minitest) = 1.0.0

%description   -n gem-standard-minitest-devel
A Standard Ruby plugin that configures rubocop-minitest development package.

%description   -n gem-standard-minitest-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета standard-minitest.
%endif


%prep
%setup
%autopatch

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CHANGELOG.md MIT-LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-standard-minitest-doc
%doc CHANGELOG.md MIT-LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-standard-minitest-devel
%doc CHANGELOG.md MIT-LICENSE README.md
%endif


%changelog
* Mon Aug 26 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
