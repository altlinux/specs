%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitest-spec-rails

Name:          gem-minitest-spec-rails
Version:       7.4.1
Release:       alt1
Summary:       Make Rails Use MiniTest::Spec!
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/metaskills/minitest-spec-rails
Vcs:           https://github.com/metaskills/minitest-spec-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(railties) >= 4.1
BuildRequires: gem(rake) >= 0
BuildRequires: gem(sqlite3) >= 0
%if_enabled check
BuildRequires: gem(minitest-focus) >= 0
BuildRequires: gem(pry) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(minitest) >= 5.0
Requires:      gem(railties) >= 4.1
Provides:      minitest-spec-rails = %EVR
Provides:      gem(minitest-spec-rails) = 7.4.1

%description
The minitest-spec-rails gem makes it easy to use the \ MiniTest::Spec DSL within
your existing Rails test suite.


%if_enabled    doc
%package       -n gem-minitest-spec-rails-doc
Version:       7.4.1
Release:       alt1
Summary:       Make Rails Use MiniTest::Spec! documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-spec-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-spec-rails) = 7.4.1

%description   -n gem-minitest-spec-rails-doc
Make Rails Use MiniTest::Spec! documentation files.

The minitest-spec-rails gem makes it easy to use the \ MiniTest::Spec DSL within
your existing Rails test suite.

%description   -n gem-minitest-spec-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-spec-rails.
%endif


%if_enabled    devel
%package       -n gem-minitest-spec-rails-devel
Version:       7.4.1
Release:       alt1
Summary:       Make Rails Use MiniTest::Spec! development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-spec-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-spec-rails) = 7.4.1
Requires:      gem(appraisal) >= 0
Requires:      gem(minitest-focus) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(sqlite3) >= 0

%description   -n gem-minitest-spec-rails-devel
Make Rails Use MiniTest::Spec! development package.

The minitest-spec-rails gem makes it easy to use the \ MiniTest::Spec DSL within
your existing Rails test suite.

%description   -n gem-minitest-spec-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-spec-rails.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md MIT-LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-minitest-spec-rails-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md MIT-LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-minitest-spec-rails-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md MIT-LICENSE README.md
%endif


%changelog
* Mon Jan 13 2025 Pavel Skrylev <majioa@altlinux.org> 7.4.1-alt1
- ^ 6.2.0 -> 7.4.1

* Sat Oct 08 2022 Pavel Skrylev <majioa@altlinux.org> 6.2.0-alt1
- ^ 6.0.4 -> 6.2.0

* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 6.0.4-alt1
- + packaged gem with Ruby Policy 2.0
