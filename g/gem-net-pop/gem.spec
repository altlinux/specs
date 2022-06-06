%define        gemname net-pop

Name:          gem-net-pop
Version:       0.1.1
Release:       alt1
Summary:       Ruby client library for POP3
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/net-pop
Vcs:           https://github.com/ruby/net-pop.git
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
Provides:      gem(net-pop) = 0.1.1


%description
This library provides functionality for retrieving email via POP3, the Post
Office Protocol version 3. For details of POP3, see RFC1939.


%package       -n gem-net-pop-doc
Version:       0.1.1
Release:       alt1
Summary:       Ruby client library for POP3 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета net-pop
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(net-pop) = 0.1.1

%description   -n gem-net-pop-doc
Ruby client library for POP3 documentation files.

This library provides functionality for retrieving email via POP3, the Post
Office Protocol version 3. For details of POP3, see RFC1939.

%description   -n gem-net-pop-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета net-pop.


%package       -n gem-net-pop-devel
Version:       0.1.1
Release:       alt1
Summary:       Ruby client library for POP3 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета net-pop
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(net-pop) = 0.1.1

%description   -n gem-net-pop-devel
Ruby client library for POP3 development package.

This library provides functionality for retrieving email via POP3, the Post
Office Protocol version 3. For details of POP3, see RFC1939.

%description   -n gem-net-pop-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета net-pop.


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

%files         -n gem-net-pop-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-net-pop-devel
%doc README.md


%changelog
* Sun Apr 03 2022 Pavel Skrylev <majioa@altlinux.org> 0.1.1-alt1
- + packaged gem with Ruby Policy 2.0
