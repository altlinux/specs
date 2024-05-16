%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname mini_magick

Name:          gem-mini-magick
Version:       4.12.0
Release:       alt1
Summary:       mini replacement for RMagick
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mini-magick/mini-magick
Vcs:           https://github.com/mini-magick/mini-magick.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.5.0
BuildRequires: gem(guard) >= 0
BuildRequires: gem(guard-rspec) >= 0
BuildRequires: gem(posix-spawn) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(pry) >= 0
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_alias_names mini_magick,mini-magick
Requires:      ImageMagick-tools
Obsoletes:     ruby-minimagick < %EVR
Provides:      ruby-minimagick = %EVR
Provides:      gem(mini_magick) = 4.12.0


%description
Using MiniMagick the ruby processes memory remains small (it spawns
ImageMagick's command line program mogrify which takes up some memory as well,
but is much smaller compared to RMagick).


%if_enabled    doc
%package       -n gem-mini-magick-doc
Version:       4.12.0
Release:       alt1
Summary:       mini replacement for RMagick documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mini_magick
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mini_magick) = 4.12.0

%description   -n gem-mini-magick-doc
mini replacement for RMagick documentation files.

Using MiniMagick the ruby processes memory remains small (it spawns
ImageMagick's command line program mogrify which takes up some memory as well,
but is much smaller compared to RMagick).

%description   -n gem-mini-magick-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mini_magick.
%endif


%if_enabled    devel
%package       -n gem-mini-magick-devel
Version:       4.12.0
Release:       alt1
Summary:       mini replacement for RMagick development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mini_magick
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mini_magick) = 4.12.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.5.0
Requires:      gem(guard) >= 0
Requires:      gem(guard-rspec) >= 0
Requires:      gem(posix-spawn) >= 0
Requires:      gem(webmock) >= 0
Requires:      gem(pry) >= 0
Conflicts:     gem(rspec) >= 4

%description   -n gem-mini-magick-devel
mini replacement for RMagick development package.

Using MiniMagick the ruby processes memory remains small (it spawns
ImageMagick's command line program mogrify which takes up some memory as well,
but is much smaller compared to RMagick).

%description   -n gem-mini-magick-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mini_magick.
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
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-mini-magick-doc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-mini-magick-devel
%endif


%changelog
* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 4.12.0-alt1
- > Ruby Policy 2.0
- ^ 4.9.2 -> 4.12.0

* Tue Sep 25 2018 Andrey Cherepanov <cas@altlinux.org> 4.9.2-alt1
- New version.

* Fri Sep 21 2018 Andrey Cherepanov <cas@altlinux.org> 4.9.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 4.8.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 4.8.0-alt1
- Initial build for Sisyphus
