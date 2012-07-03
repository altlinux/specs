Name: cpulimit
Version: 1.1
Release: alt1

Summary: CPU Usage Limiter

Packager: Vitaly Lipatov <lav@altlinux.ru>

Url: http://cpulimit.sourceforge.net/
License: GPL
Group: Monitoring

Source: http://prdownloads.sourceforge.net/cpulimit/%name-%version.tar.bz2

%description
cpulimit is a simple program that attempts to limit the cpu usage of a
process (expressed in percentage, not in cpu time). This is useful to
control batch jobs, when you don't want they eat too much cpu. It does
not act on the nice value or other scheduling priority stuff, but on
the real cpu usage. Also, it is able to adapt itself to the overall
system load, dynamically and quickly.

%prep
%setup -q

%build
%make_build

%install
mkdir -p %buildroot%_bindir
cp -p %name %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Mon Jul 06 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- initial release for ALT Linux Sisyphus

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.1-3mdv2009.0
+ Revision: 243724
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.1-1mdv2008.1
+ Revision: 136345
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jul 27 2007 Nicolas Vigier <nvigier@mandriva.com> 1.1-1mdv2008.0
+ Revision: 56274
- Import cpulimit

