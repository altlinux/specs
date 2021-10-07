%define        gemname rubocop-jekyll

Name:          gem-rubocop-jekyll
Version:       0.11.0
Release:       alt1
Summary:       Code style check for Jekyll and Jekyll plugins
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jekyll/rubocop-jekyll
Vcs:           https://github.com/jekyll/rubocop-jekyll.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rubocop) >= 0.68.0 gem(rubocop) < 2
BuildRequires: gem(rubocop-performance) >= 1.2 gem(rubocop-performance) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(rubocop) >= 0.68.0 gem(rubocop) < 2
Requires:      gem(rubocop-performance) >= 1.2 gem(rubocop-performance) < 2
Provides:      gem(rubocop-jekyll) = 0.11.0


%description
A RuboCop extension to enforce common code style in Jekyll and Jekyll plugins


%package       -n gem-rubocop-jekyll-doc
Version:       0.11.0
Release:       alt1
Summary:       Code style check for Jekyll and Jekyll plugins documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-jekyll
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-jekyll) = 0.11.0

%description   -n gem-rubocop-jekyll-doc
Code style check for Jekyll and Jekyll plugins documentation files.

A RuboCop extension to enforce common code style in Jekyll and Jekyll plugins

%description   -n gem-rubocop-jekyll-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-jekyll.


%package       -n gem-rubocop-jekyll-devel
Version:       0.11.0
Release:       alt1
Summary:       Code style check for Jekyll and Jekyll plugins development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-jekyll
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-jekyll) = 0.11.0

%description   -n gem-rubocop-jekyll-devel
Code style check for Jekyll and Jekyll plugins development package.

A RuboCop extension to enforce common code style in Jekyll and Jekyll plugins

%description   -n gem-rubocop-jekyll-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-jekyll.


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

%files         -n gem-rubocop-jekyll-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubocop-jekyll-devel
%doc README.md


%changelog
* Tue Sep 14 2021 Pavel Skrylev <majioa@altlinux.org> 0.11.0-alt1
- + packaged gem with Ruby Policy 2.0
