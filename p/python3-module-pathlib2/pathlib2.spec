%define _unpackaged_files_terminate_build 1
%global oname pathlib2

%def_with check

Name: python3-module-%oname
Version: 2.3.6
Release: alt1.1

Summary: Object-oriented filesystem paths
License: MIT
Group: Development/Python3

# Source-git: https://github.com/mcmtroffaes/pathlib2
Url: https://pypi.org/project/pathlib2
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# install_requires=
BuildRequires: python3(six)

BuildRequires: python3(test)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
%endif

BuildArch: noarch

%global _description \
The old pathlib module on bitbucket is in bugfix-only mode. The goal of\
pathlib2 is to provide a backport of standard pathlib module which tracks\
the standard library module, so all the newest features of the standard\
pathlib can be used also on older Python versions.

%description %_description

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc CHANGELOG.rst LICENSE.rst README.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version.dist-info/

%changelog
* Tue Jan 30 2024 Grigory Ustinov <grenka@altlinux.org> 2.3.6-alt1.1
- NMU: moved on modern pyproject macros.

* Wed Feb 02 2022 Stanislav Levin <slev@altlinux.org> 2.3.6-alt1
- 2.3.3 -> 2.3.6.

* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 2.3.3-alt2
- Built Python3 package from its ows src.

* Wed Dec 19 2018 Stanislav Levin <slev@altlinux.org> 2.3.3-alt1
- 2.3.2 -> 2.3.3.

* Mon Aug 20 2018 Stanislav Levin <slev@altlinux.org> 2.3.2-alt1
- 2.1.0 -> 2.3.2.

* Tue Aug 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt3
- Fixed build dependencies.

* Fri Aug 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt2
- Updated build spec.

* Wed Aug 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.0-alt1
- Initial build for ALT.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.1.0-2
- Add %%check.
- Change URL from pathlib to pathlib2 page.

* Mon Nov 14 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.1.0-1
- Initial package.
