%define _unpackaged_files_terminate_build 1

%define oname m2r
%def_with check

Name: python3-module-%oname
Epoch: 1
Version: 0.2.1
Release: alt2

Summary: Markdown to reStructuredText converter

Url: https://github.com/miyakogi/m2r
License: MIT
Group: Development/Python3

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(tox)
BuildRequires: python3(docutils)
BuildRequires: python3(mistune)
BuildRequires: python3(sphinx)
%endif

%description
M2R converts a markdown file including reST markups to a valid reST format.

%prep
%setup
%autopatch -p1

%build
%python3_build_debug

%install
%python3_install

%files
%_bindir/m2r
%python3_sitelibdir/__pycache__/
%python3_sitelibdir/m2r-%version-py%_python3_version.egg-info/
%python3_sitelibdir/m2r.py

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr

%changelog
* Wed Feb 02 2022 Stanislav Levin <slev@altlinux.org> 1:0.2.1-alt2
- Fixed FTBFS (Python3.10).

* Wed Mar 10 2021 Stanislav Levin <slev@altlinux.org> 1:0.2.1-alt1
- 0.11 -> 0.2.1.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1.qa1
- NMU: applied repocop patch

* Tue Nov 07 2017 Vitaly Lipatov <lav@altlinux.ru> 0.11-alt1
- new version 0.11 (with rpmrb script)

* Sun Oct 08 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1.12-alt1
- new version 0.1.12 (with rpmrb script)

* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1.6-alt1
- initial build for ALT Sisyphus

