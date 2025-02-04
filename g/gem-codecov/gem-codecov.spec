%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname codecov

Name:          gem-codecov
Version:       0.6.0.5
Release:       alt0.1
Summary:       Hosted code coverage
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/codecov/codecov-ruby
Vcs:           https://github.com/codecov/codecov-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(mocha) >= 1.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rubocop) >= 1.0
BuildRequires: gem(simplecov) >= 0.15
BuildRequires: gem(webmock) >= 3.0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(webmock) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 2.0,mocha < 3
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      ruby >= 2.4
Requires:      gem(simplecov) >= 0.15
Conflicts:     ruby >= 4
Conflicts:     gem(simplecov) >= 1
Provides:      gem(codecov) = 0.6.0.5

%ruby_use_gem_version codecov:0.6.0.5

%description
Hosted code coverage Ruby reporter.


%if_enabled    doc
%package       -n gem-codecov-doc
Version:       0.6.0.5
Release:       alt0.1
Summary:       Hosted code coverage documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета codecov
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(codecov) = 0.6.0.5

%description   -n gem-codecov-doc
Hosted code coverage documentation files.

Hosted code coverage Ruby reporter.

%description   -n gem-codecov-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета codecov.
%endif


%if_enabled    devel
%package       -n gem-codecov-devel
Version:       0.6.0.5
Release:       alt0.1
Summary:       Hosted code coverage development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета codecov
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(codecov) = 0.6.0.5
Requires:      gem(minitest) >= 5.0
Requires:      gem(mocha) >= 1.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rubocop) >= 1.0
Requires:      gem(webmock) >= 3.0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(webmock) >= 4

%description   -n gem-codecov-devel
Hosted code coverage development package.

Hosted code coverage Ruby reporter.

%description   -n gem-codecov-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета codecov.
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
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-codecov-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-codecov-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Mon Jan 27 2025 Pavel Skrylev <majioa@altlinux.org> 0.6.0.5-alt0.1
- ^ 0.6.0 -> 0.6.0p5

* Wed Apr 20 2022 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt1
- + packaged gem with Ruby Policy 2.0
