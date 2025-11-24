%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname chef-winrm-elevated

Name:          gem-chef-winrm-elevated
Version:       1.2.5
Release:       alt1
Summary:       Ruby library for running commands as elevated
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/chef-winrm-elevated
Vcs:           https://github.com/chef/chef-winrm-elevated.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(chef-winrm) >= 2.4
BuildRequires: gem(chef-winrm-fs) >= 1.4
BuildRequires: gem(cookstyle) >= 8.1
BuildRequires: gem(erubi) >= 1.8
BuildRequires: gem(fiddle) >= 0
BuildRequires: gem(rake) >= 13.2.1
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(rspec) >= 3.2
BuildConflicts: gem(chef-winrm) >= 3
BuildConflicts: gem(chef-winrm-fs) >= 2
BuildConflicts: gem(cookstyle) >= 9
BuildConflicts: gem(erubi) >= 2
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.1
Requires:      gem(chef-winrm) >= 2.4
Requires:      gem(chef-winrm-fs) >= 1.4
Requires:      gem(erubi) >= 1.8
Conflicts:     gem(chef-winrm) >= 3
Conflicts:     gem(chef-winrm-fs) >= 2
Conflicts:     gem(erubi) >= 2
Provides:      gem(chef-winrm-elevated) = 1.2.5

%description
Ruby library for running commands via WinRM as elevated through a scheduled task


%if_enabled    doc
%package       -n gem-chef-winrm-elevated-doc
Version:       1.2.5
Release:       alt1
Summary:       Ruby library for running commands as elevated documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-winrm-elevated
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef-winrm-elevated) = 1.2.5

%description   -n gem-chef-winrm-elevated-doc
Ruby library for running commands as elevated documentation files.

Ruby library for running commands via WinRM as elevated through a scheduled task

%description   -n gem-chef-winrm-elevated-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-winrm-elevated.
%endif


%if_enabled    devel
%package       -n gem-chef-winrm-elevated-devel
Version:       1.2.5
Release:       alt1
Summary:       Ruby library for running commands as elevated development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-winrm-elevated
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef-winrm-elevated) = 1.2.5
Requires:      gem(cookstyle) >= 8.1
Requires:      gem(fiddle) >= 0
Requires:      gem(rake) >= 13.2.1
Requires:      gem(rexml) >= 0
Requires:      gem(rspec) >= 3.2
Conflicts:     gem(cookstyle) >= 9
Conflicts:     gem(rspec) >= 4

%description   -n gem-chef-winrm-elevated-devel
Ruby library for running commands as elevated development package.

Ruby library for running commands via WinRM as elevated through a scheduled task

%description   -n gem-chef-winrm-elevated-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-winrm-elevated.
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
%files         -n gem-chef-winrm-elevated-doc
%doc LICENSE README.md changelog.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-chef-winrm-elevated-devel
%doc LICENSE README.md changelog.md
%endif


%changelog
* Sun Nov 23 2025 Pavel Skrylev <majioa@altlinux.org> 1.2.5-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
