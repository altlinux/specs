# Spec file for Hammerhead utility

Name: hammerhead

Version: 2.1.4
Release: alt1
Epoch: 1

Summary: a stress testing tool for web servers

License: %gpl2only
Group: Networking/WWW
URL: http://sourceforge.net/projects/hammerhead/


BuildRequires(pre): rpm-build-licenses

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar

Patch1: %name-2.1.3-alt-unused_vars.patch
Patch2: %name-2.1.3-alt-gcc4.3_fix.patch
Patch3: %name-2.1.3-alt-gcc4.4_fix.patch
Patch4: %name-2.1.4-alt-autoconf_2.63_fix.patch
Patch5: %name-2.1.4-alt-libssl10.patch

AutoReqProv: yes


# Automatically added by buildreq on Sat May 24 2008
BuildRequires: gcc-c++ libssl-devel net-tools

%description
Hammerhead 2 is a stress testing tool designed to test out
web server and web site. It can initiate multiple connections
from IP aliases and simulated numerous (256+) users at any given
time. The rate at which Hammerhead 2 attempts to pound your site
is fully configurable, there are numerous other options for 
trying to create problems with a web site (so you can fix them).
It can be used to test the behaviour of the port under load,
or the ability of the port to service a set of requests.

%prep
%setup
%patch1
%patch2
%patch3
%patch4
%patch5

mv -f -- Copying Copying.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/Copying) Copying


%build
%autoreconf
# Removing outdated config.sub and config.guess
rm -f -- config.sub config.guess
automake --add-missing || :
%configure --with-pthreads=yes
%make_build
make -C utils/


%install
install -d %buildroot%_bindir
install -d %buildroot%_man1dir
install -d %buildroot%_sysconfdir/%name

install -m 0644 doc/*.conf doc/*.scn %buildroot%_sysconfdir/%name/
install -m 0755 src/hammerhead %buildroot%_bindir/
install -m 0755 utils/convertLog %buildroot%_bindir/%name-convertLog
install -m 0644 doc/hammerhead.1 %buildroot%_man1dir/


%files
%doc CHANGELOG README 
%doc bin/RunHammer bin/StopHammer bin/hist2scn.pl
%doc --no-dereference Copying

%dir %_sysconfdir/%name
%config %_sysconfdir/%name/*

%_bindir/%{name}*
%_man1dir/*


%changelog
* Sun Oct 10 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1:2.1.4-alt1
- New version
- Fix typo in package version
- Fix build with libssl 1.0.0a

* Tue May 26 2009 Nikolay A. Fetisov <naf@altlinux.ru> 2.3.1-alt3
- Fix build with new toolchain and GCC 4.4

* Sat Nov 15 2008 Nikolay A. Fetisov <naf@altlinux.ru> 2.3.1-alt2
- Fix build with GCC 4.3

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.3.1-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Sun May 25 2008 Nikolay A. Fetisov <naf@altlinux.ru> 2.3.1-alt1
- Initial build for ALT Linux Sisyphus
