%define        gemname rubocop-minitest

Name:          gem-rubocop-minitest
Version:       0.13.0
Release:       alt1
Summary:       Automatic Minitest code style checking tool
License:       MIT
Group:         Development/Ruby
Url:           https://docs.rubocop.org/rubocop-minitest/
Vcs:           https://github.com/rubocop/rubocop-minitest.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rubocop) >= 0.90 gem(rubocop) < 2.0
BuildRequires: gem(minitest) >= 5.11 gem(minitest) < 6

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.13.0,rubocop < 2
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Requires:      gem(rubocop) >= 0.90 gem(rubocop) < 2.0
Provides:      gem(rubocop-minitest) = 0.13.0


%description
Automatic Minitest code style checking tool. A RuboCop extension focused on
enforcing Minitest best practices and coding conventions.


%package       -n gem-rubocop-minitest-doc
Version:       0.13.0
Release:       alt1
Summary:       Automatic Minitest code style checking tool documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-minitest
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-minitest) = 0.13.0

%description   -n gem-rubocop-minitest-doc
Automatic Minitest code style checking tool documentation files.

Automatic Minitest code style checking tool. A RuboCop extension focused on
enforcing Minitest best practices and coding conventions.

%description   -n gem-rubocop-minitest-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-minitest.


%package       -n gem-rubocop-minitest-devel
Version:       0.13.0
Release:       alt1
Summary:       Automatic Minitest code style checking tool development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-minitest
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-minitest) = 0.13.0
Requires:      gem(minitest) >= 5.11 gem(minitest) < 6

%description   -n gem-rubocop-minitest-devel
Automatic Minitest code style checking tool development package.

Automatic Minitest code style checking tool. A RuboCop extension focused on
enforcing Minitest best practices and coding conventions.

%description   -n gem-rubocop-minitest-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-minitest.


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

%files         -n gem-rubocop-minitest-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubocop-minitest-devel
%doc README.md


%changelog
* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 0.13.0-alt1
- + packaged gem with Ruby Policy 2.0
