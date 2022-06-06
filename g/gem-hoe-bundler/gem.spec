%define        gemname hoe-bundler

Name:          gem-hoe-bundler
Version:       1.5.0
Release:       alt1
Summary:       Generate a Gemfile based on a Hoe spec's declared dependencies
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/flavorjones/hoe-bundler
Vcs:           https://github.com/flavorjones/hoe-bundler.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 5.11 gem(minitest) < 6
BuildRequires: gem(hoe-git) >= 0
# BuildRequires: gem(hoe-gemspec) >= 0
BuildRequires: gem(concourse) >= 0.18 gem(concourse) < 1
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(hoe) >= 3.17 gem(hoe) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_ignore_names fixture_project
Provides:      gem(hoe-bundler) = 1.5.0

%ruby_use_gem_version hoe-bundler:1.5.0

%description
Generate a Gemfile based on a Hoe spec's declared dependencies.


%package       -n gem-hoe-bundler-doc
Version:       1.5.0
Release:       alt1
Summary:       Generate a Gemfile based on a Hoe spec's declared dependencies documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hoe-bundler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hoe-bundler) = 1.5.0

%description   -n gem-hoe-bundler-doc
Generate a Gemfile based on a Hoe spec's declared dependencies documentation
files.

%description   -n gem-hoe-bundler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hoe-bundler.


%package       -n gem-hoe-bundler-devel
Version:       1.5.0
Release:       alt1
Summary:       Generate a Gemfile based on a Hoe spec's declared dependencies development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hoe-bundler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hoe-bundler) = 1.5.0
Requires:      gem(minitest) >= 5.11 gem(minitest) < 6
Requires:      gem(hoe-git) >= 0
# Requires:      gem(hoe-gemspec) >= 0
Requires:      gem(concourse) >= 0.18 gem(concourse) < 1
Requires:      gem(rdoc) >= 4.0 gem(rdoc) < 7
Requires:      gem(hoe) >= 3.17 gem(hoe) < 4

%description   -n gem-hoe-bundler-devel
Generate a Gemfile based on a Hoe spec's declared dependencies development
package.

%description   -n gem-hoe-bundler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hoe-bundler.


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

%files         -n gem-hoe-bundler-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hoe-bundler-devel
%doc README.md


%changelog
* Thu Mar 17 2022 Pavel Skrylev <majioa@altlinux.org> 1.5.0-alt1
- + packaged gem with Ruby Policy 2.0
