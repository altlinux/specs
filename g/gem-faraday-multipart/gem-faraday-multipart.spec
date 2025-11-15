%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname faraday-multipart

Name:          gem-faraday-multipart
Version:       1.1.1
Release:       alt1
Summary:       Perform multipart-post requests using Faraday
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lostisland/faraday-multipart
Vcs:           https://github.com/lostisland/faraday-multipart.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(faraday) >= 1.0
BuildRequires: gem(multipart-parser) >= 0
BuildRequires: gem(multipart-post) >= 2.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 1.12.0
BuildRequires: gem(rubocop-packaging) >= 0.5.0
BuildRequires: gem(rubocop-performance) >= 1.0
BuildRequires: gem(rubocop-rspec) >= 2.0
BuildRequires: gem(simplecov) >= 0.17
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(multipart-post) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-packaging) >= 1
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rspec) >= 4
BuildConflicts: gem(simplecov) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rubocop-rspec >= 3.7.0,rubocop-rspec < 4
%ruby_use_gem_dependency rubocop-packaging >= 0.5.2,rubocop-packaging < 1
Requires:      ruby >= 2.4
Requires:      gem(multipart-post) >= 2.0
Conflicts:     ruby >= 4
Conflicts:     gem(multipart-post) >= 3
Provides:      gem(faraday-multipart) = 1.1.1

%description
Perform multipart-post requests using Faraday.


%if_enabled    doc
%package       -n gem-faraday-multipart-doc
Version:       1.1.1
Release:       alt1
Summary:       Perform multipart-post requests using Faraday documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday-multipart
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(faraday-multipart) = 1.1.1

%description   -n gem-faraday-multipart-doc
Perform multipart-post requests using Faraday documentation files.

%description   -n gem-faraday-multipart-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday-multipart.
%endif


%if_enabled    devel
%package       -n gem-faraday-multipart-devel
Version:       1.1.1
Release:       alt1
Summary:       Perform multipart-post requests using Faraday development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета faraday-multipart
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(faraday-multipart) = 1.1.1
Requires:      gem(bundler) >= 2.0
Requires:      gem(faraday) >= 1.0
Requires:      gem(multipart-parser) >= 0
Requires:      gem(multipart-post) >= 2.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1.12.0
Requires:      gem(rubocop-packaging) >= 0.5.0
Requires:      gem(rubocop-performance) >= 1.0
Requires:      gem(rubocop-rspec) >= 2.0
Requires:      gem(simplecov) >= 0.17
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(multipart-post) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-packaging) >= 1
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rspec) >= 4
Conflicts:     gem(simplecov) >= 1

%description   -n gem-faraday-multipart-devel
Perform multipart-post requests using Faraday development package.

%description   -n gem-faraday-multipart-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета faraday-multipart.
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
%doc CHANGELOG.md LICENSE.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-faraday-multipart-doc
%doc CHANGELOG.md LICENSE.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-faraday-multipart-devel
%doc CHANGELOG.md LICENSE.md README.md
%endif


%changelog
* Sat Nov 15 2025 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- ^ 1.0.4 -> 1.1.1

* Thu Dec 15 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.4-alt1
- + packaged gem with Ruby Policy 2.0
