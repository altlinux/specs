%define _unpackaged_files_terminate_build 1
%define oname argparse-manpage

%def_with check

Name: python3-module-%oname
Version: 2.1
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

%if_with check
# proc is required for /dev/stdout (/dev/stdout -> /proc/self/fd/1)
BuildRequires: /proc

BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
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
%python3_build

%install
%python3_install
# to avoid conflict with Python2 console script
mv %buildroot%_bindir/argparse-manpage{,.py3}

%check
cat > tox.ini <<EOF
[testenv]
usedevelop=True
commands=
    pytest {posargs:-vra}
EOF
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts

%files
%doc LICENSE README.md
%_man1dir/argparse-manpage.1.*
%_bindir/argparse-manpage.py3
%python3_sitelibdir/argparse_manpage-%version-py%_python3_version.egg-info/
%python3_sitelibdir/build_manpages/

%changelog
* Wed Jan 19 2022 Stanislav Levin <slev@altlinux.org> 2.1-alt1
- 1.5 -> 2.1.

* Thu Apr 15 2021 Stanislav Levin <slev@altlinux.org> 1.5-alt1
- 1.1 -> 1.5.

* Tue Jan 29 2019 Stanislav Levin <slev@altlinux.org> 1.1-alt1
- Initial build.
