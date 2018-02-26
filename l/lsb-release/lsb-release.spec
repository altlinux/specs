Summary: Linux Standard Base Release Tools
Name: lsb-release
Version: 2.0
Release: alt3
License: %gpl2plus
Source: %name-%version.tar
Group: System/Base
Url: http://www.linuxbase.org/
Patch:  lsb-release-2.0-alt-config.patch
BuildArch: noarch
Packager: Andriy Stepanov <stanv@altlinux.ru>

Conflicts: lsb-core < 4.0

BuildRequires: rpm-build-licenses

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

%build
make

%install
make prefix=%buildroot%_prefix mandir=%buildroot%_mandir install

%files
%defattr(-,root,root)
%doc README
%_bindir/lsb_release
%{_man1dir}/lsb_release.1*

%changelog
* Tue Apr 13 2010 Andriy Stepanov <stanv@altlinux.ru> 2.0-alt3
- Enhance lsb_release utilility.

* Tue Apr 13 2010 Andriy Stepanov <stanv@altlinux.ru> 2.0-alt2
- Add BuildRequires.

* Fri Apr 09 2010 Andriy Stepanov <stanv@altlinux.ru> 2.0-alt1
- Build as separate package

