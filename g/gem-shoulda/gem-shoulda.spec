%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname shoulda

Name:          gem-shoulda
Version:       4.0.0.23
Release:       alt0.1
Summary:       Making tests easy on the fingers and eyes
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/thoughtbot/shoulda
Vcs:           https://github.com/thoughtbot/shoulda.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 13.0.1
BuildConflicts: gem(rake) >= 14
%if_enabled check
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(m) >= 0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(minitest-reporters) >= 1.0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(rspec) >= 3.9
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-packaging) >= 0
BuildRequires: gem(rubocop-rails) >= 0
BuildRequires: gem(shoulda-context) >= 2.0.0
BuildRequires: gem(shoulda-matchers) >= 4.5.1
BuildRequires: gem(snowglobe) >= 0
BuildRequires: gem(warnings_logger) >= 0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(minitest-reporters) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(shoulda-context) >= 3
BuildConflicts: gem(shoulda-matchers) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency shoulda-matchers >= 4.5.1,shoulda-matchers < 7
Requires:      ruby >= 3.0.5
Requires:      gem(shoulda-context) >= 2.0
Requires:      gem(shoulda-matchers) >= 4.5.1
Conflicts:     gem(shoulda-context) >= 3
Conflicts:     gem(shoulda-matchers) >= 7
Provides:      gem(shoulda) = 4.0.0.23

%ruby_use_gem_version shoulda:4.0.0.23

%description
Shoulda makes it easy to write elegant, understandable, and maintainable tests.
Shoulda consists of test macros, assertions, and helpers added on to the
Test::Unit framework. It's fully compatible with your existing tests, and
requires no retooling to use.


%if_enabled    doc
%package       -n gem-shoulda-doc
Version:       4.0.0.23
Release:       alt0.1
Summary:       Making tests easy on the fingers and eyes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета shoulda
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(shoulda) = 4.0.0.23

%description   -n gem-shoulda-doc
Making tests easy on the fingers and eyes documentation files.

Shoulda makes it easy to write elegant, understandable, and maintainable tests.
Shoulda consists of test macros, assertions, and helpers added on to the
Test::Unit framework. It's fully compatible with your existing tests, and
requires no retooling to use.

%description   -n gem-shoulda-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета shoulda.
%endif


%if_enabled    devel
%package       -n gem-shoulda-devel
Version:       4.0.0.23
Release:       alt0.1
Summary:       Making tests easy on the fingers and eyes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета shoulda
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(shoulda) = 4.0.0.23
Requires:      gem(appraisal) >= 0
Requires:      gem(m) >= 0
Requires:      gem(minitest) >= 5.0
Requires:      gem(minitest-reporters) >= 1.0
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rake) >= 13.0.1
Requires:      gem(rspec) >= 3.9
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-packaging) >= 0
Requires:      gem(rubocop-rails) >= 0
Requires:      gem(snowglobe) >= 0
Requires:      gem(warnings_logger) >= 0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-reporters) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4

%description   -n gem-shoulda-devel
Making tests easy on the fingers and eyes development package.

Shoulda makes it easy to write elegant, understandable, and maintainable tests.
Shoulda consists of test macros, assertions, and helpers added on to the
Test::Unit framework. It's fully compatible with your existing tests, and
requires no retooling to use.

%description   -n gem-shoulda-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета shoulda.
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
%doc LICENSE README.md CHANGELOG.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-shoulda-doc
%doc LICENSE README.md CHANGELOG.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-shoulda-devel
%doc LICENSE README.md CHANGELOG.md
%endif


%changelog
* Mon Jan 27 2025 Pavel Skrylev <majioa@altlinux.org> 4.0.0.23-alt0.1
- ^ 4.0.0 -> 4.0.0p23

* Wed Jun 30 2021 Pavel Skrylev <majioa@altlinux.org> 4.0.0-alt1
- ^ 2.11.1 -> 4.0.0

* Tue Jul 20 2010 Alexey I. Froloff <raorn@altlinux.org> 2.11.1-alt1
- [2.11.1]

* Mon Oct 19 2009 Alexey I. Froloff <raorn@altlinux.org> 2.10.2-alt1
- Built for Sisyphus
