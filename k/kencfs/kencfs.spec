%define  kdeapp 134003

Name:    kencfs
Version: 1.2.1
Release: alt1
Summary: KEncFS is a gui frontend for encfs

License: LGPLv2.1
Group:   System/Configuration/Hardware
URL:     http://kde-apps.org/content/show.php/?content=%{kdeapp}

Source:  http://kde-apps.org/CONTENT/content-files/%kdeapp-%name-%version.tar.gz

BuildRequires(pre): qt4-devel
BuildRequires:  gcc-c++
BuildRequires:  kde4libs-devel

%description
KEncFS is a gui frontend for encfs. With KEncFS you can easily create,
mount, umount and delete your encrypted filesystem.

Use of KEncFS is very simple: to create a new encrypted filesystem you
must create new or select two existent dirs, one directory to archive
encrypted files and another directory to mount on the encrypted
filesystem with encfs (a mountpoint). After this, you can select
a conventional ID for your encrypted filesystem and then a password.

%prep
%setup -q
qmake-qt4
subst 's,^\(CXXFLAGS.\+\)$,\1 -I%_K4includedir,' Makefile

%build
%make_build SUBLIBS="-L%_K4link"

%install
%make INSTALL_ROOT=%buildroot install
rm -rf %buildroot%_datadir/doc/%name-1.2

%files
%doc README
%_bindir/%name
%_desktopdir/%name.desktop
%_K4apps/%name/

%changelog
* Wed Apr 10 2013 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1
- Initial build in Sisyphus (ALT #28796)

