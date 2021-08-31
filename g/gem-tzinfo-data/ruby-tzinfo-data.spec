%define        gemname tzinfo-data

Name:          gem-tzinfo-data
Version:       1.2021.1
Release:       alt1
Summary:       TZInfo::Data - Timezone Data for TZInfo
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/tzinfo/tzinfo-data/
Vcs:           https://github.com/tzinfo/tzinfo-data.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(tzinfo) >= 1.0.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(tzinfo) >= 1.0.0
Obsoletes:     ruby-tzinfo-data < %EVR
Provides:      ruby-tzinfo-data = %EVR
Provides:      gem(tzinfo-data) = 1.2021.1


%description
TZInfo::Data contains data from the IANA Time Zone database packaged as Ruby
modules for use with TZInfo.

If TZInfo::Data is installed, TZInfo will automatically use it as its source of
time zone data. If TZInfo::Data is not available, TZInfo will attempt to use
the system zoneinfo files instead. Please refer to the TZInfo documentation for
further details.


%package       -n gem-tzinfo-data-doc
Version:       1.2021.1
Release:       alt1
Summary:       TZInfo::Data - Timezone Data for TZInfo documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета tzinfo-data
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(tzinfo-data) = 1.2021.1

%description   -n gem-tzinfo-data-doc
TZInfo::Data - Timezone Data for TZInfo documentation files.

TZInfo::Data contains data from the IANA Time Zone database packaged as Ruby
modules for use with TZInfo.

If TZInfo::Data is installed, TZInfo will automatically use it as its source of
time zone data. If TZInfo::Data is not available, TZInfo will attempt to use
the system zoneinfo files instead. Please refer to the TZInfo documentation for
further details.

%description   -n gem-tzinfo-data-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета tzinfo-data.


%package       -n gem-tzinfo-data-devel
Version:       1.2021.1
Release:       alt1
Summary:       TZInfo::Data - Timezone Data for TZInfo development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета tzinfo-data
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(tzinfo-data) = 1.2021.1

%description   -n gem-tzinfo-data-devel
TZInfo::Data - Timezone Data for TZInfo development package.

TZInfo::Data contains data from the IANA Time Zone database packaged as Ruby
modules for use with TZInfo.

If TZInfo::Data is installed, TZInfo will automatically use it as its source of
time zone data. If TZInfo::Data is not available, TZInfo will attempt to use
the system zoneinfo files instead. Please refer to the TZInfo documentation for
further details.

%description   -n gem-tzinfo-data-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета tzinfo-data.


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

%files         -n gem-tzinfo-data-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-tzinfo-data-devel
%doc README.md


%changelog
* Tue Jun 29 2021 Pavel Skrylev <majioa@altlinux.org> 1.2021.1-alt1
- ^ 1.2018.5 -> 1.2021.1

* Tue Oct 02 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.2018.5-alt1
- Initial build for Sisyphus
