%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname fission

Name:          gem-fission
Version:       0.5.0
Release:       alt2.1
Summary:       command line tool to manage vmware fusion vms
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/thbishop/fission
Vcs:           https://github.com/thbishop/fission.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(fakefs) >= 0.4.3
BuildRequires: gem(rspec) >= 2.14
BuildRequires: gem(CFPropertyList) >= 2.2
BuildConflicts: gem(fakefs) >= 3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(CFPropertyList) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency fakefs >= 2.5.0,fakefs < 3
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency CFPropertyList >= 3.0.6,CFPropertyList < 4
Requires:      gem(CFPropertyList) >= 2.2
Conflicts:     gem(CFPropertyList) >= 4
Obsoletes:     ruby-fission < %EVR
Provides:      ruby-fission = %EVR
Provides:      gem(fission) = 0.5.0


%description
A simple utility to manage VMware Fusion VMs from the command line. Only Fusion
3.x is currently supported. See Fusion Version Support for more info.


%package       -n fission
Version:       0.5.0
Release:       alt2.1
Summary:       command line tool to manage vmware fusion vms executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета fission
Group:         Other
BuildArch:     noarch

Requires:      gem(fission) = 0.5.0

%description   -n fission
command line tool to manage vmware fusion vms executable(s).

A simple utility to manage VMware Fusion VMs from the command line. Only Fusion
3.x is currently supported. See Fusion Version Support for more info.

%description   -n fission -l ru_RU.UTF-8
Исполнямка для самоцвета fission.


%if_enabled    doc
%package       -n gem-fission-doc
Version:       0.5.0
Release:       alt2.1
Summary:       command line tool to manage vmware fusion vms documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fission
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fission) = 0.5.0

%description   -n gem-fission-doc
command line tool to manage vmware fusion vms documentation files.

A simple utility to manage VMware Fusion VMs from the command line. Only Fusion
3.x is currently supported. See Fusion Version Support for more info.

%description   -n gem-fission-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fission.
%endif


%if_enabled    devel
%package       -n gem-fission-devel
Version:       0.5.0
Release:       alt2.1
Summary:       command line tool to manage vmware fusion vms development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fission
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fission) = 0.5.0
Requires:      gem(rake) >= 0
Requires:      gem(fakefs) >= 0.4.3
Requires:      gem(rspec) >= 2.14
Conflicts:     gem(fakefs) >= 3
Conflicts:     gem(rspec) >= 4

%description   -n gem-fission-devel
command line tool to manage vmware fusion vms development package.

A simple utility to manage VMware Fusion VMs from the command line. Only Fusion
3.x is currently supported. See Fusion Version Support for more info.

%description   -n gem-fission-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fission.
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

%files         -n fission
%doc README.md
%_bindir/fission

%if_enabled    doc
%files         -n gem-fission-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fission-devel
%doc README.md
%endif


%changelog
* Sat Aug 03 2024 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt2.1
- ! spec format with fix dep to fakefs

* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt2
- ! spec

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus
