%define        _unpackaged_files_terminate_build 0
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname winrm

Name:          gem-winrm
Version:       2.3.9
Release:       alt1
Summary:       Ruby library for Windows Remote Management
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/WinRb/WinRM
Vcs:           https://github.com/winrb/winrm.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(builder) >= 2.1.2
BuildRequires: gem(erubi) >= 1.8
BuildRequires: gem(gssapi) >= 1.2
BuildRequires: gem(gyoku) >= 1.0
BuildRequires: gem(httpclient) >= 2.2.0.2
BuildRequires: gem(logging) >= 1.6.1
BuildRequires: gem(nori) >= 2.7.1
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 10.3
BuildRequires: gem(rb-readline) >= 0
BuildRequires: gem(rexml) >= 3.0
BuildRequires: gem(rspec) >= 3.2
BuildRequires: gem(rubocop) >= 1.26.0
BuildRequires: gem(rubyntlm) >= 0.6.3
BuildConflicts: gem(erubi) >= 2
BuildConflicts: gem(gssapi) >= 2
BuildConflicts: gem(gyoku) >= 2
BuildConflicts: gem(httpclient) >= 3
BuildConflicts: gem(logging) >= 3.0
BuildConflicts: gem(nori) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rexml) >= 4
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubyntlm) >= 0.7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.81.6,rubocop < 2
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency nori >= 2.7.1,nori < 3
%ruby_ignore_names rwinrm
Requires:      ruby >= 3.0
Requires:      gem(builder) >= 2.1.2
Requires:      gem(erubi) >= 1.8
Requires:      gem(gssapi) >= 1.2
Requires:      gem(gyoku) >= 1.0
Requires:      gem(httpclient) >= 2.2.0.2
Requires:      gem(logging) >= 1.6.1
Requires:      gem(nori) >= 2.7.1
Requires:      gem(rexml) >= 3.0
Requires:      gem(rubyntlm) >= 0.6.3
Conflicts:     gem(erubi) >= 2
Conflicts:     gem(gssapi) >= 2
Conflicts:     gem(gyoku) >= 2
Conflicts:     gem(httpclient) >= 3
Conflicts:     gem(logging) >= 3.0
Conflicts:     gem(nori) >= 3
Conflicts:     gem(rexml) >= 4
Conflicts:     gem(rubyntlm) >= 0.7
Provides:      gem(winrm) = 2.3.9

%description
This is a SOAP library that uses the functionality in Windows Remote Management
(WinRM) to call native object in Windows. This includes, but is not limited to,
running batch scripts, powershell scripts and fetching WMI variables. For more
information on WinRM, please visit Microsoft's WinRM site.

As of version 2.0, this gem retains the WinRM name but all powershell calls use
the more modern Powershell Remoting Protocol (PSRP) for initializing runspace
pools as well as creating and processing powershell pipelines.


%if_enabled    doc
%package       -n gem-winrm-doc
Version:       2.3.9
Release:       alt1
Summary:       Ruby library for Windows Remote Management documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета winrm
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(winrm) = 2.3.9

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
%endif


%if_enabled    devel
%package       -n gem-winrm-devel
Version:       2.3.9
Release:       alt1
Summary:       Ruby library for Windows Remote Management development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета winrm
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(winrm) = 2.3.9
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 10.3
Requires:      gem(rb-readline) >= 0
Requires:      gem(rspec) >= 3.2
Requires:      gem(rubocop) >= 1.26.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2

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
%doc LICENSE README.md changelog.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-winrm-doc
%doc LICENSE README.md changelog.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-winrm-devel
%doc LICENSE README.md changelog.md
%endif


%changelog
* Sat Nov 22 2025 Pavel Skrylev <majioa@altlinux.org> 2.3.9-alt1
- ^ 2.3.6 -> 2.3.9
- * define explicit dependencies

* Thu Jul 15 2021 Pavel Skrylev <majioa@altlinux.org> 2.3.6-alt1
- ^ 2.3.1 -> 2.3.6

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 2.3.1-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
