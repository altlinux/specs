Summary: Intel ACPI investigation tools
Summary(ru_RU.UTF-8): Утилиты для исследования ACPI
Name: pmtools
Version: 20071116
Release: alt1
License: GPL
Group: System/Kernel and hardware
Url: http://ftp.kernel.org/pub/linux/kernel/people/lenb/acpi/utils/
Source: %name-%version.tar.bz2

%description
This is a small collection of power management test and
investigation tools. (acpidump, acpidisasm, pmtest)

%description -l ru_RU.UTF-8
Это небольшая коллекция утилит для тестирования и исследования
поддержки ACPI.

%prep
%setup -q

%build
%make
%make -C madt madt

%install
%__mkdir_p %buildroot%_bindir
%__mkdir_p %buildroot%_sbindir

install -m0755 acpidump/acpidump %buildroot%_sbindir
install -m0755 madt/madt %buildroot%_bindir

#install -m0755 acpidump/acpitbl %buildroot%_bindir


# acpixtract info:
# http://lists.altlinux.org/pipermail/devel/2009-February/166212.html
# rider@ : поэтому удаляй из pmtools - оно теперь живёт в acpica-unix (iasl)
# install -m0755 acpixtract/acpixtract %buildroot%_bindir


%files
%doc README
%_bindir/*
%_sbindir/*

%changelog
* Sun Feb 08 2009 Andriy Stepanov <stanv@altlinux.ru> 20071116-alt1
- Switch up to new version

* Thu Feb 15 2007 Andriy Stepanov <stanv@altlinux.ru> 20061130-alt1
- Switch up to new version

* Fri Apr 21 2006 Anton Farygin <rider@altlinux.ru> 20051111-alt1
- new version

* Mon Dec 15 2003 Anton Farygin <rider@altlinux.ru> 20010730-alt1
- first build for Sisyphus

