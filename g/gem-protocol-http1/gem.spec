%define        gemname protocol-http1

Name:          gem-protocol-http1
Version:       0.14.2
Release:       alt1
Summary:       A low level implementation of the HTTP/1 protocol
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/protocol-http1
Vcs:           https://github.com/socketry/protocol-http1.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(protocol-http) >= 0.22 gem(protocol-http) < 1
BuildRequires: gem(bundler) >= 0
# BuildRequires: gem(covered) >= 0
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(rspec-files) >= 1.0 gem(rspec-files) < 2
BuildRequires: gem(rspec-memory) >= 1.0 gem(rspec-memory) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(protocol-http) >= 0.22 gem(protocol-http) < 1
Provides:      gem(protocol-http1) = 0.14.2


%description
A low level implementation of the HTTP/1 protocol.


%package       -n gem-protocol-http1-doc
Version:       0.14.2
Release:       alt1
Summary:       A low level implementation of the HTTP/1 protocol documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета protocol-http1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(protocol-http1) = 0.14.2

%description   -n gem-protocol-http1-doc
A low level implementation of the HTTP/1 protocol documentation files.

%description   -n gem-protocol-http1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета protocol-http1.


%package       -n gem-protocol-http1-devel
Version:       0.14.2
Release:       alt1
Summary:       A low level implementation of the HTTP/1 protocol development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета protocol-http1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(protocol-http1) = 0.14.2
Requires:      gem(bundler) >= 0
Requires:      gem(covered) >= 0
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(rspec-files) >= 1.0 gem(rspec-files) < 2
Requires:      gem(rspec-memory) >= 1.0 gem(rspec-memory) < 2

%description   -n gem-protocol-http1-devel
A low level implementation of the HTTP/1 protocol development package.

%description   -n gem-protocol-http1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета protocol-http1.


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

%files         -n gem-protocol-http1-doc
%ruby_gemdocdir

%files         -n gem-protocol-http1-devel


%changelog
* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 0.14.2-alt1
- + packaged gem with Ruby Policy 2.0
