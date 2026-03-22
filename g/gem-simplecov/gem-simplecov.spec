%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname simplecov

Name:          gem-simplecov
Version:       0.22.0
Release:       alt1.1
Summary:       Code coverage for Ruby 1.9+ with a powerful configuration library and automatic merging of coverage across test suites
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/colszowka/simplecov
Vcs:           https://github.com/simplecov-ruby/simplecov.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(activesupport) >= 6.1
BuildRequires: gem(apparition) >= 0
BuildRequires: gem(aruba) >= 0
BuildRequires: gem(capybara) >= 0
BuildRequires: gem(cucumber) >= 0
BuildRequires: gem(docile) >= 1.1
BuildRequires: gem(logger) >= 0
BuildRequires: gem(matrix) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rackup) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(simplecov-html) >= 0.11
BuildRequires: gem(simplecov_json_formatter) >= 0.1
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(webrick) >= 0
BuildConflicts: gem(activesupport) >= 8
BuildConflicts: gem(docile) >= 2
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(simplecov-html) >= 1
BuildConflicts: gem(simplecov_json_formatter) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency activesupport >= 7.1,activesupport < 8
Requires:      ruby >= 2.5.0
Requires:      gem(docile) >= 1.1
Requires:      gem(matrix) >= 0
Requires:      gem(simplecov-html) >= 0.11
Requires:      gem(simplecov_json_formatter) >= 0.1
Conflicts:     gem(docile) >= 2
Conflicts:     gem(simplecov-html) >= 1
Conflicts:     gem(simplecov_json_formatter) >= 1
Obsoletes:     ruby-simplecov < %EVR
Provides:      ruby-simplecov = %EVR
Provides:      gem(simplecov) = 0.22.0

%ruby_ignore_names rspec_rails,parallel_tests,monorepo

%description
SimpleCov is a code coverage analysis tool for Ruby. It uses Ruby's built-in
Coverage library to gather code coverage data, but makes processing its results
much easier by providing a clean API to filter, group, merge, format, and
display those results, giving you a complete code coverage suite that can be set
up with just a couple lines of code.


%package       -n gem-base
Version:       0.0.1
Release:       alt1.1
Summary:       Base stuff
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Provides:      gem(base) = 0.0.1

%description   -n gem-base
Base stuff, really


%if_enabled    doc
%package       -n gem-base-doc
Version:       0.0.1
Release:       alt1.1
Summary:       Base stuff documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета base
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(base) = 0.0.1

%description   -n gem-base-doc
Base stuff documentation files.

Base stuff, really

%description   -n gem-base-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета base.
%endif


%package       -n gem-extra
Version:       0.0.1
Release:       alt1.1
Summary:       Extra stuff
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(base) >= 0
Provides:      gem(extra) = 0.0.1

%description   -n gem-extra
Extra stuff, really


%if_enabled    doc
%package       -n gem-extra-doc
Version:       0.0.1
Release:       alt1.1
Summary:       Extra stuff documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета extra
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(extra) = 0.0.1

%description   -n gem-extra-doc
Extra stuff documentation files.

Extra stuff, really

%description   -n gem-extra-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета extra.
%endif


%if_enabled    devel
%package       -n gem-extra-devel
Version:       0.0.1
Release:       alt1.1
Summary:       Extra stuff development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета extra
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(extra) = 0.0.1

%description   -n gem-extra-devel
Extra stuff development package.

Extra stuff, really

%description   -n gem-extra-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета extra.
%endif


%if_enabled    doc
%package       -n gem-simplecov-doc
Version:       0.22.0
Release:       alt1.1
Summary:       Code coverage for Ruby 1.9+ with a powerful configuration library and automatic merging of coverage across test suites documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета simplecov
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(simplecov) = 0.22.0

%description   -n gem-simplecov-doc
Code coverage for Ruby 1.9+ with a powerful configuration library and automatic
merging of coverage across test suites documentation files.

SimpleCov is a code coverage analysis tool for Ruby. It uses Ruby's built-in
Coverage library to gather code coverage data, but makes processing its results
much easier by providing a clean API to filter, group, merge, format, and
display those results, giving you a complete code coverage suite that can be set
up with just a couple lines of code.

