Name: pentaxpj
Version: 1.0.0
Release: alt2
License: GPL
Group: System/Configuration/Printing

Url: http://ww1.pragana.net/gdiprinters.html
# Source: http://ww1.pragana.net/%name-%version.tar.gz
Source: %name-%version.tar
Patch: pentaxpj-glibc28_fix.patch
Patch1: pentaxpj-1.0.0-LDFLAGS.patch

Summary: Pentax PocketJet Printer Driver
%description
Pentax PocketJet Printer Driver for the families:

o PocketJet II
o PocketJet 200.

%prep
%setup
%patch0 -p0
%patch1 -p0

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS`  `find . -type d -name .svn` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
  if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

%build
%make CFLAGS="%optflags -DLONG_FORM_FEED"

%install
install -d %buildroot%_bindir
install -d %buildroot%_sbindir
install -d %buildroot%_libdir/pentaxpj
install -d %buildroot%_sysconfdir

cp -a BWidget-1.3.1 pentaxpj pentaxsetup pentax.xpm test-page.ps.gz %buildroot%_libdir/pentaxpj
ln -s %_libdir/pentaxpj/pentaxsetup %buildroot%_sbindir
ln -s %_libdir/pentaxpj/pentaxpj %buildroot%_bindir
cat > %buildroot%_sysconfdir/pentaxpj.conf <<EOF
#
set settings(driverpath) %_libdir/pentaxpj
EOF

%files
%doc README
%_libdir/pentaxpj
%config(noreplace) %_sysconfdir/pentaxpj.conf
%_bindir/pentaxpj
%_sbindir/pentaxsetup

%changelog
* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 1.0.0-alt2
- Initial build for ALT

