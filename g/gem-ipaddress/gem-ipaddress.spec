%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ipaddress

Name:          gem-ipaddress
Version:       0.8.3.88
Release:       alt0.1
Summary:       IPv4/IPv6 address manipulation library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bluemonk/ipaddress
Vcs:           https://github.com/bluemonk/ipaddress.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.0
BuildRequires: gem(rake) >= 10.5.0
BuildRequires: gem(minitest) >= 5.8
BuildRequires: gem(pry) >= 0.10.1
BuildRequires: gem(travis) >= 1.8.2
BuildRequires: gem(jeweler) >= 2.0.1
BuildRequires: gem(codeclimate-test-reporter) >= 0
BuildRequires: gem(simplecov) >= 0
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Provides:      gem(ipaddress) = 0.8.3.88

%ruby_use_gem_version ipaddress:0.8.3.88

%description
IPAddress is a Ruby library designed to make manipulation of IPv4 and IPv6
addresses both powerful and simple. It mantains a layer of compatibility with
Ruby's own IPAddr, while addressing many of its issues.


%if_enabled    doc
%package       -n gem-ipaddress-doc
Version:       0.8.3.88
Release:       alt0.1
Summary:       IPv4/IPv6 address manipulation library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ipaddress
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ipaddress) = 0.8.3.88

%description   -n gem-ipaddress-doc
IPv4/IPv6 address manipulation library documentation files.

IPAddress is a Ruby library designed to make manipulation of IPv4 and IPv6
addresses both powerful and simple. It mantains a layer of compatibility with
Ruby's own IPAddr, while addressing many of its issues.

%description   -n gem-ipaddress-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ipaddress.
%endif


%if_enabled    devel
%package       -n gem-ipaddress-devel
Version:       0.8.3.88
Release:       alt0.1
Summary:       IPv4/IPv6 address manipulation library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ipaddress
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ipaddress) = 0.8.3.88
Requires:      gem(bundler) >= 1.0
Requires:      gem(rake) >= 10.5.0
Requires:      gem(minitest) >= 5.8
Requires:      gem(pry) >= 0.10.1
Requires:      gem(travis) >= 1.8.2
Requires:      gem(jeweler) >= 2.0.1
Requires:      gem(codeclimate-test-reporter) >= 0
Requires:      gem(simplecov) >= 0
Conflicts:     gem(rake) >= 14

%description   -n gem-ipaddress-devel
IPv4/IPv6 address manipulation library development package.

IPAddress is a Ruby library designed to make manipulation of IPv4 and IPv6
addresses both powerful and simple. It mantains a layer of compatibility with
Ruby's own IPAddr, while addressing many of its issues.

%description   -n gem-ipaddress-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ipaddress.
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
%files         -n gem-ipaddress-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ipaddress-devel
%doc README.md
%endif


%changelog
* Fri Oct 18 2024 Pavel Skrylev <majioa@altlinux.org> 0.8.3.88-alt0.1
- ^ 0.8.3 -> 0.8.3p88

* Thu Jun 24 2021 Pavel Skrylev <majioa@altlinux.org> 0.8.3-alt1
- + packaged gem with Ruby Policy 2.0
