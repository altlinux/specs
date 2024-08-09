%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname net-protocol

Name:          gem-net-protocol
Version:       0.2.2
Release:       alt1
Summary:       The abstract interface for net-* client
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/net-protocol
Vcs:           https://github.com/ruby/net-protocol.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(test-unit-ruby-core) >= 0
BuildRequires: gem(timeout) >= 0.4.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(timeout) >= 0
Provides:      gem(net-protocol) = 0.2.2


%description
The abstract interface for net-* client.


%if_enabled    doc
%package       -n gem-net-protocol-doc
Version:       0.2.2
Release:       alt1
Summary:       The abstract interface for net-* client documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета net-protocol
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(net-protocol) = 0.2.2

%description   -n gem-net-protocol-doc
The abstract interface for net-* client documentation files.

%description   -n gem-net-protocol-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета net-protocol.
%endif


%if_enabled    devel
%package       -n gem-net-protocol-devel
Version:       0.2.2
Release:       alt1
Summary:       The abstract interface for net-* client development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета net-protocol
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(net-protocol) = 0.2.2
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(test-unit-ruby-core) >= 0

%description   -n gem-net-protocol-devel
The abstract interface for net-* client development package.

%description   -n gem-net-protocol-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета net-protocol.
%endif


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

%if_enabled    doc
%files         -n gem-net-protocol-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-net-protocol-devel
%doc README.md
%endif


%changelog
* Fri Jul 26 2024 Pavel Skrylev <majioa@altlinux.org> 0.2.2-alt1
- ^ 0.1.3 -> 0.2.2

* Sun Apr 03 2022 Pavel Skrylev <majioa@altlinux.org> 0.1.3-alt1
- + packaged gem with Ruby Policy 2.0
