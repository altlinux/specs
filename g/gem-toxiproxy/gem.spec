%define        gemname toxiproxy

Name:          gem-toxiproxy
Version:       2.0.1
Release:       alt1
Summary:       Ruby library for Toxiproxy
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/Shopify/toxiproxy
Vcs:           https://github.com/shopify/toxiproxy.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(toxiproxy) = 2.0.1


%description
A Ruby library for controlling Toxiproxy. Can be used in resiliency testing.


%package       -n gem-toxiproxy-doc
Version:       2.0.1
Release:       alt1
Summary:       Ruby library for Toxiproxy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета toxiproxy
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(toxiproxy) = 2.0.1

%description   -n gem-toxiproxy-doc
Ruby library for Toxiproxy documentation files.

A Ruby library for controlling Toxiproxy. Can be used in resiliency testing.

%description   -n gem-toxiproxy-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета toxiproxy.


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

%files         -n gem-toxiproxy-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Fri Apr 22 2022 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt1
- + packaged gem with Ruby Policy 2.0
