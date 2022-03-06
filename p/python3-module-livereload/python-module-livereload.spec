%define _unpackaged_files_terminate_build 1
%define pypi_name livereload

%def_with check

Name: python3-module-%pypi_name
Version: 2.6.1
Release: alt2.1
Summary: Utility for starting a server in a directory
License: BSD
Url: https://github.com/lepture/python-livereload
Group: Development/Python3
Source: %name-%version.tar
Patch: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3(nose)
BuildRequires: python3(tornado)
%endif

# we have several versions of Django
# so, we cannot rely on auto-requires
%filter_from_requires /^python3(django\(\..*\)\?)/d

%description
LiveReload provides a command line utility, livereload, for starting
a server in a directory. By default, it will listen to port 35729,
the common port for LiveReload browser extensions. LiveReload is designed
for web developers who know Python.

%prep
%setup
%patch -p1

%build
%python3_build

%install
%python3_install

%check
nosetests3 -s

%files
%doc README.rst CHANGES.rst LICENSE
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%version-py%_python3_version.egg-info

%changelog
* Sun Mar 06 2022 Ivan A. Melnikov <iv@altlinux.org> 2.6.1-alt2.1
- Fix FTBFS with python 3.10

* Thu May 27 2021 Grigory Ustinov <grenka@altlinux.org> 2.6.1-alt2
- Drop python2 support.

* Fri Aug 16 2019 Stanislav Levin <slev@altlinux.org> 2.6.1-alt1
- 2.5.1 -> 2.6.1.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.5.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5.1-alt2
- Fixed build.

* Mon May 29 2017 Lenar Shakirov <snejok@altlinux.ru> 2.5.1-alt1
- Initial build for ALT (based on 2.5.1-2.fc26.src)

