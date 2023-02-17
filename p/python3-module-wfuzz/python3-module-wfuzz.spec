%define _unpackaged_files_terminate_build 1
%define pypi_name wfuzz

# TODO: run autotests correctly
%def_without check

Name: python3-module-%pypi_name
Version: 3.1.0
Release: alt3

Summary: Web application fuzzer
License: GPL-2.0
Group: Development/Python3
Url: https://pypi.org/project/wfuzz
Vcs: https://github.com/xmendez/wfuzz.git

Source: %name-%version.tar
Patch0: python3-module-wfuzz-3.1.0-alt-fix-relative-imports--bz44825.patch
Patch1: wfuzz-3.1.0-Correct-dependency-specification-for-pyparsing.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pycurl)
BuildRequires: python3(chardet)

BuildRequires: /proc /dev/kvm
BuildRequires: rpm-build-vm
%endif

%py3_requires pyparsing

BuildArch: noarch

%description
Wfuzz - The Web Fuzzer

Wfuzz has been created to facilitate the task in web applications
assessments and it is based on a simple concept: it replaces any
reference to the FUZZ keyword by the value of a given payload.

A payload in Wfuzz is a source of data.

This simple concept allows any input to be injected in any field of
an HTTP request, allowing to perform complex web security attacks in
different web application components such as: parameters,
authentication, forms, directories/files, headers, etc.

Wfuzz is more than a web content scanner:

* Wfuzz could help you to secure your web applications by finding and
  exploiting web application vulnerabilities. Wfuzz's web application
  vulnerability scanner is supported by plugins.

* Wfuzz is a completely modular framework and makes it easy for even
  the newest of Python developers to contribute. Building plugins is
  simple and takes little more than a few minutes.

* Wfuzz exposes a simple language interface to the previous HTTP
  requests/responses performed using Wfuzz or other tools, such
  as Burp. This allows you to perform manual and semi-automatic tests
  with full context and understanding of your actions, without relying
  on a web application scanner underlying implementation.

It was created to facilitate the task in web applications assessments,
it's a tool by pentesters for pentesters ;)

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
# overwrite tox.ini (upstream's one uses docker)
%tox_create_default_config
vm-run "%tox_check_pyproject"

%files
%doc LICENSE README.md wordlist
%_bindir/*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Feb 14 2023 Stanislav Levin <slev@altlinux.org> 3.1.0-alt3
- Fixed FTBFS (setuptools 66).

* Sun Jan 15 2023 Anton Zhukharev <ancieg@altlinux.org> 3.1.0-alt2
- fix wrong relative imports in ui/gui/controller.py (closes: #44825)
- add explicit dependency on python3-module-pyparsing

* Mon Dec 12 2022 Anton Zhukharev <ancieg@altlinux.org> 3.1.0-alt1
- initial build for Sisyphus

