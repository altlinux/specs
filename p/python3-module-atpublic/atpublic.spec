#Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define modulename atpublic
%define subproj packages/atpublic
%def_with check

Name: python3-module-%modulename
Version: 9.0.0
Release: alt1

Summary: @public and @private decorators for Python
Group: Development/Python3
License: Apache-2.0

URL: https://pypi.org/project/atpublic
VCS: https://gitlab.com/flufl/public

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
Buildrequires: rpm-build-python3
Buildrequires: python3-module-hatchling

%if_with check
Buildrequires: python3-module-sybil
%endif

%description
This library provides two very simple decorators that document
the public visibility of the names in your module.
Also included is a function that can put at the bottom of your module
to simply infer all the public names, and populate the __all__ for you.

%prep
%setup

%build
%pyproject_build %subproj --outdir dist

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc %subproj/{LICENSE,README.rst}
%python3_sitelibdir_noarch/public
%python3_sitelibdir_noarch/%modulename-%version.dist-info

%changelog
* Wed Nov 11 2026 Polina Poidenko <polipoki@altlinux.org> 9.0.0-alt1
- New version 9.0.0.
- Removed accidentally added sphinx documentation source files.
- Changed the link to the project repository: 'warsaw/public' -> 'flufl/public'.

* Wed Apr 15 2026 Polina Poidenko <polipoki@altlinux.org> 7.0.0-alt1
- New version 7.0.0.

* Thu Feb 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt1
- Initial build for Sisyphus
