Name: arepo
Version: 1
Release: alt10

Summary: biarch repackager for Sisyphus packages
License: Public domain
Group: Development/Other
BuildArch: noarch

Source: %name-%version.tar

# Update Requires list by running:
#   egrep -o '(/usr)?/bin/[a-z]+' arepo.py | sort -u | xargs
Requires: /bin/sh /bin/tar /usr/bin/genbasedir /usr/bin/hsh /usr/bin/mkaptbox /usr/bin/python /usr/bin/rpmrdups /usr/bin/setarch

%description
Arepo (with the default config) repackages i586 files (mostly
libraries) in i586-* packages suitable for installation
on an x86_64 system. Installing these packages allows you
to emulate a biarch environment.

%prep
%setup

%install
mkdir -p %buildroot%_bindir
install -m755 %name.py %buildroot%_bindir/%name
mkdir -p %buildroot%_sysconfdir
install -m644 %name.conf %buildroot%_sysconfdir

%files
%_bindir/%name
%config(noreplace) %_sysconfdir/%name.conf

%changelog
* Fri Feb 10 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1-alt10
- Add liblockdev

* Wed Feb 01 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1-alt9
- Add wine, VirtualGL with dependencies to arepo.conf

* Tue Jan 17 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1-alt8
- use '%%set_strip_method' on old repositories without
  '%%brp_strip_none' support

* Wed Dec 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1-alt7
- change '%%set_strip_method none' with '%%brp_strip_none /*'
- introduce 'name' setting in configfile

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1-alt6.1
- Rebuild with Python-2.7

* Mon Jun 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1-alt6
- sr@: fix 'lost dependencies' error (ALT #25192)
- update default config accordingly to the arepo@people config

* Sat Feb 12 2011 Vitaly Lipatov <lav@altlinux.ru> 1-alt5
- do not process non-ELF's with ldd
- swallow filelist passed by rpm to avoid SIGPIPE

* Thu Dec 30 2010 Vitaly Lipatov <lav@altlinux.ru> 1-alt4
- force array type for header['requireflags'] (closes #24836)

* Sat Sep 04 2010 Denis Smirnov <mithraen@altlinux.ru> 1-alt3
- Multiple fixes

* Mon Mar 22 2010 Alexander Myltsev <avm@altlinux.ru> 1-alt2
- Distinguish between libraries and programs (closes #22985).
- Explicitly require all the binaries that we call (closes #22735).

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1-alt1.2
- Rebuilt with python 2.6

* Fri Feb 08 2008 Grigory Batalov <bga@altlinux.ru> 1-alt1.1
- Rebuilt with python-2.5.

* Wed Feb 06 2008 Alex V. Myltsev <avm@altlinux.ru> 1-alt1
- Works with branch 4.0.
- Removes duplicate packages.

* Sun Nov 18 2007 Alex V. Myltsev <avm@altlinux.ru> 0-alt2
- i586-gcc4.1 can be installed and works with current Sisyphus.

* Fri Nov 09 2007 Alex V. Myltsev <avm@altlinux.ru> 0-alt1
- Initial build for Sisyphus.

