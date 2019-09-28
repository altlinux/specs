# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname sass-rails

Name:          ruby-%pkgname
Version:       5.1.0
Release:       alt1
Summary:       Ruby on Rails stylesheet engine for Sass
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/sass-rails
%vcs           
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
This gem provides official integration for Ruby on Rails projects with
the Sass stylesheet language.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --ignore=sass_project,scss_project,alternate_config_project,engine_project

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 5.1.0-alt1
- 5.0.7 -> 5.1.0
- update to Ruby Policy 2.0

* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.7-alt1.1
- Rebuild with new Ruby autorequirements.

* Sun Jul 08 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.7-alt1
- Initial build for Sisyphus
