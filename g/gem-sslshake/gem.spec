%define        gemname sslshake

Name:          gem-sslshake
Version:       1.3.1
Release:       alt1
Summary:       Ruby library for pure SSL/TLS handshake testing
License:       MPL-2.0
Group:         Development/Ruby
Url:           https://github.com/arlimus/sslshake
Vcs:           https://github.com/arlimus/sslshake.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(sslshake) = 1.3.1


%description
This is a library to simulate SSL and TLS handshake from SSLv2, SSLv3, to TLS
1.0-1.2. It does not rely on OpenSSL and is not designed as a replacement
either. It targets full support for even older handshakes, which are not
available in current releases of OpenSSL anymore. It also aims to be executable
on all systems with a sufficiently modern version of Ruby without any additional
requirements or pre-compiled binaries.


%package       -n gem-sslshake-doc
Version:       1.3.1
Release:       alt1
Summary:       Ruby library for pure SSL/TLS handshake testing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sslshake
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sslshake) = 1.3.1

%description   -n gem-sslshake-doc
Ruby library for pure SSL/TLS handshake testing documentation files.

This is a library to simulate SSL and TLS handshake from SSLv2, SSLv3, to TLS
1.0-1.2. It does not rely on OpenSSL and is not designed as a replacement
either. It targets full support for even older handshakes, which are not
available in current releases of OpenSSL anymore. It also aims to be executable
on all systems with a sufficiently modern version of Ruby without any additional
requirements or pre-compiled binaries.

%description   -n gem-sslshake-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sslshake.


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

%files         -n gem-sslshake-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1
- + packaged gem with Ruby Policy 2.0
