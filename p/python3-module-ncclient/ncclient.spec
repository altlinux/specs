%define _unpackaged_files_terminate_build 1
%define oname ncclient

%def_with check

Name: python3-module-%oname
Version: 0.6.12
Release: alt1

Summary: Python library for NETCONF clients
License: Apache-2.0
Group: Development/Python3

Url: https://pypi.org/project/ncclient/
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires:
BuildRequires: python3(paramiko)
BuildRequires: python3(lxml)
BuildRequires: python3(six)

BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

%description
ncclient is a Python library that facilitates client-side scripting
and application development around the NETCONF protocol. ncclient
was developed by Shikar Bhushan. It is now maintained by Leonidas
Poulopoulos (@leopoul)

%prep
%setup

# workaround for versioneer
grep -qsF ' export-subst' .gitattributes || exit 1
vers_f="$(sed -n 's/ export-subst//p' .gitattributes)"
grep -qs '^[ ]*git_refnames[ ]*=[ ]*".*"[ ]*$' "$vers_f" || exit 1
sed -i 's/^\([ ]*\)git_refnames[ ]*=[ ]*".*"[ ]*$/\1git_refnames = " (tag: v%version, upstream\/master)"/' "$vers_f"

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr -s false

%files
%doc README.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Fri Jul 23 2021 Stanislav Levin <slev@altlinux.org> 0.6.12-alt1
- 0.6.3 -> 0.6.12.
- Enabled testing.

* Thu Jan 10 2019 Alexey Shabalin <shaba@altlinux.org> 0.6.3-alt1
- 0.6.3
- build python3 package

* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 0.5.2-alt1
- New version

* Fri Jun 10 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 0.4.7-alt1
- New version

* Tue Apr 28 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 0.4.3-alt1
- New version

* Thu Oct 30 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.4.2-alt1
- Initla build for ALT

