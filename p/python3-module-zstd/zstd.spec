%global pypi_name zstd
%global zstd_version 1.5.0

Name:           python3-module-%pypi_name
Version:        %zstd_version.4
Release:        alt1

Summary:        Zstd Bindings for Python

License:        BSD
Group:          Development/Python3
URL:            https://github.com/sergey-dryabzhinsky/python-zstd
Source:        %pypi_name-%version.tar

# Patches to fix test execution
Patch0:         python3-module-zstd-1.4.5.1-test-external.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-module-setuptools
BuildRequires:  libzstd-devel >= %zstd_version

%description
Simple Python bindings for the Zstd compression library.

%prep
%setup -n %pypi_name-%version
%patch -p1
# Remove bundled zstd library
rm -rf zstd

%build
%python3_build -- --legacy --external

%install
%python3_install

%check
%{__python3} setup.py test

%files
%doc README.rst LICENSE
%python3_sitelibdir/%pypi_name-%version-py%_python3_version.egg-info
%python3_sitelibdir/%{pypi_name}*.so

%changelog
* Mon Dec 13 2021 Grigory Ustinov <grenka@altlinux.org> 1.5.0.4-alt1
- Build new version.

* Tue Sep 29 2020 Grigory Ustinov <grenka@altlinux.org> 1.4.5.1-alt1
- Initial build for Sisiphus.
