%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_disable   doc
%def_enable    devel
%define        gemname absolute_time

Name:          gem-absolute-time
Version:       1.0.0.2
Release:       alt0.1
Summary:       Reliable monotonically increasing timer for measuring time intervals
License:       BSD
Group:         Development/Ruby
Url:           https://github.com/bwbuchanan/absolute_time
Vcs:           https://github.com/bwbuchanan/absolute_time.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names absolute_time,absolute-time
Provides:      gem(absolute_time) = 1.0.0.2

%ruby_use_gem_version absolute_time:1.0.0.2

%description
This gem provides a monotonically increasing timer to permit safe measurement of
time intervals.

Using Time.now for measuring intervals is not reliable (and sometimes unsafe)
because the system clock may be stepped forwards or backwards between the two
measurements, or may be running slower or faster than real time in order to
effect clock synchronization with UTC.

The module uses OS-specific functions such as mach_absolute_time() and
clock_gettime() to access the system tick counter. The time values returned by
this module cannot be interpreted as real time clock values; they are only
useful for comparison with another time value from this module.


%if_enabled    doc
%package       -n gem-absolute-time-doc
Version:       1.0.0.2
Release:       alt0.1
Summary:       Reliable monotonically increasing timer for measuring time intervals documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета absolute_time
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(absolute_time) = 1.0.0.2

%description   -n gem-absolute-time-doc
Reliable monotonically increasing timer for measuring time intervals
documentation files.

%description   -n gem-absolute-time-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета absolute_time.
%endif


%if_enabled    devel
%package       -n gem-absolute-time-devel
Version:       1.0.0.2
Release:       alt0.1
Summary:       Reliable monotonically increasing timer for measuring time intervals development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета absolute_time
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(absolute_time) = 1.0.0.2

%description   -n gem-absolute-time-devel
Reliable monotonically increasing timer for measuring time intervals development
package.

%description   -n gem-absolute-time-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета absolute_time.
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
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-absolute-time-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-absolute-time-devel
%doc README.md
%endif


%changelog
* Tue Jul 23 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.0.2-alt0.1
- ^ 1.0.0 -> 1.0.0p2

* Sun Feb 05 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
