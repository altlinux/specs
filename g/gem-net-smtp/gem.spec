%define        gemname net-smtp

Name:          gem-net-smtp
Version:       0.3.1
Release:       alt1
Summary:       Simple Mail Transfer Protocol client library for Ruby
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/net-smtp
Vcs:           https://github.com/ruby/net-smtp.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(net-protocol) >= 0
BuildRequires: gem(digest) >= 0
BuildRequires: gem(timeout) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(net-protocol) >= 0
Requires:      gem(digest) >= 0
Requires:      gem(timeout) >= 0
Provides:      gem(net-smtp) = 0.3.1


%description
This library provides functionality to send internet mail via SMTP, the Simple
Mail Transfer Protocol.

For details of SMTP itself, see RFC2821.


%package       -n gem-net-smtp-doc
Version:       0.3.1
Release:       alt1
Summary:       Simple Mail Transfer Protocol client library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета net-smtp
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(net-smtp) = 0.3.1

%description   -n gem-net-smtp-doc
Simple Mail Transfer Protocol client library for Ruby documentation files.

This library provides functionality to send internet mail via SMTP, the Simple
Mail Transfer Protocol.

For details of SMTP itself, see RFC2821.

%description   -n gem-net-smtp-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета net-smtp.


%package       -n gem-net-smtp-devel
Version:       0.3.1
Release:       alt1
Summary:       Simple Mail Transfer Protocol client library for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета net-smtp
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(net-smtp) = 0.3.1

%description   -n gem-net-smtp-devel
Simple Mail Transfer Protocol client library for Ruby development package.

This library provides functionality to send internet mail via SMTP, the Simple
Mail Transfer Protocol.

For details of SMTP itself, see RFC2821.

%description   -n gem-net-smtp-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета net-smtp.


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

%files         -n gem-net-smtp-doc
%ruby_gemdocdir

%files         -n gem-net-smtp-devel


%changelog
* Sun Apr 03 2022 Pavel Skrylev <majioa@altlinux.org> 0.3.1-alt1
- + packaged gem with Ruby Policy 2.0
