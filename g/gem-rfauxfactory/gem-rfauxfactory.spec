%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rfauxfactory

Name:          gem-rfauxfactory
Version:       0.1.5.1
Release:       alt0.1
Summary:       Generates random data for your tests
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/SatelliteQE/RFauxFactory
Vcs:           https://github.com/satelliteqe/rfauxfactory.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop-checkstyle_formatter) >= 0
BuildRequires: gem(simplecov) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.3
Provides:      gem(rfauxfactory) = 0.1.5.1

%ruby_use_gem_version rfauxfactory:0.1.5.1

%description
Generates random data for your tests. Ruby port for
https://github.com/omaciel/fauxfactory.


%if_enabled    doc
%package       -n gem-rfauxfactory-doc
Version:       0.1.5.1
Release:       alt0.1
Summary:       Generates random data for your tests documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rfauxfactory
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rfauxfactory) = 0.1.5.1

%description   -n gem-rfauxfactory-doc
Generates random data for your tests documentation files.

Generates random data for your tests. Ruby port for
https://github.com/omaciel/fauxfactory.

%description   -n gem-rfauxfactory-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rfauxfactory.
%endif


%if_enabled    devel
%package       -n gem-rfauxfactory-devel
Version:       0.1.5.1
Release:       alt0.1
Summary:       Generates random data for your tests development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rfauxfactory
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rfauxfactory) = 0.1.5.1
Requires:      gem(bundler) >= 0
Requires:      gem(coveralls) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop-checkstyle_formatter) >= 0
Requires:      gem(simplecov) >= 0

%description   -n gem-rfauxfactory-devel
Generates random data for your tests development package.

Generates random data for your tests. Ruby port for
https://github.com/omaciel/fauxfactory.

%description   -n gem-rfauxfactory-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rfauxfactory.
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
%doc LICENSE README.rst
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rfauxfactory-doc
%doc LICENSE README.rst
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rfauxfactory-devel
%doc LICENSE README.rst
%endif


%changelog
* Sat Aug 22 2026 Pavel Skrylev <majioa@altlinux.org> 0.1.5.1-alt0.1
- ^ 0.1.5 -> 0.1.5p1
- * rebased to upstream git flow

* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.5-alt1
- + packaged gem with Ruby Policy 2.0
