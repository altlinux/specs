%define        _unpackaged_files_terminate_build 1
%define        gemname bundler-audit

Name:          gem-bundler-audit
Version:       0.9.1
Release:       alt1
Summary:       Patch-level verification for Bundler
License:       GPL-3.0+
Group:         Development/Ruby
Url:           https://github.com/rubysec/bundler-audit#readme
Vcs:           https://github.com/rubysec/bundler-audit#readme.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubygems-tasks) >= 0.2
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(simplecov) >= 0.7
BuildRequires: gem(kramdown) >= 2.0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(yard-spellcheck) >= 0
BuildRequires: gem(thor) >= 1.0
BuildRequires: gem(bundler) >= 1.2.0
BuildConflicts: gem(rubygems-tasks) >= 1
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(kramdown) >= 3
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(thor) >= 2
BuildConflicts: gem(bundler) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(thor) >= 1.0
Requires:      gem(bundler) >= 1.2.0
Conflicts:     gem(thor) >= 2
Conflicts:     gem(bundler) >= 3
Provides:      gem(bundler-audit) = 0.9.1


%description
bundler-audit provides patch-level verification for Bundled apps.


%package       -n bundle-audit
Version:       0.9.1
Release:       alt1
Summary:       Patch-level verification for Bundler executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета bundler-audit
Group:         Other
BuildArch:     noarch

Requires:      gem(bundler-audit) = 0.9.1

%description   -n bundle-audit
Patch-level verification for Bundler executable(s).

bundler-audit provides patch-level verification for Bundled apps.

%description   -n bundle-audit -l ru_RU.UTF-8
Исполнямка для самоцвета bundler-audit.


%package       -n gem-bundler-audit-doc
Version:       0.9.1
Release:       alt1
Summary:       Patch-level verification for Bundler documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bundler-audit
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bundler-audit) = 0.9.1

%description   -n gem-bundler-audit-doc
Patch-level verification for Bundler documentation files.

bundler-audit provides patch-level verification for Bundled apps.

%description   -n gem-bundler-audit-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bundler-audit.


%package       -n gem-bundler-audit-devel
Version:       0.9.1
Release:       alt1
Summary:       Patch-level verification for Bundler development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bundler-audit
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bundler-audit) = 0.9.1
Requires:      gem(rake) >= 0
Requires:      gem(rubygems-tasks) >= 0.2
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(simplecov) >= 0.7
Requires:      gem(kramdown) >= 2.0
Requires:      gem(redcarpet) >= 0
Requires:      gem(yard) >= 0.9
Requires:      gem(yard-spellcheck) >= 0
Conflicts:     gem(rubygems-tasks) >= 1
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(kramdown) >= 3
Conflicts:     gem(yard) >= 1

%description   -n gem-bundler-audit-devel
Patch-level verification for Bundler development package.

bundler-audit provides patch-level verification for Bundled apps.

%description   -n gem-bundler-audit-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bundler-audit.


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

%files         -n bundle-audit
%doc README.md
%_bindir/bundle-audit
%_bindir/bundler-audit

%files         -n gem-bundler-audit-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-bundler-audit-devel
%doc README.md


%changelog
* Wed Jun 21 2023 Pavel Skrylev <majioa@altlinux.org> 0.9.1-alt1
- + packaged gem with Ruby Policy 2.0
