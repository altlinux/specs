%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rqrcode

Name:          gem-rqrcode
Version:       3.2.0
Release:       alt1
Summary:       A library to encode QR Codes
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/whomwah/rqrcode
Vcs:           https://github.com/whomwah/rqrcode.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(benchmark-ips) >= 2.0
BuildRequires: gem(bundler) >= 2.1.4
BuildRequires: gem(chunky_png) >= 1.0
BuildRequires: gem(memory_profiler) >= 1.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rqrcode_core) >= 2.0
BuildRequires: gem(rspec) >= 3.5
BuildRequires: gem(stackprof) >= 0.2
BuildRequires: gem(standard) >= 1.41
BuildConflicts: gem(benchmark-ips) >= 3
BuildConflicts: gem(bundler) >= 5
BuildConflicts: gem(chunky_png) >= 2
BuildConflicts: gem(memory_profiler) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rqrcode_core) >= 3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(stackprof) >= 1
BuildConflicts: gem(standard) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Requires:      ruby >= 3.2
Requires:      gem(chunky_png) >= 1.0
Requires:      gem(rqrcode_core) >= 2.0
Conflicts:     gem(chunky_png) >= 2
Conflicts:     gem(rqrcode_core) >= 3
Obsoletes:     ruby-rqrcode < %EVR
Provides:      ruby-rqrcode = %EVR
Provides:      rqrcode = %EVR
Provides:      gem(rqrcode) = 3.2.0

%description
rqrcode is a library for encoding QR Codes. The simple interface allows you to
create QR Code data structures and then render them in the way you choose.


%if_enabled    doc
%package       -n gem-rqrcode-doc
Version:       3.2.0
Release:       alt1
Summary:       A library to encode QR Codes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rqrcode
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rqrcode) = 3.2.0

%description   -n gem-rqrcode-doc
A library to encode QR Codes documentation files.

rqrcode is a library for encoding QR Codes. The simple interface allows you to
create QR Code data structures and then render them in the way you choose.

%description   -n gem-rqrcode-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rqrcode.
%endif


%if_enabled    devel
%package       -n gem-rqrcode-devel
Version:       3.2.0
Release:       alt1
Summary:       A library to encode QR Codes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rqrcode
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rqrcode) = 3.2.0
Requires:      gem(benchmark-ips) >= 2.0
Requires:      gem(bundler) >= 2.1.4
Requires:      gem(memory_profiler) >= 1.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.5
Requires:      gem(stackprof) >= 0.2
Requires:      gem(standard) >= 1.41
Conflicts:     gem(benchmark-ips) >= 3
Conflicts:     gem(bundler) >= 5
Conflicts:     gem(memory_profiler) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(stackprof) >= 1
Conflicts:     gem(standard) >= 2

%description   -n gem-rqrcode-devel
A library to encode QR Codes development package.

rqrcode is a library for encoding QR Codes. The simple interface allows you to
create QR Code data structures and then render them in the way you choose.

%description   -n gem-rqrcode-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rqrcode.
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
%files         -n gem-rqrcode-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rqrcode-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Thu Aug 27 2026 Pavel Skrylev <majioa@altlinux.org> 3.2.0-alt1
- ^ 2.1.0 -> 3.2.0

* Thu Jun 30 2022 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- ^ 1.1.2 -> 2.1.0

* Mon Feb 03 2020 Alexey Shabalin <shaba@altlinux.org> 1.1.2-alt1
- Initial build.
