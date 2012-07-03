Name: metastore
Version: 0.0
Release: alt1

Summary: Metastore stores metadata for git
License: GPL2
Group: Development/Other
Url: git://git.hardeman.nu/metastore.git
Source: %name-%version.tar.gz

Packager: Evgenii Terechkov <evg@altlinux.org>

# Automatically added by buildreq on Wed Jan 02 2008
BuildRequires: libattr-devel

%description
Metastore stores metadata for git

%prep
%setup

%build
make prefix=%_prefix mandir=%_mandir

%install
mkdir -p %buildroot%_man1dir %buildroot%_bindir
make install DESTDIR=%buildroot

%files
%_bindir/%name
%_man1dir/%{name}.*

%doc README examples

%changelog
* Tue Feb 19 2008 Terechkov Evgenii <evg@altlinux.ru> 0.0-alt1
- Rebuild with new sisyphus_check

* Wed Jan  2 2008 Terechkov Evgenii <evg@altlinux.ru> 0.0-alt0
- Initial build for ALT Linux Sisyphus
