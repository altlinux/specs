%define        gemname vegas

Name:          gem-vegas
Version:       0.1.11
Release:       alt1.2
Summary:       Vegas aims to solve the simple problem of creating executable versions of Sinatra/Rack apps
License:       MIT
Group:         Development/Ruby
Url:           http://code.quirkey.com/vegas/
Vcs:           https://github.com/quirkey/vegas.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rack) >= 1.0.0
BuildRequires: gem(mocha) >= 0.9.8
BuildRequires: gem(bacon) >= 1.1.0
BuildRequires: gem(sinatra) >= 0.9.4
BuildConflicts: gem(mocha) >= 2
BuildConflicts: gem(bacon) >= 2
BuildConflicts: gem(sinatra) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 1.11.2,mocha < 2
%ruby_use_gem_dependency sinatra >= 2.2.3,sinatra < 3
%ruby_use_gem_dependency bacon >= 1.2.0,bacon < 2
Requires:      gem(rack) >= 1.0.0
Provides:      gem(vegas) = 0.1.11


%description
Vegas aims to solve the simple problem of creating executable versions of
Sinatra/Rack apps. It includes a class Vegas::Runner that wraps Rack/Sinatra
applications and provides a simple command line interface and launching
mechanism.


%package       -n gem-vegas-doc
Version:       0.1.11
Release:       alt1.2
Summary:       Vegas aims to solve the simple problem of creating executable versions of Sinatra/Rack apps documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета vegas
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(vegas) = 0.1.11

%description   -n gem-vegas-doc
Vegas aims to solve the simple problem of creating executable versions of
Sinatra/Rack apps documentation files.

Vegas aims to solve the simple problem of creating executable versions of
Sinatra/Rack apps. It includes a class Vegas::Runner that wraps Rack/Sinatra
applications and provides a simple command line interface and launching
mechanism.

%description   -n gem-vegas-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета vegas.


%package       -n gem-vegas-devel
Version:       0.1.11
Release:       alt1.2
Summary:       Vegas aims to solve the simple problem of creating executable versions of Sinatra/Rack apps development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета vegas
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(vegas) = 0.1.11
Requires:      gem(mocha) >= 0.9.8
Requires:      gem(bacon) >= 1.1.0
Requires:      gem(sinatra) >= 0.9.4
Conflicts:     gem(mocha) >= 2
Conflicts:     gem(bacon) >= 2
Conflicts:     gem(sinatra) >= 3

%description   -n gem-vegas-devel
Vegas aims to solve the simple problem of creating executable versions of
Sinatra/Rack apps development package.

Vegas aims to solve the simple problem of creating executable versions of
Sinatra/Rack apps. It includes a class Vegas::Runner that wraps Rack/Sinatra
applications and provides a simple command line interface and launching
mechanism.

%description   -n gem-vegas-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета vegas.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-vegas-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-vegas-devel
%doc README.rdoc


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 0.1.11-alt1.2
- ! closes build deps under check condition

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.11-alt1.1
- ! spec

* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.11-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
