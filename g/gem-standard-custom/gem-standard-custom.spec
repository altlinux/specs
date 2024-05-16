%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_enable    devel
%define        gemname standard-custom

Name:          gem-standard-custom
Version:       1.0.2
Release:       alt1
Summary:       Plugin containing implementations of custom cops that are bundled as defaults in Standard Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/standardrb/standard-custom
Vcs:           https://github.com/standardrb/standard-custom.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(standard) >= 0
BuildRequires: gem(m) >= 0
BuildRequires: gem(lint_roller) >= 1.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildConflicts: gem(lint_roller) >= 2
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(lint_roller) >= 1.0
Requires:      gem(rubocop) >= 1.15.0
Conflicts:     gem(lint_roller) >= 2
Conflicts:     gem(rubocop) >= 2
Provides:      gem(standard-custom) = 1.0.2


%description
Plugin containing implementations of custom cops that are bundled as defaults in
Standard Ruby


%if_enabled    doc
%package       -n gem-standard-custom-doc
Version:       1.0.2
Release:       alt1
Summary:       Plugin containing implementations of custom cops that are bundled as defaults in Standard Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета standard-custom
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(standard-custom) = 1.0.2

%description   -n gem-standard-custom-doc
Plugin containing implementations of custom cops that are bundled as defaults in
Standard Ruby documentation files.

Plugin containing implementations of custom cops that are bundled as defaults in
Standard Ruby

%description   -n gem-standard-custom-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета standard-custom.
%endif


%if_enabled    devel
%package       -n gem-standard-custom-devel
Version:       1.0.2
Release:       alt1
Summary:       Plugin containing implementations of custom cops that are bundled as defaults in Standard Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета standard-custom
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(standard-custom) = 1.0.2
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(standard) >= 0
Requires:      gem(m) >= 0

%description   -n gem-standard-custom-devel
Plugin containing implementations of custom cops that are bundled as defaults in
Standard Ruby development package.

Plugin containing implementations of custom cops that are bundled as defaults in
Standard Ruby

%description   -n gem-standard-custom-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета standard-custom.
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
%files         -n gem-standard-custom-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-standard-custom-devel
%doc README.md
%endif


%changelog
* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- + packaged gem with Ruby Policy 2.0
