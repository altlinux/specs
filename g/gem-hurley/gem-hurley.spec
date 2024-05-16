%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname hurley

Name:          gem-hurley
Version:       0.2.18
Release:       alt0.1
Summary:       HTTP client wrapper
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lostisland/hurley
Vcs:           https://github.com/lostisland/hurley.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.0
BuildRequires: gem(addressable) >= 2.3
BuildRequires: gem(rake) >= 10.4.0
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(sinatra) >= 1.4.5
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(sinatra) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency addressable >= 2.8.0,addressable < 3
Provides:      gem(hurley) = 0.2.18

%ruby_use_gem_version hurley:0.2.18

%description
Hurley provides a common interface for working with different HTTP adapters.


%if_enabled    doc
%package       -n gem-hurley-doc
Version:       0.2.18
Release:       alt0.1
Summary:       HTTP client wrapper documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hurley
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hurley) = 0.2.18

%description   -n gem-hurley-doc
HTTP client wrapper documentation files.

Hurley provides a common interface for working with different HTTP adapters.
%description   -n gem-hurley-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hurley.
%endif


%if_enabled    devel
%package       -n gem-hurley-devel
Version:       0.2.18
Release:       alt0.1
Summary:       HTTP client wrapper development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hurley
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hurley) = 0.2.18
Requires:      gem(bundler) >= 1.0
Requires:      gem(addressable) >= 2.3
Requires:      gem(rake) >= 10.4.0
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(sinatra) >= 1.4.5
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(sinatra) >= 5

%description   -n gem-hurley-devel
HTTP client wrapper development package.

Hurley provides a common interface for working with different HTTP adapters.
%description   -n gem-hurley-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hurley.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-hurley-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-hurley-devel
%doc README.md
%endif


%changelog
* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 0.2.18-alt0.1
- ^ 0.2 -> 0.2p18

* Tue Oct 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.2-alt1
- + packaged gem with Ruby Policy 2.0
