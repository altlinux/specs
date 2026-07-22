%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%define        gemname lockfile

Name:          gem-lockfile
Version:       2.1.3
Release:       alt1
Summary:       lockfile
License:       Ruby
Group:         Development/Ruby
Url:           https://github.com/ahoward/lockfile
Vcs:           https://github.com/ahoward/lockfile.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(lockfile) = 2.1.3

%description
a ruby library for creating perfect and NFS safe lockfiles


%package       -n rlock
Version:       2.1.3
Release:       alt1
Summary:       lockfile executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета lockfile
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(lockfile) = 2.1.3

%description   -n rlock
lockfile executable(s).

a ruby library for creating perfect and NFS safe lockfiles

%description   -n rlock -l ru_RU.UTF-8
Исполнямка для самоцвета lockfile.


%if_enabled    doc
%package       -n gem-lockfile-doc
Version:       2.1.3
Release:       alt1
Summary:       lockfile documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета lockfile
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(lockfile) = 2.1.3

%description   -n gem-lockfile-doc
lockfile documentation files.

a ruby library for creating perfect and NFS safe lockfiles

%description   -n gem-lockfile-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета lockfile.
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
%doc README readme.erb
%ruby_gemspec
%ruby_gemlibdir

%files         -n rlock
%doc README readme.erb
%_bindir/rlock

%if_enabled    doc
%files         -n gem-lockfile-doc
%doc README readme.erb
%ruby_gemdocdir
%endif


%changelog
* Fri Jul 03 2026 Alexander Burmatov <thatman@altlinux.org> 2.1.3-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
