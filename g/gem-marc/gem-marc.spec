%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname marc

Name:          gem-marc
Version:       1.4.0
Release:       alt1
Summary:       Ruby library for processing Machine Readable Cataloging (MARC) bibliographic data
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby-marc/ruby-marc
Vcs:           https://github.com/ruby-marc/ruby-marc.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(nokogiri) >= 1.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(standard) >= 1.0
BuildRequires: gem(test-unit) >= 3.0
BuildRequires: gem(warning) >= 1.5
BuildRequires: gem(xml-simple) >= 0
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(standard) >= 2
BuildConflicts: gem(test-unit) >= 4
BuildConflicts: gem(warning) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.3.0
Requires:      gem(nokogiri) >= 1.0
Requires:      gem(rexml) >= 0
Conflicts:     gem(nokogiri) >= 2
Obsoletes:     ruby-marc < %EVR
Provides:      ruby-marc = %EVR
Provides:      gem(marc) = 1.4.0

%description
marc is a ruby library for reading and writing MAchine Readable Cataloging
(MARC). More information about MARC can be found at <http://www.loc.gov/marc>.


%package       -n marc
Version:       1.4.0
Release:       alt1
Summary:       Ruby library for processing Machine Readable Cataloging (MARC) bibliographic data executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета marc
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(marc) = 1.4.0

%description   -n marc
Ruby library for processing Machine Readable Cataloging (MARC) bibliographic
data executable(s).

marc is a ruby library for reading and writing MAchine Readable Cataloging
(MARC). More information about MARC can be found at <http://www.loc.gov/marc>.

%description   -n marc -l ru_RU.UTF-8
Исполнямка для самоцвета marc.


%if_enabled    doc
%package       -n gem-marc-doc
Version:       1.4.0
Release:       alt1
Summary:       Ruby library for processing Machine Readable Cataloging (MARC) bibliographic data documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета marc
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(marc) = 1.4.0

%description   -n gem-marc-doc
Ruby library for processing Machine Readable Cataloging (MARC) bibliographic
data documentation files.

marc is a ruby library for reading and writing MAchine Readable Cataloging
(MARC). More information about MARC can be found at <http://www.loc.gov/marc>.

%description   -n gem-marc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета marc.
%endif


%if_enabled    devel
%package       -n gem-marc-devel
Version:       1.4.0
Release:       alt1
Summary:       Ruby library for processing Machine Readable Cataloging (MARC) bibliographic data development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета marc
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(marc) = 1.4.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rdoc) >= 0
Requires:      gem(standard) >= 1.0
Requires:      gem(test-unit) >= 3.0
Requires:      gem(warning) >= 1.5
Requires:      gem(xml-simple) >= 0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(standard) >= 2
Conflicts:     gem(test-unit) >= 4
Conflicts:     gem(warning) >= 2

%description   -n gem-marc-devel
Ruby library for processing Machine Readable Cataloging (MARC) bibliographic
data development package.

marc is a ruby library for reading and writing MAchine Readable Cataloging
(MARC). More information about MARC can be found at <http://www.loc.gov/marc>.

%description   -n gem-marc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета marc.
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

%files         -n marc
%doc CHANGELOG.md LICENSE README.md
%_bindir/marc
%_bindir/marc2xml

%if_enabled    doc
%files         -n gem-marc-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-marc-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Wed Mar 25 2026 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- ^ 1.1.1 -> 1.4.0

* Wed Jun 30 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- ^ 1.0.2 -> 1.1.1

* Thu Jul 19 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- New version.
- Disable tests.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.2-alt1.2
- Rebuild with new Ruby autorequirements.

* Wed Dec 05 2012 Led <led@altlinux.ru> 0.2.2-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Sun May 10 2009 Alexey I. Froloff <raorn@altlinux.org> 0.2.2-alt1
- Built for Sisyphus
