%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname memoist

Name:          gem-memoist
Version:       0.16.2.5
Release:       alt0.1
Summary:       ActiveSupport::Memoizable with a few enhancements
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/matthewrudy/memoist
Vcs:           https://github.com/matthewrudy/memoist.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(minitest) >= 5.10
BuildRequires: gem(rake) >= 0
BuildConflicts: gem(minitest) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 6.0,minitest < 7
Requires:      ruby >= 1.9.2
Obsoletes:     ruby-memoist < %EVR
Provides:      ruby-memoist = %EVR
Provides:      gem(memoist) = 0.16.2.5

%ruby_use_gem_version memoist:0.16.2.5

%description
Memoist is an extraction of ActiveSupport::Memoizable.

Since June 2011 ActiveSupport::Memoizable has been deprecated. But I love it,
and so I plan to keep it alive.


%if_enabled    doc
%package       -n gem-memoist-doc
Version:       0.16.2.5
Release:       alt0.1
Summary:       ActiveSupport::Memoizable with a few enhancements documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета memoist
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(memoist) = 0.16.2.5

%description   -n gem-memoist-doc
ActiveSupport::Memoizable with a few enhancements documentation files.

Memoist is an extraction of ActiveSupport::Memoizable.

Since June 2011 ActiveSupport::Memoizable has been deprecated. But I love it,
and so I plan to keep it alive.

%description   -n gem-memoist-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета memoist.
%endif


%if_enabled    devel
%package       -n gem-memoist-devel
Version:       0.16.2.5
Release:       alt0.1
Summary:       ActiveSupport::Memoizable with a few enhancements development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета memoist
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(memoist) = 0.16.2.5
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(minitest) >= 5.10
Requires:      gem(rake) >= 0
Conflicts:     gem(minitest) >= 7

%description   -n gem-memoist-devel
ActiveSupport::Memoizable with a few enhancements development package.

Memoist is an extraction of ActiveSupport::Memoizable.

Since June 2011 ActiveSupport::Memoizable has been deprecated. But I love it,
and so I plan to keep it alive.

%description   -n gem-memoist-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета memoist.
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
%doc CHANGELOG.md LICENSE.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-memoist-doc
%doc CHANGELOG.md LICENSE.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-memoist-devel
%doc CHANGELOG.md LICENSE.md README.md
%endif


%changelog
* Thu Aug 27 2026 Pavel Skrylev <majioa@altlinux.org> 0.16.2.5-alt0.1
- ^ 0.16.2 -> 0.16.2p5

* Wed Jun 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.16.2-alt1
- ^ 0.16.0 -> 0.16.2

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.16.0-alt1.1
- Rebuild for new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.16.0-alt1
- Initial build for Sisyphus
