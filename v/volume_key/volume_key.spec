%def_enable snapshot

Name: volume_key
Version: 0.3.9
Release: alt2

Summary: An utility for manipulating storage encryption keys and passphrases
License: GPLv2
Group: System/Configuration/Hardware
Url: https://fedorahosted.org/%name/

%if_disabled snapshot
Source: https://fedorahosted.org/releases/v/o/%name/%name-%version.tar.xz
%else
# VCS: https://git.fedorahosted.org/git/volume_key.git
Source: %name-%version.tar
%endif
# fc
Patch: volume_key-0.3.9-crypt_get_error.patch

Requires: lib%name = %version-%release

BuildRequires: glib2-devel libcryptsetup-devel /usr/bin/gpg
BuildRequires: libgpgme-devel libblkid-devel libnss-devel
BuildRequires: python-devel swig

%description
This package provides a command-line tool for manipulating storage volume
encryption keys and storing them separately from volumes.

The main goal of the software is to allow restoring access to an encrypted
hard drive if the primary user forgets the passphrase.  The encryption key
back up can also be useful for extracting data after a hardware or software
failure that corrupts the header of the encrypted volume, or to access the
company data after an employee leaves abruptly.

%package -n lib%name
Summary: A library for manipulating storage encryption keys and passphrases
Group: System/Libraries
Requires: /usr/bin/gpg

%description -n lib%name
This package provides libvolume_key, a library for manipulating storage volume
encryption keys and storing them separately from volumes.

The main goal of the software is to allow restoring access to an encrypted
hard drive if the primary user forgets the passphrase.  The encryption key
back up can also be useful for extracting data after a hardware or software
failure that corrupts the header of the encrypted volume, or to access the
company data after an employee leaves abruptly.

%package -n lib%name-devel
Summary: A library for manipulating storage encryption keys and passphrases
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides libvolume_key, a library for manipulating storage volume
encryption keys and storing them separately from volumes.

The main goal of the software is to allow restoring access to an encrypted
hard drive if the primary user forgets the passphrase.  The encryption key
back up can also be useful for extracting data after a hardware or software
failure that corrupts the header of the encrypted volume, or to access the
company data after an employee leaves abruptly.

%package -n python-module-%name
Summary: Python bindings for libvolume_key
Group: Development/Python
Requires: lib%name = %version-%release

%description -n python-module-%name
This package provides Python bindings for libvolume_key, a library for
manipulating storage volume encryption keys and storing them separately from
volumes.

The main goal of the software is to allow restoring access to an encrypted
hard drive if the primary user forgets the passphrase.  The encryption key
back up can also be useful for extracting data after a hardware or software
failure that corrupts the header of the encrypted volume, or to access the
company data after an employee leaves abruptly.

volume_key currently supports only the LUKS volume encryption format.  Support
for other formats is possible, some formats are planned for future releases.

%prep
%setup
%patch -p1 -b .crypt_get_error

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files
%_bindir/%name
%_man8dir/%name.8.*
%doc README contrib

%files -n lib%name -f %name.lang
%_libdir/lib%name.so.*
%doc AUTHORS ChangeLog NEWS

%files -n lib%name-devel
%_includedir/%name/
%_libdir/lib%name.so

%files -n python-module-%name
%python_sitelibdir/_%name.so
%python_sitelibdir/%name.py*
%exclude %python_sitelibdir/_%name.la

%changelog
* Mon Jan 29 2018 Yuri N. Sedunov <aris@altlinux.org> 0.3.9-alt2
- rebuilt against libcryptsetup.so.12

* Tue Oct 18 2016 Yuri N. Sedunov <aris@altlinux.org> 0.3.9-alt1
- 0.3.9 (0.3.9-8-gd4b00ce)

