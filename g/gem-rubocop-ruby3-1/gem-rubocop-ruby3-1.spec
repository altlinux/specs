%define        gemname rubocop-ruby3_1

Name:          gem-rubocop-ruby3-1
Version:       1.0.6
Release:       alt1
Summary:       Semantically Versioned RuboCop Dependency
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubocop-lts/rubocop-ruby3_1
Vcs:           https://github.com/rubocop-lts/rubocop-ruby3_1/tree/v1.0.6.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rubocop) >= 1.15.0 gem(rubocop) < 2
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names rubocop-ruby3_1,rubocop-ruby3-1
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(rubocop) >= 1.15.0 gem(rubocop) < 2
Provides:      gem(rubocop-ruby3_1) = 1.0.6


%description
Links dependency on minimum Ruby version to maximum RuboCop version


%package       -n gem-rubocop-ruby3-1-doc
Version:       1.0.6
Release:       alt1
Summary:       Semantically Versioned RuboCop Dependency documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-ruby3_1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-ruby3_1) = 1.0.6

%description   -n gem-rubocop-ruby3-1-doc
Semantically Versioned RuboCop Dependency documentation files.

Links dependency on minimum Ruby version to maximum RuboCop version

%description   -n gem-rubocop-ruby3-1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-ruby3_1.


%package       -n gem-rubocop-ruby3-1-devel
Version:       1.0.6
Release:       alt1
Summary:       Semantically Versioned RuboCop Dependency development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-ruby3_1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-ruby3_1) = 1.0.6
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0

%description   -n gem-rubocop-ruby3-1-devel
Semantically Versioned RuboCop Dependency development package.

Links dependency on minimum Ruby version to maximum RuboCop version

%description   -n gem-rubocop-ruby3-1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-ruby3_1.


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

%files         -n gem-rubocop-ruby3-1-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubocop-ruby3-1-devel
%doc README.md


%changelog
* Thu Sep 29 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.6-alt1
- + packaged gem with Ruby Policy 2.0
