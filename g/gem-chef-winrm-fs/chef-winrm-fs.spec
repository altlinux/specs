%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname chef-winrm-fs

Name:          gem-chef-winrm-fs
Version:       1.4.2
Release:       alt1
Summary:       WinRM File System
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://github.com/WinRb/winrm-fs
Vcs:           https://github.com/winrb/winrm-fs.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(benchmark) >= 0.5.0
BuildRequires: gem(chef-winrm) >= 2.4
BuildRequires: gem(cookstyle) >= 8.5
BuildRequires: gem(csv) >= 3.3
BuildRequires: gem(erubi) >= 1.7
BuildRequires: gem(logging) >= 1.6.1
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 13.2.1
BuildRequires: gem(rb-readline) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubyzip) >= 2.0
BuildConflicts: gem(benchmark) >= 0.6
BuildConflicts: gem(chef-winrm) >= 3
BuildConflicts: gem(cookstyle) >= 9
BuildConflicts: gem(csv) >= 4
BuildConflicts: gem(logging) >= 3.0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubyzip) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.1
Requires:      gem(benchmark) >= 0.5.0
Requires:      gem(chef-winrm) >= 2.4
Requires:      gem(csv) >= 3.3
Requires:      gem(erubi) >= 1.7
Requires:      gem(logging) >= 1.6.1
Requires:      gem(rb-readline) >= 0
Requires:      gem(rubyzip) >= 2.0
Conflicts:     gem(benchmark) >= 0.6
Conflicts:     gem(chef-winrm) >= 3
Conflicts:     gem(csv) >= 4
Conflicts:     gem(logging) >= 3.0
Conflicts:     gem(rubyzip) >= 3
Provides:      gem(chef-winrm-fs) = 1.4.2

%description
Ruby library for file system operations via Windows Remote Management


%package       -n rwinrmcp
Version:       1.4.2
Release:       alt1
Summary:       WinRM File System executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета chef-winrm-fs
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef-winrm-fs) = 1.4.2
Requires:      gem(rb-readline) >= 0

%description   -n rwinrmcp
WinRM File System executable(s).

Ruby library for file system operations via Windows Remote Management

%description   -n rwinrmcp -l ru_RU.UTF-8
Исполнямка для самоцвета chef-winrm-fs.


%if_enabled    doc
%package       -n gem-chef-winrm-fs-doc
Version:       1.4.2
Release:       alt1
Summary:       WinRM File System documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-winrm-fs
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef-winrm-fs) = 1.4.2

%description   -n gem-chef-winrm-fs-doc
WinRM File System documentation files.

Ruby library for file system operations via Windows Remote Management

%description   -n gem-chef-winrm-fs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-winrm-fs.
%endif


%if_enabled    devel
%package       -n gem-chef-winrm-fs-devel
Version:       1.4.2
Release:       alt1
Summary:       WinRM File System development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-winrm-fs
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef-winrm-fs) = 1.4.2
Requires:      gem(cookstyle) >= 8.5
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 13.2.1
Requires:      gem(rspec) >= 3.0
Conflicts:     gem(cookstyle) >= 9
Conflicts:     gem(rspec) >= 4

%description   -n gem-chef-winrm-fs-devel
WinRM File System development package.

Ruby library for file system operations via Windows Remote Management

%description   -n gem-chef-winrm-fs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-winrm-fs.
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

%files         -n rwinrmcp
%doc LICENSE README.md changelog.md
%_bindir/rwinrmcp

%if_enabled    doc
%files         -n gem-chef-winrm-fs-doc
%doc LICENSE README.md changelog.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-chef-winrm-fs-devel
%doc LICENSE README.md changelog.md
%endif


%changelog
* Sun Nov 23 2025 Pavel Skrylev <majioa@altlinux.org> 1.4.2-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
