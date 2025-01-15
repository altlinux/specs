Summary: generate wtmp statistics
Name: wtmptail
Version: 1.3
Release: alt2
License: GPL-2.0
Group: Monitoring
URL: http://www.vanheusden.com/wtmptail/
Packager: Mikhail Pokidko <pma@altlinux.ru>
Source: %name-%version.tar

%description
 The  program  wtmptail  shows  all  new entries in the wtmp-file (which
resides usually in /var/log). This way one can watch  users  login  and
logout.  Optionally,  a  filename  can be given. That file will then be
used instead of the default which is /var/log/wtmp.

%prep
%setup

%build
%make

%install
%make_install DESTDIR=%buildroot install

%files
%doc license.txt
%_man1dir/%name.1*
%_bindir/%name

%changelog
* Tue Jan 14 2025 Ulysses Apokin <ulysses@altlinux.org> 1.3-alt2
- Fixed FTBS
- Memory leak fixed

* Thu Nov 17 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.3-alt1.qa1
- Fixed FTBFS (manpage packaging).

* Wed Nov 15 2006 Mikhail Pokidko <pma@altlinux.ru> 1.3-alt1
- Initial build
