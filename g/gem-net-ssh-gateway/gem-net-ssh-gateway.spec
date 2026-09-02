%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname net-ssh-gateway

Name:          gem-net-ssh-gateway
Version:       2.0.0
Release:       alt2.1
Summary:       A simple library to assist in establishing tunneled Net::SSH connections
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/net-ssh/net-ssh-gateway
Vcs:           https://github.com/net-ssh/net-ssh-gateway.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(bundler) >= 1.10
BuildRequires: gem(minitest) >= 5.8.4
BuildRequires: gem(mocha) >= 1.2.1
BuildRequires: gem(net-ssh) >= 4.0.0
BuildRequires: gem(rake) >= 10.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4
%ruby_use_gem_dependency rake >= 13.1.0
%ruby_use_gem_dependency minitest >= 5.17.0
Requires:      gem(net-ssh) >= 4.0.0
Obsoletes:     ruby-net-ssh-gateway < %EVR
Provides:      ruby-net-ssh-gateway = %EVR
Provides:      gem(net-ssh-gateway) = 2.0.0

%description
A simple library to assist in establishing tunneled Net::SSH connections.


%if_enabled    doc
%package       -n gem-net-ssh-gateway-doc
Version:       2.0.0
Release:       alt2.1
Summary:       A simple library to assist in establishing tunneled Net::SSH connections documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета net-ssh-gateway
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(net-ssh-gateway) = 2.0.0

%description   -n gem-net-ssh-gateway-doc
A simple library to assist in establishing tunneled Net::SSH connections
documentation files.

%description   -n gem-net-ssh-gateway-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета net-ssh-gateway.
%endif


%if_enabled    devel
%package       -n gem-net-ssh-gateway-devel
Version:       2.0.0
Release:       alt2.1
Summary:       A simple library to assist in establishing tunneled Net::SSH connections development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета net-ssh-gateway
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(net-ssh-gateway) = 2.0.0
Requires:      gem(bundler) >= 1.10
Requires:      gem(minitest) >= 5.8.4
Requires:      gem(mocha) >= 1.2.1
Requires:      gem(rake) >= 10.0

%description   -n gem-net-ssh-gateway-devel
A simple library to assist in establishing tunneled Net::SSH connections
development package.

%description   -n gem-net-ssh-gateway-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета net-ssh-gateway.
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
%files         -n gem-net-ssh-gateway-doc
%doc LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-net-ssh-gateway-devel
%doc LICENSE.txt README.md
%endif


%changelog
* Mon Aug 31 2026 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt2.1
- ! relaxed dep to minitest, rake and bunlder gems

* Sun Aug 16 2026 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt2
- * rebased to upstream

* Wed Jun 30 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1.1
- ! spec

* Wed Sep 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt2.3
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt2.2
- Rebuild with Ruby 2.4.1

* Wed Dec 05 2012 Led <led@altlinux.ru> 1.0.1-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Fri Dec 11 2009 Igor Zubkov <icesik@altlinux.org> 1.0.1-alt2
- fix License

* Sat Dec 05 2009 Igor Zubkov <icesik@altlinux.org> 1.0.1-alt1
- build for Sisyphus
