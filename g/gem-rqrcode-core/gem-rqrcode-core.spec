%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rqrcode_core

Name:          gem-rqrcode-core
Version:       2.1.0
Release:       alt1
Summary:       A library to encode QR Codes
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/chuckremes/ffi-rzmq-core.git
Vcs:           https://github.com/chuckremes/ffi-rzmq-core.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(benchmark-ips) >= 2.0
BuildRequires: gem(bundler) >= 2.1.4
BuildRequires: gem(memory_profiler) >= 1.0
BuildRequires: gem(minitest) >= 6.0
BuildRequires: gem(rake) >= 13.1.0
BuildRequires: gem(stackprof) >= 0.2
BuildRequires: gem(standard) >= 1.41
BuildConflicts: gem(benchmark-ips) >= 3
BuildConflicts: gem(bundler) >= 5
BuildConflicts: gem(memory_profiler) >= 2
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(stackprof) >= 1
BuildConflicts: gem(standard) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_alias_names rqrcode_core,rqrcode-core
Requires:      ruby >= 3.2
Obsoletes:     ruby-rqrcode_core < %EVR
Provides:      ruby-rqrcode_core = %EVR
Provides:      gem(rqrcode_core) = 2.1.0

%description
rqrcode_core is a Ruby library for encoding QR Codes. The simple interface (with
no runtime dependencies) allows you to create QR Code data structures.


%if_enabled    doc
%package       -n gem-rqrcode-core-doc
Version:       2.1.0
Release:       alt1
Summary:       A library to encode QR Codes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rqrcode_core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rqrcode_core) = 2.1.0

%description   -n gem-rqrcode-core-doc
A library to encode QR Codes documentation files.

rqrcode_core is a Ruby library for encoding QR Codes. The simple interface (with
no runtime dependencies) allows you to create QR Code data structures.

%description   -n gem-rqrcode-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rqrcode_core.
%endif


%if_enabled    devel
%package       -n gem-rqrcode-core-devel
Version:       2.1.0
Release:       alt1
Summary:       A library to encode QR Codes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rqrcode_core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rqrcode_core) = 2.1.0
Requires:      gem(benchmark-ips) >= 2.0
Requires:      gem(bundler) >= 2.1.4
Requires:      gem(memory_profiler) >= 1.0
Requires:      gem(minitest) >= 6.0
Requires:      gem(rake) >= 13.1.0
Requires:      gem(stackprof) >= 0.2
Requires:      gem(standard) >= 1.41
Conflicts:     gem(benchmark-ips) >= 3
Conflicts:     gem(bundler) >= 5
Conflicts:     gem(memory_profiler) >= 2
Conflicts:     gem(minitest) >= 7
Conflicts:     gem(rake) >= 14
Conflicts:     gem(stackprof) >= 1
Conflicts:     gem(standard) >= 2

%description   -n gem-rqrcode-core-devel
A library to encode QR Codes development package.

rqrcode_core is a Ruby library for encoding QR Codes. The simple interface (with
no runtime dependencies) allows you to create QR Code data structures.

%description   -n gem-rqrcode-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rqrcode_core.
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
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rqrcode-core-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rqrcode-core-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Sat Aug 22 2026 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- ^ 1.2.0 -> 2.1.0

* Thu Jun 30 2022 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- ^ 0.1.1 -> 1.2.0

* Mon Feb 03 2020 Alexey Shabalin <shaba@altlinux.org> 0.1.1-alt1
- Initial build.
