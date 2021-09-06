%define        gemname async-io

Name:          gem-async-io
Version:       1.32.1
Release:       alt1
Summary:       Provides support for asynchonous TCP, UDP, UNIX and SSL sockets
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/async-io
Vcs:           https://github.com/socketry/async-io.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(async) >= 1.14 gem(async) < 2
# BuildRequires: gem(async-container) >= 0.15 gem(async-container) < 1
# BuildRequires: gem(async-rspec) >= 1.10 gem(async-rspec) < 2
# BuildRequires: gem(covered) >= 0
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(rspec) >= 3.6 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(async) >= 1.14 gem(async) < 2
Provides:      gem(async-io) = 1.32.1


%description
Provides support for asynchonous TCP, UDP, UNIX and SSL sockets.


%package       -n gem-async-io-doc
Version:       1.32.1
Release:       alt1
Summary:       Provides support for asynchonous TCP, UDP, UNIX and SSL sockets documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета async-io
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(async-io) = 1.32.1

%description   -n gem-async-io-doc
Provides support for asynchonous TCP, UDP, UNIX and SSL sockets documentation
files.

%description   -n gem-async-io-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета async-io.


%package       -n gem-async-io-devel
Version:       1.32.1
Release:       alt1
Summary:       Provides support for asynchonous TCP, UDP, UNIX and SSL sockets development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета async-io
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(async-io) = 1.32.1
Requires:      gem(async-container) >= 0.15 gem(async-container) < 1
Requires:      gem(async-rspec) >= 1.10 gem(async-rspec) < 2
Requires:      gem(covered) >= 0
Requires:      gem(rack-test) >= 0
Requires:      gem(rspec) >= 3.6 gem(rspec) < 4

%description   -n gem-async-io-devel
Provides support for asynchonous TCP, UDP, UNIX and SSL sockets development
package.

%description   -n gem-async-io-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета async-io.


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

%files         -n gem-async-io-doc
%ruby_gemdocdir

%files         -n gem-async-io-devel


%changelog
* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 1.32.1-alt1
- + packaged gem with Ruby Policy 2.0
