%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname io-endpoint

Name:          gem-io-endpoint
Version:       0.13.0
Release:       alt1
Summary:       Provides a separation of concerns interface for IO endpoints
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/io-endpoint
Vcs:           https://github.com/socketry/io-endpoint.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(io-endpoint) = 0.13.0


%description
Provides a separation of concerns interface for IO endpoints. This allows you to
write code which is agnostic to the underlying IO implementation.


%if_enabled    doc
%package       -n gem-io-endpoint-doc
Version:       0.13.0
Release:       alt1
Summary:       Provides a separation of concerns interface for IO endpoints documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета io-endpoint
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(io-endpoint) = 0.13.0

%description   -n gem-io-endpoint-doc
Provides a separation of concerns interface for IO endpoints documentation
files.

Provides a separation of concerns interface for IO endpoints. This allows you to
write code which is agnostic to the underlying IO implementation.

%description   -n gem-io-endpoint-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета io-endpoint.
%endif


%if_enabled    devel
%package       -n gem-io-endpoint-devel
Version:       0.13.0
Release:       alt1
Summary:       Provides a separation of concerns interface for IO endpoints development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета io-endpoint
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(io-endpoint) = 0.13.0

%description   -n gem-io-endpoint-devel
Provides a separation of concerns interface for IO endpoints development
package.

Provides a separation of concerns interface for IO endpoints. This allows you to
write code which is agnostic to the underlying IO implementation.

%description   -n gem-io-endpoint-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета io-endpoint.
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
%doc readme.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-io-endpoint-doc
%doc readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-io-endpoint-devel
%doc readme.md
%endif


%changelog
* Tue Jul 30 2024 Pavel Skrylev <majioa@altlinux.org> 0.13.0-alt1
- + packaged gem with Ruby Policy 2.0
