%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname octokit

Name:          gem-octokit
Version:       8.1.0
Release:       alt1
Summary:       Ruby toolkit for the GitHub API
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/octokit/octokit.rb
Vcs:           https://github.com/octokit/octokit.rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rss) >= 0.2.9
BuildRequires: gem(awesome_print) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(rexml) >= 3.2.4
BuildRequires: gem(json) >= 2.3.0
BuildRequires: gem(jwt) >= 2.2
BuildRequires: gem(mime-types) >= 3.3.1
BuildRequires: gem(multi_json) >= 1.14
BuildRequires: gem(netrc) >= 0.11.0
BuildRequires: gem(rb-fsevent) >= 0.11.1
BuildRequires: gem(rbnacl) >= 7.1.1
BuildRequires: gem(rspec) >= 3.9
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(test-queue) >= 0
BuildRequires: gem(vcr) >= 6.1
BuildRequires: gem(webmock) >= 3.8
BuildRequires: gem(faraday) >= 1
BuildRequires: gem(faraday-multipart) >= 0
BuildRequires: gem(faraday-retry) >= 0
BuildRequires: gem(bundler) >= 1
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(base64) >= 0
BuildRequires: gem(sawyer) >= 0.9
BuildConflicts: gem(mime-types) >= 4
BuildConflicts: gem(netrc) >= 0.12
BuildConflicts: gem(rb-fsevent) >= 0.12
BuildConflicts: gem(rbnacl) >= 7.2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(vcr) >= 7
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(sawyer) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency multi_json >= 1.15.0,multi_json < 2
%ruby_use_gem_dependency jwt >= 2.2.1,jwt < 3
Requires:      gem(faraday) >= 1
Requires:      gem(base64) >= 0
Requires:      gem(sawyer) >= 0.9
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(sawyer) >= 1
Provides:      gem(octokit) = 8.1.0


%description
Ruby toolkit for the GitHub API.

API wrappers should reflect the idioms of the language in which they were
written. Octokit.rb wraps the GitHub API in a flat API client that follows Ruby
conventions and requires little knowledge of REST. Most methods have positional
arguments for required input and an options hash for optional parameters,
headers, or other options.


%if_enabled    doc
%package       -n gem-octokit-doc
Version:       8.1.0
Release:       alt1
Summary:       Ruby toolkit for the GitHub API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета octokit
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(octokit) = 8.1.0

%description   -n gem-octokit-doc
Ruby toolkit for the GitHub API documentation files.
%description   -n gem-octokit-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета octokit.
%endif


%if_enabled    devel
%package       -n gem-octokit-devel
Version:       8.1.0
Release:       alt1
Summary:       Ruby toolkit for the GitHub API development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета octokit
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(octokit) = 8.1.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rss) >= 0.2.9
Requires:      gem(awesome_print) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(rexml) >= 3.2.4
Requires:      gem(json) >= 2.3.0
Requires:      gem(jwt) >= 2.2
Requires:      gem(mime-types) >= 3.3.1
Requires:      gem(multi_json) >= 1.14
Requires:      gem(netrc) >= 0.11.0
Requires:      gem(rb-fsevent) >= 0.11.1
Requires:      gem(rbnacl) >= 7.1.1
Requires:      gem(rspec) >= 3.9
Requires:      gem(simplecov) >= 0
Requires:      gem(test-queue) >= 0
Requires:      gem(vcr) >= 6.1
Requires:      gem(webmock) >= 3.8
Requires:      gem(faraday-multipart) >= 0
Requires:      gem(faraday-retry) >= 0
Requires:      gem(bundler) >= 1
Requires:      gem(pry-byebug) >= 0
Requires:      gem(redcarpet) >= 0
Requires:      gem(rubocop) >= 1.15.0
Conflicts:     gem(mime-types) >= 4
Conflicts:     gem(netrc) >= 0.12
Conflicts:     gem(rb-fsevent) >= 0.12
Conflicts:     gem(rbnacl) >= 7.2
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(vcr) >= 7
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rubocop) >= 2

%description   -n gem-octokit-devel
Ruby toolkit for the GitHub API development package.
%description   -n gem-octokit-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета octokit.
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
%files         -n gem-octokit-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-octokit-devel
%doc README.md
%endif


%changelog
* Thu Mar 14 2024 Pavel Skrylev <majioa@altlinux.org> 8.1.0-alt1
- ^ 5.6.1 -> 8.1.0

* Fri Oct 14 2022 Pavel Skrylev <majioa@altlinux.org> 5.6.1-alt1
- ^ 4.21.0 -> 5.6.1

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 4.21.0-alt1
- ^ 4.14.0 -> 4.21.0

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 4.14.0-alt1.1
- ! spec according to changelog rules

* Fri Aug 02 2019 Pavel Skrylev <majioa@altlinux.org> 4.14.0-alt1
- + packaged gem with the Ruby Policy 2.0 usage
