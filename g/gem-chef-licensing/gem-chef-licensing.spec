%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname chef-licensing

Name:          gem-chef-licensing
Version:       1.4.3
Release:       alt1
Summary:       Chef License storage, generation, and entitlement
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/chef-licensing
Vcs:           https://github.com/chef/chef-licensing.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(chef-config) >= 15
BuildRequires: gem(cookstyle) >= 8.0
BuildRequires: gem(faraday) >= 1
BuildRequires: gem(faraday-http-cache) >= 2.7
BuildRequires: gem(mixlib-log) >= 3.0
BuildRequires: gem(ostruct) >= 0.6.0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pstore) >= 0.1.1
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(tty-prompt) >= 0.23
BuildRequires: gem(tty-spinner) >= 0.9.3
BuildRequires: gem(webmock) >= 3.13.0
BuildConflicts: gem(cookstyle) >= 9
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(mixlib-log) >= 4
BuildConflicts: gem(ostruct) >= 0.7
BuildConflicts: gem(pstore) >= 1
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(tty-prompt) >= 1
BuildConflicts: gem(tty-spinner) >= 0.10
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency pstore >= 0.2.1,pstore < 1
Requires:      ruby >= 3.1.0
Requires:      gem(chef-config) >= 15
Requires:      gem(faraday) >= 1
Requires:      gem(faraday-http-cache) >= 2.7
Requires:      gem(mixlib-log) >= 3.0
Requires:      gem(ostruct) >= 0.6.0
Requires:      gem(pstore) >= 0.1.1
Requires:      gem(tty-prompt) >= 0.23
Requires:      gem(tty-spinner) >= 0.9.3
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(mixlib-log) >= 4
Conflicts:     gem(ostruct) >= 0.7
Conflicts:     gem(pstore) >= 1
Conflicts:     gem(tty-prompt) >= 1
Conflicts:     gem(tty-spinner) >= 0.10
Provides:      gem(chef-licensing) = 1.4.3

%description
Ruby library to support CLI tools that use Progress Chef license storage,
generation, and entitlement.


%if_enabled    doc
%package       -n gem-chef-licensing-doc
Version:       1.4.3
Release:       alt1
Summary:       Chef License storage, generation, and entitlement documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-licensing
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef-licensing) = 1.4.3

%description   -n gem-chef-licensing-doc
Chef License storage, generation, and entitlement documentation files.

%description   -n gem-chef-licensing-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-licensing.
%endif


%if_enabled    devel
%package       -n gem-chef-licensing-devel
Version:       1.4.3
Release:       alt1
Summary:       Chef License storage, generation, and entitlement development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-licensing
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-licensing) = 1.4.3
Requires:      gem(byebug) >= 0
Requires:      gem(chef-config) >= 15
Requires:      gem(cookstyle) >= 8.0
Requires:      gem(faraday) >= 1
Requires:      gem(faraday-http-cache) >= 2.7
Requires:      gem(mixlib-log) >= 3.0
Requires:      gem(ostruct) >= 0.6.0
Requires:      gem(pry) >= 0
Requires:      gem(pstore) >= 0.1.1
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(tty-prompt) >= 0.23
Requires:      gem(tty-spinner) >= 0.9.3
Requires:      gem(webmock) >= 3.13.0
Conflicts:     gem(cookstyle) >= 9
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(mixlib-log) >= 4
Conflicts:     gem(ostruct) >= 0.7
Conflicts:     gem(pstore) >= 1
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(tty-prompt) >= 1
Conflicts:     gem(tty-spinner) >= 0.10

%description   -n gem-chef-licensing-devel
Chef License storage, generation, and entitlement development package.

%description   -n gem-chef-licensing-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-licensing.
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
%files         -n gem-chef-licensing-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-chef-licensing-devel
%doc README.md
%endif


%changelog
* Fri Aug 14 2026 Pavel Skrylev <majioa@altlinux.org> 1.4.3-alt1
- ^ 1.3.0 -> 1.4.3

* Sat Nov 22 2025 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- ^ 0.7.5 -> 1.3.0

* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 0.7.5-alt1
- + packaged gem with Ruby Policy 2.0
