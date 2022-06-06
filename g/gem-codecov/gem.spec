%define        gemname codecov

Name:          gem-codecov
Version:       0.6.0
Release:       alt1
Summary:       Hosted code coverage
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/codecov/codecov-ruby
Vcs:           https://github.com/codecov/codecov-ruby.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(simplecov) >= 0.15 gem(simplecov) < 1
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6
BuildRequires: gem(mocha) >= 1.0 gem(mocha) < 2
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rubocop) >= 1.0 gem(rubocop) < 2
BuildRequires: gem(webmock) >= 3.0 gem(webmock) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      gem(simplecov) >= 0.15 gem(simplecov) < 1
Provides:      gem(codecov) = 0.6.0


%description
Hosted code coverage Ruby reporter.


%package       -n gem-codecov-doc
Version:       0.6.0
Release:       alt1
Summary:       Hosted code coverage documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета codecov
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(codecov) = 0.6.0

%description   -n gem-codecov-doc
Hosted code coverage documentation files.

Hosted code coverage Ruby reporter.

%description   -n gem-codecov-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета codecov.


%package       -n gem-codecov-devel
Version:       0.6.0
Release:       alt1
Summary:       Hosted code coverage development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета codecov
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(codecov) = 0.6.0
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6
Requires:      gem(mocha) >= 1.0 gem(mocha) < 2
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rubocop) >= 1.0 gem(rubocop) < 2
Requires:      gem(webmock) >= 3.0 gem(webmock) < 4

%description   -n gem-codecov-devel
Hosted code coverage development package.

Hosted code coverage Ruby reporter.

%description   -n gem-codecov-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета codecov.


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

%files         -n gem-codecov-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-codecov-devel
%doc README.md


%changelog
* Wed Apr 20 2022 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt1
- + packaged gem with Ruby Policy 2.0
