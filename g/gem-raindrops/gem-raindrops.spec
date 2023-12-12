%define        _unpackaged_files_terminate_build 1
%define        gemname raindrops

Name:          gem-raindrops
Version:       0.20.1
Release:       alt1
Summary:       real-time stats for preforking Rack servers
License:       LGPL-2.1+
Group:         Development/Ruby
Url:           http://raindrops.bogomips.org/
Vcs:           git://bogomips.org/raindrops.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(aggregate) >= 0.2
BuildRequires: gem(test-unit) >= 3.0
BuildRequires: gem(posix_mq) >= 2.0
BuildRequires: gem(rack) >= 1.2
BuildConflicts: gem(aggregate) >= 1
BuildConflicts: gem(test-unit) >= 4
BuildConflicts: gem(posix_mq) >= 3
BuildConflicts: gem(rack) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-raindrops < %EVR
Provides:      ruby-raindrops = %EVR
Provides:      gem(raindrops) = 0.20.1


%description
Raindrops is a real time stats package to show statistics for Rack HTTP servers.
It is designed for preforking servers such as Rainbows! and Unicorn, but should
support any Rack HTTP server under Ruby and possibly Rubinius (untested) on
platforms supporting POSIX shared memory and compiled with GCC (for atomic
builtins). Raindrops includes a Struct-like Raindrops::Struct class that may be
used standalone to create atomic counters shared across any number of forked
processes under SMP.


%package       -n gem-raindrops-doc
Version:       0.20.1
Release:       alt1
Summary:       real-time stats for preforking Rack servers documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета raindrops
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(raindrops) = 0.20.1

%description   -n gem-raindrops-doc
real-time stats for preforking Rack servers documentation files.

Raindrops is a real time stats package to show statistics for Rack HTTP servers.
It is designed for preforking servers such as Rainbows! and Unicorn, but should
support any Rack HTTP server under Ruby and possibly Rubinius (untested) on
platforms supporting POSIX shared memory and compiled with GCC (for atomic
builtins). Raindrops includes a Struct-like Raindrops::Struct class that may be
used standalone to create atomic counters shared across any number of forked
processes under SMP.

%description   -n gem-raindrops-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета raindrops.


%package       -n gem-raindrops-devel
Version:       0.20.1
Release:       alt1
Summary:       real-time stats for preforking Rack servers development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета raindrops
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(raindrops) = 0.20.1
Requires:      gem(aggregate) >= 0.2
Requires:      gem(test-unit) >= 3.0
Requires:      gem(posix_mq) >= 2.0
Requires:      gem(rack) >= 1.2
Conflicts:     gem(aggregate) >= 1
Conflicts:     gem(test-unit) >= 4
Conflicts:     gem(posix_mq) >= 3
Conflicts:     gem(rack) >= 3

%description   -n gem-raindrops-devel
real-time stats for preforking Rack servers development package.

Raindrops is a real time stats package to show statistics for Rack HTTP servers.
It is designed for preforking servers such as Rainbows! and Unicorn, but should
support any Rack HTTP server under Ruby and possibly Rubinius (untested) on
platforms supporting POSIX shared memory and compiled with GCC (for atomic
builtins). Raindrops includes a Struct-like Raindrops::Struct class that may be
used standalone to create atomic counters shared across any number of forked
processes under SMP.

%description   -n gem-raindrops-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета raindrops.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-raindrops-doc
%doc README
%ruby_gemdocdir

%files         -n gem-raindrops-devel
%doc README
%ruby_includedir/*


%changelog
* Wed Dec 06 2023 Pavel Skrylev <majioa@altlinux.org> 0.20.1-alt1
- ^ 0.20.0 -> 0.20.1

* Thu Mar 17 2022 Pavel Skrylev <majioa@altlinux.org> 0.20.0-alt1
- ^ 0.19.1 -> 0.20.0

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 0.19.1-alt1
- ^ 0.19.0 -> 0.19.1
- ! spec tags and syntax

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.19.0-alt2
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt1.5
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt1.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt1.1
- Rebuild with Ruby 2.4.1

* Thu Aug 10 2017 Andrey Cherepanov <cas@altlinux.org> 0.19.0-alt1
- New version

* Thu Mar 23 2017 Andrey Cherepanov <cas@altlinux.org> 0.18.0-alt1
- New version

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.17.0-alt2
- Rebuild with new %%ruby_sitearchdir location

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 0.17.0-alt1
- new version 0.17.0

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.7.0-alt2.2
- Rebuilt with ruby-2.0.0-alt1

* Thu Dec 06 2012 Led <led@altlinux.ru> 0.7.0-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Mon Aug 15 2011 Anton Gorlov <stalker@altlinux.ru> 0.7.0-alt2
- fix wrong url

* Wed Aug 10 2011 Anton Gorlov <stalker@altlinux.ru> 0.7.0-alt1
- initial build for ALTLinux
