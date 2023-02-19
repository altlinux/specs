%define        gemname absolute_time

Name:          gem-absolute-time
Version:       1.0.0
Release:       alt1
Summary:       Reliable monotonically increasing timer for measuring time intervals
License:       BSD
Group:         Development/Ruby
Url:           https://github.com/bwbuchanan/absolute_time
Vcs:           https://github.com/bwbuchanan/absolute_time.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(absolute_time) = 1.0.0


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


%package       -n gem-absolute-time-devel
Version:       1.0.0
Release:       alt1
Summary:       Reliable monotonically increasing timer for measuring time intervals development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета absolute_time
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(absolute_time) = 1.0.0

%description   -n gem-absolute-time-devel
Reliable monotonically increasing timer for measuring time intervals development
package.

%description   -n gem-absolute-time-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета absolute_time.


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

%files         -n gem-absolute-time-devel
%doc README.md


%changelog
* Sun Feb 05 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
