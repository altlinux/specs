Name: recover
Version: 1.3c
Release: alt1

Summary: Utility which automates the rtecovery of lost files
License: GPL
Group: System/Kernel and hardware
Url: http://recover.sourceforge.net/linux/%name

Source: %url/download/%name-%version.tar.bz2

%description
Recover is a utility which automates some steps as described in the
Ext2fs-Undeletion howto in order to recover a lost file.

%prep
%setup -q

%build
%make_build CFLAGS="$RPM_OPT_FLAGS"

%install
install -p -m755 -D %name $RPM_BUILD_ROOT%_bindir/%name
install -p -m644 -D %name.1.gz $RPM_BUILD_ROOT%_mandir/man1/%name.1.gz
install -p -m644 -D recover_questions $RPM_BUILD_ROOT%_datadir/%name/recover_questions

%files
%_bindir/*
%_datadir/%name
%_mandir/man?/*
%doc CHANGES README

%changelog
* Wed Mar 26 2003 Stanislav Ievlev <inger@altlinux.ru> 1.3c-alt1
- 1.3c

* Wed Oct 02 2002 Stanislav Ievlev <inger@altlinux.ru> 1.3b-alt2
- rebuild with gcc3

* Mon May 27 2002 Stanislav Ievlev <inger@altlinux.ru> 1.3b-alt1
- 1.3b

* Fri Mar 09 2001 Dmitry V. Levin <ldv@fandra.org> 1.3-ipl1
- Initial revision.
