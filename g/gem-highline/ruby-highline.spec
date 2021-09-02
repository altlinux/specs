%define        gemname highline

Name:          gem-highline
Epoch:         1
Version:       2.0.3
Release:       alt1
Summary:       HighLine is a high-level command-line IO Ruby library
License:       Ruby
Group:         Development/Ruby
Url:           https://github.com/JEG2/highline
Vcs:           https://github.com/jeg2/highline.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-highline < %EVR
Provides:      ruby-highline = %EVR
Provides:      gem(highline) = 2.0.3


%description
A high-level IO library that provides validation, type conversion, and more for
command-line interfaces. HighLine also includes a complete menu system that can
crank out anything from simple list selection to complete shells with just
minutes of work.


%package       -n gem-highline-doc
Version:       2.0.3
Release:       alt1
Summary:       HighLine is a high-level command-line IO Ruby library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета highline
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(highline) = 2.0.3

%description   -n gem-highline-doc
HighLine is a high-level command-line IO Ruby library documentation files.

A high-level IO library that provides validation, type conversion, and more for
command-line interfaces. HighLine also includes a complete menu system that can
crank out anything from simple list selection to complete shells with just
minutes of work.

%description   -n gem-highline-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета highline.


%package       -n gem-highline-devel
Version:       2.0.3
Release:       alt1
Summary:       HighLine is a high-level command-line IO Ruby library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета highline
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(highline) = 2.0.3
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 0

%description   -n gem-highline-devel
HighLine is a high-level command-line IO Ruby library development package.

A high-level IO library that provides validation, type conversion, and more for
command-line interfaces. HighLine also includes a complete menu system that can
crank out anything from simple list selection to complete shells with just
minutes of work.

%description   -n gem-highline-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета highline.


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

%files         -n gem-highline-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-highline-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1:2.0.3-alt1
- ^ 2.0.2 -> 2.0.3

* Tue Aug 06 2019 Pavel Skrylev <majioa@altlinux.org> 1:2.0.2-alt1
- ^ v2.0.2
- ^ Ruby Policy 2.0

* Wed Apr 10 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1:1.7.9-alt1
- update to 1.7.9 for opennebula

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.6.21-alt2
- Reset to old version for ruby-commander and ruby-hiera-eyaml.

* Mon Jul 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.
- Rebuild with new Ruby autorequirements.

* Mon Sep 21 2015 Andrey Cherepanov <cas@altlinux.org> 1.7.5-alt1
- New version

* Fri Dec 07 2012 Led <led@altlinux.ru> 1.5.1-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Mon Jan 04 2010 Igor Zubkov <icesik@altlinux.org> 1.5.1-alt2
- fix Url
- fix License

* Sat Dec 12 2009 Igor Zubkov <icesik@altlinux.org> 1.5.1-alt1
- build for Sisyphus
