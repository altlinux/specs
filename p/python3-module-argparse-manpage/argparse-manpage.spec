%define _unpackaged_files_terminate_build 1
%define pypi_name argparse-manpage

%def_with check

Name: python3-module-%pypi_name
Version: 4.6
Release: alt1
Summary: Build manual page from python's ArgumentParser object
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/argparse-manpage/
Vcs: https://github.com/praiskup/argparse-manpage
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# distutils was removed in python 3.12
%filter_from_requires /python3(distutils\(\..*\)\?)/d
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
# proc is required for /dev/stdout (/dev/stdout -> /proc/self/fd/1)
BuildRequires: /proc
# pip is required for tests/test_examples.py
BuildRequires: python3-module-pip
%endif

%description
Avoid documenting your Python script arguments on two places! This is typically
done in an argparse.ArgumentParser help configuration (help=, description=,
etc.), and also in a manually crafted manual page.

The good thing about an ArgumentParser objects is that it actually provides a
traversable "tree-like" structure, with all the necessary info needed to
automatically generate documentation, for example in a groff typesetting system
(manual pages). And this is where this project can help.

There are two supported ways to generate the manual, either script it using the
installed command argparse-manpage, or via setup.py build automation (with a
slight bonus of automatic manual page installation with setup.py install).

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install
# to avoid conflict with Python2 console script
mv %buildroot%_bindir/argparse-manpage{,.py3}

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc README.md
%_man1dir/argparse-manpage.1.*
%_bindir/argparse-manpage.py3
%python3_sitelibdir/build_manpages/
%python3_sitelibdir/argparse_manpage/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Jun 06 2024 Stanislav Levin <slev@altlinux.org> 4.6-alt1
- 4.5 -> 4.6.

* Mon Nov 20 2023 Stanislav Levin <slev@altlinux.org> 4.5-alt2
- Dropped dependency on distutils (removed in Python3.12).

* Wed Nov 01 2023 Stanislav Levin <slev@altlinux.org> 4.5-alt1
- 4.3 -> 4.5.

* Thu May 18 2023 Stanislav Levin <slev@altlinux.org> 4.3-alt1
- 4.2 -> 4.3.

* Tue May 16 2023 Stanislav Levin <slev@altlinux.org> 4.2-alt1
- 3 -> 4.2.

* Mon Aug 15 2022 Stanislav Levin <slev@altlinux.org> 3-alt1
- 2.1 -> 3.

* Wed Jan 19 2022 Stanislav Levin <slev@altlinux.org> 2.1-alt1
- 1.5 -> 2.1.

* Thu Apr 15 2021 Stanislav Levin <slev@altlinux.org> 1.5-alt1
- 1.1 -> 1.5.

* Tue Jan 29 2019 Stanislav Levin <slev@altlinux.org> 1.1-alt1
- Initial build.
