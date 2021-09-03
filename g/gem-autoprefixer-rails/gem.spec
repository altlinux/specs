%define        gemname autoprefixer-rails

Name:          gem-autoprefixer-rails
Version:       10.3.1.0
Release:       alt1
Summary:       Autoprefixer for Ruby and Ruby on Rails
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ai/autoprefixer-rails
Vcs:           https://github.com/ai/autoprefixer-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(execjs) >= 2 gem(execjs) < 3
BuildRequires: gem(rails) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec-rails) >= 0
BuildRequires: gem(rubocop) >= 0.85.1 gem(rubocop) < 2
BuildRequires: gem(rubocop-packaging) >= 0.1.1 gem(rubocop-packaging) < 1
BuildRequires: gem(standard) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-packaging >= 0.5.1,rubocop-packaging < 1
Requires:      gem(execjs) >= 2 gem(execjs) < 3
Provides:      gem(autoprefixer-rails) = 10.3.1.0


%description
Autoprefixer is a tool to parse CSS and add vendor prefixes to CSS rules using
values from the Can I Use database. This gem provides Ruby and Ruby on Rails
integration with this JavaScript tool.


%package       -n gem-autoprefixer-rails-doc
Version:       10.3.1.0
Release:       alt1
Summary:       Autoprefixer for Ruby and Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета autoprefixer-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(autoprefixer-rails) = 10.3.1.0

%description   -n gem-autoprefixer-rails-doc
Autoprefixer for Ruby and Ruby on Rails documentation files.

Autoprefixer is a tool to parse CSS and add vendor prefixes to CSS rules using
values from the Can I Use database. This gem provides Ruby and Ruby on Rails
integration with this JavaScript tool.

%description   -n gem-autoprefixer-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета autoprefixer-rails.


%package       -n gem-autoprefixer-rails-devel
Version:       10.3.1.0
Release:       alt1
Summary:       Autoprefixer for Ruby and Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета autoprefixer-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(autoprefixer-rails) = 10.3.1.0
Requires:      gem(rails) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec-rails) >= 0
Requires:      gem(rubocop) >= 0.85.1 gem(rubocop) < 2
Requires:      gem(rubocop-packaging) >= 0.1.1 gem(rubocop-packaging) < 1
Requires:      gem(standard) >= 0

%description   -n gem-autoprefixer-rails-devel
Autoprefixer for Ruby and Ruby on Rails development package.

Autoprefixer is a tool to parse CSS and add vendor prefixes to CSS rules using
values from the Can I Use database. This gem provides Ruby and Ruby on Rails
integration with this JavaScript tool.

%description   -n gem-autoprefixer-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета autoprefixer-rails.


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

%files         -n gem-autoprefixer-rails-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-autoprefixer-rails-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 10.3.1.0-alt1
- ^ 9.6.0 -> 10.3.1.0

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 9.6.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
