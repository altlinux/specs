%define        gemname winrm

Name:          gem-winrm
Version:       2.3.6
Release:       alt1
Summary:       Ruby library for Windows Remote Management
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/WinRb/WinRM
Vcs:           https://github.com/winrb/winrm.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(builder) >= 2.1.2
BuildRequires: gem(erubi) >= 1.8 gem(erubi) < 2
BuildRequires: gem(gssapi) >= 1.2 gem(gssapi) < 2
BuildRequires: gem(gyoku) >= 1.0 gem(gyoku) < 2
BuildRequires: gem(httpclient) >= 2.2.0.2 gem(httpclient) < 3
BuildRequires: gem(logging) >= 1.6.1 gem(logging) < 3.0
BuildRequires: gem(nori) >= 2.0 gem(nori) < 3
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 10.3 gem(rake) < 14
BuildRequires: gem(rb-readline) >= 0
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(rspec) >= 3.2 gem(rspec) < 4
BuildRequires: gem(rubocop) >= 0.51.0 gem(rubocop) < 2
BuildRequires: gem(rubyntlm) >= 0.6.3 gem(rubyntlm) < 0.7

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(builder) >= 2.1.2
Requires:      gem(erubi) >= 1.8 gem(erubi) < 2
Requires:      gem(gssapi) >= 1.2 gem(gssapi) < 2
Requires:      gem(gyoku) >= 1.0 gem(gyoku) < 2
Requires:      gem(httpclient) >= 2.2.0.2 gem(httpclient) < 3
Requires:      gem(logging) >= 1.6.1 gem(logging) < 3.0
Requires:      gem(nori) >= 2.0 gem(nori) < 3
Requires:      gem(rubyntlm) >= 0.6.3 gem(rubyntlm) < 0.7
Provides:      gem(winrm) = 2.3.6


%description
%summary.

This is a SOAP library that uses the functionality in Windows Remote Management
(WinRM) to call native object in Windows. This includes, but is not limited to,
running batch scripts, powershell scripts and fetching WMI variables. For more
information on WinRM, please visit Microsoft's WinRM site.

As of version 2.0, this gem retains the WinRM name but all powershell calls use
the more modern Powershell Remoting Protocol (PSRP) for initializing runspace
pools as well as creating and processing powershell pipelines.


%package       -n rwinrm
Version:       2.3.6
Release:       alt1
Summary:       Ruby library for Windows Remote Management executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета winrm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(winrm) = 2.3.6

%description   -n rwinrm
Ruby library for Windows Remote Management executable(s).

This is a SOAP library that uses the functionality in Windows Remote Management
(WinRM) to call native object in Windows. This includes, but is not limited to,
running batch scripts, powershell scripts and fetching WMI variables. For more
information on WinRM, please visit Microsoft's WinRM site.

As of version 2.0, this gem retains the WinRM name but all powershell calls use
the more modern Powershell Remoting Protocol (PSRP) for initializing runspace
pools as well as creating and processing powershell pipelines.

%description   -n rwinrm -l ru_RU.UTF-8
Исполнямка для самоцвета winrm.


%package       -n gem-winrm-doc
Version:       2.3.6
Release:       alt1
Summary:       Ruby library for Windows Remote Management documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета winrm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(winrm) = 2.3.6

%description   -n gem-winrm-doc
Ruby library for Windows Remote Management documentation files.

This is a SOAP library that uses the functionality in Windows Remote Management
(WinRM) to call native object in Windows. This includes, but is not limited to,
running batch scripts, powershell scripts and fetching WMI variables. For more
information on WinRM, please visit Microsoft's WinRM site.

As of version 2.0, this gem retains the WinRM name but all powershell calls use
the more modern Powershell Remoting Protocol (PSRP) for initializing runspace
pools as well as creating and processing powershell pipelines.

%description   -n gem-winrm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета winrm.


%package       -n gem-winrm-devel
Version:       2.3.6
Release:       alt1
Summary:       Ruby library for Windows Remote Management development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета winrm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(winrm) = 2.3.6
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 10.3 gem(rake) < 14
Requires:      gem(rb-readline) >= 0
Requires:      gem(rexml) >= 0
Requires:      gem(rspec) >= 3.2 gem(rspec) < 4
Requires:      gem(rubocop) >= 0.51.0 gem(rubocop) < 2

%description   -n gem-winrm-devel
Ruby library for Windows Remote Management development package.

This is a SOAP library that uses the functionality in Windows Remote Management
(WinRM) to call native object in Windows. This includes, but is not limited to,
running batch scripts, powershell scripts and fetching WMI variables. For more
information on WinRM, please visit Microsoft's WinRM site.

As of version 2.0, this gem retains the WinRM name but all powershell calls use
the more modern Powershell Remoting Protocol (PSRP) for initializing runspace
pools as well as creating and processing powershell pipelines.

%description   -n gem-winrm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета winrm.


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

%files         -n rwinrm
%doc README.md
%_bindir/rwinrm

%files         -n gem-winrm-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-winrm-devel
%doc README.md


%changelog
* Thu Jul 15 2021 Pavel Skrylev <majioa@altlinux.org> 2.3.6-alt1
- ^ 2.3.1 -> 2.3.6

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 2.3.1-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
