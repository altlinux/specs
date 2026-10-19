%define pypi_name pg_activity

%def_without check

Name:    python3-module-%pypi_name
Version: 3.6.2
Release: alt1.1

Summary: Top like application for PostgreSQL server activity monitoring
License: PostgreSQL
Group:   Monitoring
URL:     https://github.com/dalibo/pg_activity

%add_python3_path %_datadir/%pypi_name
%add_findprov_skiplist %_datadir/%pypi_name/*

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
%if_with check
BuildRequires: codespell
BuildRequires: python3(attrs)
BuildRequires: python3(blessed)
BuildRequires: python3(humanize)
BuildRequires: python3(mypy)
BuildRequires: python3(psutil)
BuildRequires: python3(psycopg)
BuildRequires: python3(psycopg2)
BuildRequires: python3(typing_extensions)
BuildRequires: pkgconfig(libpq)
%endif

BuildArch: noarch

Source: %name-%version.tar

%package -n %pypi_name
Summary: Top like application for PostgreSQL server activity monitoring
Group:   Monitoring
Provides: pg-activity = %EVR
Provides: %name = %EVR
Obsoletes: %name < %EVR
Requires: python3-module-psycopg2

%description
%pypi_name is a top like application for PostgreSQL server activity monitoring.

%description -n %pypi_name
%pypi_name is a top like application for PostgreSQL server activity monitoring.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
# the application modules are private: do not provide python3(pgactivity)
mkdir -p %buildroot%_datadir/%pypi_name
mv -v %buildroot%python3_sitelibdir/pgactivity %buildroot%_datadir/%pypi_name/
cat > %buildroot%_bindir/%pypi_name <<'EOF'
#!/usr/bin/python3
import sys
sys.path.insert(0, '%_datadir/%pypi_name')
from pgactivity.cli import main
if __name__ == '__main__':
    sys.exit(main())
EOF
install -Dm644 docs/man/%pypi_name.1 %buildroot%_man1dir/%pypi_name.1

%check
# XXX: Exclude tests which requires orphaned and early removed modules
export PYTHONPATH=%buildroot%_datadir/%pypi_name:%buildroot%python3_sitelibdir
%pyproject_run_pytest

%files -n %pypi_name
%doc *.md LICENSE.txt
%_bindir/%pypi_name
%_man1dir/%pypi_name.1*
%_datadir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Oct 19 2026 Vitaly Lipatov <lav@altlinux.ru> 3.6.2-alt1.1
- NMU: move the application modules to private /usr/share/pg_activity, so python3(pgactivity) is no longer provided (conflicts with python3-module-django-pgactivity)
- NMU: rename the binary package to pg_activity (closes: #61090)

* Tue May 12 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 3.6.2-alt1
- New version.

* Thu Feb 26 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 3.6.1-alt2
- Check switched off due to updated dependencies.

* Mon Jun 16 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 3.6.1-alt1
- New version.

* Tue Apr 08 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 3.6.0-alt1
- New version.

* Tue Dec 03 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 3.5.1-alt3
- Added Provides(Closes #52272).

* Mon Dec 02 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 3.5.1-alt2
- Runtime requirement psycopg2 added.
- Updated Group.

* Thu Nov 28 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 3.5.1-alt1
- Initial build for Sisyphus.
