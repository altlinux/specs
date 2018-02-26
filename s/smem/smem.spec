Name: smem
Version: 1.0
Release: alt1.1

Summary: Report application memory usage in a meaningful way
License: GPLv2+
Group: Monitoring

Url: http://www.selenic.com/smem
Source0: http://www.selenic.com/smem/download/%name-%version.tar.gz
Source1: http://www.selenic.com/smem/index.html
Packager: Michael Shigorin <mike@altlinux.org>

Conflicts: secure_delete

%description
smem is a tool that can give numerous reports on memory usage
on Linux systems. Unlike existing tools, smem can report
proportional set size (PSS), which is a more meaningful
representation of the amount of memory used by libraries
and applications in a virtual memory system.

Since large portions of physical memory are typically shared
among multiple applications, the standard measure of memory usage
known as resident set size (RSS) will significantly overestimate
memory usage.  PSS measures each application's "fair share" of
each shared area instead to give more realistic sense of what's
happening.

Requires: kernel >= 2.6.27

%prep
%setup
cp -a %SOURCE1 smem.html

%build
make smemcap CFLAGS="%optflags"

%install
install -pDm755 smem %buildroot%_bindir/%name
install -pDm755 smemcap %buildroot%_bindir/smemcap
install -pDm644 smem.8 %buildroot%_man8dir/smem.8

%files
%_bindir/*
%_man8dir/*
%doc smem.html COPYING

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.1
- Rebuild with Python-2.7

* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 1.0-alt1
- 1.0
  + dropped capture script from docs (removed upstream)
  + added smemcap (no more noarch)

* Sun Dec 13 2009 Michael Shigorin <mike@altlinux.org> 0.9-alt1
- 0.9
  + dropped upstream hg patches
- added conflict with secure_delete (repocop)
- minor spec cleanup

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.1
- Rebuilt with python 2.6

* Thu May 07 2009 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- built for ALT Linux (based on spec for Fedora)
- spec/description cleanup

* Wed May  7 2009 Matthew Miller <mattdm@mattdm.org> - 0.1-4
- remove smem.pdf at request of upstream
- patch0: 741bd2646ebf -- add GPLv2+ and copyright notice
- patch1: 4320ad746bcc -- check that kernel release >= 2.6.27

* Thu Apr 30 2009 Matthew Miller <mattdm@mattdm.org> - 0.1-3
- fix minor rpmlint concerns raised in review (bz #498490)

* Thu Apr 30 2009 Matthew Miller <mattdm@mattdm.org> - 0.1-2
- whoops -- fixed group

* Thu Apr 30 2009 Matthew Miller <mattdm@mattdm.org> - 0.1-1
- initial specfile
- note gplv2+ license -- added in svn and will be in next code release
