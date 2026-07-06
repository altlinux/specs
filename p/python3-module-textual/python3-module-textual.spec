%define _unpackaged_files_terminate_build 1

%define modulename textual
%def_with check

# Common directory for documentation.
%define docdir %_docdir/%name-doc-%version

Name: python3-module-%modulename
Version: 8.2.8
Release: alt1

Summary: Textual is a Rapid Application Development framework for Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/textual/
Vcs: https://github.com/Textualize/textual.git
BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
##check filter code style, coverage, publishing, documentation modules
%add_pyproject_deps_check_filter mkdocs-exclude mkdocs-rss-plugin textual-dev types-setuptools
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Textual is a Rapid Application Development framework for Python.
Build sophisticated user interfaces with a simple Python API. Run
your apps in the terminal or a web browser!

%package -n %name-doc
Summary: Documentation for Textual
Group: Documentation
Requires: %name

%description -n %name-doc
Documentation for Textual. Textual is a Rapid Application
Development framework for Python. Build sophisticated user
interfaces with a simple Python API.

%prep
%setup
# for windows
rm src/textual/drivers/win32.py
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install
rm -rf %buildroot%python3_sitelibdir/textual/demo
rm -f %buildroot%python3_sitelibdir/textual/__main__.py

# test_snapshots needs GUI mode, tested locally
# test_textual_env_var assert None is not None
%check
%pyproject_run_pytest \
    -n auto \
    --ignore=tests/snapshot_tests/test_snapshots.py \
    --ignore=tests/test_slug.py \
    --ignore=tests/text_area/test_languages.py \
    -k 'not textual_env_var'

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info
%doc README.md LICENSE

%files doc
%doc docs/* examples/

%changelog
* Mon Jul 06 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 8.2.8-alt1
- New version (8.2.8).

* Wed Jun 03 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 8.2.7-alt1
- New version (8.2.7).

* Wed Apr 15 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 8.2.3-alt1
- New version (8.2.3).

* Tue Mar 17 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 8.1.1-alt1
- New version (8.1.1).

* Tue Mar 10 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 8.1.0-alt1
- New version (8.1.0).

* Fri Feb 27 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 8.0.0-alt1
- New version (8.0.0).

* Tue Feb 10 2026 Martynenko Evgeniy <enimalojd@altlinux.org> 7.5.0-alt1
- New version (7.5.0).

* Thu Jan 15 2026 Martynenko Evgeniy <enimalojd@altlinux.org> 7.2.0-alt1
- New version (7.2.0).
- Exclude upstream demo from the main package to avoid packaging demo as public provides.

* Wed Jul 30 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 5.0.1-alt1
- New version (5.0.1).

* Mon Jul 14 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 4.0.0-alt1
- New version (4.0.0).

* Mon Jul 07 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 3.6.0-alt1
- New version (3.6.0).

* Fri Jun 27 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 3.5.0-alt1
- New version (3.5.0).

* Wed Jun 04 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 3.3.0-alt1
- New version (3.3.0).

* Tue Nov 12 2024 Elena Dyatlenko <lenka@altlinux.org> 0.85.2-alt1
- Updated to upstream version v0.85.2.
- Add blog to doc

* Mon Oct 28 2024 Elena Dyatlenko <lenka@altlinux.org> 0.85.1-alt1
- Updated to upstream version v0.85.1.
- Group change to Development/Python3.
- Url change to pypi.

* Fri Oct 25 2024 Elena Dyatlenko <lenka@altlinux.org> 0.84.0-alt1
- Updated to upstream version v0.84.0.

* Thu Oct 17 2024 Elena Dyatlenko <lenka@altlinux.org> 0.83.0-alt1
- Updated to upstream version v0.83.0.

* Wed Oct 02 2024 Elena Dyatlenko <lenka@altlinux.org> 0.81.0-alt1
- Updated to upstream version v0.81.0.

* Fri Sep 13 2024 Elena Dyatlenko <lenka@altlinux.org> 0.79.1-alt1
- Updated to upstream version v0.79.1.

* Fri Aug 23 2024 Elena Dyatlenko <lenka@altlinux.org> 0.77.0-alt1
- Updated to upstream version v0.77.0.

* Thu Aug 22 2024 Elena Dyatlenko <lenka@altlinux.org> 0.76.0-alt1
- Updated to upstream version v0.76.0.

* Fri Jul 26 2024 Elena Dyatlenko <lenka@altlinux.org> 0.74.0-alt1
- Updated to upstream version v0.74.0.

* Mon Jul 22 2024 Elena Dyatlenko <lenka@altlinux.org> 0.73.0-alt1
- Updated to upstream version v0.73.0.

* Thu Jul 18 2024 Elena Dyatlenko <lenka@altlinux.org> 0.72.0-alt1
- Updated to upstream version v0.72.0.

* Mon Jun 17 2024 Elena Dyatlenko <lenka@altlinux.org> 0.69.0-alt1
- Updated to upstream version v0.69.0.

* Fri Jun 14 2024 Elena Dyatlenko <lenka@altlinux.org> 0.68.0-alt1
- Updated to upstream version v0.68.0.

* Fri Jun 14 2024 Elena Dyatlenko <lenka@altlinux.org> 0.67.0-alt2
- The documentation separate into a package python3-module-textual-doc.

* Tue Jun 11 2024 Elena Dyatlenko <lenka@altlinux.org> 0.67.0-alt1
- Updated to upstream version v0.67.0.

* Mon Jun 03 2024 Elena Dyatlenko <lenka@altlinux.org> 0.64.0-alt1
- Initial build for Sisyphus.
