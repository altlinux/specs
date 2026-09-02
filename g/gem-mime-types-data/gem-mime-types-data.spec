%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname mime-types-data

Name:          gem-mime-types-data
Version:       3.2026.0701
Release:       alt1
Summary:       MIME Type registry data
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mime-types/mime-types-data
Vcs:           https://github.com/mime-types/mime-types-data.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(hoe) >= 4.0
BuildRequires: gem(hoe-halostatue) >= 3.0
BuildRequires: gem(nokogiri) >= 1.6
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(standard) >= 1.0
BuildConflicts: gem(hoe) >= 5
BuildConflicts: gem(hoe-halostatue) >= 4
BuildConflicts: gem(mime-types) >= 4
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(standard) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mime-types >= 3.5.2,mime-types < 4
Requires:      ruby >= 2.0
Obsoletes:     ruby-mime-types-data < %EVR
Provides:      ruby-mime-types-data = %EVR
Provides:      mime-types-data = %EVR
Provides:      gem(mime-types-data) = 3.2026.0701

%description
mime-types-data provides a registry for information about MIME media type
definitions. It can be used with the Ruby mime-types library or other software
to determine defined filename extensions for MIME types, or to use filename
extensions to look up the likely MIME type definitions.


%if_enabled    doc
%package       -n gem-mime-types-data-doc
Version:       3.2026.0701
Release:       alt1
Summary:       MIME Type registry data documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mime-types-data
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mime-types-data) = 3.2026.0701

%description   -n gem-mime-types-data-doc
MIME Type registry data documentation files.

mime-types-data provides a registry for information about MIME media type
definitions. It can be used with the Ruby mime-types library or other software
to determine defined filename extensions for MIME types, or to use filename
extensions to look up the likely MIME type definitions.

%description   -n gem-mime-types-data-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mime-types-data.
%endif


%if_enabled    devel
%package       -n gem-mime-types-data-devel
Version:       3.2026.0701
Release:       alt1
Summary:       MIME Type registry data development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mime-types-data
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mime-types-data) = 3.2026.0701
Requires:      gem(hoe) >= 4.0
Requires:      gem(hoe-halostatue) >= 3.0
Requires:      gem(nokogiri) >= 1.6
Requires:      gem(rake) >= 10.0
Requires:      gem(standard) >= 1.0
Conflicts:     gem(hoe) >= 5
Conflicts:     gem(hoe-halostatue) >= 4
Conflicts:     gem(mime-types) >= 4
Conflicts:     gem(nokogiri) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(standard) >= 2

%description   -n gem-mime-types-data-devel
MIME Type registry data development package.

mime-types-data provides a registry for information about MIME media type
definitions. It can be used with the Ruby mime-types library or other software
to determine defined filename extensions for MIME types, or to use filename
extensions to look up the likely MIME type definitions.

%description   -n gem-mime-types-data-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mime-types-data.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-mime-types-data-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-mime-types-data-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS.md README.md
%endif


%changelog
* Tue Sep 01 2026 Pavel Skrylev <majioa@altlinux.org> 3.2026.0701-alt1
- ^ 3.2024.0820 -> 3.2026.0701

* Sat Aug 24 2024 Pavel Skrylev <majioa@altlinux.org> 3.2024.0820-alt1
- ^ 3.2021.0704 -> 3.2024.0820

* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 3.2021.0704-alt1
- ^ 3.2019.1009 -> 3.2021.0704

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 3.2019.1009-alt1
- updated (^) 3.2019.0904 -> 3.2019.1009
- fixed (!) spec

* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 3.2019.0904-alt1
- updated (^) 3.2019.0331 -> 3.2019.0904
- fixed (!) spec

* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 3.2019.0331-alt1
- updated (^) 3.2018.0812 -> 3.2019.0331
- used (>) Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.2018.0812-alt1
- New version.

* Wed Aug 22 2018 Andrey Cherepanov <cas@altlinux.org> 3.2016.0521-alt1.1
- Rebuild for new Ruby autorequirements.

* Fri Mar 31 2017 Andrey Cherepanov <cas@altlinux.org> 3.2016.0521-alt1
- Initial build in Sisyphus
