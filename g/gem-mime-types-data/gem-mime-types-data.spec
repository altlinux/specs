%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname mime-types-data

Name:          gem-mime-types-data
Version:       3.2024.0820
Release:       alt1
Summary:       MIME Type registry data
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mime-types/mime-types-data
Vcs:           https://github.com/mime-types/mime-types-data.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(hoe) >= 4.0
BuildRequires: gem(hoe-doofus) >= 1.0
BuildRequires: gem(hoe-gemspec2) >= 1.1
BuildRequires: gem(hoe-git2) >= 1.7
BuildRequires: gem(hoe-rubygems) >= 1.0
BuildRequires: gem(mime-types) >= 3.4.0
BuildRequires: gem(nokogiri) >= 1.6
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(standard) >= 1.0
BuildRequires: gem(rdoc) >= 4.0
BuildConflicts: gem(hoe) >= 5
BuildConflicts: gem(hoe-doofus) >= 2
BuildConflicts: gem(hoe-gemspec2) >= 2
BuildConflicts: gem(hoe-git2) >= 2
BuildConflicts: gem(hoe-rubygems) >= 2
BuildConflicts: gem(mime-types) >= 4
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(standard) >= 2
BuildConflicts: gem(rdoc) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-mime-types-data < %EVR
Provides:      ruby-mime-types-data = %EVR
Provides:      gem(mime-types-data) = 3.2024.0820


%description
mime-types-data provides a registry for information about MIME media type
definitions. It can be used with the Ruby mime-types library or other software
to determine defined filename extensions for MIME types, or to use filename
extensions to look up the likely MIME type definitions.


%if_enabled    doc
%package       -n gem-mime-types-data-doc
Version:       3.2024.0820
Release:       alt1
Summary:       MIME Type registry data documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mime-types-data
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mime-types-data) = 3.2024.0820

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
Version:       3.2024.0820
Release:       alt1
Summary:       MIME Type registry data development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mime-types-data
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mime-types-data) = 3.2024.0820
Requires:      gem(byebug) >= 0
Requires:      gem(hoe) >= 4.0
Requires:      gem(hoe-doofus) >= 1.0
Requires:      gem(hoe-gemspec2) >= 1.1
Requires:      gem(hoe-git2) >= 1.7
Requires:      gem(hoe-rubygems) >= 1.0
Requires:      gem(mime-types) >= 3.4.0
Requires:      gem(nokogiri) >= 1.6
Requires:      gem(rake) >= 10.0
Requires:      gem(standard) >= 1.0
Requires:      gem(rdoc) >= 4.0
Conflicts:     gem(hoe) >= 5
Conflicts:     gem(hoe-doofus) >= 2
Conflicts:     gem(hoe-gemspec2) >= 2
Conflicts:     gem(hoe-git2) >= 2
Conflicts:     gem(hoe-rubygems) >= 2
Conflicts:     gem(mime-types) >= 4
Conflicts:     gem(nokogiri) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(standard) >= 2
Conflicts:     gem(rdoc) >= 7

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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-mime-types-data-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-mime-types-data-devel
%doc README.md
%endif


%changelog
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
