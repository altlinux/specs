%define        gemname jekyll-watch

Name:          gem-jekyll-watch
Version:       2.2.1
Release:       alt1.1
Summary:       Rebuild your Jekyll site when a file changes with the `--watch` switch
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jekyll/jekyll-watch
Vcs:           https://github.com/jekyll/jekyll-watch.git
Packager:      Dmitriy Voropaev <voropaevdmtr@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(listen) >= 3.0 gem(listen) < 4
BuildRequires: gem(bundler) >= 0 gem(bundler) < 3
BuildRequires: gem(jekyll) >= 3.6 gem(jekyll) < 5.0
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(rubocop-jekyll) >= 0.5 gem(rubocop-jekyll) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Requires:      gem(listen) >= 3.0 gem(listen) < 4
Provides:      gem(jekyll-watch) = 2.2.1


%description
Rebuild your Jekyll site when a file changes with the `--watch` switch.


%package       -n gem-jekyll-watch-doc
Version:       2.2.1
Release:       alt1.1
Summary:       Rebuild your Jekyll site when a file changes with the `--watch` switch documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета jekyll-watch
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(jekyll-watch) = 2.2.1

%description   -n gem-jekyll-watch-doc
Rebuild your Jekyll site when a file changes with the `--watch` switch
documentation files.

%description   -n gem-jekyll-watch-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета jekyll-watch.


%package       -n gem-jekyll-watch-devel
Version:       2.2.1
Release:       alt1.1
Summary:       Rebuild your Jekyll site when a file changes with the `--watch` switch development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета jekyll-watch
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(jekyll-watch) = 2.2.1
Requires:      gem(bundler) >= 0 gem(bundler) < 3
Requires:      gem(jekyll) >= 3.6 gem(jekyll) < 5.0
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(rubocop-jekyll) >= 0.5 gem(rubocop-jekyll) < 1

%description   -n gem-jekyll-watch-devel
Rebuild your Jekyll site when a file changes with the `--watch` switch
development package.

%description   -n gem-jekyll-watch-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета jekyll-watch.


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

%files         -n gem-jekyll-watch-doc
%ruby_gemdocdir

%files         -n gem-jekyll-watch-devel


%changelog
* Tue Sep 14 2021 Pavel Skrylev <majioa@altlinux.org> 2.2.1-alt1.1
- ! spec

* Tue Mar 16 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 2.2.1-alt1
- initial build
