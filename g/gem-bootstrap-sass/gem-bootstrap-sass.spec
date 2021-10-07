%define        gemname bootstrap-sass

Name:          gem-bootstrap-sass
Version:       3.4.1
Release:       alt1.1
Summary:       Official Sass port of Bootstrap 2 and 3
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/twbs/bootstrap-sass
Vcs:           https://github.com/twbs/bootstrap-sass.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(sassc) >= 2.0.0
BuildRequires: gem(autoprefixer-rails) >= 5.2.1
BuildRequires: gem(minitest) >= 5.11 gem(minitest) < 6
BuildRequires: gem(minitest-reporters) >= 1.3 gem(minitest-reporters) < 2
BuildRequires: gem(capybara) >= 3.6 gem(capybara) < 4
BuildRequires: gem(poltergeist) >= 0
BuildRequires: gem(sassc-rails) >= 2.0.0
BuildRequires: gem(actionpack) >= 4.1.5
BuildRequires: gem(activesupport) >= 4.1.5 gem(activesupport) < 7
BuildRequires: gem(json) >= 1.8.1 gem(json) < 3
BuildRequires: gem(sprockets-rails) >= 2.1.3
BuildRequires: gem(jquery-rails) >= 3.1.0
BuildRequires: gem(slim-rails) >= 0
BuildRequires: gem(uglifier) >= 0
BuildRequires: gem(term-ansicolor) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency activesupport >= 6.1.3.2,activesupport < 7
%ruby_use_gem_dependency json >= 2.3.0,json < 3
%ruby_ignore_names dummy_sass_only,dummy_sass
Requires:      gem(sassc) >= 2.0.0
Requires:      gem(autoprefixer-rails) >= 5.2.1
Provides:      gem(bootstrap-sass) = 3.4.1


%description
bootstrap-sass is a Sass-powered version of Bootstrap 3, ready to drop right
into your Sass powered applications.

This is Bootstrap 3. For Bootstrap 4 use the Bootstrap rubygem if you use Ruby,
and the main repo otherwise.


%package       -n gem-bootstrap-sass-doc
Version:       3.4.1
Release:       alt1.1
Summary:       Official Sass port of Bootstrap 2 and 3 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bootstrap-sass
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bootstrap-sass) = 3.4.1

%description   -n gem-bootstrap-sass-doc
Official Sass port of Bootstrap 2 and 3 documentation files.

bootstrap-sass is a Sass-powered version of Bootstrap 3, ready to drop right
into your Sass powered applications.

This is Bootstrap 3. For Bootstrap 4 use the Bootstrap rubygem if you use Ruby,
and the main repo otherwise.

%description   -n gem-bootstrap-sass-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bootstrap-sass.


%package       -n gem-bootstrap-sass-devel
Version:       3.4.1
Release:       alt1.1
Summary:       Official Sass port of Bootstrap 2 and 3 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bootstrap-sass
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bootstrap-sass) = 3.4.1
Requires:      gem(minitest) >= 5.11 gem(minitest) < 6
Requires:      gem(minitest-reporters) >= 1.3 gem(minitest-reporters) < 2
Requires:      gem(capybara) >= 3.6 gem(capybara) < 4
Requires:      gem(poltergeist) >= 0
Requires:      gem(sassc-rails) >= 2.0.0
Requires:      gem(actionpack) >= 4.1.5
Requires:      gem(activesupport) >= 4.1.5 gem(activesupport) < 7
Requires:      gem(json) >= 1.8.1 gem(json) < 3
Requires:      gem(sprockets-rails) >= 2.1.3
Requires:      gem(jquery-rails) >= 3.1.0
Requires:      gem(slim-rails) >= 0
Requires:      gem(uglifier) >= 0
Requires:      gem(term-ansicolor) >= 0

%description   -n gem-bootstrap-sass-devel
Official Sass port of Bootstrap 2 and 3 development package.

bootstrap-sass is a Sass-powered version of Bootstrap 3, ready to drop right
into your Sass powered applications.

This is Bootstrap 3. For Bootstrap 4 use the Bootstrap rubygem if you use Ruby,
and the main repo otherwise.

%description   -n gem-bootstrap-sass-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bootstrap-sass.


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

%files         -n gem-bootstrap-sass-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-bootstrap-sass-devel
%doc README.md


%changelog
* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 3.4.1-alt1.1
- ! spec

* Tue Jul 23 2019 Pavel Skrylev <majioa@altlinux.org> 3.4.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
