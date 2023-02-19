# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname webpack-rails

Name:          gem-webpack-rails
Version:       0.9.11
Release:       alt1.2
Summary:       Integrate webpack with your Ruby on Rails application
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mipearson/webpack-rails
Vcs:           https://github.com/mipearson/webpack-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rails) >= 3.2.0
BuildRequires: gem(railties) >= 3.2.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(railties) >= 3.2.0
Obsoletes:     ruby-webpack-rails < %EVR
Provides:      ruby-webpack-rails = %EVR
Provides:      gem(webpack-rails) = 0.9.11


%description
Integrate webpack with your Ruby on Rails application.


%package       -n gem-webpack-rails-doc
Version:       0.9.11
Release:       alt1.2
Summary:       Integrate webpack with your Ruby on Rails application documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета webpack-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(webpack-rails) = 0.9.11

%description   -n gem-webpack-rails-doc
Integrate webpack with your Ruby on Rails application documentation files.

%description   -n gem-webpack-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета webpack-rails.


%package       -n gem-webpack-rails-devel
Version:       0.9.11
Release:       alt1.2
Summary:       Integrate webpack with your Ruby on Rails application development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета webpack-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(webpack-rails) = 0.9.11
Requires:      gem(rspec) >= 0
Requires:      gem(webmock) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rails) >= 3.2.0

%description   -n gem-webpack-rails-devel
Integrate webpack with your Ruby on Rails application development package.

%description   -n gem-webpack-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета webpack-rails.


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

%files         -n gem-webpack-rails-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-webpack-rails-devel
%doc README.md


%changelog
* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 0.9.11-alt1.2
- ! deps for spec

* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 0.9.11-alt1.1
- ! spec obsoletes/provides reqs

* Wed Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.11-alt1
- + packaged gem with usage Ruby Policy 2.0
