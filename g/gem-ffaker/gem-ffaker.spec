%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ffaker

Name:          gem-ffaker
Version:       2.23.0
Release:       alt1
Summary:       Ffaker generates dummy data
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ffaker/ffaker
Vcs:           https://github.com/ffaker/ffaker.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 13.0
BuildConflicts: gem(rake) >= 14
%if_enabled check
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rake) >= 0
BuildRequires: gem(test-unit) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.0
Provides:      gem(ffaker) = 2.23.0

%description
Ffaker generates dummy data. ffaker is a rewrite of faker.


%if_enabled    doc
%package       -n gem-ffaker-doc
Version:       2.23.0
Release:       alt1
Summary:       Ffaker generates dummy data documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ffaker
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ffaker) = 2.23.0

%description   -n gem-ffaker-doc
Ffaker generates dummy data documentation files.

Ffaker generates dummy data. ffaker is a rewrite of faker.

%description   -n gem-ffaker-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ffaker.
%endif


%if_enabled    devel
%package       -n gem-ffaker-devel
Version:       2.23.0
Release:       alt1
Summary:       Ffaker generates dummy data development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ffaker
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ffaker) = 2.23.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rake) >= 0
Requires:      gem(test-unit) >= 0
Conflicts:     gem(rake) >= 14

%description   -n gem-ffaker-devel
Ffaker generates dummy data development package.

Ffaker generates dummy data. ffaker is a rewrite of faker.

%description   -n gem-ffaker-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ffaker.
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
%doc Changelog.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-ffaker-doc
%doc Changelog.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ffaker-devel
%doc Changelog.md LICENSE README.md
%endif


%changelog
* Thu Jan 23 2025 Pavel Skrylev <majioa@altlinux.org> 2.23.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
