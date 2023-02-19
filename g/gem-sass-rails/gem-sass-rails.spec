%define        gemname sass-rails

Name:          gem-sass-rails
Version:       6.0.0.1
Release:       alt1.1
Summary:       Ruby on Rails stylesheet engine for Sass
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/sass-rails
Vcs:           https://github.com/rails/sass-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(sassc-rails) >= 2.1.1
BuildConflicts: gem(sassc-rails) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(sassc-rails) >= 2.1.1
Conflicts:     gem(sassc-rails) >= 3
Obsoletes:     ruby-sass-rails < %EVR
Provides:      ruby-sass-rails = %EVR
Provides:      gem(sass-rails) = 6.0.0.1

%ruby_use_gem_version sass-rails:6.0.0.1

%description
This gem provides official integration for Ruby on Rails projects with the Sass
stylesheet language.


%package       -n gem-sass-rails-doc
Version:       6.0.0.1
Release:       alt1.1
Summary:       Ruby on Rails stylesheet engine for Sass documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sass-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sass-rails) = 6.0.0.1

%description   -n gem-sass-rails-doc
Ruby on Rails stylesheet engine for Sass documentation files.

This gem provides official integration for Ruby on Rails projects with the Sass
stylesheet language.

%description   -n gem-sass-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sass-rails.


%package       -n gem-sass-rails-devel
Version:       6.0.0.1
Release:       alt1.1
Summary:       Ruby on Rails stylesheet engine for Sass development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sass-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sass-rails) = 6.0.0.1

%description   -n gem-sass-rails-devel
Ruby on Rails stylesheet engine for Sass development package.

This gem provides official integration for Ruby on Rails projects with the Sass
stylesheet language.

%description   -n gem-sass-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sass-rails.


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

%files         -n gem-sass-rails-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-sass-rails-devel
%doc README.md


%changelog
* Wed Jan 25 2023 Pavel Skrylev <majioa@altlinux.org> 6.0.0.1-alt1.1
- ! deps in spec

* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 6.0.0.1-alt1
- ^ 6.0.0 -> 6.0.0.1

* Wed Jun 10 2020 Pavel Skrylev <majioa@altlinux.org> 6.0.0-alt1
- ^ 5.1.0 -> 6.0.0
- ! spec name and syntax

* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 5.1.0-alt1
- 5.0.7 -> 5.1.0
- update to Ruby Policy 2.0

* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.7-alt1.1
- Rebuild with new Ruby autorequirements.

* Sun Jul 08 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.7-alt1
- Initial build for Sisyphus
