Summary: generate wtmp statistics
Name: logintop10
Version: 1.9
Release: alt3
License: GPL
Group: Monitoring
URL: http://www.vanheusden.com/logintop10/

Source0: %name-%version.tgz
Patch0: %name.patch

%description
LoginTop10 creates several top-10 lists from the wtmp (usally in /var/log/) on your system

%prep
%setup -q
%patch0 -p1


%build
make

%install
mkdir -p %buildroot%_bindir
%make_install DESTDIR="%buildroot" install

%files
%doc license.txt readme.txt
%_datadir/locale/*/LC_MESSAGES/%name.mo
%_man1dir/%name.1*
%_bindir/%name

%changelog
* Wed Nov 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9-alt3
- Fixed spec to allow any man pages compression.

* Thu Oct 16 2008 Mikhail Pokidko <pma@altlinux.org> 1.9-alt2
- in-spec description fix

* Wed Nov 15 2006 Mikhail Pokidko <pma@altlinux.ru> 1.9-alt1
- Initial build

