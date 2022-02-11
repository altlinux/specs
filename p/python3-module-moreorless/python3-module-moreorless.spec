%define _unpackaged_files_terminate_build 1
%define oname moreorless
%def_with check

Name: python3-module-%oname
Version: 0.4.0
Release: alt1

Summary: Python diff wrapper
License: MIT
Group: Development/Python3
BuildArch: noarch

Url: https://github.com/thatch/moreorless
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(click)
BuildRequires: python3(parameterized)
%endif

%py3_requires click

%description
This is a thin wrapper around difflib.unified_diff
that Does The Right Thing for "No newline at eof".
The args are also simplified compared to difflib.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
%__python3 -m moreorless.tests -v

%files
%doc LICENSE README.md
%python3_sitelibdir/moreorless/
%python3_sitelibdir/moreorless-%version-py%_python3_version.egg-info/

%changelog
* Tue Dec 28 2021 Ivan Alekseev <qwetwe@altlinux.org> 0.4.0-alt1
- 0.4.0
