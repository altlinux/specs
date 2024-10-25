%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname fog-aliyun

Name:          gem-fog-aliyun
Version:       0.4.0
Release:       alt1
Summary:       Fog provider for aliyun
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-aliyun
Vcs:           https://github.com/fog/fog-aliyun.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(mime-types) >= 3.4
BuildRequires: gem(pry-nav) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(memory_profiler) >= 0
BuildRequires: gem(aliyun-sdk) >= 0.8.0
BuildRequires: gem(addressable) >= 2.8.0
BuildRequires: gem(fog-core) >= 0
BuildRequires: gem(fog-json) >= 0
BuildRequires: gem(ipaddress) >= 0.8
BuildRequires: gem(xml-simple) >= 1.1
BuildConflicts: gem(mime-types) >= 4
BuildConflicts: gem(aliyun-sdk) >= 0.9
BuildConflicts: gem(addressable) >= 3
BuildConflicts: gem(ipaddress) >= 1
BuildConflicts: gem(xml-simple) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency addressable >= 2.8.0,addressable < 3
Requires:      gem(aliyun-sdk) >= 0.8.0
Requires:      gem(addressable) >= 2.8.0
Requires:      gem(fog-core) >= 0
Requires:      gem(fog-json) >= 0
Requires:      gem(ipaddress) >= 0.8
Requires:      gem(xml-simple) >= 1.1
Conflicts:     gem(aliyun-sdk) >= 0.9
Conflicts:     gem(addressable) >= 3
Conflicts:     gem(ipaddress) >= 1
Conflicts:     gem(xml-simple) >= 2
Obsoletes:     ruby-fog-aliyun < %EVR
Provides:      ruby-fog-aliyun = %EVR
Provides:      gem(fog-aliyun) = 0.4.0


%description
Fog provider for aliyun.


%if_enabled    doc
%package       -n gem-fog-aliyun-doc
Version:       0.4.0
Release:       alt1
Summary:       Fog provider for aliyun documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-aliyun
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-aliyun) = 0.4.0

%description   -n gem-fog-aliyun-doc
Fog provider for aliyun documentation files.

%description   -n gem-fog-aliyun-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-aliyun.
%endif


%if_enabled    devel
%package       -n gem-fog-aliyun-devel
Version:       0.4.0
Release:       alt1
Summary:       Fog provider for aliyun development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-aliyun
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-aliyun) = 0.4.0
Requires:      gem(bundler) >= 0
Requires:      gem(mime-types) >= 3.4
Requires:      gem(pry-nav) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(memory_profiler) >= 0
Conflicts:     gem(mime-types) >= 4

%description   -n gem-fog-aliyun-devel
Fog provider for aliyun development package.

%description   -n gem-fog-aliyun-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-aliyun.
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
%files         -n gem-fog-aliyun-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fog-aliyun-devel
%doc README.md
%endif


%changelog
* Thu Oct 24 2024 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- ^ 0.3.13 -> 0.4.0

* Thu Jun 18 2020 Pavel Skrylev <majioa@altlinux.org> 0.3.13-alt1
- > Ruby Policy 2.0
- ^ 0.3.2 -> 0.3.13

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt1
- New version.

* Fri Jun 22 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1
- New version.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus
