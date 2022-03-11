%define _unpackaged_files_terminate_build 1
%define python_sources impl/python

%def_with check

Name: anyascii
Version: 0.3.0
Release: alt1

Summary: Unicode to ASCII transliteration
License: ISC
Group: Development/Other
Url: https://github.com/anyascii/anyascii.git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
# backend for editable build
BuildRequires: python3(flit_core)

BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

BuildArch: noarch

%define descr \
Converts Unicode characters to their best ASCII representation. \
AnyAscii provides ASCII-only replacement strings for practically all Unicode \
characters. Text is converted character-by-character without considering the \
context. The mappings for each script are based on popular existing \
romanization systems. Symbolic characters are converted based on their meaning \
or appearance. All ASCII characters in the input are left unchanged, every \
other character is replaced with printable ASCII characters. Unknown \
characters and some known characters are replaced with an empty string and \
removed.

%description
%descr

%package -n python3-module-%name
Summary: %summary
Group: Development/Other

%description -n python3-module-%name
%descr

%prep
%setup
%autopatch -p1

%build
cd %python_sources
%python3_build

%install
cd %python_sources
%python3_install

%check
# Python tests
cd %python_sources
cat > tox.ini <<'EOF'
[testenv]
commands =
    {envbindir}/pytest {posargs:-vra}
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr --develop

%files -n python3-module-%name
%doc README.md
%python3_sitelibdir/%name/
%python3_sitelibdir/%name-%version-py%_python3_version.egg-info/

%changelog
* Thu Mar 10 2022 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus.
