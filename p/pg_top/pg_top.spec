Name: pg_top
Version: 4.1.3
Release: alt1
Summary: 'top' for PostgreSQL process
Group: Databases
License: BSD
Url: https://gitlab.com/pg_top/pg_top.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: cmake python3-module-docutils
BuildRequires: libncurses-devel libpq-devel libbsd-devel

%description
pg_top is 'top' for PostgreSQL processes. See running queries,
query plans, issued locks, and table and index statistics.

%prep
%setup -q
%patch -p1

%build
%cmake_insource

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc HISTORY.rst INSTALL.rst LICENSE README.rst TODO Y2K
%_bindir/*
%_man1dir/*

%changelog
* Wed May 06 2026 Alexei Takaseev <taf@altlinux.org> 4.1.3-alt1
- 4.1.3
- Use cmake for build
- Change BR postgresql-devel -> libpq-devel
- Change URL

* Fri Jul 08 2016 Alexey Shabalin <shaba@altlinux.ru> 3.7.0-alt1
- 3.7.0

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.6.2-alt1.qa1
- NMU: rebuilt for debuginfo.

* Wed Dec 08 2010 Alexey Shabalin <shaba@altlinux.ru> 3.6.2-alt1
- initial build for ALT Linux Sisyphus
