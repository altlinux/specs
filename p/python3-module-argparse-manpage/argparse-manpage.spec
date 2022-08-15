%define _unpackaged_files_terminate_build 1
%define pypi_name argparse-manpage

%def_with check

Name: python3-module-%pypi_name
Version: 3
Release: alt1

Summary: Automatically build manpage from argparse
License: Apache-2.0
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/argparse-manpage/

# Source-git: https://github.com/praiskup/argparse-manpage.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
# proc is required for /dev/stdout (/dev/stdout -> /proc/self/fd/1)
BuildRequires: /proc

BuildRequires: python3(pytest)
%endif

%description
Generate manual page an automatic way from ArgumentParser object, so the
manpage 1:1 corresponds to the automatically generated -help output. The
manpage generator needs to known the location of the object, user can specify
that by (a) the module name or corresponding python filename and (b) the
object name or the function name which returns the object. There's a limited
support for (deprecated) optparse objects, too.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install
# to avoid conflict with Python2 console script
mv %buildroot%_bindir/argparse-manpage{,.py3}

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE README.md
%_man1dir/argparse-manpage.1.*
%_bindir/argparse-manpage.py3
%python3_sitelibdir/build_manpages/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Aug 15 2022 Stanislav Levin <slev@altlinux.org> 3-alt1
- 2.1 -> 3.

* Wed Jan 19 2022 Stanislav Levin <slev@altlinux.org> 2.1-alt1
- 1.5 -> 2.1.

* Thu Apr 15 2021 Stanislav Levin <slev@altlinux.org> 1.5-alt1
- 1.1 -> 1.5.

* Tue Jan 29 2019 Stanislav Levin <slev@altlinux.org> 1.1-alt1
- Initial build.
