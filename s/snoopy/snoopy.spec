Summary: User monitoring and command logging
Name: snoopy
Version: 1.8.1
Release: alt1
Url: https://github.com/a2o/snoopy
Source: v%version.tar.gz
Group: Development/Debuggers
License: GPL

%description
Snoopy Logger, logs all the commands issued by local users on the system.
It is very useful to track and monitor the users.

%prep
%setup
#patch1
#patch2

%build
%autoreconf
%configure
%make
#DESTDIR=%buildroot

%install
%makeinstall DESTDIR=%buildroot

%files
%doc COPYING ChangeLog README* TODO
%_libdir/snoopy.so

%changelog
* Tue Feb 12 2013 Fr. Br. George <george@altlinux.ru> 1.8.1-alt1
- Autobuild version bump to 1.8.1

* Tue Feb 12 2013 Fr. Br. George <george@altlinux.ru> 0.0-alt1
- Initial zero version build

