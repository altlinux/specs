%define        gemname rfauxfactory

Name:          gem-rfauxfactory
Version:       0.1.5
Release:       alt1
Summary:       Generates random data for your tests
License:       Apache 2.0
Group:         Development/Ruby
Url:           https://github.com/SatelliteQE/RFauxFactory
Vcs:           https://github.com/satelliteqe/rfauxfactory.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.16 gem(bundler) < 3
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Provides:      gem(rfauxfactory) = 0.1.5


%description
Generates random data for your tests. Ruby port for
https://github.com/omaciel/fauxfactory.


%package       -n gem-rfauxfactory-doc
Version:       0.1.5
Release:       alt1
Summary:       Generates random data for your tests documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rfauxfactory
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rfauxfactory) = 0.1.5

%description   -n gem-rfauxfactory-doc
Generates random data for your tests documentation files.

Generates random data for your tests. Ruby port for
https://github.com/omaciel/fauxfactory.

%description   -n gem-rfauxfactory-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rfauxfactory.


%package       -n gem-rfauxfactory-devel
Version:       0.1.5
Release:       alt1
Summary:       Generates random data for your tests development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rfauxfactory
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rfauxfactory) = 0.1.5
Requires:      gem(bundler) >= 1.16 gem(bundler) < 3
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6
Requires:      gem(rake) >= 0 gem(rake) < 14

%description   -n gem-rfauxfactory-devel
Generates random data for your tests development package.

Generates random data for your tests. Ruby port for
https://github.com/omaciel/fauxfactory.

%description   -n gem-rfauxfactory-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rfauxfactory.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rst
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-rfauxfactory-doc
%doc README.rst
%ruby_gemdocdir

%files         -n gem-rfauxfactory-devel
%doc README.rst


%changelog
* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.5-alt1
- + packaged gem with Ruby Policy 2.0
