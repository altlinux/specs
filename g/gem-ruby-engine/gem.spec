%define        gemname ruby_engine

Name:          gem-ruby-engine
Version:       2.0.0
Release:       alt1
Summary:       Adds the RubyEngine pseudo-constant
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/janlelis/ruby_engine
Vcs:           https://github.com/janlelis/ruby_engine.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14
BuildRequires: gem(rdoc) >= 3.0 gem(rdoc) < 7
BuildRequires: gem(rspec) >= 2.4 gem(rspec) < 4
BuildRequires: gem(rubygems-tasks) >= 0.2 gem(rubygems-tasks) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Provides:      gem(ruby_engine) = 2.0.0


%description
Gives you an RubyEngine class that simplifies checking for your Ruby
implementation.


%package       -n gem-ruby-engine-doc
Version:       2.0.0
Release:       alt1
Summary:       Adds the RubyEngine pseudo-constant documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby_engine
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby_engine) = 2.0.0

%description   -n gem-ruby-engine-doc
Adds the RubyEngine pseudo-constant documentation files.

Gives you an RubyEngine class that simplifies checking for your Ruby
implementation.

%description   -n gem-ruby-engine-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby_engine.


%package       -n gem-ruby-engine-devel
Version:       2.0.0
Release:       alt1
Summary:       Adds the RubyEngine pseudo-constant development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby_engine
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby_engine) = 2.0.0
Requires:      gem(rake) >= 10.0 gem(rake) < 14
Requires:      gem(rdoc) >= 3.0 gem(rdoc) < 7
Requires:      gem(rspec) >= 2.4 gem(rspec) < 4
Requires:      gem(rubygems-tasks) >= 0.2 gem(rubygems-tasks) < 1

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
* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with Ruby Policy 2.0
