%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    devel
%define        gemname zlib

Name:          gem-zlib
Version:       3.2.3
Release:       alt1
Summary:       Ruby interface for the zlib compression/decompression library
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/zlib
Vcs:           https://github.com/ruby/zlib.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
BuildRequires: pkgconfig(ruby)
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(ruby-core-tasks) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(test-unit-ruby-core) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.7.0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(ruby-core-tasks) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(test-unit-ruby-core) >= 0
Provides:      gem(zlib) = 3.2.3

%description
Ruby interface for the zlib compression/decompression library


%if_enabled    devel
%package       -n gem-zlib-devel
Version:       3.2.3
Release:       alt1
Summary:       Ruby interface for the zlib compression/decompression library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета zlib
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(zlib) = 3.2.3

%description   -n gem-zlib-devel
Ruby interface for the zlib compression/decompression library development
package.

%description   -n gem-zlib-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета zlib.
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
%doc COPYING README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    devel
%files         -n gem-zlib-devel
%doc COPYING README.md
%endif


%changelog
* Tue Sep 29 2026 Pavel Skrylev <majioa@altlinux.org> 3.2.3-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
