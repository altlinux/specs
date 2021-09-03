%define        gemname octokit

Name:          gem-octokit
Version:       4.21.0
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
BuildRequires: gem(bundler) >= 1 gem(bundler) < 3
BuildRequires: gem(sawyer) >= 0.8.0 gem(sawyer) < 0.9
BuildRequires: gem(faraday) >= 0.9

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Requires:      gem(sawyer) >= 0.8.0 gem(sawyer) < 0.9
Requires:      gem(faraday) >= 0.9
Provides:      gem(octokit) = 4.21.0


%description
Ruby toolkit for the GitHub API.

API wrappers should reflect the idioms of the language in which they were
written. Octokit.rb wraps the GitHub API in a flat API client that follows Ruby
conventions and requires little knowledge of REST. Most methods have positional
arguments for required input and an options hash for optional parameters,
headers, or other options.


%package       -n gem-octokit-doc
Version:       4.21.0
Release:       alt1
Summary:       Ruby toolkit for the GitHub API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета octokit
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(octokit) = 4.21.0

%description   -n gem-octokit-doc
Ruby toolkit for the GitHub API documentation files.

API wrappers should reflect the idioms of the language in which they were
written. Octokit.rb wraps the GitHub API in a flat API client that follows Ruby
conventions and requires little knowledge of REST. Most methods have positional
arguments for required input and an options hash for optional parameters,
headers, or other options.

%description   -n gem-octokit-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета octokit.


%package       -n gem-octokit-devel
Version:       4.21.0
Release:       alt1
Summary:       Ruby toolkit for the GitHub API development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета octokit
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(octokit) = 4.21.0
Requires:      gem(bundler) >= 1 gem(bundler) < 3

%description   -n gem-octokit-devel
Ruby toolkit for the GitHub API development package.

API wrappers should reflect the idioms of the language in which they were
written. Octokit.rb wraps the GitHub API in a flat API client that follows Ruby
conventions and requires little knowledge of REST. Most methods have positional
arguments for required input and an options hash for optional parameters,
headers, or other options.

%description   -n gem-octokit-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета octokit.


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

%files         -n gem-octokit-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 4.21.0-alt1
- ^ 4.14.0 -> 4.21.0

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 4.14.0-alt1.1
- ! spec according to changelog rules

* Fri Aug 02 2019 Pavel Skrylev <majioa@altlinux.org> 4.14.0-alt1
- + packaged gem with the Ruby Policy 2.0 usage
