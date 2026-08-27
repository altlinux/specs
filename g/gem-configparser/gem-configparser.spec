%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname configparser

Name:          gem-configparser
Version:       0.1.7
Release:       alt2
Summary:       parses configuration files compatible with Python's ConfigParser
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/chrislee35/configparser
Vcs:           https://github.com/chrislee35/configparser.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(bundler) >= 1.3
BuildRequires: gem(minitest) >= 5.5
BuildRequires: gem(rake) >= 0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(minitest) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency minitest >= 6.0
Obsoletes:     ruby-configparser < %EVR
Provides:      ruby-configparser = %EVR
Provides:      gem(configparser) = 0.1.7

%description
parses configuration files compatible with Python's ConfigParser


%if_enabled    doc
%package       -n gem-configparser-doc
Version:       0.1.7
Release:       alt2
Summary:       parses configuration files compatible with Python's ConfigParser documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета configparser
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(configparser) = 0.1.7

%description   -n gem-configparser-doc
parses configuration files compatible with Python's ConfigParser documentation
files.

%description   -n gem-configparser-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета configparser.
%endif


%if_enabled    devel
%package       -n gem-configparser-devel
Version:       0.1.7
Release:       alt2
Summary:       parses configuration files compatible with Python's ConfigParser development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета configparser
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(configparser) = 0.1.7
Requires:      gem(bundler) >= 1.3
Requires:      gem(minitest) >= 5.5
Requires:      gem(rake) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(minitest) >= 7

%description   -n gem-configparser-devel
parses configuration files compatible with Python's ConfigParser development
package.

%description   -n gem-configparser-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета configparser.
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
%doc LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-configparser-doc
%doc LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-configparser-devel
%doc LICENSE.txt README.md
%endif


%changelog
* Wed Aug 19 2026 Pavel Skrylev <majioa@altlinux.org> 0.1.7-alt2
- * rebase to upstream
- ! fixed dep to minitest gem

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.7-alt1.1
- ! spec

* Tue Apr 09 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.1.7-alt1
- Initial build for Sisyphus
