%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname bundler-audit

Name:          gem-bundler-audit
Version:       0.9.3
Release:       alt1
Summary:       Patch-level verification for Bundler
License:       GPL-3.0-or-later
Group:         Development/Ruby
Url:           https://github.com/rubysec/bundler-audit#readme
Vcs:           https://github.com/rubysec/bundler-audit.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.2.0
BuildRequires: gem(kramdown) >= 2.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubygems-tasks) >= 0.3
BuildRequires: gem(simplecov) >= 0.7
BuildRequires: gem(thor) >= 1.0
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(yard-spellcheck) >= 0
BuildConflicts: gem(kramdown) >= 3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubygems-tasks) >= 1
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(thor) >= 2
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      ruby >= 2.0.0
Requires:      rubygems >= 1.8.0
Requires:      gem(bundler) >= 1.2.0
Requires:      gem(thor) >= 1.0
Conflicts:     gem(thor) >= 2
Provides:      gem(bundler-audit) = 0.9.3

%description
bundler-audit provides patch-level verification for Bundled apps.


%package       -n bundle-audit
Version:       0.9.3
Release:       alt1
Summary:       Patch-level verification for Bundler executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета bundler-audit
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(bundler-audit) = 0.9.3

%description   -n bundle-audit
Patch-level verification for Bundler executable(s).

bundler-audit provides patch-level verification for Bundled apps.

%description   -n bundle-audit -l ru_RU.UTF-8
Исполнямка для самоцвета bundler-audit.


%if_enabled    doc
%package       -n gem-bundler-audit-doc
Version:       0.9.3
Release:       alt1
Summary:       Patch-level verification for Bundler documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bundler-audit
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(bundler-audit) = 0.9.3

%description   -n gem-bundler-audit-doc
Patch-level verification for Bundler documentation files.

bundler-audit provides patch-level verification for Bundled apps.

%description   -n gem-bundler-audit-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bundler-audit.
%endif


%if_enabled    devel
%package       -n gem-bundler-audit-devel
Version:       0.9.3
Release:       alt1
Summary:       Patch-level verification for Bundler development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bundler-audit
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(bundler-audit) = 0.9.3
Requires:      gem(bundler) >= 1.2.0
Requires:      gem(kramdown) >= 2.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubygems-tasks) >= 0.3
Requires:      gem(simplecov) >= 0.7
Requires:      gem(thor) >= 1.0
Requires:      gem(yard) >= 0.9
Requires:      gem(yard-spellcheck) >= 0
Conflicts:     gem(kramdown) >= 3
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubygems-tasks) >= 1
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(thor) >= 2
Conflicts:     gem(yard) >= 1

%description   -n gem-bundler-audit-devel
Patch-level verification for Bundler development package.

bundler-audit provides patch-level verification for Bundled apps.

%description   -n gem-bundler-audit-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bundler-audit.
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
%doc COPYING.txt ChangeLog.md README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n bundle-audit
%doc COPYING.txt ChangeLog.md README.md
%_bindir/bundle-audit
%_bindir/bundler-audit

%if_enabled    doc
%files         -n gem-bundler-audit-doc
%doc COPYING.txt ChangeLog.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-bundler-audit-devel
%doc COPYING.txt ChangeLog.md README.md
%endif


%changelog
* Sat Nov 29 2025 Pavel Skrylev <majioa@altlinux.org> 0.9.3-alt1
- ^ 0.9.1 -> 0.9.3

* Wed Jun 21 2023 Pavel Skrylev <majioa@altlinux.org> 0.9.1-alt1
- + packaged gem with Ruby Policy 2.0
