%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname timeout-interrupt

Name:          gem-timeout-interrupt
Version:       0.4.0
Release:       alt1
Summary:       "Interrupts systemcalls too."
License:       LGPLv3
Group:         Development/Ruby
Url:           https://git.denkn.at/deac/ruby-timeout-interrupt
Vcs:           https://git.denkn.at/deac/ruby-timeout-interrupt.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(shoulda) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(ffi-libc) >= 0.1.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ffi-libc) >= 0.1.1
Provides:      gem(timeout-interrupt) = 0.4.0


%description
Timeout-lib, which interrupts everything, also systemcalls. It uses libc-alarm.


%if_enabled    doc
%package       -n gem-timeout-interrupt-doc
Version:       0.4.0
Release:       alt1
Summary:       "Interrupts systemcalls too." documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета timeout-interrupt
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(timeout-interrupt) = 0.4.0

%description   -n gem-timeout-interrupt-doc
"Interrupts systemcalls too." documentation files.

Timeout-lib, which interrupts everything, also systemcalls. It uses libc-alarm.

%description   -n gem-timeout-interrupt-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета timeout-interrupt.
%endif


%if_enabled    devel
%package       -n gem-timeout-interrupt-devel
Version:       0.4.0
Release:       alt1
Summary:       "Interrupts systemcalls too." development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета timeout-interrupt
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(timeout-interrupt) = 0.4.0
Requires:      gem(test-unit) >= 0
Requires:      gem(shoulda) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(bundler) >= 0

%description   -n gem-timeout-interrupt-devel
"Interrupts systemcalls too." development package.

Timeout-lib, which interrupts everything, also systemcalls. It uses libc-alarm.

%description   -n gem-timeout-interrupt-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета timeout-interrupt.
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
%files         -n gem-timeout-interrupt-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-timeout-interrupt-devel
%doc README.md
%endif


%changelog
* Tue Jul 30 2024 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- + packaged gem with Ruby Policy 2.0
