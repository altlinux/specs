%define        gemname faraday-em_synchrony

Name:          gem-faraday-em-synchrony
Version:       1.0.0
Release:       alt1
Summary:       Faraday adapter for EM::Synchrony
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lostisland/faraday-em_synchrony
Vcs:           https://github.com/lostisland/faraday-em_synchrony.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 2.0 gem(bundler) < 3
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(simplecov) >= 0.19 gem(simplecov) < 1
BuildRequires: gem(rubocop) >= 0.91.1 gem(rubocop) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.13.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Provides:      gem(faraday-em_synchrony) = 1.0.0


%description
Faraday adapter for EM::Synchrony


%package       -n gem-faraday-em-synchrony-doc
Version:       1.0.0
Release:       alt1
Summary:       Faraday adapter for EM::Synchrony documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday-em_synchrony
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faraday-em_synchrony) = 1.0.0

%description   -n gem-faraday-em-synchrony-doc
Faraday adapter for EM::Synchrony documentation files.

Faraday adapter for EM::Synchrony

%description   -n gem-faraday-em-synchrony-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday-em_synchrony.


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

%files         -n gem-faraday-em-synchrony-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Sat Jun 05 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
