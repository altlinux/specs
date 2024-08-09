%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ffi-libc

Name:          gem-ffi-libc
Version:       0.1.1
Release:       alt1
Summary:       Useful FFI bindings for libc
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/postmodern/ffi-libc#redme
Vcs:           https://github.com/postmodern/ffi-libc.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubygems-tasks) >= 0.2
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(ffi) >= 1.0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rubygems-tasks) >= 1
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(ffi) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ffi) >= 1.0
Conflicts:     gem(ffi) >= 2
Provides:      gem(ffi-libc) = 0.1.1


%description
Useful Ruby FFI bindings for libc.


%if_enabled    doc
%package       -n gem-ffi-libc-doc
Version:       0.1.1
Release:       alt1
Summary:       Useful FFI bindings for libc documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ffi-libc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ffi-libc) = 0.1.1

%description   -n gem-ffi-libc-doc
Useful FFI bindings for libc documentation files.

Useful Ruby FFI bindings for libc.

%description   -n gem-ffi-libc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ffi-libc.
%endif


%if_enabled    devel
%package       -n gem-ffi-libc-devel
Version:       0.1.1
Release:       alt1
Summary:       Useful FFI bindings for libc development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ffi-libc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ffi-libc) = 0.1.1
Requires:      gem(bundler) >= 2.0
Requires:      gem(rake) >= 0
Requires:      gem(rubygems-tasks) >= 0.2
Requires:      gem(rspec) >= 3.0
Requires:      gem(kramdown) >= 0
Requires:      gem(yard) >= 0.9
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rubygems-tasks) >= 1
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(yard) >= 1

%description   -n gem-ffi-libc-devel
Useful FFI bindings for libc development package.

Useful Ruby FFI bindings for libc.

%description   -n gem-ffi-libc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ffi-libc.
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
%files         -n gem-ffi-libc-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ffi-libc-devel
%doc README.md
%endif


%changelog
* Tue Jul 30 2024 Pavel Skrylev <majioa@altlinux.org> 0.1.1-alt1
- + packaged gem with Ruby Policy 2.0
