%define        _unpackaged_files_terminate_build 1
%define        gemname rubygems-server

Name:          gem-rubygems-server
Version:       0.3.0
Release:       alt1
Summary:       Gem::Server and allows users to serve gems for consumption by `gem --remote-install`
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubygems/rubygems-server
Vcs:           https://github.com/rubygems/rubygems-server.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(webrick) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(webrick) >= 0
Provides:      gem(rubygems-server) = 0.3.0


%description
Gem::Server and allows users to serve gems for consumption by `gem
--remote-install`.


%package       -n gem-rubygems-server-doc
Version:       0.3.0
Release:       alt1
Summary:       Gem::Server and allows users to serve gems for consumption by `gem --remote-install` documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubygems-server
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubygems-server) = 0.3.0

%description   -n gem-rubygems-server-doc
Gem::Server and allows users to serve gems for consumption by `gem
--remote-install` documentation files.

%description   -n gem-rubygems-server-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubygems-server.


%package       -n gem-rubygems-server-devel
Version:       0.3.0
Release:       alt1
Summary:       Gem::Server and allows users to serve gems for consumption by `gem --remote-install` development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubygems-server
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubygems-server) = 0.3.0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-rubygems-server-devel
Gem::Server and allows users to serve gems for consumption by `gem
--remote-install` development package.

%description   -n gem-rubygems-server-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubygems-server.


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

%files         -n gem-rubygems-server-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubygems-server-devel
%doc README.md


%changelog
* Tue Nov 28 2023 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- + packaged gem with Ruby Policy 2.0
