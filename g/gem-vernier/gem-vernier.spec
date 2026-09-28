%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname vernier

Name:          gem-vernier
Version:       1.11.0
Release:       alt1
Summary:       A next generation CRuby profiler
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jhawthorn/vernier
Vcs:           https://github.com/jhawthorn/vernier.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
BuildRequires: pkgconfig(ruby)
%if_enabled check
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(cgi) >= 0
BuildRequires: gem(gvltest) >= 0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(rack) >= 0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(zlib) >= 3.2.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 6.0
%ruby_use_gem_dependency rake >= 13.0
Requires:      ruby >= 3.2.1
Provides:      gem(vernier) = 1.11.0

%description
Next-generation Ruby 3.2.1+ sampling profiler. Tracks multiple threads, GVL
activity, GC pauses, idle time, and more.


%package       -n vernier
Version:       1.11.0
Release:       alt1
Summary:       A next generation CRuby profiler executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета vernier
Group:         Other
BuildArch:     noarch

Requires:      gem(vernier) = 1.11.0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(cgi) >= 0
Requires:      gem(minitest) >= 5.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(zlib) >= 3.2.1

%description   -n vernier
A next generation CRuby profiler executable(s).

Next-generation Ruby 3.2.1+ sampling profiler. Tracks multiple threads, GVL
activity, GC pauses, idle time, and more.

%description   -n vernier -l ru_RU.UTF-8
Исполнямка для самоцвета vernier.


%if_enabled    doc
%package       -n gem-vernier-doc
Version:       1.11.0
Release:       alt1
Summary:       A next generation CRuby profiler documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета vernier
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(vernier) = 1.11.0

%description   -n gem-vernier-doc
A next generation CRuby profiler documentation files.

Next-generation Ruby 3.2.1+ sampling profiler. Tracks multiple threads, GVL
activity, GC pauses, idle time, and more.

%description   -n gem-vernier-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета vernier.
%endif


%if_enabled    devel
%package       -n gem-vernier-devel
Version:       1.11.0
Release:       alt1
Summary:       A next generation CRuby profiler development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета vernier
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(vernier) = 1.11.0
Requires:      gem(activesupport) >= 0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(cgi) >= 0
Requires:      gem(gvltest) >= 0
Requires:      gem(minitest) >= 5.0
Requires:      gem(rack) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(zlib) >= 3.2.1

%description   -n gem-vernier-devel
A next generation CRuby profiler development package.

Next-generation Ruby 3.2.1+ sampling profiler. Tracks multiple threads, GVL
activity, GC pauses, idle time, and more.

%description   -n gem-vernier-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета vernier.
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
%doc CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n vernier
%doc CODE_OF_CONDUCT.md LICENSE.txt README.md
%_bindir/vernier

%if_enabled    doc
%files         -n gem-vernier-doc
%doc CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-vernier-devel
%doc CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_includedir/*
%endif


%changelog
* Tue Sep 29 2026 Pavel Skrylev <majioa@altlinux.org> 1.11.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
