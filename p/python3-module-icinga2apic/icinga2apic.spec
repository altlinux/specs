%define _unpackaged_files_terminate_build 1
%define oname icinga2apic

Name: python3-module-%oname
Version: 0.7.5
Release: alt3

Summary: Python Icinga 2 API
License: 2-Clause BSD
Group: Development/Python3
Url: https://github.com/TeraIT-at/icinga2apic

Source: %name-%version.tar

Patch0: %name-%version-events_connect.patch

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel

BuildArch: noarch

%description
icinga2apic is a Python module to interact with the Icinga 2 RESTful API.

%prep
%setup
%patch0 -p1

%build
%python3_build

%install
%python3_install
%python3_prune

%files
%python3_sitelibdir/*

%changelog
* Tue Apr 02 2024 Paul Wolneykien <manowar@altlinux.org> 0.7.5-alt3
- Wrap the event stream generator into a function in order to run
  the initialization code immediately (patch).

* Sat Mar 30 2021 Paul Wolneykien <manowar@altlinux.org> 0.7.5-alt2
- Make unpackaged files terminate build.

* Mon Mar 29 2021 Paul Wolneykien <manowar@altlinux.org> 0.7.5-alt1
- Switch to icinga2apic: a "continued" fork of the original icinga2api
  project.

* Mon Mar 29 2021 Paul Wolneykien <manowar@altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus.
