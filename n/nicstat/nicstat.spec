Name: nicstat
Version: 1.95
Release: alt1
Summary: Network traffic statics utility
Group: Monitoring
License: Artistic License 2.0
Url: https://github.com/scotte/nicstat.git
Source: %name.tar
Patch: %name-alt.patch
Packager: Evgenii Terechkov <evg@altlinux.org>

%description
Network traffic statics utility

%prep
%setup -n %name

%build
mv Makefile.Linux Makefile
make CMODEL="" NATIVE_BINARY=.nicstat.Linux_unknown_%_arch

%install
mkdir -p %buildroot%_bindir %buildroot%_man1dir
make CMODEL="" BASEDIR=%buildroot%_prefix SETUINSTALL=install INSTALL=install NATIVE_BINARY=.nicstat.Linux_unknown_%_arch install

%files
%_bindir/%name
%_man1dir/*.1.*
%doc README* ChangeLog.txt BUGS.md

%changelog
* Wed Dec  2 2015 Terechkov Evgenii <evg@altlinux.org> 1.95-alt1
- Initial build for ALT Linux Sisyphus
