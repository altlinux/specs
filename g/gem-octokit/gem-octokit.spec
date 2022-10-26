%define        gemname octokit

Name:          gem-octokit
Version:       5.6.1
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
%if_with check
BuildRequires: gem(jruby-openssl) >= 0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rss) >= 0.2.9
BuildRequires: gem(awesome_print) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(rexml) >= 3.2.4
BuildRequires: gem(json) >= 2.3.0
BuildRequires: gem(jwt) >= 2.2
BuildRequires: gem(mime-types) >= 3.3.1 gem(mime-types) < 4
BuildRequires: gem(multi_json) >= 1.14
BuildRequires: gem(netrc) >= 0.11.0 gem(netrc) < 0.12
BuildRequires: gem(rb-fsevent) >= 0.11.1 gem(rb-fsevent) < 0.12
BuildRequires: gem(rbnacl) >= 7.1.1 gem(rbnacl) < 7.2
BuildRequires: gem(rspec) >= 3.9 gem(rspec) < 4
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(vcr) >= 6.1 gem(vcr) < 7
BuildRequires: gem(webmock) >= 3.8
BuildRequires: gem(faraday) >= 2.0 gem(faraday) < 3
BuildRequires: gem(faraday-multipart) >= 0
BuildRequires: gem(faraday-retry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(rubocop) >= 1.15.0 gem(rubocop) < 2
BuildRequires: gem(bundler) >= 1 gem(bundler) < 3
BuildRequires: gem(faraday) >= 1 gem(faraday) < 3
BuildRequires: gem(sawyer) >= 0.9 gem(sawyer) < 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency multi_json >= 1.15.0,multi_json < 2
%ruby_use_gem_dependency jwt >= 2.2.1,jwt < 3
Requires:      gem(faraday) >= 1 gem(faraday) < 3
Requires:      gem(sawyer) >= 0.9 gem(sawyer) < 1
Provides:      gem(octokit) = 5.6.1


%description
Ruby toolkit for the GitHub API.

API wrappers should reflect the idioms of the language in which they were
written. Octokit.rb wraps the GitHub API in a flat API client that follows Ruby
conventions and requires little knowledge of REST. Most methods have positional
arguments for required input and an options hash for optional parameters,
headers, or other options.


%package       -n gem-octokit-doc
Version:       5.6.1
Release:       alt1
Summary:       Ruby toolkit for the GitHub API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета octokit
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(octokit) = 5.6.1

%description   -n gem-octokit-doc
Ruby toolkit for the GitHub API documentation files.

%description   -n gem-octokit-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета octokit.


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

%files         -n gem-octokit-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Fri Oct 14 2022 Pavel Skrylev <majioa@altlinux.org> 5.6.1-alt1
- ^ 4.21.0 -> 5.6.1

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 4.21.0-alt1
- ^ 4.14.0 -> 4.21.0

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 4.14.0-alt1.1
- ! spec according to changelog rules

* Fri Aug 02 2019 Pavel Skrylev <majioa@altlinux.org> 4.14.0-alt1
- + packaged gem with the Ruby Policy 2.0 usage
