%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname faraday-typhoeus

Name:          gem-faraday-typhoeus
Version:       1.1.0
Release:       alt1
Summary:       Faraday adapter for Typhoeus
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/dleavitt/faraday-typhoeus
Vcs:           https://github.com/dleavitt/faraday-typhoeus.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(rack) >= 2.2
BuildRequires: gem(rake) >= 13.1
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(multipart-parser) >= 0.1.1
BuildRequires: gem(webmock) >= 3.4
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-packaging) >= 0.5
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(rubocop-rspec) >= 2.4.0
BuildRequires: gem(faraday) >= 2.0
BuildRequires: gem(typhoeus) >= 1.4
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rack) >= 4
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(multipart-parser) >= 0.2
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-packaging) >= 1
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rspec) >= 3
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(typhoeus) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rack >= 3.0.0,rack < 4
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
Requires:      gem(faraday) >= 2.0
Requires:      gem(typhoeus) >= 1.4
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(typhoeus) >= 2
Provides:      gem(faraday-typhoeus) = 1.1.0


%description
Faraday adapter for Typhoeus


%if_enabled    doc
%package       -n gem-faraday-typhoeus-doc
Version:       1.1.0
Release:       alt1
Summary:       Faraday adapter for Typhoeus documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday-typhoeus
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faraday-typhoeus) = 1.1.0

%description   -n gem-faraday-typhoeus-doc
Faraday adapter for Typhoeus documentation files.

%description   -n gem-faraday-typhoeus-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday-typhoeus.
%endif


%if_enabled    devel
%package       -n gem-faraday-typhoeus-devel
Version:       1.1.0
Release:       alt1
Summary:       Faraday adapter for Typhoeus development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета faraday-typhoeus
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(faraday-typhoeus) = 1.1.0
Requires:      gem(bundler) >= 2.0
Requires:      gem(rack) >= 2.2
Requires:      gem(rake) >= 13.1
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(multipart-parser) >= 0.1.1
Requires:      gem(webmock) >= 3.4
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-packaging) >= 0.5
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(rubocop-rspec) >= 2.4.0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rack) >= 4
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(multipart-parser) >= 0.2
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-packaging) >= 1
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rspec) >= 3

%description   -n gem-faraday-typhoeus-devel
Faraday adapter for Typhoeus development package.

%description   -n gem-faraday-typhoeus-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета faraday-typhoeus.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-faraday-typhoeus-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-faraday-typhoeus-devel
%doc README.md
%endif


%changelog
* Fri Oct 18 2024 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with Ruby Policy 2.0
