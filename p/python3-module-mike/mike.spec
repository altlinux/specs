%define _unpackaged_files_terminate_build 1
%define pypi_name mike

Name: python3-module-%pypi_name
Version: 1.1.2
Release: alt2

Summary: Deploy multiple versions of your MkDocs

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/mike

Source: mike-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
Mike is a Python utility to easily deploy multiple versions of your
MkDocs-powered docs to a Git branch, suitable for deploying to Github
via gh-pages. To see an example of this in action, take a look at the
documentation for bfg9000.The parsing module is an alternative approach
to creating and executing

%prep
%setup -n mike-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%python3_sitelibdir/mike/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%_bindir/mike

%changelog
* Wed Nov 09 2022 Stanislav Levin <slev@altlinux.org> 1.1.2-alt2
- Fixed FTBFS (flit_core 3.7.1).

* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 1.1.2-alt1
- Autobuild version bump to 1.1.2

* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 1.1.1-alt1
- Initial build for ALT
