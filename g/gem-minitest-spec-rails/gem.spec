%define        gemname minitest-spec-rails

Name:          gem-minitest-spec-rails
Version:       6.0.4
Release:       alt1
Summary:       Make Rails Use MiniTest::Spec!
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/metaskills/minitest-spec-rails
Vcs:           https://github.com/metaskills/minitest-spec-rails.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6
BuildRequires: gem(railties) >= 4.1
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(sqlite3) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6
Requires:      gem(railties) >= 4.1
Provides:      gem(minitest-spec-rails) = 6.0.4


%description
The minitest-spec-rails gem makes it easy to use the \ MiniTest::Spec DSL within
your existing Rails test suite.


%package       -n gem-minitest-spec-rails-doc
Version:       6.0.4
Release:       alt1
Summary:       Make Rails Use MiniTest::Spec! documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-spec-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-spec-rails) = 6.0.4

%description   -n gem-minitest-spec-rails-doc
Make Rails Use MiniTest::Spec! documentation files.

The minitest-spec-rails gem makes it easy to use the \ MiniTest::Spec DSL within
your existing Rails test suite.

%description   -n gem-minitest-spec-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-spec-rails.


%package       -n gem-minitest-spec-rails-devel
Version:       6.0.4
Release:       alt1
Summary:       Make Rails Use MiniTest::Spec! development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-spec-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-spec-rails) = 6.0.4
Requires:      gem(appraisal) >= 0
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(sqlite3) >= 0

%description   -n gem-minitest-spec-rails-devel
Make Rails Use MiniTest::Spec! development package.

The minitest-spec-rails gem makes it easy to use the \ MiniTest::Spec DSL within
your existing Rails test suite.

%description   -n gem-minitest-spec-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-spec-rails.


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

%files         -n gem-minitest-spec-rails-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-minitest-spec-rails-devel
%doc README.md


%changelog
* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 6.0.4-alt1
- + packaged gem with Ruby Policy 2.0
