%define _unpackaged_files_terminate_build 1

%def_with check

Name: gaphor
Version: 3.3.2
Release: alt1
Summary: A powerful UML and SysML modeling tool in Python
License: Apache-2.0
Group: Editors
Url: https://gaphor.org/
Vcs: https://github.com/gaphor/gaphor.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

# Drop better-exceptions: replaced with traceback.TracebackException
Patch1: drop-better-exceptions.patch

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: libadwaita-gir-devel
BuildRequires: libgtksourceview5-devel
BuildRequires: libgtksourceview5-gir-devel

%if_with check
# Filter better-exceptions from check deps (removed by patch)
%add_pyproject_deps_check_filter better-exception
# Filter babelgladeextractor from check deps (unused in tests)
%add_pyproject_deps_check_filter babelgladeextractor
# pygobject-stubs needed only for mypy pre-commit hook, not for pytest
%add_pyproject_deps_check_filter pygobject-stubs
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: libgtk4-gir
BuildRequires: libgraphene-gir
BuildRequires: xvfb-run
%endif

%description
Gaphor is a Python-based UML and SysML modeling tool, blending simplicity and
power. It supports a full UML 2 data model for robust diagrams and complex
models. With a GTK interface and Cairo rendering, it ensures a smooth
experience. Gaphor offers UML, SysML, RAAML, and C4 Model templates, plus
scripting and Jupyter integration. Perfect for intuitive, powerful modeling.

%package -n python3-module-%name
Summary: Python module for Gaphor
Group: Development/Python3

# Filter better-exceptions from runtime deps (removed by patch)
%add_pyproject_deps_runtime_filter better-exception
%pyproject_runtimedeps_metadata

# Require libgtksourceview5-gir, as typelib(GtkSource) may match multiple packages
Requires: libgtksourceview5-gir

%description -n python3-module-%name
Contains the Python modules of Gaphor, a UML and SysML modeling tool.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%__python3 scripts/build_babel.py
%pyproject_build

%install
%pyproject_install
install -Dm644 gaphor/ui/installschemas/org.gaphor.Gaphor.gschema.xml %buildroot%_datadir/glib-2.0/schemas/org.gaphor.Gaphor.gschema.xml
install -Dm644 data/org.gaphor.Gaphor.appdata.xml %buildroot%_datadir/metainfo/org.gaphor.Gaphor.appdata.xml
install -Dm644 data/org.gaphor.Gaphor.desktop %buildroot%_desktopdir/org.gaphor.Gaphor.desktop
install -Dm644 data/org.gaphor.Gaphor.service %buildroot%_datadir/dbus-1/services/org.gaphor.Gaphor.service
install -Dm644 data/org.gaphor.Gaphor.xml %buildroot%_datadir/mime/packages/org.gaphor.Gaphor.xml
install -Dm644 data/logos/gaphor-24x24.png %buildroot%_iconsdir/hicolor/24x24/apps/org.gaphor.Gaphor.png
install -Dm644 data/logos/gaphor-48x48.png %buildroot%_iconsdir/hicolor/48x48/apps/org.gaphor.Gaphor.png
install -Dm644 data/logos/org.gaphor.Gaphor.svg %buildroot%_iconsdir/hicolor/scalable/apps/org.gaphor.Gaphor.svg
install -Dm644 data/logos/org.gaphor.Gaphor-symbolic.svg %buildroot%_iconsdir/hicolor/symbolic/apps/org.gaphor.Gaphor-symbolic.svg
%find_lang gaphor

%check
# Disable tests that crash when GTK windows are created or destroyed in headless CI (xvfb under hasher).
# These include session recovery and placement tests that rely on interactive UI components.
%pyproject_run -- xvfb-run -s "-screen 0 1600x1200x24 -noreset" \
    python -m pytest -v tests \
    --deselect tests/test_architecture.py::test_gtk_dependency \
    --deselect tests/test_diagramexport.py::test_export_png \
    --deselect tests/test_comment_line_placement.py::test_placement \
    --ignore tests/test_session_recovery.py \
    --ignore tests/test_placement_tools.py

%files
%_bindir/%name
%_datadir/glib-2.0/schemas/org.gaphor.Gaphor.gschema.xml
%_datadir/metainfo/org.gaphor.Gaphor.appdata.xml
%_desktopdir/org.gaphor.Gaphor.desktop
%_datadir/dbus-1/services/org.gaphor.Gaphor.service
%_datadir/mime/packages/org.gaphor.Gaphor.xml
%_iconsdir/hicolor/24x24/apps/org.gaphor.Gaphor.png
%_iconsdir/hicolor/48x48/apps/org.gaphor.Gaphor.png
%_iconsdir/hicolor/scalable/apps/org.gaphor.Gaphor.svg
%_iconsdir/hicolor/symbolic/apps/org.gaphor.Gaphor-symbolic.svg

%files -n python3-module-%name -f %name.lang
%python3_sitelibdir_noarch/%name
%python3_sitelibdir_noarch/%{pyproject_distinfo %name}

%changelog
* Thu Jun 25 2026 Aleksandr A. Voyt <sobue@altlinux.org> 3.3.2-alt1
- 3.2.0 -> 3.3.2

* Mon Nov 10 2025 Aleksandr A. Voyt <sobue@altlinux.org> 3.2.0-alt1
- 3.1.0 -> 3.2.0

* Wed Aug 13 2025 Aleksandr A. Voyt <sobue@altlinux.org> 3.1.0-alt1
- 3.0.0 -> 3.1.0

* Wed Apr 16 2024 Aleksandr A. Voyt <sobue@altlinux.org> 3.0.0-alt1
- Initial build
