%define _unpackaged_files_terminate_build 1

%define pypi_name pymunk
%define mod_name %pypi_name

Name: python3-module-%pypi_name
Version: 6.7.0
Release: alt1
Summary: Pymunk is a easy-to-use pythonic 2d physics library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pymunk/
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: Chipmunk2D.tar
# manually manage extras dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
Pymunk is an easy-to-use pythonic 2d physics library that can be used whenever
you need 2d rigid body physics from Python. Perfect when you need 2d physics in
your game, demo or simulation! It is built on top of the very capable 2d physics
library Chipmunk.

%package examples
Summary: Example files for %name
Group: Development/Python3
BuildArch: noarch
Provides: pymunk-examples = %EVR
Obsoletes: pymunk-examples <= 6.0.0-alt1

%description examples
Example files for %pypi_name

%prep
%setup -a2
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- bash -s <<-'ENDTESTS'
set -eu
mkdir temp
cd temp
python -m %pypi_name.tests
ENDTESTS

%files examples
%doc %mod_name/examples

%files
%python3_sitelibdir/%mod_name/
%exclude %python3_sitelibdir/%mod_name/examples/
%exclude %python3_sitelibdir/%mod_name/tests/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri May 03 2024 Stanislav Levin <slev@altlinux.org> 6.7.0-alt1
- 6.6.0 -> 6.7.0.

* Thu Feb 08 2024 Stanislav Levin <slev@altlinux.org> 6.6.0-alt1
- 6.0.0 -> 6.6.0.

* Sun May 16 2021 Fr. Br. George <george@altlinux.ru> 6.0.0-alt1
- Autobuild version bump to 6.0.0

* Sun May 16 2021 Fr. Br. George <george@altlinux.ru> 5.5.0-alt3
- Build with separate sphinx extensions required

* Tue Apr 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 5.5.0-alt2
- Build for python2 disabled.

* Mon Oct 28 2019 Fr. Br. George <george@altlinux.ru> 5.5.0-alt1
- Autobuild version bump to 5.5.0
- Introduce Python3 package
- Rename %name to %name-examples, as it is

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 5.1.0-alt1
- Autobuild version bump to 5.1.0
- Fix still queer _libload.py

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 5.0.0-alt1
- Autobuild version bump to 5.0.0

* Wed Oct 16 2013 Fr. Br. George <george@altlinux.ru> 4.0.0-alt1
- Autobuild version bump to 4.0.0
- Drop inactual patch

* Sun Mar 03 2013 Fr. Br. George <george@altlinux.ru> 3.0.0-alt1
- Autobuild version bump to 3.0.0
- Provide clean version of libload.py
- Add required internal libchipmunk functions

* Sun Mar 03 2013 Fr. Br. George <george@altlinux.ru> 2.1.0-alt1
- Initial build from scratch

