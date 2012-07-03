Name:     bup
Version:  0.25
Release:  alt1.rc1.1

Summary:  bup is a program that backs things up
License:  LGPLv2+
Group:    Archiving/Backup
URL:      https://github.com/apenwarr/bup/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildPreReq:   python-devel 
BuildRequires: git-core
BuildRequires: pandoc
BuildRequires: python-module-fuse
BuildRequires: python-module-fuse
BuildRequires: python-module-pyxattr
BuildRequires: python-module-libacl

%description
bup is a program that backs things up. It's short for "backup."

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix} \
	--execdir=%{_bindir} \
	--sbindir=%{_sbindir} \
	--confdir=%{_sysconfdir} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--mandir=%{_mandir}
%make_build
pushd Documentation
%make
popd

%install
%makeinstall_std

%files
%doc README README.md DESIGN
%doc %_defaultdocdir/%name/
%_bindir/%name
%_libexecdir/%name/
%_man1dir/%{name}*

%changelog
* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.25-alt1.rc1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Jan 30 2012 Andrey Cherepanov <cas@altlinux.org> 0.25-alt1.rc1
- New version 0.25_rc1 (needed for kde4-kup)
- Fix package version to LGPLv2+

* Thu Jan 26 2012 Andrey Cherepanov <cas@altlinux.org> 0.24-alt1
- Initial build in Sisyphus

