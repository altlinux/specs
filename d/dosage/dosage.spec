%define pypi_name dosage

%def_with check

Name:       dosage
Version:    3.0
Release:    alt1

Summary:    dosage is a comic strip downloader and archiver
License:    MIT
Group:      Other
URL:        https://pypi.org/project/dosage
Vcs:        https://github.com/webcomics/dosage

BuildArch:  noarch

Source0:    %name-%version.tar
Patch:      drop-distutils.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-colorama
BuildRequires: python3-module-lxml
BuildRequires: python3-module-imagesize
BuildRequires: python3-module-appdirs
BuildRequires: python3-module-requests
BuildRequires: python3-module-platformdirs
BuildRequires: python3-module-responses
%endif

%add_python3_req_skip requests.packages.urllib3.util.retry

%description
Dosage is designed to keep a local copy of specific webcomics
and other picture-based content such as Picture of the Day sites.
With the dosage commandline script you can get the latest strip
of webcomic, or catch-up to the last strip downloaded, or
download a strip for a particular date/index (except if the
webcomic's site layout makes this impossible).

%prep
%setup
%patch -p0

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.*
%_bindir/%pypi_name
%python3_sitelibdir/dosagelib
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}


%changelog
* Tue Oct 17 2023 Anton Vyatkin <toni@altlinux.org> 3.0-alt1
- New version 3.0.

* Mon Feb 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.15-alt2
- Porting to python3.

* Wed Sep 10 2014 Nikolay A. Fetisov <naf@altlinux.ru> 2.15-alt1
- New version 2.15

* Wed Feb 26 2014 Nikolay A. Fetisov <naf@altlinux.ru> 2.12-alt1
- New version 2.12

* Sun Dec 01 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.7-alt1
- New version 2.7

* Sat Aug 10 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.5-alt1
- New version 2.5

* Sat Jun 29 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.4-alt1
- New version 2.4

* Sun Jun 09 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.3-alt1
- New version 2.3

* Sun May 19 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.2-alt1
- New version 2.2

* Fri Jan 04 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.8-alt1
- Initial build for ALT Linux Sisyphus

