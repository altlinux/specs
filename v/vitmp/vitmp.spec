Name: vitmp
Version: 1.0
Release: alt4

Summary: The temporary text files editor
License: public domain
Group: Editors
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source0: vitmp.c
Source1: vitmp.1

Requires: vim-minimal

%description
vitmp is a wrapper around the VIM text editor which may be used to
invoke the editor in a way that is guaranteed to be suitable for editing
temporary files used with programs such as crontab(1) and edquota(8).
The instance of the editor that is invoked is /bin/vi.

%prep
%setup -qcT

%build
%__cc %optflags -W %_sourcedir/vitmp.c -o vitmp

%install
install -pD -m755 vitmp %buildroot/bin/vitmp
install -pD -m644 %_sourcedir/vitmp.1 %buildroot%_man1dir/vitmp.1

%files
/bin/*
%_man1dir/*

%changelog
* Thu Apr 12 2007 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt4
- Rebuilt.

* Sun Jul 09 2006 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt3
- Updated vi commands to disable backups in modern VIM.
- Fixed compilation warnings.
- Cleaned up specfile.

* Thu Oct 31 2002 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt2
- Rebuilt in new environment.

* Tue May 14 2002 Dmitry V. Levin <ldv@altlinux.org> 1.0-alt1
- Initial revision (the vitmp itself came from Owl).
