%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%define        gemname protocol-http

Name:          gem-protocol-http
Version:       0.60.0
Release:       alt1
Summary:       Provides abstractions to handle HTTP protocols
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/protocol-http
Vcs:           https://github.com/socketry/protocol-http.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.3
Provides:      protocol-http = %EVR
Provides:      gem(protocol-http) = 0.60.0

%description
Provides abstractions to handle HTTP protocols.


%if_enabled    doc
%package       -n gem-protocol-http-doc
Version:       0.60.0
Release:       alt1
Summary:       Provides abstractions to handle HTTP protocols documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета protocol-http
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(protocol-http) = 0.60.0

%description   -n gem-protocol-http-doc
Provides abstractions to handle HTTP protocols documentation files.

%description   -n gem-protocol-http-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета protocol-http.
%endif


%if_enabled    devel
%package       -n gem-protocol-http-devel
Version:       0.60.0
Release:       alt1
Summary:       Provides abstractions to handle HTTP protocols development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета protocol-http
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(protocol-http) = 0.60.0

%description   -n gem-protocol-http-devel
Provides abstractions to handle HTTP protocols development package.

%description   -n gem-protocol-http-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета protocol-http.
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
%files         -n gem-protocol-http-doc
%doc license.md readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-protocol-http-devel
%doc license.md readme.md
%endif


%changelog
* Sat Mar 21 2026 Pavel Skrylev <majioa@altlinux.org> 0.60.0-alt1
- ^ 0.23.12 -> 0.60.0

* Tue Oct 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.23.12-alt1
- ^ 0.22.5 -> 0.23.12

* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 0.22.5-alt1
- + packaged gem with Ruby Policy 2.0
