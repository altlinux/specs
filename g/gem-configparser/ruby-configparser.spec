%define        gemname configparser

Name:          gem-configparser
Version:       0.1.7
Release:       alt1.1
Summary:       parses configuration files compatible with Python's ConfigParser
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/chrislee35/configparser
Vcs:           https://github.com/chrislee35/configparser.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 5.5 gem(minitest) < 6
BuildRequires: gem(bundler) >= 1.3 gem(bundler) < 3
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Obsoletes:     ruby-configparser < %EVR
Provides:      ruby-configparser = %EVR
Provides:      gem(configparser) = 0.1.7


%description
Configparser parses configuration files compatible with Python's ConfigParser.


%package       -n gem-configparser-doc
Version:       0.1.7
Release:       alt1.1
Summary:       parses configuration files compatible with Python's ConfigParser documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета configparser
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(configparser) = 0.1.7

%description   -n gem-configparser-doc
parses configuration files compatible with Python's ConfigParser documentation
files.

Configparser parses configuration files compatible with Python's ConfigParser.

%description   -n gem-configparser-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета configparser.


%package       -n gem-configparser-devel
Version:       0.1.7
Release:       alt1.1
Summary:       parses configuration files compatible with Python's ConfigParser development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета configparser
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(configparser) = 0.1.7
Requires:      gem(minitest) >= 5.5 gem(minitest) < 6
Requires:      gem(bundler) >= 1.3 gem(bundler) < 3
Requires:      gem(rake) >= 0

%description   -n gem-configparser-devel
parses configuration files compatible with Python's ConfigParser development
package.

Configparser parses configuration files compatible with Python's ConfigParser.

%description   -n gem-configparser-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета configparser.


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

%files         -n gem-configparser-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-configparser-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.7-alt1.1
- ! spec

* Tue Apr 09 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.7-alt1
- Initial build for Sisyphus
