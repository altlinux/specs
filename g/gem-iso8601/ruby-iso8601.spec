%define        gemname iso8601

Name:          gem-iso8601
Version:       0.13.0
Release:       alt1
Summary:       Ruby parser to work with ISO8601 dateTimes and durations
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/arnau/ISO8601
Vcs:           https://github.com/arnau/iso8601.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(pry) >= 0.13.1 gem(pry) < 1
BuildRequires: gem(pry-doc) >= 1.1.0 gem(pry-doc) < 1.2
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.9 gem(rspec) < 4
BuildRequires: gem(rubocop) >= 0.85 gem(rubocop) < 2
BuildRequires: gem(rubocop-packaging) >= 0.1.1 gem(rubocop-packaging) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency rubocop-packaging >= 0.5.1,rubocop-packaging < 1
Obsoletes:     ruby-iso8601 < %EVR
Provides:      ruby-iso8601 = %EVR
Provides:      gem(iso8601) = 0.13.0


%description
ISO8601 is a simple implementation of the ISO 8601 (Data elements and
interchange formats - Information interchange - Representation of dates and
times) standard.
http://en.wikipedia.org/wiki/ISO_8601


%package       -n gem-iso8601-doc
Version:       0.13.0
Release:       alt1
Summary:       Ruby parser to work with ISO8601 dateTimes and durations documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета iso8601
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(iso8601) = 0.13.0

%description   -n gem-iso8601-doc
Ruby parser to work with ISO8601 dateTimes and durations documentation files.

ISO8601 is a simple implementation of the ISO 8601 (Data elements and
interchange formats - Information interchange - Representation of dates and
times) standard.
http://en.wikipedia.org/wiki/ISO_8601

%description   -n gem-iso8601-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета iso8601.


%package       -n gem-iso8601-devel
Version:       0.13.0
Release:       alt1
Summary:       Ruby parser to work with ISO8601 dateTimes and durations development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета iso8601
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(iso8601) = 0.13.0
Requires:      gem(pry) >= 0.13.1 gem(pry) < 1
Requires:      gem(pry-doc) >= 1.1.0 gem(pry-doc) < 1.2
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(rubocop) >= 0.85 gem(rubocop) < 2
Requires:      gem(rubocop-packaging) >= 0.1.1 gem(rubocop-packaging) < 1

%description   -n gem-iso8601-devel
Ruby parser to work with ISO8601 dateTimes and durations development package.

ISO8601 is a simple implementation of the ISO 8601 (Data elements and
interchange formats - Information interchange - Representation of dates and
times) standard.
http://en.wikipedia.org/wiki/ISO_8601

%description   -n gem-iso8601-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета iso8601.


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

%files         -n gem-iso8601-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-iso8601-devel
%doc README.md


%changelog
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
