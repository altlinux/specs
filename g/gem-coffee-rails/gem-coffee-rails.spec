%define        gemname coffee-rails

Name:          gem-coffee-rails
Version:       5.0.0.1
Release:       alt1
Summary:       CoffeeScript adapter for the Rails asset pipeline. Also adds support for .coffee views
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/coffee-rails
Vcs:           https://github.com/rails/coffee-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(coffee-script) >= 2.2.0
BuildRequires: gem(railties) >= 5.2.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(coffee-script) >= 2.2.0
Requires:      gem(railties) >= 5.2.0
Obsoletes:     ruby-coffee-rails < %EVR
Provides:      ruby-coffee-rails = %EVR
Provides:      gem(coffee-rails) = 5.0.0.1

%ruby_use_gem_version coffee-rails:5.0.0.1

%description
CoffeeScript adapter for the Rails asset pipeline. Also adds support to use
CoffeeScript to respond to JavaScript requests (use .coffee views).


%package       -n gem-coffee-rails-doc
Version:       5.0.0.1
Release:       alt1
Summary:       CoffeeScript adapter for the Rails asset pipeline. Also adds support for .coffee views documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета coffee-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(coffee-rails) = 5.0.0.1

%description   -n gem-coffee-rails-doc
CoffeeScript adapter for the Rails asset pipeline. Also adds support for .coffee
views documentation files.

CoffeeScript adapter for the Rails asset pipeline. Also adds support to use
CoffeeScript to respond to JavaScript requests (use .coffee views).

%description   -n gem-coffee-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета coffee-rails.


%package       -n gem-coffee-rails-devel
Version:       5.0.0.1
Release:       alt1
Summary:       CoffeeScript adapter for the Rails asset pipeline. Also adds support for .coffee views development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета coffee-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(coffee-rails) = 5.0.0.1

%description   -n gem-coffee-rails-devel
CoffeeScript adapter for the Rails asset pipeline. Also adds support for .coffee
views development package.

CoffeeScript adapter for the Rails asset pipeline. Also adds support to use
CoffeeScript to respond to JavaScript requests (use .coffee views).

%description   -n gem-coffee-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета coffee-rails.


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

%files         -n gem-coffee-rails-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-coffee-rails-devel
%doc README.md


%changelog
* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 5.0.0.1-alt1
- ^ 5.0.0 -> 5.0.0.1

* Wed Jun 10 2020 Pavel Skrylev <majioa@altlinux.org> 5.0.0-alt1
- ^ 4.2.2 -> 5.0.0
- ! spec name and syntax

* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.2-alt1
- Initial build for Sisyphus
