%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname train-winrm

Name:          gem-train-winrm
Version:       0.4.1
Release:       alt1
Summary:       Windows WinRM API Transport for Train
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/inspec/train-winrm
Vcs:           https://github.com/inspec/train-winrm.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(chef-winrm) >= 2.4.4
BuildRequires: gem(chef-winrm-elevated) >= 1.2.5
BuildRequires: gem(chef-winrm-fs) >= 1.4.1
BuildRequires: gem(cookstyle) >= 7.32.8
BuildRequires: gem(m) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(socksify) >= 1.8
BuildRequires: gem(syslog) >= 0
BuildRequires: gem(train-core) >= 3.0
BuildConflicts: gem(chef-winrm) >= 2.5
BuildConflicts: gem(chef-winrm-elevated) >= 1.3
BuildConflicts: gem(chef-winrm-fs) >= 1.5
BuildConflicts: gem(socksify) >= 2
BuildConflicts: gem(train-core) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.1.0
Requires:      gem(chef-winrm) >= 2.4.4
Requires:      gem(chef-winrm-elevated) >= 1.2.5
Requires:      gem(chef-winrm-fs) >= 1.4.1
Requires:      gem(socksify) >= 1.8
Conflicts:     gem(chef-winrm) >= 2.5
Conflicts:     gem(chef-winrm-elevated) >= 1.3
Conflicts:     gem(chef-winrm-fs) >= 1.5
Conflicts:     gem(socksify) >= 2
Provides:      gem(train-winrm) = 0.4.1

%description
Allows applictaions using Train to speak to Windows using Remote Management;
handles authentication, cacheing, and SDK dependency management.


%if_enabled    doc
%package       -n gem-train-winrm-doc
Version:       0.4.1
Release:       alt1
Summary:       Windows WinRM API Transport for Train documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета train-winrm
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(train-winrm) = 0.4.1

%description   -n gem-train-winrm-doc
Windows WinRM API Transport for Train documentation files.

Allows applictaions using Train to speak to Windows using Remote Management;
handles authentication, cacheing, and SDK dependency management.

%description   -n gem-train-winrm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета train-winrm.
%endif


%if_enabled    devel
%package       -n gem-train-winrm-devel
Version:       0.4.1
Release:       alt1
Summary:       Windows WinRM API Transport for Train development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета train-winrm
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(train-winrm) = 0.4.1
Requires:      gem(bundler) >= 0
Requires:      gem(byebug) >= 0
Requires:      gem(cookstyle) >= 7.32.8
Requires:      gem(m) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(syslog) >= 0
Requires:      gem(train-core) >= 3.0
Conflicts:     gem(train-core) >= 4

%description   -n gem-train-winrm-devel
Windows WinRM API Transport for Train development package.

Allows applictaions using Train to speak to Windows using Remote Management;
handles authentication, cacheing, and SDK dependency management.

%description   -n gem-train-winrm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета train-winrm.
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
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-train-winrm-doc
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-train-winrm-devel
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%endif


%changelog
* Sat Nov 22 2025 Pavel Skrylev <majioa@altlinux.org> 0.4.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
