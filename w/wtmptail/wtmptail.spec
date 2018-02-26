Summary: generate wtmp statistics
Name: wtmptail
Version: 1.3
Release: alt1
License: GPL
Group: Monitoring
URL: http://www.vanheusden.com/wtmptail/
Packager: Mikhail Pokidko <pma@altlinux.ru>
Source0: %name-%version.tgz
Patch0: %name.patch

#BuildRequires: libncurses-devel


# Automatically added by buildreq on Wed Nov 15 2006
BuildRequires: libncurses-devel

%description
 The  program  wtmptail  shows  all  new entries in the wtmp-file (which
resides usually in /var/log). This way one can watch  users  login  and
logout.  Optionally,  a  filename  can be given. That file will then be
used instead of the default which is /var/log/wtmp.


%prep
%setup -q
%patch0 -p0


%build
make

%install
mkdir -p %buildroot%_bindir

%make_install DESTDIR="%buildroot" install

%files
%doc license.txt
%_man1dir/%name.1.gz
%_bindir/%name

%changelog
* Wed Nov 15 2006 Mikhail Pokidko <pma@altlinux.ru> 1.3-alt1
- Initial build

