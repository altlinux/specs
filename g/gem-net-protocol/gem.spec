%define        gemname net-protocol

Name:          gem-net-protocol
Version:       0.1.3
Release:       alt1
Summary:       The abstract interface for net-* client
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/net-protocol
Vcs:           https://github.com/ruby/net-protocol.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(timeout) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(timeout) >= 0
Provides:      gem(net-protocol) = 0.1.3


%description
The abstract interface for net-* client.


%package       -n gem-net-protocol-doc
Version:       0.1.3
Release:       alt1
Summary:       The abstract interface for net-* client documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета net-protocol
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(net-protocol) = 0.1.3

%description   -n gem-net-protocol-doc
The abstract interface for net-* client documentation files.

%description   -n gem-net-protocol-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета net-protocol.


%package       -n gem-net-protocol-devel
Version:       0.1.3
Release:       alt1
Summary:       The abstract interface for net-* client development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета net-protocol
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(net-protocol) = 0.1.3

%description   -n gem-net-protocol-devel
The abstract interface for net-* client development package.

%description   -n gem-net-protocol-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета net-protocol.


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

%files         -n gem-net-protocol-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-net-protocol-devel
%doc README.md


%changelog
* Sun Apr 03 2022 Pavel Skrylev <majioa@altlinux.org> 0.1.3-alt1
- + packaged gem with Ruby Policy 2.0
