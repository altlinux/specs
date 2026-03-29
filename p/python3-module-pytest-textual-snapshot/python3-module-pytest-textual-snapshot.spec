%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-textual-snapshot

Name: python3-module-%pypi_name
Version: 1.1.0
Release: alt1.1

Summary: Snapshot testing for Textual applications
License: MIT
Group: Development/Python3
Url: https://github.com/Textualize/pytest-textual-snapshot
Vcs: https://github.com/Textualize/pytest-textual-snapshot.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core

%description
A pytest-textual-snapshot test saves an SVG screenshot of a running Textual
app to disk. The next time the test runs, it takes another screenshot and
compares it to the saved one. If the new screenshot differs from the old one,
the test fails. This is a convenient way to quickly and automatically detect
visual regressions in your applications.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
# https://github.com/Textualize/pytest-textual-snapshot/issues/22
install -Dm 644 resources/snapshot_report_template.jinja2 \
  -t %buildroot/%python3_sitelibdir_noarch/resources/

%files
%doc README.md
%python3_sitelibdir_noarch/*
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1.1
- Demodernized packaging.

* Sun Jun 29 2025 Ivan Khanas <xeno@altlinux.org> 1.1.0-alt1
- New version.

* Wed May 22 2024 Elena Dyatlenko <lenka@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus.
