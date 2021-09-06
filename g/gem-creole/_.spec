%define        gemname creole

Name:          gem-creole
Version:       0.5.0.1
Release:       alt0.1
Summary:       Creole 1.0 to XHTML converter written in ruby
License:       Ruby
Group:         Development/Ruby
Url:           https://github.com/minad/creole
Vcs:           https://github.com/minad/creole.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bacon) >= 0
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_version creole:0.5.0.1
Provides:      gem(creole) = 0.5.0.1


%description
Creole is a Creole-to-HTML converter for Creole, the lightweight markup language
(http://wikicreole.org/). Github uses this converter to render *.creole files.


%package       -n gem-creole-doc
Version:       0.5.0.1
Release:       alt0.1
Summary:       Creole 1.0 to XHTML converter written in ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета creole
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(creole) = 0.5.0.1

%description   -n gem-creole-doc
Creole 1.0 to XHTML converter written in ruby documentation files.

Creole is a Creole-to-HTML converter for Creole, the lightweight markup language
(http://wikicreole.org/). Github uses this converter to render *.creole files.

%description   -n gem-creole-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета creole.


%package       -n gem-creole-devel
Version:       0.5.0.1
Release:       alt0.1
Summary:       Creole 1.0 to XHTML converter written in ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета creole
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(creole) = 0.5.0.1
Requires:      gem(bacon) >= 0
Requires:      gem(rake) >= 0

%description   -n gem-creole-devel
Creole 1.0 to XHTML converter written in ruby development package.

Creole is a Creole-to-HTML converter for Creole, the lightweight markup language
(http://wikicreole.org/). Github uses this converter to render *.creole files.

%description   -n gem-creole-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета creole.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.creole
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-creole-doc
%doc README.creole
%ruby_gemdocdir

%files         -n gem-creole-devel
%doc README.creole


%changelog
* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.0.1-alt0.1
- ^ 0.5.0 -> 0.5.0[.1]

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
