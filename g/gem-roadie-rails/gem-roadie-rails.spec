%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname roadie-rails

Name:          gem-roadie-rails
Version:       3.3.0
Release:       alt1
Summary:       Making HTML emails comfortable for the Rails rockstars
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/Mange/roadie-rails
Vcs:           https://github.com/mange/roadie-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 2.1.4
BuildRequires: gem(rails) >= 6.1.3.2
BuildRequires: gem(railties) >= 5.1
BuildRequires: gem(roadie) >= 5.0
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(rspec-collection_matchers) >= 0
BuildRequires: gem(rspec-rails) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-cobertura) >= 0
BuildRequires: gem(standard) >= 0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rails) >= 8.1
BuildConflicts: gem(railties) >= 8.1
BuildConflicts: gem(roadie) >= 6
BuildConflicts: gem(rspec) >= 4
%if_enabled check
BuildRequires: gem(bootsnap) >= 1.4.4
BuildRequires: gem(listen) >= 0
BuildRequires: gem(propshaft) >= 0
BuildRequires: gem(sass-rails) >= 6
BuildRequires: gem(sprockets-rails) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Requires:      ruby >= 2.7
Requires:      gem(railties) >= 5.1
Requires:      gem(roadie) >= 5.0
Conflicts:     gem(railties) >= 8.1
Conflicts:     gem(roadie) >= 6
Obsoletes:     ruby-roadie-rails < %EVR
Provides:      ruby-roadie-rails = %EVR
Provides:      roadie-rails = %EVR
Provides:      gem(roadie-rails) = 3.3.0

%description
This gem hooks up your Rails application with Roadie to help you generate HTML
emails.


%if_enabled    doc
%package       -n gem-roadie-rails-doc
Version:       3.3.0
Release:       alt1
Summary:       Making HTML emails comfortable for the Rails rockstars documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета roadie-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(roadie-rails) = 3.3.0

%description   -n gem-roadie-rails-doc
Making HTML emails comfortable for the Rails rockstars documentation files.

%description   -n gem-roadie-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета roadie-rails.
%endif


%if_enabled    devel
%package       -n gem-roadie-rails-devel
Version:       3.3.0
Release:       alt1
Summary:       Making HTML emails comfortable for the Rails rockstars development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета roadie-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(roadie-rails) = 3.3.0
Requires:      gem(bundler) >= 2.1.4
Requires:      gem(rails) >= 5.1
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(rspec-collection_matchers) >= 0
Requires:      gem(rspec-rails) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-cobertura) >= 0
Requires:      gem(standard) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rails) >= 8.1
Conflicts:     gem(rspec) >= 4

%description   -n gem-roadie-rails-devel
Making HTML emails comfortable for the Rails rockstars development package.

%description   -n gem-roadie-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета roadie-rails.
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
%doc Changelog.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-roadie-rails-doc
%doc Changelog.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-roadie-rails-devel
%doc Changelog.md LICENSE.txt README.md
%endif


%changelog
* Wed Jan 15 2025 Pavel Skrylev <majioa@altlinux.org> 3.3.0-alt1
- ^ 3.0.0 -> 3.3.0

* Mon Dec 19 2022 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- ^ 2.3.0 -> 3.0.0

* Sun Oct 09 2022 Pavel Skrylev <majioa@altlinux.org> 2.3.0-alt1
- ^ 2.2.0 -> 2.3.0

* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- ^ 2.1.1 -> 2.2.0

* Wed Mar 11 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt1
- ^ 2.1.0 -> 2.1.1
- ! spec

* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- > Ruby Policy 2.0
- ^ 1.3.0 -> 2.1.0

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- Initial gemified build for Sisyphus
