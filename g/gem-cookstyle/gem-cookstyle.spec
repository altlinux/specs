%define        gemname cookstyle

Name:          gem-cookstyle
Version:       7.32.1
Release:       alt1
Summary:       Cookstyle is a code linting tool that helps you to write better Chef Infra cookbooks by detecting and automatically correcting style, syntax, and logic mistakes in your code
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://docs.chef.io/workstation/cookstyle/
Vcs:           https://github.com/chef/cookstyle.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(pry) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(memory_profiler) >= 0
BuildRequires: gem(stackprof) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.4
BuildRequires: gem(rubocop) >= 1.15.0 gem(rubocop) < 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(rubocop) >= 1.15.0 gem(rubocop) < 2
Provides:      gem(cookstyle) = 7.32.1


%description
Cookstyle is a code linting tool that helps you to write better Chef Infra
cookbooks by detecting and automatically correcting style, syntax, and logic
mistakes in your code.


%package       -n cookstyle
Version:       7.32.1
Release:       alt1
Summary:       Cookstyle is a code linting tool that helps you to write better Chef Infra cookbooks by detecting and automatically correcting style, syntax, and logic mistakes in your code executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета cookstyle
Group:         Other
BuildArch:     noarch

Requires:      gem(cookstyle) = 7.32.1

%description   -n cookstyle
Cookstyle is a code linting tool that helps you to write better Chef Infra
cookbooks by detecting and automatically correcting style, syntax, and logic
mistakes in your code executable(s).

%description   -n cookstyle -l ru_RU.UTF-8
Исполнямка для самоцвета cookstyle.


%package       -n gem-cookstyle-doc
Version:       7.32.1
Release:       alt1
Summary:       Cookstyle is a code linting tool that helps you to write better Chef Infra cookbooks by detecting and automatically correcting style, syntax, and logic mistakes in your code documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cookstyle
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(cookstyle) = 7.32.1

%description   -n gem-cookstyle-doc
Cookstyle is a code linting tool that helps you to write better Chef Infra
cookbooks by detecting and automatically correcting style, syntax, and logic
mistakes in your code documentation files.

%description   -n gem-cookstyle-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cookstyle.


%package       -n gem-cookstyle-devel
Version:       7.32.1
Release:       alt1
Summary:       Cookstyle is a code linting tool that helps you to write better Chef Infra cookbooks by detecting and automatically correcting style, syntax, and logic mistakes in your code development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cookstyle
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(cookstyle) = 7.32.1
Requires:      gem(pry) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(memory_profiler) >= 0
Requires:      gem(stackprof) >= 0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.4

%description   -n gem-cookstyle-devel
Cookstyle is a code linting tool that helps you to write better Chef Infra
cookbooks by detecting and automatically correcting style, syntax, and logic
mistakes in your code development package.

%description   -n gem-cookstyle-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cookstyle.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n cookstyle
%_bindir/cookstyle

%files         -n gem-cookstyle-doc
%ruby_gemdocdir

%files         -n gem-cookstyle-devel


%changelog
* Sat Oct 29 2022 Pavel Skrylev <majioa@altlinux.org> 7.32.1-alt1
- + packaged gem with Ruby Policy 2.0
