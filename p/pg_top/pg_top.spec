
Name: pg_top
Version: 3.6.2
Release: alt1
License: BSD

Summary: 'top' for PostgreSQL process
Group: Databases

Source: %name-%version.tar
Url: http://pgfoundry.org/projects/ptop

Patch: %name-%version-%release.patch
BuildRequires: libelf-devel libncurses-devel postgresql-devel

%description
pg_top is 'top' for PostgreSQL processes. See running queries,
query plans, issued locks, and table and index statistics.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc FAQ HISTORY INSTALL LICENSE README TODO Y2K
%_bindir/%name
%_man1dir/*

%changelog
* Wed Dec 08 2010 Alexey Shabalin <shaba@altlinux.ru> 3.6.2-alt1
- initial build for ALT Linux Sisyphus
