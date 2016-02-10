Name:		cqrlog
Version:	1.9.1
Release:	alt1
Summary:	An amateur radio contact logging program

Group:		Communications
License:	GPLv2
URL:		http://www.cqrlog.com/
Source0:	http://www.cqrlog.com/files/%{name}_%{version}/%{name}-%{version}.tar.gz

Patch0:		cqrlog-install.patch
Patch2:		cqrlog-build-with-fpc-3.0.0.patch

BuildRequires:	fpc >= 2.6.4
BuildRequires:	lazarus
BuildRequires:	hamlib-devel
BuildRequires:	libssl-devel
BuildRequires:	desktop-file-utils

Requires:	mariadb-server
Requires:	trustedqsl
Requires:       hamlib

%description
CQRLOG is an advanced ham radio logger based on MySQL database. Provides
radio control based on hamlib libraries (currently support of 140+ radio
types and models), DX cluster connection, QRZ callbook (web version), a
grayliner, internal QSL manager database support and a most accurate
country resolution algorithm based on country tables developed by OK1RR.
CQRLOG is intended for daily general logging of HF, CW & SSB contacts
and strongly focused on easy operation and maintenance.

%prep
%setup -q
%patch0 -p1
%patch2 -p2

chmod -x src/*.pas \
         voice_keyer/voice_keyer.sh

%build
%make_build

%install
%makeinstall_std

find %buildroot%_datadir/%name -name \*.txt | xargs subst 's/\r//'
subst 's/\r//' %buildroot%_datadir/%name/ctyfiles/CountryDel.tab
subst 's/\r//' %buildroot%_datadir/%name/ctyfiles/MASTER.SCP

iconv -f iso8859-1 -t utf-8 %buildroot%_datadir/%name/ctyfiles/eqsl.txt > eqsl.txt.conv && /bin/mv -f eqsl.txt.conv %buildroot%_datadir/%name/ctyfiles/eqsl.txt

rm -rf %buildroot%_datadir/%name/cqrlog-apparmor-fix

%files
%doc README.md src/AUTHORS src/CHANGELOG src/README src/COPYING
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_pixmapsdir/%name/%name.png
%_man1dir/%name.1.*

%changelog
* Wed Feb 10 2016 Andrey Cherepanov <cas@altlinux.org> 1.9.1-alt1
- New version

* Thu Jan 07 2016 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt4
- Fix build with fpc-3.0.0

* Thu Nov 19 2015 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt3
- Add trustedqsl in requirements

* Mon Nov 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt2
- Add hamlib to requirements

* Thu Nov 12 2015 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt1
- Initial build in Sisyphus (thanks Fedora for spec)

