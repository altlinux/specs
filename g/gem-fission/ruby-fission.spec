%define        gemname fission

Name:          gem-fission
Version:       0.5.0
Release:       alt2
Summary:       command line tool to manage vmware fusion vms
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/thbishop/fission
Vcs:           https://github.com/thbishop/fission.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(CFPropertyList) >= 2.2 gem(CFPropertyList) < 4
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(fakefs) >= 0.4.3 gem(fakefs) < 2
BuildRequires: gem(rspec) >= 2.14 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency CFPropertyList >= 2.2,CFPropertyList < 4
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency fakefs >= 1.3.2,fakefs < 2
Requires:      gem(CFPropertyList) >= 2.2 gem(CFPropertyList) < 4
Obsoletes:     ruby-fission < %EVR
Provides:      ruby-fission = %EVR
Provides:      gem(fission) = 0.5.0


%description
A simple utility to manage VMware Fusion VMs from the command line. Only Fusion
3.x is currently supported. See Fusion Version Support for more info.


%package       -n fission
Version:       0.5.0
Release:       alt2
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


%package       -n gem-fission-doc
Version:       0.5.0
Release:       alt2
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


%package       -n gem-fission-devel
Version:       0.5.0
Release:       alt2
Summary:       command line tool to manage vmware fusion vms development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fission
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fission) = 0.5.0
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(fakefs) >= 0.4.3 gem(fakefs) < 2
Requires:      gem(rspec) >= 2.14 gem(rspec) < 4

%description   -n gem-fission-devel
command line tool to manage vmware fusion vms development package.

A simple utility to manage VMware Fusion VMs from the command line. Only Fusion
3.x is currently supported. See Fusion Version Support for more info.

%description   -n gem-fission-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fission.


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

%files         -n gem-fission-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fission-devel
%doc README.md


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt2
- ! spec

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus
