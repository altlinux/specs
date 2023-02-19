%define        gemname slim-rails

Name:          gem-slim-rails
Version:       3.5.1
Release:       alt1
Summary:       Slim templates generator for Rails
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/slim-template/slim-rails
Vcs:           https://github.com/slim-template/slim-rails.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(sprockets-rails) >= 0
BuildRequires: gem(slim_lint) >= 0.21.0
BuildRequires: gem(rocco) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(awesome_print) >= 0
BuildRequires: gem(actionmailer) >= 3.1
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(standardrb) >= 0
BuildRequires: gem(actionpack) >= 3.1
BuildRequires: gem(railties) >= 3.1
BuildRequires: gem(slim) >= 3.0
BuildConflicts: gem(slim_lint) >= 1
BuildConflicts: gem(slim) >= 5.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency slim_lint >= 0.22.1,slim_lint < 1
Requires:      gem(actionpack) >= 3.1
Requires:      gem(railties) >= 3.1
Requires:      gem(slim) >= 3.0
Conflicts:     gem(slim) >= 5.0
Provides:      gem(slim-rails) = 3.5.1


%description
Provides the generator settings required for Rails to use Slim


%package       -n gem-slim-rails-doc
Version:       3.5.1
Release:       alt1
Summary:       Slim templates generator for Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета slim-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(slim-rails) = 3.5.1

%description   -n gem-slim-rails-doc
Slim templates generator for Rails documentation files.

Provides the generator settings required for Rails to use Slim

%description   -n gem-slim-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета slim-rails.


%package       -n gem-slim-rails-devel
Version:       3.5.1
Release:       alt1
Summary:       Slim templates generator for Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета slim-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(slim-rails) = 3.5.1
Requires:      gem(sprockets-rails) >= 0
Requires:      gem(slim_lint) >= 0.21.0
Requires:      gem(rocco) >= 0
Requires:      gem(redcarpet) >= 0
Requires:      gem(awesome_print) >= 0
Requires:      gem(actionmailer) >= 3.1
Requires:      gem(appraisal) >= 0
Requires:      gem(standardrb) >= 0
Conflicts:     gem(slim_lint) >= 1

%description   -n gem-slim-rails-devel
Slim templates generator for Rails development package.

Provides the generator settings required for Rails to use Slim

%description   -n gem-slim-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета slim-rails.


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

%files         -n gem-slim-rails-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-slim-rails-devel
%doc README.md


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt1
- ^ 3.3.0 -> 3.5.1

* Sun Sep 12 2021 Pavel Skrylev <majioa@altlinux.org> 3.3.0-alt1
- + packaged gem with Ruby Policy 2.0
