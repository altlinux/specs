%define        gemname simplecov-lcov

Name:          gem-simplecov-lcov
Version:       0.8.0
Release:       alt1
Summary:       Custom SimpleCov formatter to generate a lcov style coverage
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/fortissimo1997/simplecov-lcov
Vcs:           https://github.com/fortissimo1997/simplecov-lcov.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(activesupport) >= 0
BuildConflicts: gem(simplecov) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Provides:      gem(simplecov-lcov) = 0.8.0


%description
Custom SimpleCov formatter to generate a lcov style coverage.


%package       -n gem-simplecov-lcov-doc
Version:       0.8.0
Release:       alt1
Summary:       Custom SimpleCov formatter to generate a lcov style coverage documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета simplecov-lcov
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(simplecov-lcov) = 0.8.0

%description   -n gem-simplecov-lcov-doc
Custom SimpleCov formatter to generate a lcov style coverage documentation
files.

%description   -n gem-simplecov-lcov-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета simplecov-lcov.


%package       -n gem-simplecov-lcov-devel
Version:       0.8.0
Release:       alt1
Summary:       Custom SimpleCov formatter to generate a lcov style coverage development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета simplecov-lcov
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(simplecov-lcov) = 0.8.0
Requires:      gem(rspec) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(coveralls) >= 0
Requires:      gem(activesupport) >= 0
Conflicts:     gem(simplecov) >= 1

%description   -n gem-simplecov-lcov-devel
Custom SimpleCov formatter to generate a lcov style coverage development
package.

%description   -n gem-simplecov-lcov-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета simplecov-lcov.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.markdown
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-simplecov-lcov-doc
%doc README.markdown
%ruby_gemdocdir

%files         -n gem-simplecov-lcov-devel
%doc README.markdown


%changelog
* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- + packaged gem with Ruby Policy 2.0
