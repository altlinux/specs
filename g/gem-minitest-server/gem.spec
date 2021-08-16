%define        gemname minitest-server

Name:          gem-minitest-server
Version:       1.0.6
Release:       alt1
Summary:       minitest-server provides a client/server setup with your minitest process, allowing your test run to send its results directly to a handler
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/minitest-server
Vcs:           https://github.com/seattlerb/minitest-server.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(hoe) >= 3.22 gem(hoe) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6
Provides:      gem(minitest-server) = 1.0.6


%description
minitest-server provides a client/server setup with your minitest process,
allowing your test run to send its results directly to a handler.


%package       -n gem-minitest-server-doc
Version:       1.0.6
Release:       alt1
Summary:       minitest-server provides a client/server setup with your minitest process, allowing your test run to send its results directly to a handler documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-server
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-server) = 1.0.6

%description   -n gem-minitest-server-doc
minitest-server provides a client/server setup with your minitest process,
allowing your test run to send its results directly to a handler documentation
files.

minitest-server provides a client/server setup with your minitest process,
allowing your test run to send its results directly to a handler.

%description   -n gem-minitest-server-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-server.


%package       -n gem-minitest-server-devel
Version:       1.0.6
Release:       alt1
Summary:       minitest-server provides a client/server setup with your minitest process, allowing your test run to send its results directly to a handler development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-server
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-server) = 1.0.6
Requires:      gem(rdoc) >= 4.0 gem(rdoc) < 7
Requires:      gem(hoe) >= 3.22 gem(hoe) < 4

%description   -n gem-minitest-server-devel
minitest-server provides a client/server setup with your minitest process,
allowing your test run to send its results directly to a handler development
package.

minitest-server provides a client/server setup with your minitest process,
allowing your test run to send its results directly to a handler.

%description   -n gem-minitest-server-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-server.


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

%files         -n gem-minitest-server-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-minitest-server-devel
%doc README.rdoc


%changelog
* Thu Jul 15 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.6-alt1
- + packaged gem with Ruby Policy 2.0
