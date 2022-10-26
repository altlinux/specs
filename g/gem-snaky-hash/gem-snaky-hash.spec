%define        gemname snaky_hash

Name:          gem-snaky-hash
Version:       2.0.1
Release:       alt1
Summary:       A very snaky hash
License:       MIT
Group:         Development/Ruby
Url:           https://gitlab.com/oauth-xx/snaky_hash
Vcs:           https://gitlab.com/oauth-xx/snaky_hash/-/tree/v2.0.1.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(hashie) >= 0
BuildRequires: gem(version_gem) >= 1.1.1 gem(version_gem) < 2
BuildRequires: gem(rake) >= 12
BuildRequires: gem(rspec) >= 3
BuildRequires: gem(rspec-block_is_expected) >= 0
BuildRequires: gem(rubocop-lts) >= 8.0 gem(rubocop-lts) < 23
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop-lts >= 22.0.1,rubocop-lts < 23
Requires:      gem(hashie) >= 0
Requires:      gem(version_gem) >= 1.1.1 gem(version_gem) < 2
Provides:      gem(snaky_hash) = 2.0.1


%description
A Hashie::Mash joint to make #snakelife better


%package       -n gem-snaky-hash-doc
Version:       2.0.1
Release:       alt1
Summary:       A very snaky hash documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета snaky_hash
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(snaky_hash) = 2.0.1

%description   -n gem-snaky-hash-doc
A very snaky hash documentation files.

A Hashie::Mash joint to make #snakelife better

%description   -n gem-snaky-hash-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета snaky_hash.


%package       -n gem-snaky-hash-devel
Version:       2.0.1
Release:       alt1
Summary:       A very snaky hash development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета snaky_hash
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(snaky_hash) = 2.0.1
Requires:      gem(rake) >= 12
Requires:      gem(rspec) >= 3
Requires:      gem(rspec-block_is_expected) >= 0
Requires:      gem(rubocop-lts) >= 8.0 gem(rubocop-lts) < 23

%description   -n gem-snaky-hash-devel
A very snaky hash development package.

A Hashie::Mash joint to make #snakelife better

%description   -n gem-snaky-hash-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета snaky_hash.


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

%files         -n gem-snaky-hash-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-snaky-hash-devel
%doc README.md


%changelog
* Thu Sep 29 2022 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt1
- + packaged gem with Ruby Policy 2.0
