%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname thin

Name:          gem-thin
Version:       1.8.2
Release:       alt1
Summary:       A very fast & simple Ruby web server
License:       GPL-2.0+ or Ruby
Group:         Development/Ruby
Url:           https://github.com/macournoyer/thin
Vcs:           https://github.com/macournoyer/thin.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rspec) >= 3.5
BuildRequires: gem(rack) >= 1
BuildRequires: gem(eventmachine) >= 1.0.4
BuildRequires: gem(daemons) >= 1.0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rack) >= 4
BuildConflicts: gem(eventmachine) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency daemons >= 1.4.0,daemons < 2
%ruby_use_gem_dependency rack >= 3.0.0,rack < 4
Requires:      gem(rack) >= 1
Requires:      gem(eventmachine) >= 1.0.4
Requires:      gem(daemons) >= 1.0
Conflicts:     gem(rack) >= 4
Conflicts:     gem(eventmachine) >= 2
Provides:      gem(thin) = 1.8.2


%description
A very fast & simple Ruby web server.


%package       -n thin
Version:       1.8.2
Release:       alt1
Summary:       A very fast & simple Ruby web server executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета thin
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(thin) = 1.8.2

%description   -n thin
A very fast & simple Ruby web server executable(s).

%description   -n thin -l ru_RU.UTF-8
Исполнямка для самоцвета thin.


%if_enabled    doc
%package       -n gem-thin-doc
Version:       1.8.2
Release:       alt1
Summary:       A very fast & simple Ruby web server documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета thin
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(thin) = 1.8.2

%description   -n gem-thin-doc
A very fast & simple Ruby web server documentation files.

%description   -n gem-thin-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета thin.
%endif


%if_enabled    devel
%package       -n gem-thin-devel
Version:       1.8.2
Release:       alt1
Summary:       A very fast & simple Ruby web server development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета thin
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(thin) = 1.8.2
Requires:      gem(rake-compiler) >= 0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rspec) >= 3.5
Conflicts:     gem(rspec) >= 4

%description   -n gem-thin-devel
A very fast & simple Ruby web server development package.

%description   -n gem-thin-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета thin.
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
%doc README.md example/thin_solaris_smf.readme.txt
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n thin
%doc README.md example/thin_solaris_smf.readme.txt
%_bindir/thin

%if_enabled    doc
%files         -n gem-thin-doc
%doc README.md example/thin_solaris_smf.readme.txt
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-thin-devel
%doc README.md example/thin_solaris_smf.readme.txt
%ruby_includedir/*
%endif


%changelog
* Tue Apr 16 2024 Pavel Skrylev <majioa@altlinux.org> 1.8.2-alt1
- ^ 1.8.1 -> 1.8.2

* Thu Mar 17 2022 Pavel Skrylev <majioa@altlinux.org> 1.8.1-alt1
- ^ 1.8.0 -> 1.8.1

* Sat Apr 24 2021 Pavel Skrylev <majioa@altlinux.org> 1.8.0-alt1
- new version 1.8.0

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 1.7.2-alt1.1
- ! spec syntax and tags

* Thu Apr 11 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.7.2-alt1
- Initial build for Sisyphus
