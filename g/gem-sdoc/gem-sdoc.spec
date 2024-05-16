%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname sdoc

Name:          gem-sdoc
Version:       3.0.0
Release:       alt0.0.1
Summary:       rdoc html with javascript search index
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/zzak/sdoc
Vcs:           https://github.com/zzak/sdoc.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rdoc) >= 5.0
BuildRequires: gem(rack) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(hoe) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(importmap-rails) >= 0
BuildRequires: gem(railties) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rdoc) >= 5.0
Provides:      gem(sdoc) = 3.0.0

%ruby_use_gem_version sdoc:3.0.0

%description
SDoc is an HTML template built on top of the RDoc documentation generator for
Ruby code.


%package       -n sdoc
Version:       3.0.0
Release:       alt0.0.1
Summary:       rdoc html with javascript search index executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета sdoc
Group:         Other
BuildArch:     noarch

Requires:      gem(sdoc) = 3.0.0

%description   -n sdoc
rdoc html with javascript search index executable(s).

SDoc is an HTML template built on top of the RDoc documentation generator for
Ruby code.

%description   -n sdoc -l ru_RU.UTF-8
Исполнямка для самоцвета sdoc.


%if_enabled    doc
%package       -n gem-sdoc-doc
Version:       3.0.0
Release:       alt0.0.1
Summary:       rdoc html with javascript search index documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sdoc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sdoc) = 3.0.0
Obsoletes:     sdoc-doc < %EVR
Provides:      sdoc-doc = %EVR

%description   -n gem-sdoc-doc
rdoc html with javascript search index documentation files.

SDoc is an HTML template built on top of the RDoc documentation generator for
Ruby code.

%description   -n gem-sdoc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sdoc.
%endif


%if_enabled    devel
%package       -n gem-sdoc-devel
Version:       3.0.0
Release:       alt0.0.1
Summary:       rdoc html with javascript search index development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sdoc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sdoc) = 3.0.0
Requires:      gem(rack) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(hoe) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(importmap-rails) >= 0
Requires:      gem(railties) >= 0

%description   -n gem-sdoc-devel
rdoc html with javascript search index development package.

SDoc is an HTML template built on top of the RDoc documentation generator for
Ruby code.

%description   -n gem-sdoc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sdoc.
%endif


%prep
%setup
%autopatch

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

%files         -n sdoc
%doc CHANGELOG.md LICENSE README.md
%_bindir/sdoc

%if_enabled    doc
%files         -n gem-sdoc-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-sdoc-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Sun Apr 14 2024 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt0.0.1
- ^ 2.2.0 -> 3.0.0.alpha

* Tue Jun 29 2021 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1.1
- ! spec

* Tue Jun 15 2021 Andrey Cherepanov <cas@altlinux.org> 2.2.0-alt1
- New version.

* Tue Jan 26 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.3-alt1
- New version.

* Mon Mar 30 2020 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version.

* Thu Jul 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
