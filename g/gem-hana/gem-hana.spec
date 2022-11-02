%define        gemname hana

Name:          gem-hana
Version:       1.3.7
Release:       alt1
Summary:       Implementation of [JSON Patch][1] and [JSON Pointer][2] RFC
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/tenderlove/hana
Vcs:           https://github.com/tenderlove/hana.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(minitest) >= 5.16 gem(minitest) < 6
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(hoe) >= 3.23 gem(hoe) < 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(hana) = 1.3.7


%description
Implementation of [JSON Patch][1] and [JSON Pointer][2] RFC.


%package       -n gem-hana-doc
Version:       1.3.7
Release:       alt1
Summary:       Implementation of [JSON Patch][1] and [JSON Pointer][2] RFC documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hana
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hana) = 1.3.7

%description   -n gem-hana-doc
Implementation of [JSON Patch][1] and [JSON Pointer][2] RFC documentation files.

%description   -n gem-hana-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hana.


%package       -n gem-hana-devel
Version:       1.3.7
Release:       alt1
Summary:       Implementation of [JSON Patch][1] and [JSON Pointer][2] RFC development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hana
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hana) = 1.3.7
Requires:      gem(minitest) >= 5.16 gem(minitest) < 6
Requires:      gem(rdoc) >= 4.0 gem(rdoc) < 7
Requires:      gem(hoe) >= 3.23 gem(hoe) < 4

%description   -n gem-hana-devel
Implementation of [JSON Patch][1] and [JSON Pointer][2] RFC development package.

%description   -n gem-hana-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hana.


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

%files         -n gem-hana-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hana-devel
%doc README.md


%changelog
* Sat Oct 29 2022 Pavel Skrylev <majioa@altlinux.org> 1.3.7-alt1
- + packaged gem with Ruby Policy 2.0
