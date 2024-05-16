%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname blade-qunit_adapter

Name:          gem-blade-qunit-adapter
Version:       2.0.1
Release:       alt1
Summary:       Blade adapter for the QUnit JavaScript testing framework
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/javan/blade-qunit_adapter
Vcs:           https://github.com/javan/blade-qunit_adapter.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.10
BuildRequires: gem(rake) >= 10.0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
Provides:      gem(blade-qunit_adapter) = 2.0.1


%description
Blade adapter for the QUnit JavaScript testing framework.


%if_enabled    doc
%package       -n gem-blade-qunit-adapter-doc
Version:       2.0.1
Release:       alt1
Summary:       Blade adapter for the QUnit JavaScript testing framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета blade-qunit_adapter
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(blade-qunit_adapter) = 2.0.1

%description   -n gem-blade-qunit-adapter-doc
Blade adapter for the QUnit JavaScript testing framework documentation files.

%description   -n gem-blade-qunit-adapter-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета blade-qunit_adapter.
%endif


%if_enabled    devel
%package       -n gem-blade-qunit-adapter-devel
Version:       2.0.1
Release:       alt1
Summary:       Blade adapter for the QUnit JavaScript testing framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета blade-qunit_adapter
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(blade-qunit_adapter) = 2.0.1
Requires:      gem(bundler) >= 1.10
Requires:      gem(rake) >= 10.0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14

%description   -n gem-blade-qunit-adapter-devel
Blade adapter for the QUnit JavaScript testing framework development package.

%description   -n gem-blade-qunit-adapter-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета blade-qunit_adapter.
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
%files         -n gem-blade-qunit-adapter-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-blade-qunit-adapter-devel
%doc README.md
%endif


%changelog
* Wed Apr 24 2024 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt1
- + packaged gem with Ruby Policy 2.0
