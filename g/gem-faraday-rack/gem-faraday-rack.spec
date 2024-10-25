%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname faraday-rack

Name:          gem-faraday-rack
Version:       2.0.0
Release:       alt1
Summary:       Faraday adapter for Rack
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lostisland/faraday-rack
Vcs:           https://github.com/lostisland/faraday-rack.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(multipart-parser) >= 0.1
BuildRequires: gem(rack-test) >= 0.6
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-packaging) >= 0.5
BuildRequires: gem(rubocop-performance) >= 1.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(webmock) >= 3.4
BuildRequires: gem(faraday) >= 2.0
BuildConflicts: gem(multipart-parser) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-packaging) >= 1
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(faraday) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      gem(faraday) >= 2.0
Conflicts:     gem(faraday) >= 3
Provides:      gem(faraday-rack) = 2.0.0


%description
Faraday adapter for Rack


%if_enabled    doc
%package       -n gem-faraday-rack-doc
Version:       2.0.0
Release:       alt1
Summary:       Faraday adapter for Rack documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday-rack
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faraday-rack) = 2.0.0

%description   -n gem-faraday-rack-doc
Faraday adapter for Rack documentation files.

%description   -n gem-faraday-rack-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday-rack.
%endif


%if_enabled    devel
%package       -n gem-faraday-rack-devel
Version:       2.0.0
Release:       alt1
Summary:       Faraday adapter for Rack development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета faraday-rack
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(faraday-rack) = 2.0.0
Requires:      gem(multipart-parser) >= 0.1
Requires:      gem(rack-test) >= 0.6
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-packaging) >= 0.5
Requires:      gem(rubocop-performance) >= 1.0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(webmock) >= 3.4
Conflicts:     gem(multipart-parser) >= 1
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-packaging) >= 1
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(webmock) >= 4

%description   -n gem-faraday-rack-devel
Faraday adapter for Rack development package.

%description   -n gem-faraday-rack-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета faraday-rack.
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
%files         -n gem-faraday-rack-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-faraday-rack-devel
%doc README.md
%endif


%changelog
* Fri Oct 18 2024 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with Ruby Policy 2.0
