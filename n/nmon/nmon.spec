Name: nmon
Version: 14g
Release: alt0.3

Summary: IBM nmon - system monitor
License: BSD-like
Group: Graphical desktop/Other

URL: http://nmon.sourceforge.net
Source: %name-%version.tar

Packager: %packager

# Automatically added by buildreq on Mon Apr 30 2012
# optimized out: libtinfo-devel
BuildRequires: libncurses-devel

%description
nmon is a monitoring console program developed by IBM.

%description -l ru_RU.UTF-8
nmon - это программа мониторинга рабочей станции/сервера,
разработанная в IBM.

%prep
%setup -n %name-%version

%build
%make

%install
# make DESTDIR=%buildroot install
install -d %buildroot%_bindir
install -pm755 nmon %buildroot%_bindir

%files

%_bindir/*

%changelog
* Tue May 15 2012 Andrey Bergman <vkni@altlinux.org> 14g-alt0.3
- Added URL.

* Mon Apr 30 2012 Andrey Bergman <vkni@altlinux.org> 14g-alt0.2
- Corrected build requires.

* Sun Apr 29 2012 Andrey Bergman <vkni@altlinux.org> 14g-alt0.1
- Initial release for Sisyphus.

