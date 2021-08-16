%define        gemname ipaddress

Name:          gem-ipaddress
Version:       0.8.3
Release:       alt1
Summary:       IPv4/IPv6 address manipulation library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bluemonk/ipaddress
Vcs:           https://github.com/bluemonk/ipaddress.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Provides:      gem(ipaddress) = 0.8.3


%description
IPAddress is a Ruby library designed to make manipulation of IPv4 and IPv6
addresses both powerful and simple. It mantains a layer of compatibility with
Ruby's own IPAddr, while addressing many of its issues.


%package       -n gem-ipaddress-doc
Version:       0.8.3
Release:       alt1
Summary:       IPv4/IPv6 address manipulation library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ipaddress
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ipaddress) = 0.8.3

%description   -n gem-ipaddress-doc
IPv4/IPv6 address manipulation library documentation files.

IPAddress is a Ruby library designed to make manipulation of IPv4 and IPv6
addresses both powerful and simple. It mantains a layer of compatibility with
Ruby's own IPAddr, while addressing many of its issues.

%description   -n gem-ipaddress-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ipaddress.


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

%files         -n gem-ipaddress-doc
%doc README.rdoc
%ruby_gemdocdir


%changelog
* Thu Jun 24 2021 Pavel Skrylev <majioa@altlinux.org> 0.8.3-alt1
- + packaged gem with Ruby Policy 2.0
