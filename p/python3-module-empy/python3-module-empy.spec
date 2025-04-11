%define pypi_name empy

%def_without check

Name:    python3-module-%pypi_name
Version: 3.3.4
Release: alt1

Summary: EmPy is a system for embedding Python expressions and statements in template text
License: LGPL-2.0
Group:   Development/Python3
URL:     https://pypi.org/project/empy/

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
EmPy is a system for embedding Python expressions and statements
in template text; it takes an EmPy source file, processes it, and produces
output. This is accomplished via expansions, which are special signals to the
EmPy system and are set off by a special prefix (by default the at sign, '@').
EmPy can expand arbitrary Python expressions and statements in this way, as
well as a variety of special forms. Textual data not explicitly delimited in
this way is sent unaffected to the output, allowing Python to be used in effect
as a markup language. Also supported are "hook" callbacks, recording and
playback via diversions, and dynamic, chainable filters. The system is highly
configurable via command line options and embedded commands.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%python3_sitelibdir/em.py
%python3_sitelibdir/__pycache__/em.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 22 2023 Andrey Cherepanov <cas@altlinux.org> 3.3.4-alt1
- Inital built for Sisyphus.
