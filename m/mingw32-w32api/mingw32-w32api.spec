%define __strip %_mingw32_strip
%define __objdump %_mingw32_objdump

Name: mingw32-w32api
Version: 3.13
Release: alt3
Summary: Win32 header files and stubs

License: Public Domain
Group: System/Libraries
Url: http://www.mingw.org/
Packager: Boris Savelev <boris@altlinux.org>

Source: http://dl.sourceforge.net/sourceforge/mingw/w32api-%version-mingw32-src.tar.gz

BuildArch: noarch

BuildRequires: rpm-build-mingw32
BuildRequires: mingw32-gcc >= 4.4.0
BuildRequires: mingw32-runtime

Requires: mingw32-runtime

# Once this is installed, mingw32-bootstrap (binary bootstrapper) is no
# longer needed.
Obsoletes: mingw32-w32api-bootstrap

%description
MinGW Windows cross-compiler Win32 header files.

%prep
%setup -q -n w32api-%version-mingw32

%build
%_mingw32_configure
%make

%install
%_mingw32_makeinstall

%files
%_mingw32_includedir/*
%_mingw32_libdir/*.a

%changelog
* Mon Jul 27 2009 Boris Savelev <boris@altlinux.org> 3.13-alt3
- rebuild

* Mon Jul 20 2009 Boris Savelev <boris@altlinux.org> 3.13-alt2
- initial build

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 3.13-2
- Rebuild for mingw32-gcc 4.4

* Mon Dec 15 2008 Richard W.M. Jones <rjones@redhat.com> - 3.13-1
- New upstream version 3.13.

* Tue Dec  9 2008 Richard W.M. Jones <rjones@redhat.com> - 3.12-8
- Force rebuild to get rid of the binary bootstrap package and replace
  with package built from source.

* Wed Nov 26 2008 Richard W.M. Jones <rjones@redhat.com> - 3.12-7
- No runtime dependency on binutils or gcc.

* Mon Nov 24 2008 Richard W.M. Jones <rjones@redhat.com> - 3.12-6
- Rebuild against latest filesystem package.
- Rewrite the summary for accuracy and brevity.

* Fri Nov 21 2008 Richard W.M. Jones <rjones@redhat.com> - 3.12-4
- Remove obsoletes for a long dead package.
- Enable _mingw32_configure (Levente Farkas).

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 3.12-3
- Rebuild against mingw32-filesystem 37

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 3.12-2
- Rebuild against mingw32-filesystem 36

* Thu Oct 16 2008 Richard W.M. Jones <rjones@redhat.com> - 3.12-1
- New upstream version 3.12.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 3.11-7
- Rename mingw -> mingw32.

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 3.11-6
- Moved ole provides to mingw-filesystem package.

* Thu Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 3.11-3
- Use the RPM macros from mingw-filesystem.

* Mon Jul  7 2008 Richard W.M. Jones <rjones@redhat.com> - 3.11-2
- Initial RPM release, largely based on earlier work from several sources.
