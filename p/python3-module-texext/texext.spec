%define _unpackaged_files_terminate_build 1

%define oname texext

%def_with check

Name: python3-module-%oname
Version: 0.6.7
Release: alt1

Summary: Sphinx extensions for working with LaTeX math
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/texext
Vcs: https://github.com/matthew-brett/texext.git

BuildArch: noarch

Source: %name-%version.tar
Patch: drop-distutils.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-sphinxtesters
BuildRequires: python3-module-sympy
BuildRequires: python3-module-matplotlib-sphinxext
%endif

%description
Texext - sphinx extensions for working with LaTeX math.

%prep
%setup
%patch -p0

# fix version info
sed -i \
	-e "s/git_refnames\s*=\s*\"[^\"]*\"/git_refnames = \" \(tag: %version\)\"/" \
	%oname/_version.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.*
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Mon Oct 16 2023 Anton Vyatkin <toni@altlinux.org> 0.6.7-alt1
- New version 0.6.7.

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 0.6.6-alt1
- NMU: new version 0.6.6
- NMU: disable tests (wait for real users of texext)

* Thu Apr 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.6.1-alt3
- Build for python2 disabled.

* Tue Oct 01 2019 Stanislav Levin <slev@altlinux.org> 0.6.1-alt2
- Fixed testing against Sphinx 2.x.

* Mon Dec 24 2018 Grigory Ustinov <grenka@altlinux.org> 0.6.1-alt1
- Build new version.

* Tue Nov 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5-alt1
- Initial build for ALT.
