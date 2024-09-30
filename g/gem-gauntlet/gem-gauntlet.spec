# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname gauntlet

Name:          gem-gauntlet
Version:       2.1.0
Release:       alt1.1
Summary:       Gauntlet is a pluggable means of running code against all the latest gems and storing off the data
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/gauntlet
Vcs:           https://github.com/seattlerb/gauntlet.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(hoe) >= 4.2
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(net-http-persistent) >= 1.4.1
BuildRequires: gem(rdoc) >= 4.0
BuildConflicts: gem(hoe) >= 5
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(net-http-persistent) >= 5
BuildConflicts: gem(rdoc) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency net-http-persistent >= 4.0.1,net-http-persistent < 5
Requires:      gem(net-http-persistent) >= 1.4.1
Conflicts:     gem(net-http-persistent) >= 5
Provides:      gem(gauntlet) = 2.1.0


%description
Gauntlet is a pluggable means of running code against all the latest gems and
storing off the data.

* Downloads all the latest gems and converts them to tarballs for easy access.
* Iterates through all downloaded gems, unpacks them, and then runs your code.
* Automates storage of results to YAML files.
* Easily skips over projects that already have results (overridable).
* gauntlet commandline locates your gauntlet library via rubygems: * eg.
`gauntlet flog` finds gauntlet_flog.rb in the flog gem.


%package       -n gauntlet
Version:       2.1.0
Release:       alt1.1
Summary:       Gauntlet is a pluggable means of running code against all the latest gems and storing off the data executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета gauntlet
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gauntlet) = 2.1.0

%description   -n gauntlet
Gauntlet is a pluggable means of running code against all the latest gems and
storing off the data executable(s).

%description   -n gauntlet -l ru_RU.UTF-8
Исполнямка для самоцвета gauntlet.


%if_enabled    doc
%package       -n gem-gauntlet-doc
Version:       2.1.0
Release:       alt1.1
Summary:       Gauntlet is a pluggable means of running code against all the latest gems and storing off the data documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gauntlet
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gauntlet) = 2.1.0

%description   -n gem-gauntlet-doc
Gauntlet is a pluggable means of running code against all the latest gems and
storing off the data documentation files.

%description   -n gem-gauntlet-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gauntlet.
%endif


%if_enabled    devel
%package       -n gem-gauntlet-devel
Version:       2.1.0
Release:       alt1.1
Summary:       Gauntlet is a pluggable means of running code against all the latest gems and storing off the data development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gauntlet
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gauntlet) = 2.1.0
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(rdoc) >= 4.0
Requires:      gem(hoe) >= 4.2
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(hoe) >= 5

%description   -n gem-gauntlet-devel
Gauntlet is a pluggable means of running code against all the latest gems and
storing off the data development package.

%description   -n gem-gauntlet-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gauntlet.
%endif


%prep
%setup
%autopatch -p1

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc History.txt README.txt
%ruby_gemspec
%ruby_gemlibdir

%files         -n gauntlet
%doc History.txt README.txt
%_bindir/gauntlet

%if_enabled    doc
%files         -n gem-gauntlet-doc
%doc README.txt
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-gauntlet-devel
%doc README.txt
%endif


%changelog
* Fri Sep 27 2024 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1.1
- ! spec

* Fri Jul 17 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- + packaged gem with usage Ruby Policy 2.0
