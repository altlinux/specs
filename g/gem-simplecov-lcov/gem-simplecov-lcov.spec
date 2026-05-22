%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname simplecov-lcov

Name:          gem-simplecov-lcov
Version:       0.9.0
Release:       alt1
Summary:       Custom SimpleCov formatter to generate a lcov style coverage
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/fortissimo1997/simplecov-lcov
Vcs:           https://github.com/fortissimo1997/simplecov-lcov.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(simplecov) >= 0.17
BuildConflicts: gem(simplecov) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Provides:      gem(simplecov-lcov) = 0.9.0

%description
Custom SimpleCov formatter to generate a lcov style coverage.


%if_enabled    doc
%package       -n gem-simplecov-lcov-doc
Version:       0.9.0
Release:       alt1
Summary:       Custom SimpleCov formatter to generate a lcov style coverage documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета simplecov-lcov
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(simplecov-lcov) = 0.9.0

%description   -n gem-simplecov-lcov-doc
Custom SimpleCov formatter to generate a lcov style coverage documentation
files.

%description   -n gem-simplecov-lcov-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета simplecov-lcov.
%endif


%if_enabled    devel
%package       -n gem-simplecov-lcov-devel
Version:       0.9.0
Release:       alt1
Summary:       Custom SimpleCov formatter to generate a lcov style coverage development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета simplecov-lcov
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(simplecov-lcov) = 0.9.0
Requires:      gem(activesupport) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(coveralls) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(simplecov) >= 0.17
Conflicts:     gem(simplecov) >= 1

%description   -n gem-simplecov-lcov-devel
Custom SimpleCov formatter to generate a lcov style coverage development
package.

%description   -n gem-simplecov-lcov-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета simplecov-lcov.
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
%doc LICENSE.txt README.markdown CHANGELOG.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-simplecov-lcov-doc
%doc LICENSE.txt README.markdown CHANGELOG.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-simplecov-lcov-devel
%doc LICENSE.txt README.markdown CHANGELOG.md
%endif


%changelog
* Thu May 21 2026 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt1
- ^ 0.8.0 -> 0.9.0

* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- + packaged gem with Ruby Policy 2.0
