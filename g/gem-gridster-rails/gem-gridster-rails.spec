%define        gemname gridster-rails

Name:          gem-gridster-rails
Version:       0.5.6.1
Release:       alt1.2
Summary:       This gem provides jquery.gridster.js and jquery.gridster.css for your Rails 3+ application
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/vanetten/gridster-rails
Vcs:           https://github.com/vanetten/gridster-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(railties) >= 3.1.0
BuildConflicts: gem(railties) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency railties >= 6.1.3.2,railties < 7
%ruby_ignore_names rails
Requires:      gem(railties) >= 3.1.0
Conflicts:     gem(railties) >= 7
Provides:      gem(gridster-rails) = 0.5.6.1


%description
This is gridster.js GEMified for the Rails >= 3.1 asset pipeline. Gridster is a
jQuery plugin that makes building intuitive draggable layouts from elements
spanning multiple columns. You can even dynamically add and remove elements from
the grid.


%package       -n gem-gridster-rails-doc
Version:       0.5.6.1
Release:       alt1.2
Summary:       This gem provides jquery.gridster.js and jquery.gridster.css for your Rails 3+ application documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gridster-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gridster-rails) = 0.5.6.1

%description   -n gem-gridster-rails-doc
This gem provides jquery.gridster.js and jquery.gridster.css for your Rails 3+
application documentation files.

This is gridster.js GEMified for the Rails >= 3.1 asset pipeline. Gridster is a
jQuery plugin that makes building intuitive draggable layouts from elements
spanning multiple columns. You can even dynamically add and remove elements from
the grid.

%description   -n gem-gridster-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gridster-rails.


%package       -n gem-gridster-rails-devel
Version:       0.5.6.1
Release:       alt1.2
Summary:       This gem provides jquery.gridster.js and jquery.gridster.css for your Rails 3+ application development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gridster-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gridster-rails) = 0.5.6.1

%description   -n gem-gridster-rails-devel
This gem provides jquery.gridster.js and jquery.gridster.css for your Rails 3+
application development package.

This is gridster.js GEMified for the Rails >= 3.1 asset pipeline. Gridster is a
jQuery plugin that makes building intuitive draggable layouts from elements
spanning multiple columns. You can even dynamically add and remove elements from
the grid.

%description   -n gem-gridster-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gridster-rails.


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

%files         -n gem-gridster-rails-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-gridster-rails-devel
%doc README.md


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 0.5.6.1-alt1.2
- ! closes build deps under check condition

* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.6.1-alt1.1
- ! spec

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.6.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
