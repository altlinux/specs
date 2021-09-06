%define        gemname protocol-http2

Name:          gem-protocol-http2
Version:       0.14.2
Release:       alt1
Summary:       A low level implementation of the HTTP/2 protocol
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/protocol-http2
Vcs:           https://github.com/socketry/protocol-http2.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(protocol-hpack) >= 1.4 gem(protocol-hpack) < 2
BuildRequires: gem(protocol-http) >= 0.18 gem(protocol-http) < 1
BuildRequires: gem(bundler) >= 0
# BuildRequires: gem(covered) >= 0
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(protocol-hpack) >= 1.4 gem(protocol-hpack) < 2
Requires:      gem(protocol-http) >= 0.18 gem(protocol-http) < 1
Provides:      gem(protocol-http2) = 0.14.2


%description
A low level implementation of the HTTP/2 protocol.


%package       -n gem-protocol-http2-doc
Version:       0.14.2
Release:       alt1
Summary:       A low level implementation of the HTTP/2 protocol documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета protocol-http2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(protocol-http2) = 0.14.2

%description   -n gem-protocol-http2-doc
A low level implementation of the HTTP/2 protocol documentation files.

%description   -n gem-protocol-http2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета protocol-http2.


%package       -n gem-protocol-http2-devel
Version:       0.14.2
Release:       alt1
Summary:       A low level implementation of the HTTP/2 protocol development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета protocol-http2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(protocol-http2) = 0.14.2
Requires:      gem(bundler) >= 0
Requires:      gem(covered) >= 0
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4

%description   -n gem-protocol-http2-devel
A low level implementation of the HTTP/2 protocol development package.

%description   -n gem-protocol-http2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета protocol-http2.


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

%files         -n gem-protocol-http2-doc
%ruby_gemdocdir

%files         -n gem-protocol-http2-devel


%changelog
* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 0.14.2-alt1
- + packaged gem with Ruby Policy 2.0
