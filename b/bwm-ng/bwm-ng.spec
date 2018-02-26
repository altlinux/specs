Name: bwm-ng
Version: 0.6
Release: alt1

Summary: Bandwidth Monitor NG is a small and simple console-based live bandwidth monitor.
License: GPLv2+
Group: Monitoring
Url: http://www.gropp.org/
Packager: Ilya Mashkin <oddity at altlinux.ru>

Source0: %name-%version.tar.gz
Source1: bwm-ng.conf
Patch0:bwm-ng-alt-as-needed.patch

# Automatically added by buildreq on Mon Mar 13 2006 (-bi)
BuildRequires: libncurses-devel libtinfo-devel net-tools pkg-config

%description
Bandwidth Monitor NG is a small and simple console-based live bandwidth monitor for Linux, BSD, Solaris, Mac OS X and others.

%prep
%setup -q -n %name-%version
#patch0 -p0

%build
%configure --prefix=%buildroot --enable-64bit \
			--enable-netstatbyte \
			--enable-netstatlink \
			--with-ncurses \
			--with-time	\
			--with-getopt_long \
			--with-getifaddrs \
			--with-sysctl \
			--with-procnetdev \
			--with-libstatgrab \
			--with-netstatlinux	\
			--without-strip
%make_build

%install
%makeinstall
install -D -m644 %SOURCE1 $RPM_BUILD_ROOT%_sysconfdir/bwm-ng.conf

%files
%_bindir/bwm-ng
%_man1dir/*
%config(noreplace) %_sysconfdir/bwm-ng.conf
%doc AUTHORS ChangeLog NEWS README INSTALL bwm-ng.conf-example bwm-ng.css


%changelog
* Sun Sep 30 2007 Ilya Mashkin <oddity at altlinux.ru> 0.6-alt1
- new version 0.6

* Sat Mar 18 2006 Dmitry Marochko <mothlike@altlinux.ru> 0.5-alt1.1
- as-needed fix

* Mon Mar 13 2006 Dmitry Marochko <mothlike@altlinux.ru> 0.5-alt1
- Initial build for Sisyphus
