Name: apf
Version: 0.3
Release: alt1
Summary: Search for a package containing given file
Group: System/Configuration/Packaging
License: WTFPL
Source: %name-%version.tar.gz
Requires: perl rsync
Provides: apt-file
Obsoletes: apt-file
BuildArch: noarch

# Most build environments safely override this
BuildRoot: %{_tmppath}/%{name}-%{version}-root

Packager: Gremlin from Kremlin <gremlin@altlinux.org>

%description
%name is a command line tool to search for a package containing
given file or to list the contents of a package available from
repository

%package update
Summary: cron job for daily updates
Group: System/Configuration/Packaging
Requires: %name

%description update
%summary

%prep
%setup

%install
rm -rf %buildroot
umask 022
mkdir -p %buildroot%_bindir \
	%buildroot%_man1dir \
	%buildroot%_cachedir/%name \
	%buildroot%_sysconfdir/%name \
	%buildroot%_sysconfdir/cron.daily \
	;
install -m 644 %name.1 %buildroot%_man1dir/
install -m 644 %name.conf %buildroot%_sysconfdir/%name/
install -m 755 %name.update %buildroot%_sysconfdir/cron.daily/
install -m 755 %name %buildroot%_bindir/
sed -i -re 's,\./,%_sysconfdir/%name/,g' %buildroot%_bindir/%name
sed -i -re 's,"\.","%_cachedir/%name",g' \
	%buildroot%_sysconfdir/%name/%name.conf

%clean
# Not necessary, but just in case of manual build
rm -rf %buildroot

%files
%defattr(-,root,root)
%_bindir/%name
%_man1dir/%name.*
%dir %_cachedir/%name
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%{name}.conf

%files update
%_sysconfdir/cron.daily/%name.update

%changelog
* Tue Nov 14 2017 Oleg Solovyov <mcpain@altlinux.org> 0.3-alt1
- search is now case-insensitive (Closes: #34187)

* Wed Sep 20 2017 Gremlin from Kremlin <gremlin@altlinux.org> 0.2-alt1
- incorporated fixes proposed by mcpain@
- check whether cache directory is writable
- try to create cache directory if it does not exist
- stop update process on rsync failure or interrupt

* Wed Aug 30 2017 Gremlin from Kremlin <gremlin@altlinux.org> 0.1-alt1
- First public release
