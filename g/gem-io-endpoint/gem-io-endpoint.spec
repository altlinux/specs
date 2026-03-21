%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%define        gemname io-endpoint

Name:          gem-io-endpoint
Version:       0.17.2
Release:       alt1
Summary:       Provides a separation of concerns interface for IO endpoints
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/io-endpoint
Vcs:           https://github.com/socketry/io-endpoint.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.2
Provides:      gem(io-endpoint) = 0.17.2

%description
Provides a separation of concerns interface for IO endpoints. This allows you to
write code which is agnostic to the underlying IO implementation.


%if_enabled    doc
%package       -n gem-io-endpoint-doc
Version:       0.17.2
Release:       alt1
Summary:       Provides a separation of concerns interface for IO endpoints documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета io-endpoint
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(io-endpoint) = 0.17.2

%description   -n gem-io-endpoint-doc
Provides a separation of concerns interface for IO endpoints documentation
files.

Provides a separation of concerns interface for IO endpoints. This allows you to
write code which is agnostic to the underlying IO implementation.

%description   -n gem-io-endpoint-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета io-endpoint.
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
%files         -n gem-io-endpoint-doc
%doc license.md readme.md
%ruby_gemdocdir
%endif


%changelog
* Fri Mar 20 2026 Pavel Skrylev <majioa@altlinux.org> 0.17.2-alt1
- ^ 0.13.0 -> 0.17.2

* Tue Jul 30 2024 Pavel Skrylev <majioa@altlinux.org> 0.13.0-alt1
- + packaged gem with Ruby Policy 2.0
