%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname codeclimate-engine-rb

Name:          gem-codeclimate-engine-rb
Version:       0.4.2
Release:       alt1
Summary:       JSON issue formatter for the Code Climate engine
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/andyw8/codeclimate-engine-rb
Vcs:           https://github.com/andyw8/codeclimate-engine-rb.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.9
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(rspec) >= 3.3
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
Provides:      gem(codeclimate-engine-rb) = 0.4.2


%description
JSON issue formatter for the Code Climate engine


%if_enabled    doc
%package       -n gem-codeclimate-engine-rb-doc
Version:       0.4.2
Release:       alt1
Summary:       JSON issue formatter for the Code Climate engine documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета codeclimate-engine-rb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(codeclimate-engine-rb) = 0.4.2

%description   -n gem-codeclimate-engine-rb-doc
JSON issue formatter for the Code Climate engine documentation files.
%description   -n gem-codeclimate-engine-rb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета codeclimate-engine-rb.
%endif


%if_enabled    devel
%package       -n gem-codeclimate-engine-rb-devel
Version:       0.4.2
Release:       alt1
Summary:       JSON issue formatter for the Code Climate engine development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета codeclimate-engine-rb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(codeclimate-engine-rb) = 0.4.2
Requires:      gem(bundler) >= 1.9
Requires:      gem(rake) >= 10.0
Requires:      gem(rspec) >= 3.3
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4

%description   -n gem-codeclimate-engine-rb-devel
JSON issue formatter for the Code Climate engine development package.
%description   -n gem-codeclimate-engine-rb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета codeclimate-engine-rb.
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
%files         -n gem-codeclimate-engine-rb-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-codeclimate-engine-rb-devel
%doc README.md
%endif


%changelog
* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 0.4.2-alt1
- + packaged gem with Ruby Policy 2.0
