Name: apt-file
Version: 0.1
Release: alt2
Group: System/Configuration/Packaging
Summary: Search for a package containing given file
License: WTFPL
Source: %name-%version.tar
AutoReq: false
Requires: perl >= 5.8 , rsync >= 3.0.9
BuildArch: noarch

# Most build environments would safely override this
BuildRoot: %{_tmppath}/%{name}-%{version}-root

Packager: Gremlin from Kremlin <gremlin@altlinux.org>

%description
%name is a command line tool to search for a package containing given file

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
%config(noreplace) %_sysconfdir/%name/%{name}.conf
%_sysconfdir/cron.daily/%name.update
%dir %_cachedir/%name

%changelog
* Thu Aug 31 2017 Terechkov Evgenii <evg@altlinux.org> 0.1-alt2
- Add true quiet mode support (when debug=0)

* Tue Aug 29 2017 Gremlin from Kremlin <gremlin@altlinux.org> 0.1-alt1
- First public release
