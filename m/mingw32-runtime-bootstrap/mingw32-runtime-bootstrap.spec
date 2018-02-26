Name: mingw32-runtime-bootstrap
Version: 3.15.2
Release: alt1
Summary: MinGW Windows cross-compiler runtime

License: Public Domain
Group: Development/Other
Url: http://www.mingw.org/
Packager: Boris Savelev <boris@altlinux.org>

Source: http://dl.sourceforge.net/sourceforge/mingw/mingwrt-%version-mingw32-dev.tar.gz
Source1: http://dl.sourceforge.net/sourceforge/mingw/mingwrt-%version-mingw32-dll.tar.gz

BuildArch: noarch

Requires: mingw32-filesystem
BuildRequires: rpm-build-mingw32
Provides: mingw32-runtime

%description
MinGW Windows cross-compiler runtime, base libraries.

%prep
%build
%install
mkdir -p %buildroot%_mingw32_prefix
cd %buildroot%_mingw32_prefix
tar -xzf %SOURCE0
tar -xzf %SOURCE1
mv %buildroot%_mingw32_prefix/doc  %buildroot%_mingw32_datadir

%files
%_mingw32_bindir/*
%_mingw32_docdir/*
%_mingw32_includedir/*
%_mingw32_libdir/*
%_mingw32_mandir/man3/*

%changelog
* Sat Jul 18 2009 Boris Savelev <boris@altlinux.org> 3.15.2-alt1
- initial build

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.15.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 3.15.2-2
- Rebuild for mingw32-gcc 4.4

* Tue Feb 10 2009 Richard W.M. Jones <rjones@redhat.com> - 3.15.2-1
- New upstream release 3.15.2.

* Tue Dec  9 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-10
- Force rebuild to get rid of the binary bootstrap package and replace
  with package built from source.

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-9
- No runtime dependency on binutils or gcc.
- But it DOES BR w32api.

* Mon Nov 24 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-8
- Rebuild against latest filesystem package.
- MINGW_CFLAGS -> MINGW32_CFLAGS.
- Rewrite the summary for accuracy and brevity.

* Fri Nov 21 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-6
- Remove obsoletes for a long dead package.
- Reenable (and fix) _mingw32_configure (Levente Farkas).

* Thu Nov 20 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-5
- Don't use _mingw32_configure macro - doesn't work here.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-4
- Rebuild against mingw32-filesystem 37

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-3
- Remove the useconds patch, which is no longer needed (Levente Farkas).
- Use _mingw32_configure macro.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-2
- Rebuild against mingw32-filesystem 36

* Thu Oct 16 2008 Richard W.M. Jones <rjones@redhat.com> - 3.15.1-1
- New upstream version 3.15.1.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 3.14-6
- Rename mingw -> mingw32.

* Thu Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 3.14-4
- Use RPM macros from mingw-filesystem.

* Mon Jul  7 2008 Richard W.M. Jones <rjones@redhat.com> - 3.14-2
- Initial RPM release, largely based on earlier work from several sources.
