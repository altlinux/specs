%def_with check

Name: tomcli
Version: 0.10.0
Release: alt1

Summary: CLI for working with TOML files
License: MIT
Group: Development/Python3
BuildArch: noarch

Url: https://pypi.org/project/tomcli
Vcs: https://git.sr.ht/~gotmax23/tomcli

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(flit_core)
%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(click)
BuildRequires: python3(tomli_w)
BuildRequires: python3(tomli)
BuildRequires: python3(tomlkit)
%endif

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir

TOMCLI="%buildroot%_bindir/tomcli"
cp pyproject.toml test.toml
name="$($TOMCLI get test.toml project.name)"
test "${name}" = "tomcli"

$TOMCLI set test.toml str project.name not-tomcli
newname="$($TOMCLI get test.toml project.name)"
test "${newname}" = "not-tomcli"

py.test-3 -vrs

%files
%doc LICENSE *.md
%_bindir/tomcli*
%python3_sitelibdir_noarch/%{pyproject_distinfo %name}
%python3_sitelibdir_noarch/%{pep427_name %name}

%changelog
* Wed Jul 30 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.10.0-alt1
- Initial build for Sisyphus (thx lesyafox@).
