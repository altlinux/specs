%define        gemname rubocop-lts

Name:          gem-rubocop-lts
Version:       22.0.1
Release:       alt1
Summary:       Rubocop LTS - Semantically Versioned
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubocop-lts/rubocop-lts
Vcs:           https://github.com/rubocop-lts/rubocop-lts/tree/v22.0.1.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rubocop-ruby3_1) >= 1.0.6 gem(rubocop-ruby3_1) < 1.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rubocop-ruby3_1) >= 1.0.6 gem(rubocop-ruby3_1) < 1.1
Provides:      gem(rubocop-lts) = 22.0.1


%description
Rubocop LTS - Chaos Reduction In a Bottle


%package       -n gem-rubocop-lts-doc
Version:       22.0.1
Release:       alt1
Summary:       Rubocop LTS - Semantically Versioned documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-lts
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-lts) = 22.0.1

%description   -n gem-rubocop-lts-doc
Rubocop LTS - Semantically Versioned documentation files.

Rubocop LTS - Chaos Reduction In a Bottle

%description   -n gem-rubocop-lts-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-lts.


%package       -n gem-rubocop-lts-devel
Version:       22.0.1
Release:       alt1
Summary:       Rubocop LTS - Semantically Versioned development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-lts
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-lts) = 22.0.1

%description   -n gem-rubocop-lts-devel
Rubocop LTS - Semantically Versioned development package.

Rubocop LTS - Chaos Reduction In a Bottle

%description   -n gem-rubocop-lts-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-lts.


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

%files         -n gem-rubocop-lts-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubocop-lts-devel
%doc README.md


%changelog
* Thu Sep 29 2022 Pavel Skrylev <majioa@altlinux.org> 22.0.1-alt1
- + packaged gem with Ruby Policy 2.0
