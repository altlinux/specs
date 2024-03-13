%define _unpackaged_files_terminate_build 1
%def_with check
%define pypi_name about-time
%define mod_name about_time

Name: python3-module-%pypi_name
Version: 4.2.1
Release: alt2

Summary: A cool helper for tracking time and throughput of code blocks
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/about-time/
Vcs: https://github.com/rsalmei/about-time

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
%if_with check
BuildRequires: python3-module-pytest
%endif

%description
Did you ever need to measure the duration of an operation? Yeah, this is easy.
But how to:
- measure the duration of two or more blocks at the same time, including
    the whole duration?
- instrument a code to cleanly retrieve durations in one line, to log
    or send to time series databases?
- easily see human friendly durations in s (seconds), ms (milliseconds),
    ms (microseconds) and even ns (nanoseconds)?
- easily see human friendly counts with SI prefixes like k, M, G, T, etc?
- measure the actual throughput of a block? (this is way harder, since
    it needs to measure both duration and number of iterations)
- easily see human friendly throughputs in "/second", "/minute",
    "/hour" or even "/day", including SI prefixes?
Yes, it can get tricky!
If you'd tried to do it without these magic, it would probably get messy and
immensely pollute the code being instrumented.
I have the solution, behold!

%prep
%setup -q

%build
%pyproject_build

%install
%pyproject_install
# Remove wrongly installed LICENSE
rm %buildroot/%_usr/LICENSE

%check
%pyproject_run_pytest

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Tue Mar 12 2024 Alexander Kuznetov <kuznetsovam@altlinux.org> 4.2.1-alt2
- Add setuptools BR.

* Sun Dec 24 2023 Alexander Kuznetsov <kuznetsovam@altlinux.org> 4.2.1-alt1
- Initial build.
