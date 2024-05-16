%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname useragent

Name:          gem-useragent
Version:       0.16.10.4
Release:       alt0.1
Summary:       HTTP User Agent parser
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/gshutler/useragent
Vcs:           https://github.com/gshutler/useragent.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(rspec) >= 3.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
Obsoletes:     ruby-useragent < %EVR
Provides:      ruby-useragent = %EVR
Provides:      gem(useragent) = 0.16.10.4

%ruby_use_gem_version useragent:0.16.10.4

%description
UserAgent is a Ruby library that parses and compares HTTP User Agents.


%if_enabled    doc
%package       -n gem-useragent-doc
Version:       0.16.10.4
Release:       alt0.1
Summary:       HTTP User Agent parser documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета useragent
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(useragent) = 0.16.10.4

%description   -n gem-useragent-doc
HTTP User Agent parser documentation files.

UserAgent is a Ruby library that parses and compares HTTP User Agents.

%description   -n gem-useragent-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета useragent.
%endif


%if_enabled    devel
%package       -n gem-useragent-devel
Version:       0.16.10.4
Release:       alt0.1
Summary:       HTTP User Agent parser development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета useragent
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(useragent) = 0.16.10.4
Requires:      gem(rake) >= 10.0
Requires:      gem(rspec) >= 3.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4

%description   -n gem-useragent-devel
HTTP User Agent parser development package.

UserAgent is a Ruby library that parses and compares HTTP User Agents.

%description   -n gem-useragent-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета useragent.
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
%files         -n gem-useragent-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-useragent-devel
%doc README.md
%endif


%changelog
* Wed Apr 24 2024 Pavel Skrylev <majioa@altlinux.org> 0.16.10.4-alt0.1
- ^ 0.16.10 -> 0.16.10p4

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.16.10-alt1.1
- Rebuild for new Ruby autorequirements.

* Fri Jun 01 2018 Andrey Cherepanov <cas@altlinux.org> 0.16.10-alt1
- Initial build for Sisyphus
