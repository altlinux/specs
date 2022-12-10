%define _unpackaged_files_terminate_build 1
%define pypi_name udatetime

%def_with check

Name: python3-module-%pypi_name
Version: 0.0.17
Release: alt1

Summary: Fast RFC3339 compliant Python date-time library 
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/udatetime
Vcs: https://github.com/freach/udatetime.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

%description
Handling date-times is a painful act because of the sheer endless amount
of formats used by people. Luckily there are a couple of specified
standards out there like ISO 8601. But even ISO 8601 leaves to many
options on how to define date and time. That's why I encourage using the
RFC3339 specified date-time format.

udatetime offers on average 76%% faster datetime object instantiation,
serialization and deserialization of RFC3339 date-time strings.
udatetime is using Python's datetime class under the hood and code
already using datetime should be able to easily switch to udatetime.
All datetime objects created by udatetime are timezone-aware. The
timezones that udatetime uses are fixed-offset timezones, meaning
that they don't observe daylight savings time (DST), and thus return
a fixed offset from UTC all year round.

%package benchmark
Summary: Benchmark for %pypi_name
Group: Development/Python3
BuildArch: noarch

%description benchmark
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

mv %buildroot%_bindir/bench_udatetime.py \
   %buildroot%_bindir/udatetime_benchmark.py3

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.md LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files benchmark
%_bindir/udatetime_benchmark.py3

%changelog
* Sat Dec 10 2022 Anton Zhukharev <ancieg@altlinux.org> 0.0.17-alt1
- initial build for Sisyphus
