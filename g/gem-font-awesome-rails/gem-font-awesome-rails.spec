%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname font-awesome-rails

Name:          gem-font-awesome-rails
Version:       4.7.0.8
Release:       alt1
Summary:       the font-awesome font bundled as an asset for the rails asset pipeline
License:       MIT or SIL Open Font License
Group:         Development/Ruby
Url:           https://github.com/bokmann/font-awesome-rails
Vcs:           https://github.com/bokmann/font-awesome-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(sassc-rails) >= 0
BuildRequires: gem(guard) >= 2.9
BuildRequires: gem(guard-minitest) >= 0
BuildRequires: gem(railties) >= 3.2
BuildConflicts: gem(railties) >= 8.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(railties) >= 3.2
Conflicts:     gem(railties) >= 8.0
Obsoletes:     ruby-font-awesome-rails < %EVR
Provides:      ruby-font-awesome-rails = %EVR
Provides:      gem(font-awesome-rails) = 4.7.0.8


%description
the font-awesome font bundled as an asset for the rails asset pipeline


%if_enabled    doc
%package       -n gem-font-awesome-rails-doc
Version:       4.7.0.8
Release:       alt1
Summary:       the font-awesome font bundled as an asset for the rails asset pipeline documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета font-awesome-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(font-awesome-rails) = 4.7.0.8

%description   -n gem-font-awesome-rails-doc
the font-awesome font bundled as an asset for the rails asset pipeline
documentation files.

%description   -n gem-font-awesome-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета font-awesome-rails.
%endif


%if_enabled    devel
%package       -n gem-font-awesome-rails-devel
Version:       4.7.0.8
Release:       alt1
Summary:       the font-awesome font bundled as an asset for the rails asset pipeline development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета font-awesome-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(font-awesome-rails) = 4.7.0.8
Requires:      gem(activesupport) >= 0
Requires:      gem(sassc-rails) >= 0
Requires:      gem(guard) >= 2.9
Requires:      gem(guard-minitest) >= 0

%description   -n gem-font-awesome-rails-devel
the font-awesome font bundled as an asset for the rails asset pipeline
development package.

%description   -n gem-font-awesome-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета font-awesome-rails.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-font-awesome-rails-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-font-awesome-rails-devel
%doc README.md
%endif


%changelog
* Thu Oct 17 2024 Pavel Skrylev <majioa@altlinux.org> 4.7.0.8-alt1
- ^ 4.7.0.5 -> 4.7.0.8

* Thu Dec 17 2020 Pavel Skrylev <majioa@altlinux.org> 4.7.0.5-alt1
- new version 4.7.0.5

* Mon Feb 04 2019 Mikhail Gordeev <obirvalger@altlinux.org> 4.7.0.4-alt1
- Initial build for Sisyphus
