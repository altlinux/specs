%define        gemname faraday-multipart

Name:          gem-faraday-multipart
Version:       1.0.4
Release:       alt1
Summary:       Perform multipart-post requests using Faraday
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lostisland/faraday-multipart
Vcs:           https://github.com/lostisland/faraday-multipart.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 2.0 gem(bundler) < 3
BuildRequires: gem(faraday) >= 1.0
BuildRequires: gem(multipart-parser) >= 0
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(rubocop) >= 1.12.0 gem(rubocop) < 2
BuildRequires: gem(rubocop-packaging) >= 0.5.0 gem(rubocop-packaging) < 0.6
BuildRequires: gem(rubocop-performance) >= 1.0 gem(rubocop-performance) < 2
BuildRequires: gem(rubocop-rspec) >= 2.0 gem(rubocop-rspec) < 3
BuildRequires: gem(simplecov) >= 0.17 gem(simplecov) < 1
BuildRequires: gem(multipart-post) >= 2 gem(multipart-post) < 3
BuildRequires: gem(bundler) >= 2.0 gem(bundler) < 3
BuildRequires: gem(faraday) >= 1.0
BuildRequires: gem(multipart-parser) >= 0
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(rubocop) >= 1.12.0 gem(rubocop) < 2
BuildRequires: gem(rubocop-packaging) >= 0.5.0 gem(rubocop-packaging) < 0.6
BuildRequires: gem(rubocop-performance) >= 1.0 gem(rubocop-performance) < 2
BuildRequires: gem(rubocop-rspec) >= 2.0 gem(rubocop-rspec) < 3
BuildRequires: gem(simplecov) >= 0.17 gem(simplecov) < 1
BuildRequires: gem(multipart-post) >= 2 gem(multipart-post) < 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      gem(multipart-post) >= 2 gem(multipart-post) < 3
Provides:      gem(faraday-multipart) = 1.0.4


%description
Perform multipart-post requests using Faraday.


%package       -n gem-faraday-multipart-doc
Version:       1.0.4
Release:       alt1
Summary:       Perform multipart-post requests using Faraday documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета faraday-multipart
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(faraday-multipart) = 1.0.4

%description   -n gem-faraday-multipart-doc
Perform multipart-post requests using Faraday documentation files.

%description   -n gem-faraday-multipart-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета faraday-multipart.


%package       -n gem-faraday-multipart-devel
Version:       1.0.4
Release:       alt1
Summary:       Perform multipart-post requests using Faraday development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета faraday-multipart
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(faraday-multipart) = 1.0.4
Requires:      gem(bundler) >= 2.0 gem(bundler) < 3
Requires:      gem(faraday) >= 1.0
Requires:      gem(multipart-parser) >= 0
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(rubocop) >= 1.12.0 gem(rubocop) < 2
Requires:      gem(rubocop-packaging) >= 0.5.0 gem(rubocop-packaging) < 0.6
Requires:      gem(rubocop-performance) >= 1.0 gem(rubocop-performance) < 2
Requires:      gem(rubocop-rspec) >= 2.0 gem(rubocop-rspec) < 3
Requires:      gem(simplecov) >= 0.17 gem(simplecov) < 1

%description   -n gem-faraday-multipart-devel
Perform multipart-post requests using Faraday development package.

%description   -n gem-faraday-multipart-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета faraday-multipart.


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

%files         -n gem-faraday-multipart-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-faraday-multipart-devel
%doc README.md


%changelog
* Thu Dec 15 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.4-alt1
- + packaged gem with Ruby Policy 2.0
