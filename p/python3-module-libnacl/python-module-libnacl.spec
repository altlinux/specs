%define oname libnacl

Name: python3-module-%oname
Version: 2.1.0
Release: alt1

Summary: Python ctypes wrapper for libsodium

License: Apache-2.0
Group: Development/Python3
Url: https://github.com/saltstack/libnacl
Packager: Python Development Team <python@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%{?!_without_check:%{?!_disable_check:BuildRequires: libsodium-devel}}

Requires: libsodium


%description
This library is used to gain direct access to the functions exposed by
Daniel J. Bernstein's nacl library via libsodium. It has been constructed
to maintain extensive documentation on how to use nacl as well as being
completely portable. The file in libnacl/__init__.py can be pulled out
and placed directly in any project to give a single file binding to all
of nacl.


%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest discover --start-directory tests -v

%files
%doc LICENSE MANIFEST.in README.rst doc/index.rst doc/topics
%python3_sitelibdir/*


%changelog
* Sat Sep 16 2023 Vitaly Chikunov <vt@altlinux.org> 2.1.0-alt1
- NMU: Fix for libsodium-1.0.19 (libsodium.so.26). This change is required
  to update libsodium.
- Update to v2.1.0 (2023-08-06). Update is required becasue unittest
  fails on i586 but fixed upstream.
- spec: Switch to %%pyproject_build.
- spec: Update Packager tag and description to reflect upstream changes.
- spec: Add %%check section with unittest run.
- spec: Package docs.

* Sat Jul 24 2021 Grigory Ustinov <grenka@altlinux.org> 1.7.1-alt2
- Fixed BuildRequires.
- Fixed License tag.
- Fixed Group tag.

* Wed Jan 15 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.7.1-alt1
- Version updated to 1.7.1
- porting on python3

* Mon Feb 12 2018 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt2.1
- NMU: autorebuild with libsodium-1.0.16 (libsodium23)

* Mon Mar 27 2017 Denis Smirnov <mithraen@altlinux.ru> 1.5.0-alt2
- rebuild with libsodium18

* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.5.0-alt1
- New version

* Fri Jun 24 2016 Lenar Shakirov <snejok@altlinux.ru> 1.4.5-alt2
- Requires: libsodium13 added

* Fri Jun 10 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.4.5-alt1
- New version

* Tue Apr 28 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 1.4.2-alt1
- New version

* Thu Feb 12 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 1.4.0-alt1
- Initial build for ALT

