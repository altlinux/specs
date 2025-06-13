Summary: Linux Standard Base Release Tools
Name: lsb-release
Version: 3.3
Release: alt2
License: GPL-2.0-or-later
Source: %name-%version.tar
Patch: lsb-release-3.3-alt-fix.patch
Group: System/Base
Url: http://www.linuxbase.org/
Vcs: https://github.com/thkukuk/lsb-release_os-release

BuildArch: noarch
Packager: Andriy Stepanov <stanv@altlinux.ru>

Conflicts: lsb-core < 4.0

%description
LSB version query program

The program queries the installed state of the distribution
to display certain properties such as the version of the
LSB against which the distribution claims compliance as 
well. It can also attempt to display the name and release
of the distribution along with an identifier of who produces
the distribution.

The lsb_release command is a simple tool to help identify the Linux
distribution being used and its compliance with the Linux Standard
Base. LSB conformance will not be reported unless the required
metapackages are installed.
While it is intended for use by LSB packages, this command may also be
useful for programmatically distinguishing between a original one and
derived distributions.
%prep
%setup
%patch -p1
subst 's|prefix=/usr/local|prefix=/usr|' Makefile

%build
make

%install
make prefix=%buildroot%_prefix mandir=%buildroot%_mandir install

%files
%defattr(-,root,root)
%doc README COPYING
%_bindir/lsb?release
%{_man1dir}/lsb?release.1*

%changelog
* Fri Jun 13 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.3-alt2
- fixed Codename display

* Thu Jun 12 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.3-alt1
- 2.0 -> 3.3 (ALT #48518)
- removed patch

* Thu Jan 31 2019 Andrey Cherepanov <cas@altlinux.org> 2.0-alt5
- Fix extract text in brackets.

* Thu Jan 31 2019 Andrey Cherepanov <cas@altlinux.org> 2.0-alt4
- Do not check 'ALT Linux' prefix and 'release' delimiter in description.

* Tue Apr 13 2010 Andriy Stepanov <stanv@altlinux.ru> 2.0-alt3
- Enhance lsb_release utilility.

* Tue Apr 13 2010 Andriy Stepanov <stanv@altlinux.ru> 2.0-alt2
- Add BuildRequires.

* Fri Apr 09 2010 Andriy Stepanov <stanv@altlinux.ru> 2.0-alt1
- Build as separate package

