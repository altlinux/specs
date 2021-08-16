%define        gemname proxifier

Name:          gem-proxifier
Version:       1.0.3
Release:       alt2
Summary:       Proxifier adds support for HTTP or SOCKS proxies and lets you force TCPSocket to use proxies
License:       MIT or Ruby
Group:         Development/Ruby
Url:           https://github.com/samuelkadolph/ruby-proxifier
Vcs:           https://github.com/samuelkadolph/ruby-proxifier.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-proxifier < %EVR
Provides:      ruby-proxifier = %EVR
Provides:      gem(proxifier) = 1.0.3


%description
This gem was created for 2 purposes.

First is to enable ruby programmers to use HTTP or SOCKS proxies interchangeably
when using TCPSockets. Either manually with Proxifier::Proxy#open or by require
"proxifier/env".

The second purpose is to use ruby code that doesn't use proxies for users that
have to use proxies. The pruby and pirb executables are simple wrappers for
their respective ruby executables that support proxies from environment
variables.


%package       -n proxifier
Version:       1.0.3
Release:       alt2
Summary:       Proxifier adds support for HTTP or SOCKS proxies and lets you force TCPSocket to use proxies executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета proxifier
Group:         Other
BuildArch:     noarch

Requires:      gem(proxifier) = 1.0.3

%description   -n proxifier
Proxifier adds support for HTTP or SOCKS proxies and lets you force TCPSocket to
use proxies executable(s).

This gem was created for 2 purposes.

First is to enable ruby programmers to use HTTP or SOCKS proxies interchangeably
when using TCPSockets. Either manually with Proxifier::Proxy#open or by require
"proxifier/env".

The second purpose is to use ruby code that doesn't use proxies for users that
have to use proxies. The pruby and pirb executables are simple wrappers for
their respective ruby executables that support proxies from environment
variables.

%description   -n proxifier -l ru_RU.UTF-8
Исполнямка для самоцвета proxifier.


%package       -n gem-proxifier-doc
Version:       1.0.3
Release:       alt2
Summary:       Proxifier adds support for HTTP or SOCKS proxies and lets you force TCPSocket to use proxies documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета proxifier
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(proxifier) = 1.0.3

%description   -n gem-proxifier-doc
Proxifier adds support for HTTP or SOCKS proxies and lets you force TCPSocket to
use proxies documentation files.

This gem was created for 2 purposes.

First is to enable ruby programmers to use HTTP or SOCKS proxies interchangeably
when using TCPSockets. Either manually with Proxifier::Proxy#open or by require
"proxifier/env".

The second purpose is to use ruby code that doesn't use proxies for users that
have to use proxies. The pruby and pirb executables are simple wrappers for
their respective ruby executables that support proxies from environment
variables.

%description   -n gem-proxifier-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета proxifier.


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

%files         -n proxifier
%doc README.md
%_bindir/pirb
%_bindir/pruby

%files         -n gem-proxifier-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Wed Jun 30 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.3-alt2
- ! spec

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Jan 19 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1
- Initial build for ALT Linux
