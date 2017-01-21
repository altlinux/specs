Name: nmon
Version: 16f
Release: alt1

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
* Sat Jan 21 2017 Andrey Bergman <vkni@altlinux.org> 16f-alt1
- Version update.

* Tue Apr 26 2016 Andrey Bergman <vkni@altlinux.org> 16e-alt1
- Version update.

* Mon Mar 21 2016 Andrey Bergman <vkni@altlinux.org> 16d-alt1
- Version update.

* Sun Feb 07 2016 Andrey Bergman <vkni@altlinux.org> 16c-alt1
- Version update.

* Thu Aug 13 2015 Andrey Bergman <vkni@altlinux.org> 15h-alt1
- Version update.

* Thu Jun 04 2015 Andrey Bergman <vkni@altlinux.org> 15e-alt1
- Version update.

* Sat Dec 28 2013 Andrey Bergman <vkni@altlinux.org> 14i-alt1
- Version update.

* Fri Jul 26 2013 Andrey Bergman <vkni@altlinux.org> 14h-alt1
- Version update.

* Tue May 15 2012 Andrey Bergman <vkni@altlinux.org> 14g-alt0.3
- Added URL.

* Mon Apr 30 2012 Andrey Bergman <vkni@altlinux.org> 14g-alt0.2
- Corrected build requires.

* Sun Apr 29 2012 Andrey Bergman <vkni@altlinux.org> 14g-alt0.1
- Initial release for Sisyphus.

