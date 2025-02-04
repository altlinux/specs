%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname stub_env

Name:          gem-stub-env
Version:       1.0.4
Release:       alt1
Summary:       Stub ENV values in RSpec tests
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/littleowllabs/stub_env
Vcs:           https://github.com/littleowllabs/stub_env.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.0
BuildRequires: gem(rake) >= 11.0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
%if_enabled check
BuildRequires: gem(rspec) >= 2.0
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_alias_names stub_env,stub-env
Requires:      gem(rspec) >= 2.0
Conflicts:     gem(rspec) >= 4
Provides:      gem(stub_env) = 1.0.4

%description
RSpec helper for stubbing ENV values


%if_enabled    doc
%package       -n gem-stub-env-doc
Version:       1.0.4
Release:       alt1
Summary:       Stub ENV values in RSpec tests documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета stub_env
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(stub_env) = 1.0.4

%description   -n gem-stub-env-doc
Stub ENV values in RSpec tests documentation files.

RSpec helper for stubbing ENV values

%description   -n gem-stub-env-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета stub_env.
%endif


%if_enabled    devel
%package       -n gem-stub-env-devel
Version:       1.0.4
Release:       alt1
Summary:       Stub ENV values in RSpec tests development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета stub_env
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(stub_env) = 1.0.4
Requires:      gem(bundler) >= 1.0
Requires:      gem(rake) >= 11.0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14

%description   -n gem-stub-env-devel
Stub ENV values in RSpec tests development package.

RSpec helper for stubbing ENV values

%description   -n gem-stub-env-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета stub_env.
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
%doc LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-stub-env-doc
%doc LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-stub-env-devel
%doc LICENSE.txt README.md
%endif


%changelog
* Mon Jan 27 2025 Pavel Skrylev <majioa@altlinux.org> 1.0.4-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
