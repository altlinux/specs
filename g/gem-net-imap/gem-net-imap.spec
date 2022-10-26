%define        gemname net-imap

Name:          gem-net-imap
Version:       0.3.1
Release:       alt1
Summary:       Ruby client api for Internet Message Access Protocol
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/net-imap
Vcs:           https://github.com/ruby/net-imap.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(net-protocol) >= 0
BuildRequires: gem(digest) >= 0
BuildRequires: gem(strscan) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(net-protocol) >= 0
Provides:      gem(net-imap) = 0.3.1


%description
Ruby client api for Internet Message Access Protocol


%package       -n gem-net-imap-doc
Version:       0.3.1
Release:       alt1
Summary:       Ruby client api for Internet Message Access Protocol documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета net-imap
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(net-imap) = 0.3.1

%description   -n gem-net-imap-doc
Ruby client api for Internet Message Access Protocol documentation files.

%description   -n gem-net-imap-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета net-imap.


%package       -n gem-net-imap-devel
Version:       0.3.1
Release:       alt1
Summary:       Ruby client api for Internet Message Access Protocol development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета net-imap
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(net-imap) = 0.3.1
Requires:      gem(digest) >= 0
Requires:      gem(strscan) >= 0

%description   -n gem-net-imap-devel
Ruby client api for Internet Message Access Protocol development package.

%description   -n gem-net-imap-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета net-imap.


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

%files         -n gem-net-imap-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-net-imap-devel
%doc README.md


%changelog
* Sat Oct 08 2022 Pavel Skrylev <majioa@altlinux.org> 0.3.1-alt1
- ^ 0.2.3 -> 0.3.1

* Sun Apr 03 2022 Pavel Skrylev <majioa@altlinux.org> 0.2.3-alt1
- + packaged gem with Ruby Policy 2.0
