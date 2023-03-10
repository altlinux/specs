%define        _unpackaged_files_terminate_build 1
%define        gemname proxifier2

Name:          gem-proxifier2
Version:       1.1.0
Release:       alt1
Summary:       Proxifier is a gem to force ruby to use a proxy
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/chef/ruby-proxifier
Vcs:           https://github.com/chef/ruby-proxifier.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(proxifier2) = 1.1.0


%description
Proxifier adds support for HTTP or SOCKS proxies and lets you force TCPSocket to
use proxies.


%package       -n proxifier2
Version:       1.1.0
Release:       alt1
Summary:       Proxifier is a gem to force ruby to use a proxy executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета proxifier2
Group:         Other
BuildArch:     noarch

Requires:      gem(proxifier2) = 1.1.0

%description   -n proxifier2
Proxifier is a gem to force ruby to use a proxy executable(s).

Proxifier adds support for HTTP or SOCKS proxies and lets you force TCPSocket to
use proxies.

%description   -n proxifier2 -l ru_RU.UTF-8
Исполнямка для самоцвета proxifier2.


%package       -n gem-proxifier2-doc
Version:       1.1.0
Release:       alt1
Summary:       Proxifier is a gem to force ruby to use a proxy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета proxifier2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(proxifier2) = 1.1.0

%description   -n gem-proxifier2-doc
Proxifier is a gem to force ruby to use a proxy documentation files.

Proxifier adds support for HTTP or SOCKS proxies and lets you force TCPSocket to
use proxies.

%description   -n gem-proxifier2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета proxifier2.


%package       -n gem-proxifier2-devel
Version:       1.1.0
Release:       alt1
Summary:       Proxifier is a gem to force ruby to use a proxy development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета proxifier2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(proxifier2) = 1.1.0

%description   -n gem-proxifier2-devel
Proxifier is a gem to force ruby to use a proxy development package.

Proxifier adds support for HTTP or SOCKS proxies and lets you force TCPSocket to
use proxies.

%description   -n gem-proxifier2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета proxifier2.


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

%files         -n proxifier2
%doc README.md
%_bindir/pirb
%_bindir/pruby

%files         -n gem-proxifier2-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-proxifier2-devel
%doc README.md


%changelog
* Fri Mar 10 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with Ruby Policy 2.0
