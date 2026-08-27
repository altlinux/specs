%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname rspec-pending_for

Name:          gem-rspec-pending-for
Version:       0.1.27
Release:       alt1
Summary:       Mark specs pending or skipped for specific Ruby engine (e.g. MRI or JRuby) / version combinations
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/pboling/rspec-pending_for
Vcs:           https://github.com/pboling/rspec-pending_for.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(addressable) >= 2.8.0
BuildRequires: gem(anonymous_loader) >= 0.1.3
BuildRequires: gem(appraisal2) >= 3.2.2
BuildRequires: gem(bundler-audit) >= 0.9.3
BuildRequires: gem(erb) >= 6.0.7
BuildRequires: gem(gem_bench) >= 2.0.5
BuildRequires: gem(gitmoji-regex) >= 2.0.12
BuildRequires: gem(irb) >= 1.17
BuildRequires: gem(kettle-dev) >= 3.0.6
BuildRequires: gem(kettle-family) >= 1.2.51
BuildRequires: gem(kettle-test) >= 2.0.19
BuildRequires: gem(kramdown) >= 2.3.1
BuildRequires: gem(kramdown-parser-gfm) >= 1.1
BuildRequires: gem(mutex_m) >= 0.2
BuildRequires: gem(nomono) >= 1.1.4
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rbs) >= 3.0
BuildRequires: gem(reek) >= 6.5
BuildRequires: gem(require_bench) >= 1.0.4
BuildRequires: gem(rspec-core) >= 3.0
BuildRequires: gem(ruby-progressbar) >= 1.13
BuildRequires: gem(ruby_engine) >= 2.0
BuildRequires: gem(ruby_version) >= 1.0
BuildRequires: gem(stone_checksums) >= 1.0.8
BuildRequires: gem(stringio) >= 3.0
BuildRequires: gem(turbo_tests2) >= 3.2.6
BuildRequires: gem(yaml-converter) >= 0.2.5
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(yard-fence) >= 0.9.8
BuildRequires: gem(yard-junk) >= 0.1
BuildRequires: gem(yard-lint) >= 1.11
BuildRequires: gem(yard-relative_markdown_links) >= 0.6
BuildRequires: gem(yard-timekeeper) >= 0.2.6
BuildRequires: gem(yard-yaml) >= 0.2.5
BuildConflicts: gem(addressable) >= 3
BuildConflicts: gem(anonymous_loader) >= 1
BuildConflicts: gem(appraisal2) >= 4
BuildConflicts: gem(bundler-audit) >= 0.10
BuildConflicts: gem(erb) >= 7
BuildConflicts: gem(gem_bench) >= 3
BuildConflicts: gem(gitmoji-regex) >= 3
BuildConflicts: gem(irb) >= 2
BuildConflicts: gem(kettle-dev) >= 4
BuildConflicts: gem(kettle-family) >= 2
BuildConflicts: gem(kettle-test) >= 3
BuildConflicts: gem(kramdown-parser-gfm) >= 2
BuildConflicts: gem(mutex_m) >= 1
BuildConflicts: gem(nomono) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(reek) >= 7
BuildConflicts: gem(require_bench) >= 2
BuildConflicts: gem(rspec-core) >= 4
BuildConflicts: gem(ruby-progressbar) >= 2
BuildConflicts: gem(ruby_engine) >= 3
BuildConflicts: gem(ruby_version) >= 2
BuildConflicts: gem(stone_checksums) >= 2
BuildConflicts: gem(turbo_tests2) >= 4
BuildConflicts: gem(yaml-converter) >= 1
BuildConflicts: gem(yard-fence) >= 1
BuildConflicts: gem(yard-junk) >= 1
BuildConflicts: gem(yard-lint) >= 2
BuildConflicts: gem(yard-relative_markdown_links) >= 1
BuildConflicts: gem(yard-timekeeper) >= 1
BuildConflicts: gem(yard-yaml) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency kramdown >= 2.3.1,kramdown < 3
%ruby_use_gem_dependency rubocop-minitest >= 0.13.0,rubocop-minitest < 1
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
%ruby_alias_names rspec-pending_for,rspec-pending-for
Requires:      ruby >= 1.8.7
Requires:      gem(rspec-core) >= 3.0
Requires:      gem(ruby_engine) >= 2.0
Requires:      gem(ruby_version) >= 1.0
Conflicts:     gem(rspec-core) >= 4
Conflicts:     gem(ruby_engine) >= 3
Conflicts:     gem(ruby_version) >= 2
Provides:      gem(rspec-pending_for) = 0.1.27

%description
Mark specs pending or skipped for specific Ruby engine (e.g. MRI or JRuby) /
version combinations.


%if_enabled    doc
%package       -n gem-rspec-pending-for-doc
Version:       0.1.27
Release:       alt1
Summary:       Mark specs pending or skipped for specific Ruby engine (e.g. MRI or JRuby) / version combinations documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-pending_for
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-pending_for) = 0.1.27

