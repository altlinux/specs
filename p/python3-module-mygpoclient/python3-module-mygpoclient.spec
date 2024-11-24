%define pypi_name mygpoclient
%def_enable check

Name: python3-module-%pypi_name
Version: 1.10
Release: alt1

Summary: gpodder.net API Client Library for Python3
License: GPLv3+
Group: Development/Python3
Url: https://github.com/gpodder/%pypi_name
#https://pypi.org/project/mygpoclient/

Vcs: https://github.com/gpodder/mygpoclient.git

#Source: %url/archive/%pypi_name-%version.tar.gz
Source: https://pypi.io/packages/source/m/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)
%{?_enable_check:BuildRequires: python3(pytest) python3(pytest-cov)
BuildRequires: python3(coverage) python3(minimock)}

%description
This Python 3 library provides an easy and structured way to access the
my.gpodder.org web services. In addition to subscription list
synchronization and storage, the advanced API support allows to upload
and download episode status changes.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
py.test-3 %pypi_name

%files
%_bindir/mygpo-bpsync
%_bindir/mygpo-list-devices
%_bindir/mygpo-simple-client
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%_man1dir/mygpo-bpsync.1.*
%doc AUTHORS README*


%changelog
* Sun Nov 24 2024 Yuri N. Sedunov <aris@altlinux.org> 1.10-alt1
- 1.10
- ported to %%pyproject macros, enabled %%check

* Fri Jun 24 2022 Yuri N. Sedunov <aris@altlinux.org> 1.9-alt1
- 1.9

* Thu Aug 05 2021 Yuri N. Sedunov <aris@altlinux.org> 1.8-alt3
- python3-only build

* Fri Mar 23 2018 Yuri N. Sedunov <aris@altlinux.org> 1.8-alt2
- added python3 subpackage

* Fri Nov 03 2017 Yuri N. Sedunov <aris@altlinux.org> 1.8-alt1
- 1.8

* Fri Jun 06 2014 Yuri N. Sedunov <aris@altlinux.org> 1.7-alt1
- 1.7

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6-alt1.1
- Rebuild with Python-2.7

* Fri Aug 19 2011 Yuri N. Sedunov <aris@altlinux.org> 1.6-alt1
- 1.6

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- first build for Sisyphus

