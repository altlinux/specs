%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname puma_worker_killer

Name:          gem-puma-worker-killer
Version:       1.0.0
Release:       alt1
Summary:       In-check memory leaks keeper
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/schneems/puma_worker_killer
Vcs:           https://github.com/schneems/puma_worker_killer.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 13.0
%if_enabled check
BuildRequires: gem(bigdecimal) >= 2.0
BuildRequires: gem(get_process_mem) >= 0.2
BuildRequires: gem(puma) >= 2.7
BuildRequires: gem(rack) >= 3.0.0
BuildRequires: gem(rackup) >= 2.1
BuildRequires: gem(standard) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(wait_for_it) >= 0.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names puma_worker_killer,puma-worker-killer
Requires:      gem(bigdecimal) >= 2.0
Requires:      gem(get_process_mem) >= 0.2
Requires:      gem(puma) >= 2.7
Requires:      gem(standard) >= 0
Provides:      gem(puma_worker_killer) = 1.0.0

%description
If you have a memory leak in your web code puma_worker_killer can keep it in
check. Kills pumas, the code kind.

Before you use this gem, know that it is dangerous. If you have a memory issue,
you need to fix the issue. The original idea behind this gem is that it would
act as a temporary band-aid to buy you time to allow you to fix your issues. If
you turn this on and don't fix the underlying memory problems, then things will
only get worse over time.

This gem can also make your performance WORSE. When a worker is killed, and
comes back it takes CPU cycles and time. If you are frequently restarting your
workers then you're killing your performance.

If you have a memory leak in your code, finding and plugging it can be a
herculean effort. Instead what if you just killed your processes when they got
to be too large? The Puma Worker Killer does just that. Similar to Unicorn
Worker Killer but for the Puma web server.

Puma worker killer can only function if you have enabled cluster mode or hybrid
mode (threads + worker cluster). If you are only using threads (and not workers)
then puma worker killer cannot help keep your memory in control.

BTW restarting your processes to control memory is like putting a bandaid on a
gunshot wound, try figuring out the reason you're seeing so much memory bloat
derailed benchmarks can help.


%if_enabled    doc
%package       -n gem-puma-worker-killer-doc
Version:       1.0.0
Release:       alt1
Summary:       In-check memory leaks keeper documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета puma_worker_killer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(puma_worker_killer) = 1.0.0

%description   -n gem-puma-worker-killer-doc
If you have a memory leak in your web code puma_worker_killer can keep it in
check documentation files.

Kills pumas, the code kind.

Before you use this gem, know that it is dangerous. If you have a memory issue,
you need to fix the issue. The original idea behind this gem is that it would
act as a temporary band-aid to buy you time to allow you to fix your issues. If
you turn this on and don't fix the underlying memory problems, then things will
only get worse over time.

This gem can also make your performance WORSE. When a worker is killed, and
comes back it takes CPU cycles and time. If you are frequently restarting your
workers then you're killing your performance.

%description   -n gem-puma-worker-killer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета puma_worker_killer.
%endif


%if_enabled    devel
%package       -n gem-puma-worker-killer-devel
Version:       1.0.0
Release:       alt1
Summary:       In-check memory leaks keeper development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета puma_worker_killer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(puma_worker_killer) = 1.0.0
Requires:      gem(rack) >= 3.0.0
Requires:      gem(rackup) >= 2.1
Requires:      gem(rake) >= 13.0
Requires:      gem(test-unit) >= 0
Requires:      gem(wait_for_it) >= 0.1

%description   -n gem-puma-worker-killer-devel
If you have a memory leak in your web code puma_worker_killer can keep it in
check development package.

Kills pumas, the code kind.

Before you use this gem, know that it is dangerous. If you have a memory issue,
you need to fix the issue. The original idea behind this gem is that it would
act as a temporary band-aid to buy you time to allow you to fix your issues. If
you turn this on and don't fix the underlying memory problems, then things will
only get worse over time.

This gem can also make your performance WORSE. When a worker is killed, and
comes back it takes CPU cycles and time. If you are frequently restarting your
workers then you're killing your performance.

%description   -n gem-puma-worker-killer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета puma_worker_killer.
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
%doc CHANGELOG.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-puma-worker-killer-doc
%doc CHANGELOG.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-puma-worker-killer-devel
%doc CHANGELOG.md README.md
%endif


%changelog
* Thu Mar 06 2025 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
