%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rack-cache

Name:          gem-rack-cache
Version:       1.17.0
Release:       alt1
Summary:       Real HTTP Caching for Ruby Web Apps
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rack/rack-cache
Vcs:           https://github.com/rack/rack-cache.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         dep-gem-name.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rack) >= 0.4
BuildRequires: gem(maxitest) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(mutex_m) >= 0
BuildRequires: gem(dalli) >= 0
BuildRequires: gem(bump) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(hanna) >= 1.5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rack) >= 0.4
Obsoletes:     ruby-rack-cache < %EVR
Provides:      ruby-rack-cache = %EVR
Provides:      gem(rack-cache) = 1.17.0


%description
Rack::Cache is suitable as a quick drop-in component to enable HTTP caching for
Rack-based applications that produce freshness (Expires, Cache-Control) and/or
validation (Last-Modified, ETag) information:

* Standards-based (RFC 2616)
* Freshness/expiration based caching
* Validation (If-Modified-Since / If-None-Match)
* Vary support
* Cache-Control: public, private, max-age, s-maxage, must-revalidate, and
  proxy-revalidate.
* Portable: 100% Ruby / works with any Rack-enabled framework
* Disk, memcached, and heap memory storage backends


%if_enabled    doc
%package       -n gem-rack-cache-doc
Version:       1.17.0
Release:       alt1
Summary:       Real HTTP Caching for Ruby Web Apps documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rack-cache
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rack-cache) = 1.17.0

%description   -n gem-rack-cache-doc
Real HTTP Caching for Ruby Web Apps documentation files.

Rack::Cache is suitable as a quick drop-in component to enable HTTP caching for
Rack-based applications that produce freshness (Expires, Cache-Control) and/or
validation (Last-Modified, ETag) information:

* Standards-based (RFC 2616)
* Freshness/expiration based caching
* Validation (If-Modified-Since / If-None-Match)
* Vary support
* Cache-Control: public, private, max-age, s-maxage, must-revalidate, and
  proxy-revalidate.
* Portable: 100% Ruby / works with any Rack-enabled framework
* Disk, memcached, and heap memory storage backends

%description   -n gem-rack-cache-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rack-cache.
%endif


%if_enabled    devel
%package       -n gem-rack-cache-devel
Version:       1.17.0
Release:       alt1
Summary:       Real HTTP Caching for Ruby Web Apps development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rack-cache
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rack-cache) = 1.17.0
Requires:      gem(maxitest) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(mutex_m) >= 0
Requires:      gem(dalli) >= 0
Requires:      gem(bump) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(hanna) >= 1.5

%description   -n gem-rack-cache-devel
Real HTTP Caching for Ruby Web Apps development package.

Rack::Cache is suitable as a quick drop-in component to enable HTTP caching for
Rack-based applications that produce freshness (Expires, Cache-Control) and/or
validation (Last-Modified, ETag) information:

* Standards-based (RFC 2616)
* Freshness/expiration based caching
* Validation (If-Modified-Since / If-None-Match)
* Vary support
* Cache-Control: public, private, max-age, s-maxage, must-revalidate, and
  proxy-revalidate.
* Portable: 100% Ruby / works with any Rack-enabled framework
* Disk, memcached, and heap memory storage backends

%description   -n gem-rack-cache-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rack-cache.
%endif


%prep
%setup
%autopatch -p1

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
%files         -n gem-rack-cache-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rack-cache-devel
%doc README.md
%endif


%changelog
* Tue May 14 2024 Pavel Skrylev <majioa@altlinux.org> 1.17.0-alt1
- ^ 1.13.0 -> 1.17.0

* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 1.13.0-alt1
- ^ 1.8.0 -> 1.13.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 1.8.0-alt1
- Initial build for Sisyphus
