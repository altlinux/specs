%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname lolcat

Name:          gem-lolcat
Version:       100.0.1
Release:       alt1
Summary:       Okay, no unicorns. But rainbows!!
License:       BSD-3-Clause
Group:         Development/Ruby
Url:           https://github.com/busyloop/lolcat
Vcs:           https://github.com/busyloop/lolcat.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(manpages) >= 0.6.1
BuildRequires: gem(optimist) >= 3.0.0
BuildRequires: gem(paint) >= 2.1
BuildRequires: gem(rake) >= 0
BuildConflicts: gem(manpages) >= 1
BuildConflicts: gem(optimist) >= 4
BuildConflicts: gem(paint) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency manpages >= 0.7.0,manpages < 1
%ruby_use_gem_dependency optimist >= 3.0.1,optimist < 4
Requires:      gem(manpages) >= 0.6.1
Requires:      gem(optimist) >= 3.0.0
Requires:      gem(paint) >= 2.1
Conflicts:     gem(manpages) >= 1
Conflicts:     gem(optimist) >= 4
Conflicts:     gem(paint) >= 3
Provides:      gem(lolcat) = 100.0.1

%description
Rainbows and unicorns!


%package       -n lolcat-rb
Version:       100.0.1
Release:       alt1
Summary:       Okay, no unicorns. But rainbows!! executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета lolcat
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(lolcat) = 100.0.1

%description   -n lolcat-rb
Okay, no unicorns. But rainbows!! executable(s).

Rainbows and unicorns!

%description   -n lolcat-rb -l ru_RU.UTF-8
Исполнямка для самоцвета lolcat.


%if_enabled    doc
%package       -n gem-lolcat-doc
Version:       100.0.1
Release:       alt1
Summary:       Okay, no unicorns. But rainbows!! documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета lolcat
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(lolcat) = 100.0.1

%description   -n gem-lolcat-doc
Okay, no unicorns. But rainbows!! documentation files.

Rainbows and unicorns!

%description   -n gem-lolcat-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета lolcat.
%endif


%if_enabled    devel
%package       -n gem-lolcat-devel
Version:       100.0.1
Release:       alt1
Summary:       Okay, no unicorns. But rainbows!! development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета lolcat
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(lolcat) = 100.0.1
Requires:      gem(rake) >= 0

%description   -n gem-lolcat-devel
Okay, no unicorns. But rainbows!! development package.

Rainbows and unicorns!

%description   -n gem-lolcat-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета lolcat.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install
# rename executable and man page to avoid file conflict with the lolcat package
mv %buildroot%_bindir/lolcat %buildroot%_bindir/lolcat-rb
mv %buildroot%_mandir/lolcat.6 %buildroot%_mandir/lolcat-rb.6

%check
%ruby_test

%files
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n lolcat-rb
%doc LICENSE README.md
%_bindir/lolcat-rb
%_mandir/lolcat-rb.*

%if_enabled    doc
%files         -n gem-lolcat-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-lolcat-devel
%doc LICENSE README.md
%endif


%changelog
* Tue Jul 07 2026 Alexander Burmatov <thatman@altlinux.org> 100.0.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
