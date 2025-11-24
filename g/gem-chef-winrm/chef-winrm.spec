%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname chef-winrm

Name:          gem-chef-winrm
Version:       2.4.4
Release:       alt1
Summary:       Ruby library for Windows Remote Management
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/WinRb/WinRM
Vcs:           https://github.com/winrb/winrm.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(benchmark) >= 0
BuildRequires: gem(builder) >= 2.1.2
BuildRequires: gem(chef-gyoku) >= 1.5
BuildRequires: gem(cookstyle) >= 8.1
BuildRequires: gem(erubi) >= 1.8
BuildRequires: gem(fiddle) >= 0
BuildRequires: gem(gssapi) >= 1.2
BuildRequires: gem(httpclient) >= 2.2.0.2
BuildRequires: gem(logging) >= 1.6.1
BuildRequires: gem(nori) >= 2.7.0
BuildRequires: gem(ostruct) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 10.3
BuildRequires: gem(rb-readline) >= 0
BuildRequires: gem(rexml) >= 3.3
BuildRequires: gem(rspec) >= 3.2
BuildRequires: gem(rubyntlm) >= 0.6.3
BuildRequires: gem(syslog) >= 0
BuildConflicts: gem(chef-gyoku) >= 2
BuildConflicts: gem(cookstyle) >= 9
BuildConflicts: gem(erubi) >= 2
BuildConflicts: gem(gssapi) >= 2
BuildConflicts: gem(httpclient) >= 3
BuildConflicts: gem(logging) >= 3.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rexml) >= 4
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubyntlm) >= 0.7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency nori >= 2.7.1,nori < 3
%ruby_use_gem_dependency rake >= 13.0,rake < 14
Requires:      ruby >= 3.1
Requires:      gem(builder) >= 2.1.2
Requires:      gem(chef-gyoku) >= 1.5
Requires:      gem(erubi) >= 1.8
Requires:      gem(gssapi) >= 1.2
Requires:      gem(httpclient) >= 2.2.0.2
Requires:      gem(logging) >= 1.6.1
Requires:      gem(nori) >= 2.7.0
Requires:      gem(rexml) >= 3.3
Requires:      gem(rubyntlm) >= 0.6.3
Conflicts:     gem(chef-gyoku) >= 2
Conflicts:     gem(erubi) >= 2
Conflicts:     gem(gssapi) >= 2
Conflicts:     gem(httpclient) >= 3
Conflicts:     gem(logging) >= 3.0
Conflicts:     gem(rexml) >= 4
Conflicts:     gem(rubyntlm) >= 0.7
Provides:      gem(chef-winrm) = 2.4.4

%description
Ruby library for Windows Remote Management


%package       -n rwinrm
Version:       2.4.4
Release:       alt1
Summary:       Ruby library for Windows Remote Management executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета chef-winrm
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef-winrm) = 2.4.4

%description   -n rwinrm
Ruby library for Windows Remote Management executable(s).

%description   -n rwinrm -l ru_RU.UTF-8
Исполнямка для самоцвета chef-winrm.


%if_enabled    doc
%package       -n gem-chef-winrm-doc
Version:       2.4.4
Release:       alt1
Summary:       Ruby library for Windows Remote Management documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-winrm
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef-winrm) = 2.4.4

%description   -n gem-chef-winrm-doc
Ruby library for Windows Remote Management documentation files.

%description   -n gem-chef-winrm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-winrm.
%endif


%if_enabled    devel
%package       -n gem-chef-winrm-devel
Version:       2.4.4
Release:       alt1
Summary:       Ruby library for Windows Remote Management development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-winrm
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef-winrm) = 2.4.4
Requires:      gem(benchmark) >= 0
Requires:      gem(cookstyle) >= 8.1
Requires:      gem(fiddle) >= 0
Requires:      gem(ostruct) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 10.3
Requires:      gem(rb-readline) >= 0
Requires:      gem(rspec) >= 3.2
Requires:      gem(syslog) >= 0
Conflicts:     gem(cookstyle) >= 9
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4

%description   -n gem-chef-winrm-devel
Ruby library for Windows Remote Management development package.

%description   -n gem-chef-winrm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-winrm.
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

%files         -n rwinrm
%doc LICENSE README.md changelog.md
%_bindir/rwinrm

%if_enabled    doc
%files         -n gem-chef-winrm-doc
%doc LICENSE README.md changelog.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-chef-winrm-devel
%doc LICENSE README.md changelog.md
%endif


%changelog
* Sat Nov 22 2025 Pavel Skrylev <majioa@altlinux.org> 2.4.4-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
