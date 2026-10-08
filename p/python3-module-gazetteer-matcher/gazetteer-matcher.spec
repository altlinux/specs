Name: python3-module-gazetteer-matcher
Version: 1.2.0
Release: alt1

Summary: Intent recognizer for Home Assistant voice commands
License: Apache-2.0
Group: Development/Python
URL: https://pypi.org/project/gazetteer-matcher
VCS: https://github.com/ohf-voice/gazetteer-matcher

Source0: %name-%version.tar
Source1: pyproject_deps.json

AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires: gcc-c++
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra dev

%description
An English-language, constraint-driven intent recognizer for Home Assistant
voice commands. It complements Home Assistant's built-in sentence grammars by
handling home-specific names, fuzzy wording, compound requests, and explicit
conversation references while rejecting interpretations that do not fit
the upstream intent schema.

%prep
%setup
%ifarch %ix86
%add_optflags -mfpmath=sse -msse
%endif
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%_bindir/*
%python3_sitelibdir/gazetteer_matcher
%python3_sitelibdir/gazetteer_matcher-%version.dist-info

%changelog
* Tue Oct 06 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.2.0-alt1
- 1.2.0 released

