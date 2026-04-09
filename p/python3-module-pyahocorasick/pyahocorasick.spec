%global _unpackaged_files_terminate_build 1
%define pypi_name pyahocorasick

%ifnarch %ix86
%def_with check
%else
%def_without check
%endif

Name: python3-module-pyahocorasick
Version: 2.3.0
Release: alt3
Summary: Fast and memory efficient python library for exact or approximate multi-pattern string search
Group: Development/Python3
License: BSD-3-Clause
Url: https://pypi.org/project/pyahocorasick/
VCS: https://github.com/WojciechMula/pyahocorasick
AutoReq: yes, nopython3

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_runtimedeps_metadata

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
pyahocorasick is a fast and memory efficient library for exact or
approximate multi-pattern string search. With the
ahocorasick.Automaton class, you can find multiple key string
occurrences at once in some input text. You can use it as a plain
dict-like Trie or convert a Trie to an automaton for efficient
Aho-Corasick search. And pickle to disk for easy reuse of large
automatons. Implemented in C and tested on Python 3.6+.
%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/ahocorasick*.so
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Apr 09 2026 Anton Farygin <rider@altlinux.org> 2.3.0-alt3
- fixed summary and description (closes: #58596)

* Wed Apr 08 2026 Anton Farygin <rider@altlinux.org> 2.3.0-alt2
- fixed license

* Tue Apr 07 2026 Anton Farygin <rider@altlinux.org> 2.3.0-alt1
- initial build for ALT Linux

