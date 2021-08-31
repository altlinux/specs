%define        gemname sdoc

Name:          gem-sdoc
Version:       2.2.0
Release:       alt1.1
Summary:       rdoc generator html with javascript search index
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/zzak/sdoc
Vcs:           https://github.com/zzak/sdoc.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rdoc) >= 5.0 gem(rdoc) < 7
BuildRequires: gem(rack) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
Requires:      gem(rdoc) >= 5.0 gem(rdoc) < 7
Provides:      gem(sdoc) = 2.2.0


%description
SDoc is an HTML template built on top of the RDoc documentation generator for
Ruby code.


%package       -n sdoc
Version:       2.2.0
Release:       alt1.1
Summary:       rdoc generator html with javascript search index executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета sdoc
Group:         Other
BuildArch:     noarch

Requires:      gem(sdoc) = 2.2.0

%description   -n sdoc
rdoc generator html with javascript search index executable(s).

SDoc is an HTML template built on top of the RDoc documentation generator for
Ruby code.

%description   -n sdoc -l ru_RU.UTF-8
Исполнямка для самоцвета sdoc.


%package       -n gem-sdoc-doc
Version:       2.2.0
Release:       alt1.1
Summary:       rdoc generator html with javascript search index documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sdoc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sdoc) = 2.2.0
Obsoletes:     sdoc-doc
Provides:      sdoc-doc

%description   -n gem-sdoc-doc
rdoc generator html with javascript search index documentation files.

SDoc is an HTML template built on top of the RDoc documentation generator for
Ruby code.

%description   -n gem-sdoc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sdoc.


%package       -n gem-sdoc-devel
Version:       2.2.0
Release:       alt1.1
Summary:       rdoc generator html with javascript search index development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sdoc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sdoc) = 2.2.0
Requires:      gem(rack) >= 0

%description   -n gem-sdoc-devel
rdoc generator html with javascript search index development package.

SDoc is an HTML template built on top of the RDoc documentation generator for
Ruby code.

%description   -n gem-sdoc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sdoc.


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

%files         -n sdoc
%doc README.md
%_bindir/sdoc
%_bindir/sdoc-merge

%files         -n gem-sdoc-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-sdoc-devel
%doc README.md


%changelog
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
