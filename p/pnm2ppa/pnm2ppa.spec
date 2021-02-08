Summary: Drivers for printing to HP PPA printers

Name: pnm2ppa
Version: 1.13
Release: alt2

Packager: Stanislav Ievlev <inger@altlinux.org>

URL: http://sourceforge.net/projects/pnm2ppa 

Source: http://download.sourceforge.net/pnm2ppa/pnm2ppa-%{version}.tar.gz
Patch: pnm2ppa-1.11-rh-build.patch
Patch1: alt-fix-ftbfs.patch

License: GPL
Group: Publishing

%description
Pnm2ppa is a color driver for HP PPA host-based printers such as the
HP710C, 712C, 720C, 722C, 820Cse, 820Cxi, 1000Cse, and 1000Cxi.
Pnm2ppa accepts Ghostscript output in PPM format and sends it to the
printer in PPA format.

Install pnm2ppa if you need to print to a PPA printer.

%prep
%setup -q
%patch -p1
%patch1 -p1

%build
%configure
%make


%install
install -d %buildroot/%_bindir
install -d %buildroot/%_sysconfdir
install -d %buildroot%_man1dir

make \
    DESTDIR=%buildroot \
    install

for i in utils/Linux/*; do
%__install -Dpm 755 $i %buildroot/%_bindir/`basename $i`
done

chmod 644 docs/en/LICENSE


%files 
%defattr(-,root,root)
%doc docs/en/* test.ps
%_bindir/*
%_man1dir/*
%config(noreplace) /etc/pnm2ppa.conf

%changelog
* Mon Feb 08 2021 Oleg Solovyov <mcpain@altlinux.org> 1.13-alt2
- fix ftbfs

* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 1.13-alt1
- Build version 1.13 from mageia package

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.04-alt1.qa1
- NMU: rebuilt for debuginfo.

* Wed Nov 07 2007 Stanislav Ievlev <inger@altlinux.org> 1.04-alt1
- Build as a separate package

