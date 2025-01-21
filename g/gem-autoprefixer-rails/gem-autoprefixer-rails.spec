%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname autoprefixer-rails

Name:          gem-autoprefixer-rails
Version:       10.4.19.0
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
BuildRequires: gem(execjs) >= 2
BuildRequires: gem(rails) >= 5.0.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(sassc-rails) >= 0
BuildRequires: gem(sprockets) >= 4.0.0
BuildRequires: gem(standard) >= 0
BuildConflicts: gem(execjs) >= 3
%if_enabled check
BuildRequires: gem(mini_racer) >= 0
BuildRequires: gem(rspec-rails) >= 0
BuildRequires: gem(rubocop) >= 0.85.1
BuildRequires: gem(rubocop-packaging) >= 0.1.1
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-packaging) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-packaging >= 0.5.2,rubocop-packaging < 1
Requires:      ruby >= 2.4
Requires:      gem(execjs) >= 2
Conflicts:     gem(execjs) >= 3
Provides:      autoprefixer-rails = %EVR
Provides:      gem(autoprefixer-rails) = 10.4.19.0

%description
Autoprefixer is a tool to parse CSS and add vendor prefixes to CSS rules using
values from the Can I Use database. This gem provides Ruby and Ruby on Rails
integration with this JavaScript tool.


%if_enabled    doc
%package       -n gem-autoprefixer-rails-doc
Version:       10.4.19.0
Release:       alt1
Summary:       Autoprefixer for Ruby and Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета autoprefixer-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(autoprefixer-rails) = 10.4.19.0

%description   -n gem-autoprefixer-rails-doc
Autoprefixer for Ruby and Ruby on Rails documentation files.

Autoprefixer is a tool to parse CSS and add vendor prefixes to CSS rules using
values from the Can I Use database. This gem provides Ruby and Ruby on Rails
integration with this JavaScript tool.

%description   -n gem-autoprefixer-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета autoprefixer-rails.
%endif


%if_enabled    devel
%package       -n gem-autoprefixer-rails-devel
Version:       10.4.19.0
Release:       alt1
Summary:       Autoprefixer for Ruby and Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета autoprefixer-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(autoprefixer-rails) = 10.4.19.0
Requires:      gem(mini_racer) >= 0
Requires:      gem(rails) >= 5.0.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec-rails) >= 0
Requires:      gem(rubocop) >= 0.85.1
Requires:      gem(rubocop-packaging) >= 0.1.1
Requires:      gem(sassc-rails) >= 0
Requires:      gem(sprockets) >= 4.0.0
Requires:      gem(standard) >= 0
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-packaging) >= 1

%description   -n gem-autoprefixer-rails-devel
Autoprefixer for Ruby and Ruby on Rails development package.

Autoprefixer is a tool to parse CSS and add vendor prefixes to CSS rules using
values from the Can I Use database. This gem provides Ruby and Ruby on Rails
integration with this JavaScript tool.

%description   -n gem-autoprefixer-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета autoprefixer-rails.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-autoprefixer-rails-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-autoprefixer-rails-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Mon Jan 20 2025 Pavel Skrylev <majioa@altlinux.org> 10.4.19.0-alt1
- ^ 10.4.7.0 -> 10.4.19.0

* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 10.4.7.0-alt1
- ^ 10.3.1.0 -> 10.4.7.0

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 10.3.1.0-alt1
- ^ 9.6.0 -> 10.3.1.0

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 9.6.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
