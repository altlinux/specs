%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname chef-licensing

Name:          gem-chef-licensing
Version:       0.7.5
Release:       alt1
Summary:       Chef License storage, generation, and entitlement
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/chef-licensing
Vcs:           https://github.com/chef/chef-licensing.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(chefstyle) >= 2.2
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(webmock) >= 3.13.0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(chef-config) >= 15
BuildRequires: gem(tty-prompt) >= 0.23
BuildRequires: gem(faraday) >= 1
BuildRequires: gem(faraday-http-cache) >= 0
BuildRequires: gem(tty-spinner) >= 0.9.3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(tty-prompt) >= 1
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(activesupport) >= 8
BuildConflicts: gem(tty-spinner) >= 0.10
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency activesupport >= 6.1.3.2,activesupport < 7
%ruby_use_gem_dependency chefstyle >= 2.2.2,chefstyle < 3
%ruby_ignore_names gem-chef-licensing
Requires:      gem(chef-config) >= 15
Requires:      gem(tty-prompt) >= 0.23
Requires:      gem(faraday) >= 1
Requires:      gem(faraday-http-cache) >= 0
Requires:      gem(tty-spinner) >= 0.9.3
Conflicts:     gem(tty-prompt) >= 1
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(activesupport) >= 8
Conflicts:     gem(tty-spinner) >= 0.10
Provides:      gem(chef-licensing) = 0.7.5


%description
Ruby library to support CLI tools that use Progress Chef license storage,
generation, and entitlement.


%if_enabled    doc
%package       -n gem-chef-licensing-doc
Version:       0.7.5
Release:       alt1
Summary:       Chef License storage, generation, and entitlement documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-licensing
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef-licensing) = 0.7.5

%description   -n gem-chef-licensing-doc
Chef License storage, generation, and entitlement documentation files.

%description   -n gem-chef-licensing-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-licensing.
%endif


%if_enabled    devel
%package       -n gem-chef-licensing-devel
Version:       0.7.5
Release:       alt1
Summary:       Chef License storage, generation, and entitlement development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-licensing
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-licensing) = 0.7.5
Requires:      gem(chefstyle) >= 2.2
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(webmock) >= 3.13.0
Requires:      gem(pry) >= 0
Requires:      gem(byebug) >= 0
Conflicts:     gem(rspec) >= 4

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
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-chef-licensing-doc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-chef-licensing-devel
%endif


%changelog
* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 0.7.5-alt1
- + packaged gem with Ruby Policy 2.0
