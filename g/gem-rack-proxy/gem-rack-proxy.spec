%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rack-proxy

Name:          gem-rack-proxy
Version:       0.7.7
Release:       alt1
Summary:       A request/response rewriting HTTP proxy. A Rack app
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ncr/rack-proxy
Vcs:           https://github.com/ncr/rack-proxy.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(rack) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rack) >= 0
Provides:      gem(rack-proxy) = 0.7.7


%description
A Rack app that provides request/response rewriting proxy capabilities with
streaming.


%if_enabled    doc
%package       -n gem-rack-proxy-doc
Version:       0.7.7
Release:       alt1
Summary:       A request/response rewriting HTTP proxy. A Rack app documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rack-proxy
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rack-proxy) = 0.7.7

%description   -n gem-rack-proxy-doc
A request/response rewriting HTTP proxy. A Rack app documentation files.

A Rack app that provides request/response rewriting proxy capabilities with
streaming.

%description   -n gem-rack-proxy-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rack-proxy.
%endif


%if_enabled    devel
%package       -n gem-rack-proxy-devel
Version:       0.7.7
Release:       alt1
Summary:       A request/response rewriting HTTP proxy. A Rack app development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rack-proxy
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rack-proxy) = 0.7.7
Requires:      gem(rake) >= 0
Requires:      gem(rack-test) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-rack-proxy-devel
A request/response rewriting HTTP proxy. A Rack app development package.

A Rack app that provides request/response rewriting proxy capabilities with
streaming.

%description   -n gem-rack-proxy-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rack-proxy.
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
%files         -n gem-rack-proxy-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rack-proxy-devel
%doc README.md
%endif


%changelog
* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 0.7.7-alt1
- + packaged gem with Ruby Policy 2.0
