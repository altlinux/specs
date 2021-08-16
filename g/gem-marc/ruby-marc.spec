%define        gemname marc

Name:          gem-marc
Version:       1.1.1
Release:       alt1
Summary:       Ruby library for processing Machine Readable Cataloging (MARC) bibliographic data
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby-marc/ruby-marc
Vcs:           https://github.com/ruby-marc/ruby-marc.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(scrub_rb) >= 1.0.1 gem(scrub_rb) < 2
BuildRequires: gem(unf) >= 0
BuildRequires: gem(rexml) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(scrub_rb) >= 1.0.1 gem(scrub_rb) < 2
Requires:      gem(unf) >= 0
Requires:      gem(rexml) >= 0
Obsoletes:     ruby-marc < %EVR
Provides:      ruby-marc = %EVR
Provides:      gem(marc) = 1.1.1


%description
marc is a ruby library for reading and writing MAchine Readable Cataloging
(MARC). More information about MARC can be found at <http://www.loc.gov/marc>.


%package       -n gem-marc-doc
Version:       1.1.1
Release:       alt1
Summary:       Ruby library for processing Machine Readable Cataloging (MARC) bibliographic data documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета marc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(marc) = 1.1.1

%description   -n gem-marc-doc
Ruby library for processing Machine Readable Cataloging (MARC) bibliographic
data documentation files.

marc is a ruby library for reading and writing MAchine Readable Cataloging
(MARC). More information about MARC can be found at <http://www.loc.gov/marc>.

%description   -n gem-marc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета marc.


%package       -n gem-marc-devel
Version:       1.1.1
Release:       alt1
Summary:       Ruby library for processing Machine Readable Cataloging (MARC) bibliographic data development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета marc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(marc) = 1.1.1

%description   -n gem-marc-devel
Ruby library for processing Machine Readable Cataloging (MARC) bibliographic
data development package.

marc is a ruby library for reading and writing MAchine Readable Cataloging
(MARC). More information about MARC can be found at <http://www.loc.gov/marc>.

%description   -n gem-marc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета marc.


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

%files         -n gem-marc-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-marc-devel
%doc README.md


%changelog
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
