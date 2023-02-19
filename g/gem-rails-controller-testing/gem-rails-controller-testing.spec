%define        gemname rails-controller-testing

Name:          gem-rails-controller-testing
Version:       1.0.5.1
Release:       alt0.1
Summary:       Extracting `assigns` and `assert_template` from ActionDispatch
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/rails-controller-testing
Vcs:           https://github.com/rails/rails-controller-testing.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(railties) >= 5.0.1
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(actionpack) >= 5.0.1
BuildRequires: gem(actionview) >= 5.0.1
BuildRequires: gem(activesupport) >= 5.0.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(actionpack) >= 5.0.1
Requires:      gem(actionview) >= 5.0.1
Requires:      gem(activesupport) >= 5.0.1
Provides:      gem(rails-controller-testing) = 1.0.5.1

%ruby_use_gem_version rails-controller-testing:1.0.5.1

%description
This gem brings back assigns to your controller tests as well as assert_template
to both controller and integration tests.

These methods were removed in Rails 5.


%package       -n gem-rails-controller-testing-doc
Version:       1.0.5.1
Release:       alt0.1
Summary:       Extracting `assigns` and `assert_template` from ActionDispatch documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rails-controller-testing
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rails-controller-testing) = 1.0.5.1

%description   -n gem-rails-controller-testing-doc
Extracting `assigns` and `assert_template` from ActionDispatch documentation
files.

This gem brings back assigns to your controller tests as well as assert_template
to both controller and integration tests.

These methods were removed in Rails 5.

%description   -n gem-rails-controller-testing-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rails-controller-testing.


%package       -n gem-rails-controller-testing-devel
Version:       1.0.5.1
Release:       alt0.1
Summary:       Extracting `assigns` and `assert_template` from ActionDispatch development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rails-controller-testing
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rails-controller-testing) = 1.0.5.1
Requires:      gem(railties) >= 5.0.1
Requires:      gem(sqlite3) >= 0

%description   -n gem-rails-controller-testing-devel
Extracting `assigns` and `assert_template` from ActionDispatch development
package.

This gem brings back assigns to your controller tests as well as assert_template
to both controller and integration tests.

These methods were removed in Rails 5.

%description   -n gem-rails-controller-testing-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rails-controller-testing.


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

%files         -n gem-rails-controller-testing-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rails-controller-testing-devel
%doc README.md


%changelog
* Wed Jan 25 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.5.1-alt0.1
- ^ 1.0.5 -> 1.0.5[1]

* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt1
- + packaged gem with Ruby Policy 2.0
