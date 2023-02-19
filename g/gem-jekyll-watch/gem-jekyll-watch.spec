%define        gemname jekyll-watch

Name:          gem-jekyll-watch
Version:       2.2.1.8
Release:       alt0.1
Summary:       Rebuild your Jekyll site when a file changes with the `--watch` switch
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jekyll/jekyll-watch
Vcs:           https://github.com/jekyll/jekyll-watch.git
Packager:      Dmitriy Voropaev <voropaevdmtr@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(jekyll) >= 3.6
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop-jekyll) >= 0.11
BuildRequires: gem(listen) >= 3.0
BuildConflicts: gem(jekyll) >= 5.0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop-jekyll) >= 1
BuildConflicts: gem(listen) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(listen) >= 3.0
Conflicts:     gem(listen) >= 4
Provides:      gem(jekyll-watch) = 2.2.1.8

%ruby_use_gem_version jekyll-watch:2.2.1.8

%description
Rebuild your Jekyll site when a file changes with the `--watch` switch.


%package       -n gem-jekyll-watch-doc
Version:       2.2.1.8
Release:       alt0.1
Summary:       Rebuild your Jekyll site when a file changes with the `--watch` switch documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета jekyll-watch
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(jekyll-watch) = 2.2.1.8

%description   -n gem-jekyll-watch-doc
Rebuild your Jekyll site when a file changes with the `--watch` switch
documentation files.

%description   -n gem-jekyll-watch-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета jekyll-watch.


%package       -n gem-jekyll-watch-devel
Version:       2.2.1.8
Release:       alt0.1
Summary:       Rebuild your Jekyll site when a file changes with the `--watch` switch development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета jekyll-watch
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(jekyll-watch) = 2.2.1.8
Requires:      gem(bundler) >= 0
Requires:      gem(jekyll) >= 3.6
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop-jekyll) >= 0.11
Conflicts:     gem(jekyll) >= 5.0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop-jekyll) >= 1

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
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 2.2.1.8-alt0.1
- ^ 2.2.1 -> 2.2.1p8

* Tue Sep 14 2021 Pavel Skrylev <majioa@altlinux.org> 2.2.1-alt1.1
- ! spec

* Tue Mar 16 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 2.2.1-alt1
- initial build