%description   -n gem-rspec-pending-for-doc
Mark specs pending or skipped for specific Ruby engine (e.g. MRI or JRuby) /
version combinations documentation files.

%description   -n gem-rspec-pending-for-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-pending_for.
%endif


%if_enabled    devel
%package       -n gem-rspec-pending-for-devel
Version:       0.1.27
Release:       alt1
Summary:       Mark specs pending or skipped for specific Ruby engine (e.g. MRI or JRuby) / version combinations development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-pending_for
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-pending_for) = 0.1.27
Requires:      gem(addressable) >= 2.8.0
Requires:      gem(anonymous_loader) >= 0.1.3
Requires:      gem(appraisal2) >= 3.2.2
Requires:      gem(bundler-audit) >= 0.9.3
Requires:      gem(erb) >= 6.0.7
Requires:      gem(gem_bench) >= 2.0.5
Requires:      gem(gitmoji-regex) >= 2.0.12
Requires:      gem(irb) >= 1.17
Requires:      gem(kettle-dev) >= 3.0.6
Requires:      gem(kettle-family) >= 1.2.51
Requires:      gem(kettle-test) >= 2.0.19
Requires:      gem(kramdown) >= 2.3.1
Requires:      gem(kramdown-parser-gfm) >= 1.1
Requires:      gem(mutex_m) >= 0.2
Requires:      gem(nomono) >= 1.1.4
Requires:      gem(rake) >= 13.0
Requires:      gem(rbs) >= 3.0
Requires:      gem(reek) >= 6.5
Requires:      gem(require_bench) >= 1.0.4
Requires:      gem(rspec-core) >= 3.0
Requires:      gem(ruby-progressbar) >= 1.13
Requires:      gem(ruby_engine) >= 2.0
Requires:      gem(ruby_version) >= 1.0
Requires:      gem(stone_checksums) >= 1.0.8
Requires:      gem(stringio) >= 3.0
Requires:      gem(turbo_tests2) >= 3.2.6
Requires:      gem(yaml-converter) >= 0.2.5
Requires:      gem(yard) >= 0.9
Requires:      gem(yard-fence) >= 0.9.8
Requires:      gem(yard-junk) >= 0.1
Requires:      gem(yard-lint) >= 1.11
Requires:      gem(yard-relative_markdown_links) >= 0.6
Requires:      gem(yard-timekeeper) >= 0.2.6
Requires:      gem(yard-yaml) >= 0.2.5
Conflicts:     gem(addressable) >= 3
Conflicts:     gem(anonymous_loader) >= 1
Conflicts:     gem(appraisal2) >= 4
Conflicts:     gem(bundler-audit) >= 0.10
Conflicts:     gem(erb) >= 7
Conflicts:     gem(gem_bench) >= 3
Conflicts:     gem(gitmoji-regex) >= 3
Conflicts:     gem(irb) >= 2
Conflicts:     gem(kettle-dev) >= 4
Conflicts:     gem(kettle-family) >= 2
Conflicts:     gem(kettle-test) >= 3
Conflicts:     gem(kramdown-parser-gfm) >= 2
Conflicts:     gem(mutex_m) >= 1
Conflicts:     gem(nomono) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(reek) >= 7
Conflicts:     gem(require_bench) >= 2
Conflicts:     gem(rspec-core) >= 4
Conflicts:     gem(ruby-progressbar) >= 2
Conflicts:     gem(ruby_engine) >= 3
Conflicts:     gem(ruby_version) >= 2
Conflicts:     gem(stone_checksums) >= 2
Conflicts:     gem(turbo_tests2) >= 4
Conflicts:     gem(yaml-converter) >= 1
Conflicts:     gem(yard-fence) >= 1
Conflicts:     gem(yard-junk) >= 1
Conflicts:     gem(yard-lint) >= 2
Conflicts:     gem(yard-relative_markdown_links) >= 1
Conflicts:     gem(yard-timekeeper) >= 1
Conflicts:     gem(yard-yaml) >= 1

%description   -n gem-rspec-pending-for-devel
Mark specs pending or skipped for specific Ruby engine (e.g. MRI or JRuby) /
version combinations development package.

%description   -n gem-rspec-pending-for-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-pending_for.
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
%doc CHANGELOG.md LICENSE.md README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rspec-pending-for-doc
%doc CHANGELOG.md LICENSE.md README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rspec-pending-for-devel
%doc CHANGELOG.md LICENSE.md README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%endif


%changelog
* Sun Aug 23 2026 Pavel Skrylev <majioa@altlinux.org> 0.1.27-alt1
- ^ 0.1.16 -> 0.1.27

* Thu Sep 29 2022 Pavel Skrylev <majioa@altlinux.org> 0.1.16-alt1
- + packaged gem with Ruby Policy 2.0
