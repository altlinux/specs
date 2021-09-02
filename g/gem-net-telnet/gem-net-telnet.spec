%define        gemname net-telnet

Name:          gem-net-telnet
Version:       0.2.0.1
Release:       alt0.1
Summary:       Provides telnet client functionality
License:       ruby
Group:         Development/Ruby
Url:           https://github.com/ruby/net-telnet.git
Vcs:           https://github.com/ruby/net-telnet.git.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(mspec) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_version net-telnet:0.2.0.1
Obsoletes:     ruby-net-telnet < %EVR
Provides:      ruby-net-telnet = %EVR
Provides:      gem(net-telnet) = 0.2.0.1


%description
Provides telnet client functionality.

This class also has, through delegation, all the methods of a socket object (by
default, a TCPSocket, but can be set by the Proxy option to new()). This
provides methods such as close() to end the session and sysread() to read data
directly from the host, instead of via the waitfor() mechanism. Note that if you
do use sysread() directly when in telnet mode, you should probably pass the
output through preprocess() to extract telnet command sequences.


%package       -n gem-net-telnet-doc
Version:       0.2.0.1
Release:       alt0.1
Summary:       Provides telnet client functionality documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета net-telnet
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(net-telnet) = 0.2.0.1

%description   -n gem-net-telnet-doc
Provides telnet client functionality documentation files.

Provides telnet client functionality.

This class also has, through delegation, all the methods of a socket object (by
default, a TCPSocket, but can be set by the Proxy option to new()). This
provides methods such as close() to end the session and sysread() to read data
directly from the host, instead of via the waitfor() mechanism. Note that if you
do use sysread() directly when in telnet mode, you should probably pass the
output through preprocess() to extract telnet command sequences.

%description   -n gem-net-telnet-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета net-telnet.


%package       -n gem-net-telnet-devel
Version:       0.2.0.1
Release:       alt0.1
Summary:       Provides telnet client functionality development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета net-telnet
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(net-telnet) = 0.2.0.1
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(mspec) >= 0

%description   -n gem-net-telnet-devel
Provides telnet client functionality development package.

Provides telnet client functionality.

This class also has, through delegation, all the methods of a socket object (by
default, a TCPSocket, but can be set by the Proxy option to new()). This
provides methods such as close() to end the session and sysread() to read data
directly from the host, instead of via the waitfor() mechanism. Note that if you
do use sysread() directly when in telnet mode, you should probably pass the
output through preprocess() to extract telnet command sequences.

%description   -n gem-net-telnet-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета net-telnet.


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

%files         -n gem-net-telnet-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-net-telnet-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.0.1-alt0.1
- ^ 0.2.0 -> 0.2.0.1

* Mon Jan 14 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus, packaged as a gem
