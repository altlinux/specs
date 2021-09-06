%define        gemname protocol-http

Name:          gem-protocol-http
Version:       0.22.5
Release:       alt1
Summary:       Provides abstractions to handle HTTP protocols
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/protocol-http
Vcs:           https://github.com/socketry/protocol-http.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
# BuildRequires: gem(covered) >= 0
BuildRequires: gem(rspec) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(protocol-http) = 0.22.5


%description
Provides abstractions to handle HTTP protocols.


%package       -n gem-protocol-http-doc
Version:       0.22.5
Release:       alt1
Summary:       Provides abstractions to handle HTTP protocols documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета protocol-http
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(protocol-http) = 0.22.5

%description   -n gem-protocol-http-doc
Provides abstractions to handle HTTP protocols documentation files.

%description   -n gem-protocol-http-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета protocol-http.


%package       -n gem-protocol-http-devel
Version:       0.22.5
Release:       alt1
Summary:       Provides abstractions to handle HTTP protocols development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета protocol-http
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(protocol-http) = 0.22.5
Requires:      gem(bundler) >= 0
Requires:      gem(covered) >= 0
Requires:      gem(rspec) >= 0

%description   -n gem-protocol-http-devel
Provides abstractions to handle HTTP protocols development package.

%description   -n gem-protocol-http-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета protocol-http.


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

%files         -n gem-protocol-http-doc
%ruby_gemdocdir

%files         -n gem-protocol-http-devel


%changelog
* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 0.22.5-alt1
- + packaged gem with Ruby Policy 2.0
