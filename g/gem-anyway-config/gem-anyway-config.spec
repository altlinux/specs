%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname anyway_config

Name:          gem-anyway-config
Version:       2.6.3
Release:       alt1
Summary:       Configuration DSL for Ruby libraries and applications
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/palkan/anyway_config
Vcs:           https://github.com/palkan/anyway_config.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(debug) >= 0
BuildRequires: gem(ammeter) >= 1.1.3
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.8
BuildRequires: gem(webmock) >= 3.13.0
BuildRequires: gem(ejson) >= 1.3.1
BuildRequires: gem(rubocop-md) >= 1.0
BuildRequires: gem(standard) >= 1.0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(ruby-next) >= 1.0
BuildRequires: gem(ruby-next-core) >= 1.0
BuildRequires: gem(rbs) >= 3.0
BuildRequires: gem(steep) >= 1.4
BuildRequires: gem(rails) >= 6.1.3.2
BuildConflicts: gem(ammeter) >= 1.2
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(rubocop-md) >= 2
BuildConflicts: gem(standard) >= 2
BuildConflicts: gem(ruby-next) >= 2
BuildConflicts: gem(ruby-next-core) >= 2
BuildConflicts: gem(rbs) >= 4
BuildConflicts: gem(steep) >= 2
BuildConflicts: gem(rails) >= 8
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency rails >= 6.1.3.2,rails < 7
Requires:      gem(ruby-next-core) >= 1.0
Conflicts:     gem(ruby-next-core) >= 2
Provides:      gem(anyway_config) = 2.6.3


%description
Configuration DSL for Ruby libraries and applications. Allows you to easily
follow the twelve-factor application principles (https://12factor.net/config).


%if_enabled    doc
%package       -n gem-anyway-config-doc
Version:       2.6.3
Release:       alt1
Summary:       Configuration DSL for Ruby libraries and applications documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета anyway_config
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(anyway_config) = 2.6.3

%description   -n gem-anyway-config-doc
Configuration DSL for Ruby libraries and applications documentation
files.

Configuration DSL for Ruby libraries and applications. Allows you to easily
follow the twelve-factor application principles (https://12factor.net/config).

%description   -n gem-anyway-config-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета anyway_config.
%endif


%if_enabled    devel
%package       -n gem-anyway-config-devel
Version:       2.6.3
Release:       alt1
Summary:       Configuration DSL for Ruby libraries and applications development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета anyway_config
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(anyway_config) = 2.6.3
Requires:      gem(debug) >= 0
Requires:      gem(ammeter) >= 1.1.3
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.8
Requires:      gem(webmock) >= 3.13.0
Requires:      gem(ejson) >= 1.3.1
Requires:      gem(rubocop-md) >= 1.0
Requires:      gem(standard) >= 1.0
Requires:      gem(rubocop-rspec) >= 0
Requires:      gem(rbs) >= 3.0
Requires:      gem(steep) >= 1.4
Requires:      gem(rails) >= 6.1.3.2
Requires:      gem(ruby-next) >= 1.0
Conflicts:     gem(ruby-next) >= 2
Conflicts:     gem(ammeter) >= 1.2
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(rubocop-md) >= 2
Conflicts:     gem(standard) >= 2
Conflicts:     gem(rbs) >= 4
Conflicts:     gem(steep) >= 2
Conflicts:     gem(rails) >= 8

%description   -n gem-anyway-config-devel
Configuration DSL for Ruby libraries and applications development
package.

Configuration DSL for Ruby libraries and applications. Allows you to easily
follow the twelve-factor application principles (https://12factor.net/config).

%description   -n gem-anyway-config-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета anyway_config.
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
%files         -n gem-anyway-config-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-anyway-config-devel
%doc README.md
%endif


%changelog
* Tue Apr 16 2024 Pavel Skrylev <majioa@altlinux.org> 2.6.3-alt1
- + packaged gem with Ruby Policy 2.0
