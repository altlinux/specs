%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname afm

Name:          gem-afm
Version:       1.0.0
Release:       alt1
Summary:       reading Adobe Font Metrics (afm) files
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/halfbyte/afm
Vcs:           https://github.com/halfbyte/afm.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(minitest) >= 6.0
BuildRequires: gem(rake) >= 13.1.0
BuildRequires: gem(rdoc) >= 6.1.1
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rdoc) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency minitest >= 6.0
Requires:      ruby >= 3.2.0
Provides:      gem(afm) = 1.0.0

%description
a simple library to read afm files and use the data conveniently


%if_enabled    doc
%package       -n gem-afm-doc
Version:       1.0.0
Release:       alt1
Summary:       reading Adobe Font Metrics (afm) files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета afm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(afm) = 1.0.0

%description   -n gem-afm-doc
reading Adobe Font Metrics (afm) files documentation files.

a simple library to read afm files and use the data conveniently

%description   -n gem-afm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета afm.
%endif


%if_enabled    devel
%package       -n gem-afm-devel
Version:       1.0.0
Release:       alt1
Summary:       reading Adobe Font Metrics (afm) files development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета afm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(afm) = 1.0.0
Requires:      gem(minitest) >= 6.0
Requires:      gem(rake) >= 13.1.0
Requires:      gem(rdoc) >= 6.1.1
Conflicts:     gem(minitest) >= 7
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rdoc) >= 7

%description   -n gem-afm-devel
reading Adobe Font Metrics (afm) files development package.

a simple library to read afm files and use the data conveniently

%description   -n gem-afm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета afm.
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
%files         -n gem-afm-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-afm-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Tue Aug 18 2026 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- ^ 0.2.2 -> 1.0.0

* Sun Sep 12 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.2-alt1
- + packaged gem with Ruby Policy 2.0
