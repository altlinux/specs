%define        gemname ruby_version

Name:          gem-ruby-version
Version:       1.0.2
Release:       alt1
Summary:       Adds the RubyVersion pseudo-constant
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/janlelis/ruby_version
Vcs:           https://github.com/janlelis/ruby_version.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 10.1 gem(rake) < 14
BuildRequires: gem(rdoc) >= 3.0 gem(rdoc) < 7
BuildRequires: gem(rspec) >= 2.4 gem(rspec) < 4
BuildRequires: gem(rubygems-tasks) >= 0.2 gem(rubygems-tasks) < 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Provides:      gem(ruby_version) = 1.0.2


%description
Provides a RubyVersion class which offers a convenient DSL for checking for the
right Ruby version


%package       -n gem-ruby-version-doc
Version:       1.0.2
Release:       alt1
Summary:       Adds the RubyVersion pseudo-constant documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby_version
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby_version) = 1.0.2

%description   -n gem-ruby-version-doc
Adds the RubyVersion pseudo-constant documentation files.

Provides a RubyVersion class which offers a convenient DSL for checking for the
right Ruby version

%description   -n gem-ruby-version-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby_version.


%package       -n gem-ruby-version-devel
Version:       1.0.2
Release:       alt1
Summary:       Adds the RubyVersion pseudo-constant development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby_version
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby_version) = 1.0.2
Requires:      gem(rake) >= 10.1 gem(rake) < 14
Requires:      gem(rdoc) >= 3.0 gem(rdoc) < 7
Requires:      gem(rspec) >= 2.4 gem(rspec) < 4
Requires:      gem(rubygems-tasks) >= 0.2 gem(rubygems-tasks) < 1

%description   -n gem-ruby-version-devel
Adds the RubyVersion pseudo-constant development package.

Provides a RubyVersion class which offers a convenient DSL for checking for the
right Ruby version

%description   -n gem-ruby-version-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby_version.


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

%files         -n gem-ruby-version-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-ruby-version-devel
%doc README.rdoc


%changelog
* Thu Sep 29 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- + packaged gem with Ruby Policy 2.0
