%define        _unpackaged_files_terminate_build 1
%define        gemname ruby_engine

Name:          gem-ruby-engine
Version:       2.0.0.3
Release:       alt0.1
Summary:       Adds the RubyEngine pseudo-constant
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/janlelis/ruby_engine
Vcs:           https://github.com/janlelis/ruby_engine.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 2.99
BuildRequires: gem(rubygems-tasks) >= 0.2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubygems-tasks) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_alias_names ruby_engine,ruby-engine
Provides:      gem(ruby_engine) = 2.0.0.3

%ruby_use_gem_version ruby_engine:2.0.0.3

%description
Gives you an RubyEngine class that simplifies checking for your Ruby
implementation.


%package       -n gem-ruby-engine-doc
Version:       2.0.0.3
Release:       alt0.1
Summary:       Adds the RubyEngine pseudo-constant documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby_engine
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby_engine) = 2.0.0.3

%description   -n gem-ruby-engine-doc
Adds the RubyEngine pseudo-constant documentation files.

Gives you an RubyEngine class that simplifies checking for your Ruby
implementation.

%description   -n gem-ruby-engine-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby_engine.


%package       -n gem-ruby-engine-devel
Version:       2.0.0.3
Release:       alt0.1
Summary:       Adds the RubyEngine pseudo-constant development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby_engine
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby_engine) = 2.0.0.3
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 2.99
Requires:      gem(rubygems-tasks) >= 0.2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubygems-tasks) >= 1

%description   -n gem-ruby-engine-devel
Adds the RubyEngine pseudo-constant development package.

Gives you an RubyEngine class that simplifies checking for your Ruby
implementation.

%description   -n gem-ruby-engine-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby_engine.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-ruby-engine-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-ruby-engine-devel
%doc README.rdoc


%changelog
* Mon Dec 11 2023 Pavel Skrylev <majioa@altlinux.org> 2.0.0.3-alt0.1
- ^ 2.0.0 -> 2.0.0p3

* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with Ruby Policy 2.0
