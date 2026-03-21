%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname protocol-http1

Name:          gem-protocol-http1
Version:       0.37.0
Release:       alt1
Summary:       A low level implementation of the HTTP/1 protocol
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/protocol-http1
Vcs:           https://github.com/socketry/protocol-http1.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(protocol-http) >= 0.58
BuildConflicts: gem(protocol-http) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.3
Requires:      gem(protocol-http) >= 0.58
Conflicts:     gem(protocol-http) >= 1
Provides:      gem(protocol-http1) = 0.37.0

%description
A low level implementation of the HTTP/1 protocol.


%if_enabled    doc
%package       -n gem-protocol-http1-doc
Version:       0.37.0
Release:       alt1
Summary:       A low level implementation of the HTTP/1 protocol documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета protocol-http1
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(protocol-http1) = 0.37.0

%description   -n gem-protocol-http1-doc
A low level implementation of the HTTP/1 protocol documentation files.

%description   -n gem-protocol-http1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета protocol-http1.
%endif


%if_enabled    devel
%package       -n gem-protocol-http1-devel
Version:       0.37.0
Release:       alt1
Summary:       A low level implementation of the HTTP/1 protocol development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета protocol-http1
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(protocol-http1) = 0.37.0

%description   -n gem-protocol-http1-devel
A low level implementation of the HTTP/1 protocol development package.

%description   -n gem-protocol-http1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета protocol-http1.
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
%doc license.md readme.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-protocol-http1-doc
%doc license.md readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-protocol-http1-devel
%doc license.md readme.md
%endif


%changelog
* Sat Mar 21 2026 Pavel Skrylev <majioa@altlinux.org> 0.37.0-alt1
- ^ 0.14.2 -> 0.37.0

* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 0.14.2-alt1
- + packaged gem with Ruby Policy 2.0
