%define _unpackaged_files_terminate_build 1
%define bname aubuild

Name:     %bname-source
Version:  0.1.1
Release:  alt2

Summary:  Extract package build logs from audit logs
Summary(ru_RU.UTF-8): Извлекает данные о сборке пакетов из журналов аудита
License:  GPL-2.0-or-later
Group:    Development/Tools
Url:      http://git.altlinux.org/gears/a/%bname.git

Packager: Paul Wolneykien <manowar@altlinux.org>

Source:   %bname-%version.tar

BuildRequires: rpm-build-python3 python3-module-pip python3-module-build
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: ronn python3-module-sphinx
BuildRequires: python3-module-sphinx-autodoc-typehints
BuildRequires: python3-module-audit

BuildRequires: pytest3
BuildRequires: python3-module-clickhouse-driver
BuildRequires: python3-module-hypothesis python3-module-hypothesis-cats >= 0.1.2

%ifarch aarch64 x86_64
BuildRequires: /proc clickhouse-server auditd-plugin-clickhouse >= 20221028.1.2
%endif

Requires: python3-module-%bname = %version-%release

%description
%bname(1) extracts package build logs from audit logs.

%description -l ru_RU.UTF-8
%bname(1) извлекает данные о сборке пакетов из журналов аудита.

%package -n %bname
Summary:  Extract package build logs from audit logs
Summary(ru_RU.UTF-8): Извлекает данные о сборке пакетов из журналов аудита
Group:    Development/Tools
BuildArch: noarch

%description -n %bname
%bname(1) extracts package build logs from audit logs.

%description -l ru_RU.UTF-8 -n %bname
%bname(1) извлекает данные о сборке пакетов из журналов аудита.

%package -n python3-module-%bname
Summary:  Python module to extract package build logs from audit logs
Summary(ru_RU.UTF-8): Модуль на Python для извлечения данных о сборке пакетов из журналов аудита
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-%bname
AuditBuildReportBuilder extracts package build logs from audit logs.

%description -l ru_RU.UTF-8 -n python3-module-%bname
AuditBuildReportBuilder извлекает данные о сборке пакетов из журналов аудита.

%prep
%setup -n %bname-%version

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_datadir/doc/python3-module-%bname-%version
mv -v %buildroot%_datadir/doc/%bname/html \
      %buildroot%_datadir/doc/python3-module-%bname-%version/
%find_lang %bname

%check
%make_build check

%files -f %bname.lang -n %bname
%doc README
%_bindir/%bname
%lang(ru) %_mandir/ru/man1/%bname.1*

%files -n python3-module-%bname
%python3_sitelibdir_noarch/%bname
%python3_sitelibdir_noarch/%bname-%version.dist-info
%_datadir/doc/python3-module-%bname-%version

%changelog
* Fri Nov 04 2022 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt2
- Try to install clickhouse-server only on aarch64 and x86_64.

* Fri Nov 04 2022 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Fix/improve: Protect the parser from OSErrors when it tries to
  get an int value of a field.
- Fix: Don't expect a split EXECVE argument to have more than
  one part.
- Fixed tests on 32-bit platforms.
  valid on the particular platform.
- Made the source package arch-dependent, while keeping binary
  packages noarch.
- Don't try to install ClickHouse server on i586.
- Mark the ClickHouse tests as XFAIL if the server executable is
  not available.

* Wed Nov 02 2022 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial version.