%description   -n gem-simplecov-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета simplecov.
%endif


%if_enabled    devel
%package       -n gem-simplecov-devel
Version:       0.22.0
Release:       alt1.1
Summary:       Code coverage for Ruby 1.9+ with a powerful configuration library and automatic merging of coverage across test suites development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета simplecov
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(simplecov) = 0.22.0
Requires:      gem(activesupport) >= 6.1
Requires:      gem(apparition) >= 0
Requires:      gem(aruba) >= 0
Requires:      gem(capybara) >= 0
Requires:      gem(cucumber) >= 0
Requires:      gem(logger) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rackup) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(test-unit) >= 0
Requires:      gem(webrick) >= 0
Conflicts:     gem(activesupport) >= 8
Conflicts:     gem(rubocop) >= 2

%description   -n gem-simplecov-devel
Code coverage for Ruby 1.9+ with a powerful configuration library and automatic
merging of coverage across test suites development package.

SimpleCov is a code coverage analysis tool for Ruby. It uses Ruby's built-in
Coverage library to gather code coverage data, but makes processing its results
much easier by providing a clean API to filter, group, merge, format, and
display those results, giving you a complete code coverage suite that can be set
up with just a couple lines of code.

%description   -n gem-simplecov-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета simplecov.
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
%doc CHANGELOG.md LICENSE README.md CHANGELOG.old.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-base
%ruby_gemspecdir/base-0.0.1.gemspec
%ruby_gemslibdir/base-0.0.1

%if_enabled    doc
%files         -n gem-base-doc
%ruby_gemsdocdir/base-0.0.1
%endif

%files         -n gem-extra
%ruby_gemspecdir/extra-0.0.1.gemspec
%ruby_gemslibdir/extra-0.0.1

%if_enabled    doc
%files         -n gem-extra-doc
%ruby_gemsdocdir/extra-0.0.1
%endif

%if_enabled    devel
%files         -n gem-extra-devel
%endif

%if_enabled    doc
%files         -n gem-simplecov-doc
%doc CHANGELOG.md LICENSE README.md CHANGELOG.old.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-simplecov-devel
%doc CHANGELOG.md LICENSE README.md CHANGELOG.old.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%endif


%changelog
* Mon Mar 23 2026 Pavel Skrylev <majioa@altlinux.org> 0.22.0-alt1.1
- ! fixed spec filtering out rspec_rails, parallel_tests, and monorepo sources

* Wed Nov 05 2025 Pavel Skrylev <majioa@altlinux.org> 0.22.0-alt1
- ^ 0.21.2 -> 0.22.0

* Thu May 27 2021 Pavel Skrylev <majioa@altlinux.org> 0.21.2-alt1
- ^ 0.17.0 -> 0.21.2

* Tue Jul 09 2019 Pavel Skrylev <majioa@altlinux.org> 0.17.0-alt1
- Bump to 0.17.0
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.16.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Mar 16 2018 Andrey Cherepanov <cas@altlinux.org> 0.16.1-alt1
- New version.

* Thu Feb 01 2018 Andrey Cherepanov <cas@altlinux.org> 0.15.1-alt0.M70C.1
- Rebuild with Ruby 2.4.3

* Wed Sep 13 2017 Andrey Cherepanov <cas@altlinux.org> 0.15.1-alt1
- New version

* Tue Aug 15 2017 Andrey Cherepanov <cas@altlinux.org> 0.15.0-alt1
- New version

* Mon Mar 20 2017 Andrey Cherepanov <cas@altlinux.org> 0.14.1-alt1
- New version

* Fri Mar 17 2017 Andrey Cherepanov <cas@altlinux.org> 0.14.0-alt1
- New version

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Tue Oct 25 2016 Andrey Cherepanov <cas@altlinux.org> 0.12.0-alt2
- Rebuild with missing requirements

* Tue Oct 25 2016 Andrey Cherepanov <cas@altlinux.org> 0.12.0-alt1
- Initial build in Sisyphus
