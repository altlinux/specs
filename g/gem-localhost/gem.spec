%define        gemname localhost

Name:          gem-localhost
Version:       1.1.8
Release:       alt1
Summary:       Manage a local certificate authority for self-signed localhost development servers
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/localhost
Vcs:           https://github.com/socketry/localhost.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
# BuildRequires: gem(covered) >= 0
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Provides:      gem(localhost) = 1.1.8


%description
Manage a local certificate authority for self-signed localhost development
servers.


%package       -n gem-localhost-doc
Version:       1.1.8
Release:       alt1
Summary:       Manage a local certificate authority for self-signed localhost development servers documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета localhost
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(localhost) = 1.1.8

%description   -n gem-localhost-doc
Manage a local certificate authority for self-signed localhost development
servers documentation files.

%description   -n gem-localhost-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета localhost.


%package       -n gem-localhost-devel
Version:       1.1.8
Release:       alt1
Summary:       Manage a local certificate authority for self-signed localhost development servers development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета localhost
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(localhost) = 1.1.8
Requires:      gem(bundler) >= 0
Requires:      gem(covered) >= 0
Requires:      gem(rake) >= 10.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4

%description   -n gem-localhost-devel
Manage a local certificate authority for self-signed localhost development
servers development package.

%description   -n gem-localhost-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета localhost.


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

%files         -n gem-localhost-doc
%ruby_gemdocdir

%files         -n gem-localhost-devel


%changelog
* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.8-alt1
- + packaged gem with Ruby Policy 2.0
