%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname iso8601

Name:          gem-iso8601
Version:       0.13.0.5
Release:       alt0.1
Summary:       Ruby parser to work with ISO8601 dateTimes and durations
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/arnau/ISO8601
Vcs:           https://github.com/arnau/iso8601.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(pry) >= 0.13.1
BuildRequires: gem(pry-doc) >= 1.1.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.9
BuildRequires: gem(rubocop) >= 0.89
BuildRequires: gem(rubocop-packaging) >= 0.3.0
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(pry-doc) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-packaging) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency pry-doc >= 1.5.0,pry-doc < 2
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency rubocop-packaging >= 0.5.2,rubocop-packaging < 1
Requires:      ruby >= 2.4.0
Obsoletes:     ruby-iso8601 < %EVR
Provides:      ruby-iso8601 = %EVR
Provides:      gem(iso8601) = 0.13.0.5

%ruby_use_gem_version iso8601:0.13.0.5

%description
ISO8601 is a simple implementation of the ISO 8601 (Data elements and
interchange formats - Information interchange - Representation of dates and
times) standard. http://en.wikipedia.org/wiki/ISO_8601


%if_enabled    doc
%package       -n gem-iso8601-doc
Version:       0.13.0.5
Release:       alt0.1
Summary:       Ruby parser to work with ISO8601 dateTimes and durations documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета iso8601
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(iso8601) = 0.13.0.5

%description   -n gem-iso8601-doc
Ruby parser to work with ISO8601 dateTimes and durations documentation
files.

ISO8601 is a simple implementation of the ISO 8601 (Data elements and
interchange formats - Information interchange - Representation of dates and
times) standard. http://en.wikipedia.org/wiki/ISO_8601

%description   -n gem-iso8601-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета iso8601.
%endif


%if_enabled    devel
%package       -n gem-iso8601-devel
Version:       0.13.0.5
Release:       alt0.1
Summary:       Ruby parser to work with ISO8601 dateTimes and durations development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета iso8601
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(iso8601) = 0.13.0.5
Requires:      gem(pry) >= 0.13.1
Requires:      gem(pry-doc) >= 1.1.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.9
Requires:      gem(rubocop) >= 0.89
Requires:      gem(rubocop-packaging) >= 0.3.0
Conflicts:     gem(pry) >= 1
Conflicts:     gem(pry-doc) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-packaging) >= 1

%description   -n gem-iso8601-devel
Ruby parser to work with ISO8601 dateTimes and durations development
package.

ISO8601 is a simple implementation of the ISO 8601 (Data elements and
interchange formats - Information interchange - Representation of dates and
times) standard. http://en.wikipedia.org/wiki/ISO_8601

%description   -n gem-iso8601-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета iso8601.
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
%doc LICENSE README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-iso8601-doc
%doc LICENSE README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-iso8601-devel
%doc LICENSE README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%endif


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.13.0.5-alt0.1
- ^ 0.13.0 -> 0.13.0p5

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.13.0-alt1
- ^ 0.12.1 -> 0.13.0

* Mon Oct 29 2018 Pavel Skrylev <majioa@altlinux.org> 0.12.1-alt1
- new version 0.12.1

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 0.11.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.10.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.10.1-alt1
- Initial build for Sisyphus
