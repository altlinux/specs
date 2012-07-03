Name: unifdef
Version: 2.6
Release: alt1
Summary: A tool for removing ifdef'd lines
License: BSD
Group: Development/C
Url: http://dotat.at/prog/unifdef/
%define srcname %name-%version-%release
# git://git.altlinux.org/gears/u/unifdef.git
Source: %srcname.tar

%description
Unifdef is useful for removing ifdefed lines from a file while otherwise
leaving the file alone. Unifdef acts on #ifdef, #ifndef, #else, and #endif
lines, and it knows only enough about C and C++ to know when one of these
is inactive because it is inside a comment, or a single or double quote.

%prep
%setup -n %srcname

%build
%make_build CFLAGS='%optflags'

%install
%makeinstall_std prefix=/usr

%check
make test

%files
%_bindir/unifdef*
%_man1dir/unifdef*

%changelog
* Fri Jan 20 2012 Dmitry V. Levin <ldv@altlinux.org> 2.6-alt1
- Updated to unifdef-2.6-5-gac55802.

* Thu Dec 03 2009 Dmitry V. Levin <ldv@altlinux.org> 1.171-alt3
- Synced with linux kernel's unifdef.

* Thu May 07 2009 Dmitry V. Levin <ldv@altlinux.org> 1.171-alt2
- Fixed build with new toolchain.

* Thu Dec 18 2008 Anton Protopopov <aspsk@altlinux.org> 1.171-alt1
- Initial build for ALT

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.171-7
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 David Woodhouse <dwmw2@infradead.org> - 1.171-6
- Rebuild

* Sat Jul 15 2006 David Woodhouse <dwmw2@infradead.org> - 1.171-5
- Don't redefine %%dist

* Fri Jul 14 2006 Jesse Keating <jkeating@redhat.com> - 1.171-4
- Minor specfile cleanups from review

* Tue May  2 2006 David Woodhouse <dwmw2@infradead.org> - 1.171-3
- Minor specfile cleanups from review

* Wed Apr 26 2006 David Woodhouse <dwmw2@infradead.org> - 1.171-2
- Change BuildRoot

* Tue Apr 25 2006 David Woodhouse <dwmw2@infradead.org> - 1.171-1
- Initial import from FreeBSD CVS
