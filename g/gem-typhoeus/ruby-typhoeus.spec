%define        gemname typhoeus

Name:          gem-typhoeus
Version:       1.4.0
Release:       alt1
Summary:       Typhoeus wraps libcurl in order to make fast and reliable requests
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/typhoeus/typhoeus
Vcs:           https://github.com/typhoeus/typhoeus.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(ethon) >= 0.9.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ethon) >= 0.9.0
Obsoletes:     ruby-typhoeus < %EVR
Provides:      ruby-typhoeus = %EVR
Provides:      gem(typhoeus) = 1.4.0


%description
Like a modern code version of the mythical beast with 100 serpent heads,
Typhoeus runs HTTP requests in parallel while cleanly encapsulating handling
logic.


%package       -n gem-typhoeus-doc
Version:       1.4.0
Release:       alt1
Summary:       Typhoeus wraps libcurl in order to make fast and reliable requests documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета typhoeus
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(typhoeus) = 1.4.0

%description   -n gem-typhoeus-doc
Typhoeus wraps libcurl in order to make fast and reliable requests documentation
files.

Like a modern code version of the mythical beast with 100 serpent heads,
Typhoeus runs HTTP requests in parallel while cleanly encapsulating handling
logic.


%description   -n gem-typhoeus-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета typhoeus.


%package       -n gem-typhoeus-devel
Version:       1.4.0
Release:       alt1
Summary:       Typhoeus wraps libcurl in order to make fast and reliable requests development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета typhoeus
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(typhoeus) = 1.4.0

%description   -n gem-typhoeus-devel
Typhoeus wraps libcurl in order to make fast and reliable requests development
package.

Like a modern code version of the mythical beast with 100 serpent heads,
Typhoeus runs HTTP requests in parallel while cleanly encapsulating handling
logic.


%description   -n gem-typhoeus-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета typhoeus.


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

%files         -n gem-typhoeus-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-typhoeus-devel
%doc README.md


%changelog
* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- ^ 1.3.0 -> 1.4.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus
