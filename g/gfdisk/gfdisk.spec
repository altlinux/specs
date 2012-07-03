%define realname fdisk

Name: gfdisk
Version: 1.2.5
Release: alt2

Summary: The GNU version of fdisk
License: GPLv3
Group: System/Configuration/Hardware

Url: http://www.gnu.org/software/fdisk
Source: http://ftp.gnu.org/gnu/fdisk/%realname-%version.tar.bz2
Patch0: fdisk-1.1-remove-termcap.patch
Packager: Alexey Gladkov <legion@altlinux.ru>

BuildRequires: libparted-devel
BuildRequires: libcheck-devel libncurses-devel
BuildRequires: libreadline-devel libuuid-devel

%description
Small partitioning program with command line interface that might
be hard for linux newbie but is extra stable and dependable.

%package -n gcfdisk
Summary: The GNU version of cfdisk
Group: System/Configuration/Hardware

%description -n gcfdisk
Small user-friendly ncurses-based partitioning program which
can help you to partition your disk easily.

%prep
%setup -n %realname-%version
#patch0 -p1

%build
%add_optflags %optflags_warnings -Wunused-function -Wunused-label -Wunused-variable -Wunused-value
%autoreconf
%configure \
	--with-gnu-ext \
	--disable-rpath
%make_build

%install
%makeinstall

cd %buildroot
rm -f -- .%_sbindir/{gfdisk,lfdisk}

find .%_sbindir .%_infodir .%_man8dir -name '*fdisk*' |
while read f; do
	cd "${f%%/*}"
	mv -vf -- "${f##*/}" "g${f##*/}"
	cd -
done

%files
%_sbindir/gfdisk
%_infodir/gfdisk*
%_man8dir/gfdisk*

%files -n gcfdisk
%_sbindir/gcfdisk
%_infodir/gcfdisk*
%_man8dir/gcfdisk*

%changelog
* Thu May 17 2012 Michael Shigorin <mike@altlinux.org> 1.2.5-alt2
- rebuilt for Sisyphus (1.3, 2.0 are in alpha stage yet)
- minor spec proofreading

* Wed Jun 22 2011 Alexey Gladkov <legion@altlinux.ru> 1.2.5-alt1
- New version (1.2.5).

* Mon Dec 06 2010 Alexey Gladkov <legion@altlinux.ru> 1.2.4-alt2
- Rebuilt with new libparted.

* Fri Mar 05 2010 Alexey Gladkov <legion@altlinux.ru> 1.2.4-alt1
- New version (1.2.4).

* Fri Dec 26 2008 Alexey Gladkov <legion@altlinux.ru> 1.1-alt1
- New version (1.1).

* Tue Jul 17 2007 Alexey Gladkov <legion@altlinux.ru> 1.0-alt1
- New version (1.0).
- Change license to GPLv3.

* Wed May 09 2007 Alexey Gladkov <legion@altlinux.ru> 0.9.3-alt1
- New version (0.9.3)

* Tue Apr 17 2007 Alexey Gladkov <legion@altlinux.ru> 0.9.2-alt2
- Fix SIGSERV (patch0).

* Fri Apr 06 2007 Alexey Gladkov <legion@altlinux.ru> 0.9.2-alt1
- first build for ALT Linux.
