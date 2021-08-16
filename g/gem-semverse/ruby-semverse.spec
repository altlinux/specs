%define        gemname semverse

Name:          gem-semverse
Version:       3.0.0
Release:       alt1
Summary:       An elegant library for representing and comparing SemVer versions and constraints
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/berkshelf/semverse
Vcs:           https://github.com/berkshelf/semverse.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-semverse < %EVR
Provides:      ruby-semverse = %EVR
Provides:      gem(semverse) = 3.0.0


%description
An elegant library for representing and comparing SemVer versions and
constraints.


%package       -n gem-semverse-doc
Version:       3.0.0
Release:       alt1
Summary:       An elegant library for representing and comparing SemVer versions and constraints documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета semverse
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(semverse) = 3.0.0

%description   -n gem-semverse-doc
An elegant library for representing and comparing SemVer versions and
constraints documentation files.

%description   -n gem-semverse-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета semverse.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-semverse-doc
%ruby_gemdocdir


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- ^ 2.0.0 -> 3.0.0

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1.1
- Rebuild for new Ruby autorequirements.

* Mon May 28 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus
