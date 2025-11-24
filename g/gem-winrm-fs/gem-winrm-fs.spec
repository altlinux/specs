%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname winrm-fs

Name:          gem-winrm-fs
Version:       1.3.5.7
Release:       alt0.1
Summary:       WinRM File Manager
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/WinRb/winrm-fs
Vcs:           https://github.com/winrb/winrm-fs.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(erubi) >= 1.7
BuildRequires: gem(logging) >= 1.6.1
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 10.3
BuildRequires: gem(rb-readline) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubyzip) >= 2.0
BuildRequires: gem(winrm) >= 2.0
BuildConflicts: gem(logging) >= 3.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubyzip) >= 3
BuildConflicts: gem(winrm) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      ruby >= 2.5.0
Requires:      gem(erubi) >= 1.7
Requires:      gem(logging) >= 1.6.1
Requires:      gem(rb-readline) >= 0
Requires:      gem(rubyzip) >= 2.0
Requires:      gem(winrm) >= 2.0
Conflicts:     gem(logging) >= 3.0
Conflicts:     gem(rubyzip) >= 3
Conflicts:     gem(winrm) >= 3
Provides:      gem(winrm-fs) = 1.3.5.7

%ruby_use_gem_version winrm-fs:1.3.5.7

%description
WinRM File Manager.

Files may be copied from the local machine to the winrm endpoint. Individual
files or directories, as well as arrays of files and directories may be
specified.


%package       -n rwinrmcp-utils
Version:       1.3.5.7
Release:       alt0.1
Summary:       WinRM File Manager executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета winrm-fs
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(winrm-fs) = 1.3.5.7
Requires:      gem(rb-readline) >= 0
Conflicts:     rwinrmcp

%description   -n rwinrmcp-utils
WinRM File Manager executable(s).

%description   -n rwinrmcp-utils -l ru_RU.UTF-8
Исполнямка для самоцвета winrm-fs.


%if_enabled    doc
%package       -n gem-winrm-fs-doc
Version:       1.3.5.7
Release:       alt0.1
Summary:       WinRM File Manager documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета winrm-fs
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(winrm-fs) = 1.3.5.7

%description   -n gem-winrm-fs-doc
WinRM File Manager documentation files.

%description   -n gem-winrm-fs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета winrm-fs.
%endif


%if_enabled    devel
%package       -n gem-winrm-fs-devel
Version:       1.3.5.7
Release:       alt0.1
Summary:       WinRM File Manager development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета winrm-fs
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(winrm-fs) = 1.3.5.7
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 10.3
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1.15.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2

%description   -n gem-winrm-fs-devel
WinRM File Manager development package.

%description   -n gem-winrm-fs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета winrm-fs.
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

%files         -n rwinrmcp-utils
%doc LICENSE README.md changelog.md
%_bindir/rwinrmcp

%if_enabled    doc
%files         -n gem-winrm-fs-doc
%doc LICENSE README.md changelog.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-winrm-fs-devel
%doc LICENSE README.md changelog.md
%endif


%changelog
* Sun Nov 23 2025 Pavel Skrylev <majioa@altlinux.org> 1.3.5.7-alt0.1
- * define explicit dependencies
- ^ 1.3.5 -> 1.3.5p7

* Thu Dec 17 2020 Pavel Skrylev <majioa@altlinux.org> 1.3.5-alt1
- ^ 1.3.2 -> 1.3.5
- ! spec

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.2-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
